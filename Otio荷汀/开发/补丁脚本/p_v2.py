import re
d='/tmp/claude-0/-home-user-claude-code/5304f462-4324-55e0-ae4d-a872d232e3d9/scratchpad/'
p=d+'sgtob/vera-care-sg.html';s=open(p,encoding='utf-8').read()
def R(a,b):
    global s
    assert s.count(a)==1,(a[:70],s.count(a));s=s.replace(a,b)
# helpers
R("function lotusMini(){","""function rb(c,lo,hi,v,fmt){fmt=fmt||(x=>x);const w=Math.max(hi-lo,1e-6);let mn=lo-w*1.1,mx=hi+w*1.1;if(v!=null){mn=Math.min(mn,v-w*.4);mx=Math.max(mx,v+w*.4)}return rbar(c,lo,hi,mn,mx,v,[fmt(lo),fmt(hi)])}
function vrow2(o){return `<button class="vrow2" style="--c:${o.c}" data-go="${o.go}"><span class="ic">${ic(o.ic,17)}</span><span class="nm"><b>${o.k}</b><span class="st">${o.st}</span></span><span class="rt">${o.v!==''&&o.v!=null?`<span class="vv">${o.v}${o.u?`<small>${o.u}</small>`:''}</span>`:`<span class="sm mu" style="white-space:nowrap">${o.u||''}</span>`}${o.bar||''}</span><span class="chev">${ic('chev',14)}</span></button>`}
function lotusMini(){""")
a=s.index("P.health=()=>");b=s.index("/* generic metric page */",a);seg=s[a:b]
seg=seg.replace("vrow({","vrow2({")
seg=re.sub(r",src:`[^`]*`","",seg)
seg=re.sub(r",src:ring\([01]\)","",seg)
# autoscale bars
seg=seg.replace("rbar('var(--c-sq)',65,69,45,90,vit(),[65,69])","rb('var(--c-sq)',65,69,vit())")
seg=seg.replace("rbar('var(--c-dl)',6.5,6.75,4,9,n?6.08:6.8,['6:29','6:44'])","rb('var(--c-dl)',6.48,6.73,n?6.08:6.8,x=>Math.floor(x)+':'+String(Math.round(x%1*60)).padStart(2,'0'))")
seg=seg.replace("rbar('var(--c-oh)',61,63,50,80,n?71:62,[61,63])","rb('var(--c-oh)',61,63,n?71:62)")
seg=seg.replace("(()=>{const t=tband('resp');return rbar('var(--c-tsb)',t[0],t[1],12,17,n?13.2:14.6,[t[0].toFixed(1),t[1].toFixed(1)])})()","(()=>{const t=tband('resp');return rb('var(--c-tsb)',+t[0].toFixed(1),+t[1].toFixed(1),n?13.2:14.6)})()")
seg=seg.replace("(()=>{const t=tband('spo2');return rbar('var(--c-qb)',t[0],t[1],88,100,n?93:95,[t[0].toFixed(1),t[1].toFixed(1)])})()","(()=>{const t=tband('spo2');return rb('var(--c-qb)',+t[0].toFixed(1),+t[1].toFixed(1),n?93:95)})()")
seg=seg.replace("rbar('var(--c-zs)',5800,6700,3000,10000,6480,['5,800','6,700'])","rb('var(--c-zs)',5800,6700,6480,x=>x.toLocaleString('en-US'))")
seg=seg.replace("rbar('var(--c-jz)',110,135,95,180,b?172:128,[lk?L('目标','target'):L('参考','ref'),'<135'])","rbar('var(--c-jz)',110,135,100,175,b?172:128,[lk?L('目标','target'):L('参考','ref'),'<135'])")
seg=seg.replace("rbar('var(--c-xs)',3.9,10,2.5,14,6.2,['3.9','10'])","rb('var(--c-xs)',3.9,10,6.2)")
seg=seg.replace('<div class="card vitals">','<div class="card vitals2">')
s=s[:a]+seg+s[b:]
css="""
.card.vitals2{padding:0;overflow:hidden}
.vrow2{display:grid;grid-template-columns:30px 1fr minmax(128px,46%) 14px;gap:0 10px;align-items:center;width:100%;padding:12px 12px 10px 14px;background:linear-gradient(90deg,color-mix(in srgb,var(--c) 14%,transparent),color-mix(in srgb,var(--c) 4%,transparent));border:0;color:inherit;font:inherit;text-align:left;cursor:pointer}
.vrow2+.vrow2{box-shadow:inset 0 1px 0 var(--line)}
.vrow2 .ic{width:30px;height:30px;border-radius:50%;display:grid;place-items:center;color:var(--c);background:color-mix(in srgb,var(--c) 16%,transparent)}
.vrow2 .nm b{display:block;font-size:16px;font-weight:600}.vrow2 .nm .st{display:block;font-size:13px;font-weight:600;color:var(--c);margin-top:1px;line-height:1.35}
.vrow2 .rt{display:flex;flex-direction:column;align-items:stretch;text-align:right}
.vrow2 .vv{font-family:var(--num);font-size:30px;font-weight:500;line-height:1}.vrow2 .vv small{font-family:var(--sans);font-size:12px;color:var(--mu);margin-left:3px}
.vrow2 .rbar{margin-top:4px;height:26px}
.vrow2 .chev{color:var(--mu)}
"""
i=s.index('</style>');s=s[:i]+css+s[i:]
R("L('<b>v3.8.20</b>：","L('<b>v3.8.21</b>：身体页压缩：大数字和平常范围条放右侧，来源和“护理团队可见”移到详情页；范围条按每项自动缩放（同中国版，亮段占约三分之一，今天的点能看出变化）。<br><b>v3.8.20</b>：")
R("'<b>v3.8.20</b>: Both","'<b>v3.8.21</b>: Health compressed: large number and usual-range bar on the right; source and care-team marks moved to detail pages; bars scale per measure as in the China version, so today’s dot visibly moves.<br><b>v3.8.20</b>: Both")
open(p,'w',encoding='utf-8').write(s)
i=s.rindex('})();');s=s[:i]+'window.__t={get S(){return S},go,render,tband,tseries};\n'+s[i:]
open(d+'otiagen/sw_test.html','w',encoding='utf-8').write(s)
print(seg.count('vrow2('), seg.count('rbar('), seg.count('rb('))
