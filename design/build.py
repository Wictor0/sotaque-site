import re
s=open('/home/claude/src/Main.src.html').read()
v=open('/home/claude/stq/STQ/Vector.svg').read()
ds=[re.search(r'd="([^"]+)"',p).group(1) for p in re.findall(r'<path\b.*?/>',v,re.S)]
stq=open('/home/claude/stq_new_paths.txt').read()
for i,d in enumerate(ds): s=s.replace('%%D'+str(i)+'%%',d)
import json
st=json.load(open('/home/claude/styles.json'))
BJ=json.load(open('/home/claude/brand.json'))
brand=BJ['brand']; mo=BJ['mono']
mono={'S':mo['s'],'O':mo['s'],'T':mo['t'],'A':mo['t'],'Q':mo['q'],'U':mo['q'],'E':mo['q']}
for kk,vv in brand.items(): s=s.replace('%%B_'+kk+'%%',vv)
s=s.replace('%%STYLES%%',json.dumps([{'n':'brand','L':brand}]+st+[{'n':'mono','L':mono}],separators=(',',':')))
s=s.replace('%%STQ%%',stq); assert '%%' not in s and '"%M' not in s
P='/tmp/claude-0/-home-claude/5c0eb615-8342-5b98-9e59-c48af48f4d48/scratchpad/canvas/project/'
open(P+'Main.dc.html','w').write(s)
m=s.replace('<title>Sotaque — Landing</title>','<title>Sotaque — Landing mobile</title>').replace('"$preview":{"width":1440,"height":8600}','"$preview":{"width":390,"height":9400}')
assert m!=s
open(P+'Mobile.dc.html','w').write(m)
open('/home/claude/harness/main.html','w').write(s.replace('<script src="./support.js"></script>','<script src="./dc-runtime.js"></script>'))
open('/home/claude/harness/mob.html','w').write(m.replace('<script src="./support.js"></script>','<script src="./dc-runtime.js"></script>'))
print('ok')
