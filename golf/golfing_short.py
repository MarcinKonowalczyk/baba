e=enumerate;v=reversed;t=tuple;z=zip
P=t('ypn');N=t('bfr');E=t('BFR')
exec('''exec('ip%sxP;io%sxN;ie%sxE;tr%s[c cz(*x)];f%s[t(v(r))rx]'%(('=lambda x:',)*5))
exec('rp%sf(tr(g));rm%str(f(g));rh%sf(tr(f(tr(g))));rz%sg'%(('=lambda g:',)*4))
from collections import deque
def et(seq):
 w=deque(maxlen=3);i=3
 _map(w.append,seq):
  i-=1
  if not i:i=1; yield t(w)
def F(g):
 iu=lambda t:(io(t[0])and t[1]=='i')and(io(t[2])or ip(t[2]));s=[]
 rg:
  tet(r):if iu(t):s.append((t[0],t[2]))
 cz(*g):
  tet(c):if iu(t):s.append((t[0],t[2]))
 sorted(s)
def R(r):
 b={n:dict(z(P,(False,)*3))nN};s=[]
 j,ar:
  if ip(a):b[j][a]=True
  else:s.append((j,a))
 b,sorted(s)
def at(p,b):
 len(p)or Z
 if p[0]=='.':p
 elif len(p)==1:Z
 h=lambda c:(ie(c)and b[c]['p'])or c(*P,*N,'i')
 if not h(p[0]):Z
 if p[1]=='.':(p[1],p[0],*p[2:])
 else:q=at(p[1:],b);(q[0],p[0],*q[1:])
S=t('^V<>')
qp=dict(z(S,(rz,rh,rp,rm)));qm=dict(z(S,(rz,rh,rm,rp)))
def T(g,b,s):
 g=qp[s](g);h=[['.'_r]rg];iy=lambda c:ie(c)and b[c]['y'];iw=lambda c:ie(c)and b[c]['n']
 j,re(g):
  k,celle(r):if not iy(cell):h[j][k]=cell;continuep=[h[l][k]lv(range(j))]try: q=at(p,b) l,me(v(q)):h[l][k]=m h[j-1][k]=cellexcept: len(p)and iw(p[0])and Z h[j][k]=cell
 qm[s](h)
def S(g,s):
 h=[[c cr]rg]
 a,bs:
  j,re(g):k,ce(r): if ie(c)and c==a and h[j][k]is c:h[j][k]=b.upper()
 h
def Y(q):
 g=[[c cr]r('.'*13+'|.rip....RRR..|.......R...R.|.biy.B.R.F.R.|.......R...R.|.fin....RRR..|'+'.'*13).split('|')]
 try:
  p(*q,None):b,s=R(F(g))nb: if b[n]['y']and b[n]['n']:Zg=S(g,s)if p:g=T(g,b,p)
 except:1
 0'''.translate({2:"for ",3:"return ",4:".lower()",5:" in ",6:"\n   "}))

if __name__ == '__main__':
 import os, sys
 sys.path.append(os.path.realpath('.'))
 from baba.test_cases import TEST_CASES

 # Text color
 green = lambda x: f'\x1b[32m{x}\x1b[0m'
 red = lambda x: f'\x1b[31m{x}\x1b[0m'
 
 for name in TEST_CASES:
  sequence = TEST_CASES[name]['sequence']
  expected = TEST_CASES[name]['outcome']
  result = green('- PASS -') if Y(sequence)==expected else red('! FAIL !')
  print(f'{name}\n{sequence}\n{result}')