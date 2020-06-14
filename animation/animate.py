# %%
from more_itertools import flatten

import os, sys
sys.path.append(os.path.realpath('..'))
from baba.utils import *
from baba.rules import *
from baba.play import timestep, swap, YouWin

sn = symbol_to_name

from PIL import Image

# %% Load sprites

SPRITES = {}
for symbol in SYMBOLS:
    if isentity(symbol):
        filename = f'./sprites/entity_{sn(symbol)}.png'
    else:
        filename = f'./sprites/text_{sn(symbol)}.png'
    SPRITES[symbol] = Image.open(filename)

BACKGROUND_COLOUR = '#1c1e26';

hex2rgb = lambda h: tuple(int(h[i+1:i+3],16) for i in range(0,len(h)-1,2))

BLANK = Image.new('RGBA',(24,24),color=hex2rgb(BACKGROUND_COLOUR+'88'))
YOUWIN = Image.open('./sprites/youwin.png')
YOULOSE = Image.open('./sprites/youlose.png')
STARS = Image.open('./sprites/stars.png')

def rulefinder2(grid):
    ''' Find the position of all the elements in rules '''
    N, M = len(grid), len(grid[0])
    isinrule = empty_NM(N,M,element=False)
    # Check every candidate against the grammar
    # Noun is (Noun OR Property)
    isrule = lambda t:(
        isnoun(t[0]) and isis(t[1]) and
        (isnoun(t[2]) or isproperty(t[2])))

    # Horizontal rules
    if M>=3:
        for j,row in enumerate(grid):
            for k,t in enumerate(windowed(row,3)):
                if isrule(t):
                    for o in range(3):
                        isinrule[j][k+o] = True

    # Vertical rules
    if N>=3:
        for k,col in enumerate(zip(*grid)):
            for j,t in enumerate(windowed(col,3)):
                if isrule(t):
                    for o in range(3):
                        isinrule[j+o][k] = True

    return isinrule

# %%
def draw_frame(grid,behaviours):
    ''' Draw a frame of the animation '''
    N, M = len(grid), len(grid[0])
    img = Image.new('RGBA',(M*24,N*24),
        color=hex2rgb(BACKGROUND_COLOUR))
    
    isinrule = rulefinder2(grid)

    for j,row in enumerate(grid):
        for k,cell in enumerate(row):
            if issymbol(cell):
                img.paste(SPRITES[cell],(k*24,j*24),SPRITES[cell])
                # Fade out if not part of a rule
                if not isentity(cell) and not isinrule[j][k]:
                        img.paste(BLANK,(k*24,j*24),BLANK)
                # Add stars to anything which is win
                if isentity(cell) and behaviours[cell.lower()]['n']:
                    img.paste(STARS,(k*24,j*24),STARS)
    return img

def add_lose_to_frame(frame):
    ''' Add YouLose text to the frame '''
    blank = Image.new('RGBA',frame.size,
        color=hex2rgb(BACKGROUND_COLOUR+'88'))
    frame.paste(blank,(0,0),blank)
    text = YOULOSE
    text_position = tuple(round((fs - ts)/2) for fs,ts in zip(frame.size,text.size))
    frame.paste(text,text_position,text)

def add_win_to_frame(frame):
    ''' Add YouWin text to the frame '''
    blank = Image.new('RGBA',frame.size,
        color=hex2rgb(BACKGROUND_COLOUR+'88'))
    frame.paste(blank,(0,0),blank)
    text = YOUWIN
    text_position = tuple(round((fs - ts)/2) for fs,ts in zip(frame.size,text.size))
    frame.paste(text,text_position,text)
# %%

def animate_play(grid,sequence):
    ''' Play a game, given the sequence of moves and make an animated gif of it '''
    
    isvalidgrid(grid)
    behaviours, _ = ruleparser(rulefinder(grid))

    images = []
    images.append(draw_frame(grid,behaviours)) # First frame

    # Animate sequence
    youwon, youlost = (False, False)
    youlost = False
    for step in (*sequence,None):
        rules = rulefinder(grid)
        behaviours, swaps = ruleparser(rules)

        # Check for you is win condition
        for noun in behaviours:
            if behaviours[noun]['y'] and behaviours[noun]['n']:
                youwon = True

        # Do the swap
        grid = swap(grid,swaps)
        images.append(draw_frame(grid,behaviours))

        entities_present = {j.lower() for j in flatten(grid) if isentity(j)}
        if not any(behaviours[e]['y'] for e in entities_present):
            youlost = True

        # Timestep the grid
        if step:
            (grid,yw) = timestep(grid,behaviours,step)
            if yw:
                youwon = True
                images.append(draw_frame(grid,behaviours))
        
        if youwon or youlost:
            break

    if youlost:
        add_lose_to_frame(images[-1])
    elif youwon:
        add_win_to_frame(images[-1])

    images.append(images[-1].copy())
    images.append(images[-1].copy())

    return images