d='/tmp/claude-0/-home-user-claude-code/5304f462-4324-55e0-ae4d-a872d232e3d9/scratchpad/'
p=d+'sgtob/vera-care-sg.html';s=open(p,encoding='utf-8').read()
def R(a,b):
    global s
    assert s.count(a)==1,(a[:70],s.count(a));s=s.replace(a,b)
# ring colours
R("const col=t==='low'?'var(--tLow)':t==='mid'?'var(--tMid)':t==='ok'?'var(--tOk)':'var(--mu)';","const col=t==='low'||t==='mid'?'var(--tLow)':o.c||(t==='ok'?'var(--tOk)':'var(--mu)');")
R("""<path d="${arc(ang(o.lo),ang(o.hi))}" fill="none" stroke="var(--tx)" stroke-opacity=".5" stroke-width="6" stroke-linecap="round"/>""","""<path d="${arc(ang(o.lo),ang(o.hi))}" fill="none" stroke="${o.c||'var(--tx)'}" stroke-opacity=".5" stroke-width="6" stroke-linecap="round"/>""")
R("o:{lo:62,hi:76,mn:45,mx:90},t:low?'low':'ok',st:low?L('比平常低','Below usual'):'',go:'metric:vit'}","o:{lo:65,hi:69,mn:55,mx:79,c:'var(--c-sq)'},t:low?'low':'ok',st:low?L('比平常低','Below usual'):'',go:'trend:vit'}")
R("o:{lo:6.3,hi:7.2,mn:4,mx:9.5},t:low?'mid':'ok',st:low?L('夜里醒了 3 次','Woke 3 times'):'',go:'metric:sleep'}","o:{lo:6.48,hi:6.73,mn:5.5,mx:7.7,c:'var(--c-dl)'},t:low?'mid':'ok',st:low?L('夜里醒了 3 次','Woke 3 times'):'',go:'trend:sleep'}")
R("o:{lo:5000,hi:7000,mn:0,mx:9000},t:'',st:'',go:'metric:act'","o:{lo:5800,hi:6700,mn:0,mx:9000,c:'var(--c-zs)'},t:'ok',st:'',go:'trend:steps'")
# entries -> watch list
a=s.index("function entries(){");b=s.index("\nP.today=",a)
s=s[:a]+r"""function entries(){const n=S.scen==='night',b=S.scen==='bp',rows=[];
  if(n){rows.push(vrow2({go:'trend:spo2',c:'var(--c-qb)',ic:'drop',k:L('血氧','Oxygen'),st:`<span style="color:var(--tLow)">${L('最低 88%','Lowest 88%')}</span>`,v:93,u:'%'}));
   rows.push(vrow2({go:'trend:rhr',c:'var(--c-oh)',ic:'heart',k:L('静息心率','Resting heart rate'),st:`<span style="color:var(--tLow)">${L('比平常高','Above usual')}</span>`,v:71,u:L('次/分','bpm')}))}
  if(b)rows.push(vrow2({go:'bp',c:'var(--c-jz)',ic:'gauge',k:L('血压','Blood pressure'),st:`<span style="color:var(--tLow)">${L('高于上限','Above limit')}</span>`,v:'172/104',u:'mmHg'}));
  if(!rows.length)return `<button class="link" data-act="gohealth" style="text-align:left;color:var(--mu);font-weight:500;padding:4px 2px">${L('其他各项都和平常差不多 · 去身体页看看 ›','Everything else is about usual · see Health ›')}</button>`;
  return `<div><div class="h3" style="margin:0 2px 8px">${L('今天要留意的','Worth a look today')}</div><div class="card vitals2">${rows.join('')}</div></div>`}"""+s[b:]
R("    qoff(){","    gohealth(){S.stack=['health'];render(true)},\n    qoff(){")
# delete old hrv page; route metric:hr to trend
a=s.index("P.hrv=()=>{");b=s.index("\n",s.index("`}};",a))+1
s=s[:a]+s[b:]
R("P.metric=k=>{if(k==='hr')return P.hrv();","P.metric=k=>{if(k==='hr')return P.trend('rhr');")
R("L('<b>v3.8.22</b>：","L('<b>v3.8.23</b>：首页联动：三个圆环换成和身体页同一套传统色，点进趋势页；原来的心率、呼吸血氧、血压三行改成“今天要留意的”，只在有异常时出现（样式同身体页），平常显示一行“其他各项都和平常差不多 · 去身体页看看”；删掉旧的“静息心率与 HRV”页。<br><b>v3.8.22</b>：")
R("'<b>v3.8.22</b>: Health","'<b>v3.8.23</b>: Today linked to Health: the three rings use the same traditional colours and open trends; the heart/breathing/BP rows become Worth a look today, shown only when something is off (Health style), otherwise one line pointing to Health; the old resting HR & HRV page is removed.<br><b>v3.8.22</b>: Health")
open(p,'w',encoding='utf-8').write(s)
i=s.rindex('})();');s=s[:i]+'window.__t={get S(){return S},go,render,tband,tseries};\n'+s[i:]
open(d+'otiagen/sw_test.html','w',encoding='utf-8').write(s)
print('ok')
