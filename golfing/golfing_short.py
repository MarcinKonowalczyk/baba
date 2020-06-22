e=enumerate;v=reversed;X=Exception;t=tuple;z=zip
P=t('ypn');N=t('bfr');E=t('BFR')
exec('ip%sx in P;io%sx in N;ie%sx in E;tr%s[c for c in z(*x)];f%s[t(v(r))for r in x]'%(('=lambda x:',)*5))
exec('rp%sf(tr(g));rm%str(f(g));rh%sf(tr(f(tr(g))));rz%sg'%(('=lambda g:',)*4))
from collections import deque
def et(seq):
	w=deque(maxlen=3);i=3
	for _ in map(w.append,seq):
		i-=1
		if not i:i=1; yield t(w)
def F(g):
	iu=lambda t:(io(t[0])and t[1]=='i')and(io(t[2])or ip(t[2]));s=[]
	for r in g:
		for t in et(r):
			if iu(t):s.append((t[0],t[2]))
	for c in z(*g):
		for t in et(c):
			if iu(t):s.append((t[0],t[2]))
	return sorted(s)
def R(r):
	b={n:dict(z(P,(False,)*3))for n in N};s=[]
	for j,a in r:
		if ip(a):b[j][a]=True
		else:s.append((j,a))
	return b,sorted(s)
class U(X):pass
def at(p,b):
	if len(p)==0:raise U
	if p[0]=='.':return p
	elif len(p)==1:raise U
	h=lambda c:(ie(c)and b[c.lower()]['p'])or c in(*P,*N,'i')
	if not h(p[0]):raise U
	if p[1]=='.':return(p[1],p[0],*p[2:])
	else:q=at(p[1:],b);return(q[0],p[0],*q[1:])
S=t('^V<>')
qp=dict(z(S,(rz,rh,rp,rm)));qm=dict(z(S,(rz,rh,rm,rp)))
class W(X):pass
def T(g,b,s):
	g=qp[s](g);h=[['.'for _ in r]for r in g];iy=lambda c:ie(c)and b[c.lower()]['y'];iw=lambda c:ie(c)and b[c.lower()]['n']
	for j,r in e(g):
		for k,cell in e(r):
			if not iy(cell):h[j][k]=cell;continue
			p=[h[l][k]for l in v(range(j))]
			try:
				q=at(p,b)
				for l,m in e(v(q)):h[l][k]=m
				h[j-1][k]=cell
			except U:
				if len(p)>0 and iw(p[0]):raise W
				h[j][k]=cell
	return qm[s](h)
def S(g,s):
	h=[[c for c in r]for r in g]
	for a,b in s:
		for j,r in e(g):
			for k,c in e(r):
				if ie(c)and c.lower()==a and h[j][k]is c:h[j][k]=b.upper()
	return h
def Y(q):
	g=[[c for c in r]for r in('.'*13+'|.rip....RRR..|.......R...R.|.biy.B.R.F.R.|.......R...R.|.fin....RRR..|'+'.'*13).split('|')]
	try:
		for p in(*q,None):
			b,s=R(F(g))
			for n in b:
				if b[n]['y']and b[n]['n']:raise W
			g=S(g,s)
			if p:g=T(g,b,p)
	except W:return 1
	return 0

if __name__ == '__main__':

    # A pile of test sequences and the result expected on the golfing grid
    tests = (('>>^>>V',1),
        ('<^<V',0),
        ('<^^^<<V^>>VV<<>>',1),
        ('<VV<V<<^V>>^<',1),
        ('<^^^<<V>V<>>',1),
        ('<^^^<<V^<<VV>><<^>><<',1),
        ('<VVV<^<^>V>^^V<<<<^^^>^>>>>VVV<^>>>',1),
        ('<^<<<<V>>>V>VV<<^^^>^<VV>>V<V<^^>^<V>>>>>>>V<^^^^>^<<<<<<<<<',1),
        ('<V<<<<V>>V>^^',0),
        ('<V<<<<V>>V>>^^VV>^^',0),
        ('<V<<V^<V>>>^^<^>^^<<V^<<VV>>>^>VVVV^^^<<<<^>>^>VVVV>>V^<<V>>^^>>',1),
        ('<V<<<<V>>V>>>^V<<<^>V>>^V<<^>V>>^^^>>^>>V',0),
        ('<V<<<<V>>V>>>^V<<<^>V>>^V<<^>><^^^>V>V<^<V<VV>>>>^<<<>^^>>^>>V',0),
        ('<^<<<<V>>^<<^^>>V^<<VV>>^><V><V><<<VVV>^^<^>>V>^^<^>VVV>VV<<^^^<^>V>^<^>><<V<<^>>>>>V<^<VV<<',1),
        ('<^<<<<V>>^<<^^>>VV<V>V>>VV<<^V<<^>^^^<^>^>VV>V<V<V>^^>V>V>>>^^<<',1),
        ('<^^^<<V^<<V><VVVVV>>^V<<^>^<^><',0),
        ('<^^^<<V^<<V>>>><<<V>>><<<<VVVV>>^V<<<^^>>>><<<<V>>>><<<<^^>>>><',0),
		('VVVV>>>>>>>>^^^^^^^>^^>^>^<<<<<<<<<<<<<VVVVVVV^^>>>>>>>>^>',1))

    green = lambda x: f'\x1b[32m{x}\x1b[0m'
    red = lambda x: f'\x1b[31m{x}\x1b[0m'
    for sequence,expected in tests:
        result = green('- PASS -') if Y(sequence)==expected else red('! FAIL !')
        print(f'{sequence}\n{result}')