import json,base64,glob,os,re
here=os.path.dirname(os.path.abspath(__file__))
s=open(os.path.join(here,'src.html')).read()
A={os.path.basename(f)[:-4]:'data:audio/mpeg;base64,'+base64.b64encode(open(f,'rb').read()).decode() for f in sorted(glob.glob(os.path.join(here,'build','*.mp3')))}
T=json.load(open(os.path.join(here,'audio','timings.json')))
T={('story-'+k if not k.startswith(('intro','night')) else k):[[w[0],w[1],w[2]] for w in v] for k,v in T.items()}
s=s.replace('/*ASSETS*/{}/*END*/',json.dumps(A)).replace('/*TIMINGS*/{}/*END*/',json.dumps(T,separators=(',',':')))
open(os.path.join(here,'index.html'),'w').write(s)
print(len(A),'assets',len(T),'timings',round(len(s)/1e6,2),'MB')
