[![TravisCI](https://travis-ci.org/MarcinKonowalczyk/baba.svg?branch=master&service=github)](https://travis-ci.org/MarcinKonowalczyk/baba?branch=master)

# baba
Simplified implementation of [Baba Is You](https://hempuli.com/baba/).

This is a work-in-progress project. The intended scope, however, is as follows:

- 4 possible entities: `Baba`, `Wall`, `Flag`, `Rock` (uppercase)
- 4 corresponding nouns (lowercase)
- 4 properties: `Push`, `Stop`, `Win` and the pronoun `You`
- Operator `is`
  
Overall this gives 13 possible grid states + empty. The following interactions are simplified in this version.

- Entities cannot overlap. If a move leading to an overlap is requested, the objects act as if they were `stop`. This *should* prevent the game from becoming too broken and makes programming easier.
- The game is played by providing a sequence of actions. The allowed actions are `up`, `down`, `left` and `right`. No idle nor undo actions are implemented as they are not necessary to play the game.

The following, however, are supposed to work:

- Noun is Noun. Something like `baba is wall`, for example.
- NounA is NounA overruling the behaviors of NounA is NounB. For example if `wall is wall`, `wall` cannot be `baba`. The rule `wall is baba` can exist but it does nothing.

## ToDo's

- Actually meet the scope
- Write a nice renderer of a game (make a gif of it, for example)
- Write an tiny codegolf version. _Given a sequence of moves, does it win on a standardised level?_ For this it might be best to make a smaller level with just `Baba`, `Flag` and `Rock`. Maybe something like that(?):

```
...............
.rim....RRRRR..
........R...R..
.biy..B.R.F.R..
........R...R..
.fin....RRRRR..
...............
```

Also:

- Actually put things into classes?
- Write more tests
- Hook up coveralls?

