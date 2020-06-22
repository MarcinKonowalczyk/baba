f='for ';r='return ';l='.lower()';i=' in ';t='\n\t\t\t'
exec(f'''e=enumerate;v=reversed;X=Exception;t=tuple;z=zip
P=t('ypn');N=t('bfr');E=t('BFR')
exec('ip%sx{i}P;io%sx{i}N;ie%sx{i}E;tr%s[c {f}c{i}z(*x)];f%s[t(v(r)){f}r{i}x]'%(('=lambda x:',)*5))
exec('rp%sf(tr(g));rm%str(f(g));rh%sf(tr(f(tr(g))));rz%sg'%(('=lambda g:',)*4))
from collections import deque
def et(seq):
	w=deque(maxlen=3);i=3
	{f}_{i}map(w.append,seq):
		i-=1
		if not i:i=1; yield t(w)
def F(g):
	iu=lambda t:(io(t[0])and t[1]=='i')and(io(t[2])or ip(t[2]));s=[]
	{f}r{i}g:
		{f}t{i}et(r):{t}if iu(t):s.append((t[0],t[2]))
	{f}c{i}z(*g):
		{f}t{i}et(c):{t}if iu(t):s.append((t[0],t[2]))
	{r}sorted(s)
def R(r):
	b={{n:dict(z(P,(False,)*3)){f}n{i}N}};s=[]
	{f}j,a{i}r:
		if ip(a):b[j][a]=True
		else:s.append((j,a))
	{r}b,sorted(s)
class U(X):pass
def at(p,b):
	if len(p)==0:raise U
	if p[0]=='.':{r}p
	elif len(p)==1:raise U
	h=lambda c:(ie(c)and b[c{l}]['p'])or c{i}(*P,*N,'i')
	if not h(p[0]):raise U
	if p[1]=='.':{r}(p[1],p[0],*p[2:])
	else:q=at(p[1:],b);{r}(q[0],p[0],*q[1:])
S=t('^V<>')
qp=dict(z(S,(rz,rh,rp,rm)));qm=dict(z(S,(rz,rh,rm,rp)))
class W(X):pass
def T(g,b,s):
	g=qp[s](g);h=[['.'{f}_{i}r]{f}r{i}g];iy=lambda c:ie(c)and b[c{l}]['y'];iw=lambda c:ie(c)and b[c{l}]['n']
	{f}j,r{i}e(g):
		{f}k,cell{i}e(r):{t}if not iy(cell):h[j][k]=cell;continue{t}p=[h[l][k]{f}l{i}v(range(j))]{t}try:{t}	q=at(p,b){t}	{f}l,m{i}e(v(q)):h[l][k]=m{t}	h[j-1][k]=cell{t}except U:{t}	if len(p)>0 and iw(p[0]):raise W{t}	h[j][k]=cell
	{r}qm[s](h)
def S(g,s):
	h=[[c {f}c{i}r]{f}r{i}g]
	{f}a,b{i}s:
		{f}j,r{i}e(g):{t}{f}k,c{i}e(r):{t}	if ie(c)and c{l}==a and h[j][k]is c:h[j][k]=b.upper()
	{r}h
def Y(q):
	g=[[c {f}c{i}r]{f}r{i}('.'*13+'|.rip....RRR..|.......R...R.|.biy.B.R.F.R.|.......R...R.|.fin....RRR..|'+'.'*13).split('|')]
	try:
		{f}p{i}(*q,None):{t}b,s=R(F(g)){t}{f}n{i}b:{t}	if b[n]['y']and b[n]['n']:raise W{t}g=S(g,s){t}if p:g=T(g,b,p)
	except W:{r}1
	{r}0''')

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
		('<V<<<<V>>V>^^>>^^>>^>>V',0),
		('<V<<<<V>>V>>^^VV>^^',0),
		('<V<<V^<V>>>^^<^>^^<<V^<<VV>>>^>VVVV^^^<<<<^>>^>VVVV>>V^<<V>>^^>>',1),
		('>VV>^^<^>V>^VV<<<<<<<V^>V>>^>V^^<<^>^^<<V^<<VV>>>^>VVVV^^^<<<<^>>^>VVVVV^^>>>>>>',1),
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