import sys
d='/tmp/claude-0/-home-user-claude-code/5304f462-4324-55e0-ae4d-a872d232e3d9/scratchpad/'
p=d+'sgtob/vera-care-sg.html';s=open(p,encoding='utf-8').read()
def R(a,b):
    global s
    assert s.count(a)==1,(a[:60],s.count(a));s=s.replace(a,b)
R("""  if(linked()){const k=S.tm==='night'?'med2':'bppm';return S.tm==='night'?{t:L('22:30 阿托伐他汀 20 mg','22:30 Atorvastatin 20 mg'),act:'one'}:{t:L('20:00 晚上量血压','8 pm evening BP'),act:'one'}}""",
"""  if(linked())return S.tm==='night'?{t:L('22:30 阿托伐他汀 20 mg','22:30 Atorvastatin 20 mg'),src:'care',id:'med2',kind:'med'}:{t:L('20:00 晚上量血压','8 pm evening BP'),src:'care',id:'bppm',kind:'bp'};""")
R("""  if(!nx)return{t:L('明天 '+m.wake+' 起床','Up at '+m.wake+' tomorrow'),act:'one'};""","""  if(!nx)return{t:L('明天 '+m.wake+' 起床','Up at '+m.wake+' tomorrow'),src:'none'};""")
R("""rain?L(' · 傍晚有雨，组屋走廊也行',' · rain later, the HDB corridor works too'):''),act:'one'}}""",
"""rain?L(' · 傍晚有雨，组屋走廊也行',' · rain later, the HDB corridor works too'):''),src:'plan',id:nx.id,kind:nx.go?'go':nx.id==='bpam'?'bp':nx.k==='med'?'med':nx.auto?'ring':'manual',go:nx.go}}""")
R("""function oneRow(){const o=oneThing(),done=o.done||(o.act&&S.oneDone);""",
"""function oneRow(){const o=oneThing();
  if(o.src==='care'||o.src==='plan'||o.src==='none'){const done=o.src==='care'?!!S.tasks[o.id]:o.src==='plan'?isDone(o.id):false;
   const right=done?`<span class="sm mu">${o.kind==='med'?L('已吃','Taken'):L('完成','Done')}</span>`:o.kind==='med'?`<button class="btn sm" data-act="one2" data-v="${o.src}:${o.id}">${L('吃了','Taken')}</button>`:o.kind==='manual'?`<button class="btn sm ghost" data-act="one2" data-v="${o.src}:${o.id}">${L('做了','Done')}</button>`:o.kind==='go'?`<button class="btn sm ghost" data-go="${o.go}">${L('打开','Open')}</button>`:o.kind==='ring'?`<span class="sm mu">${L('戒指自动记','Ring records it')}</span>`:o.kind==='bp'?`<span class="sm mu">${L('血压计自动记','BP monitor records it')}</span>`:'';
   return `<div class="onerow"><span class="ring0${done?' on':''}" aria-hidden="true">${done?ic('check',12,2.6):''}</span><span class="t">${o.t}</span>${right}</div>`}
  const done=o.done||(o.act&&S.oneDone);""")
R("    qoff(){","    one2(){const [src,id]=v.split(':');if(src==='care')S.tasks[id]=!S.tasks[id];else{const m=MP();m.done=m.done.includes(id)?m.done.filter(x=>x!==id):m.done.concat(id)}render()},\n    qoff(){")
R("L('<b>v3.8.6</b>：","L('<b>v3.8.7</b>：首页“一件事”和护理计划、计划页用同一条记录；右侧按类型显示：吃药“吃了”，戒指或血压计能记的写“自动记”不放按钮，其他“做了”；去掉含义不清的“+”。<br><b>v3.8.6</b>：")
R("'<b>v3.8.6</b>: Date","'<b>v3.8.7</b>: Today’s one thing shares its record with the care plan and plan; the right side depends on the item (Taken for medicines, auto-recorded items show no button, otherwise Done); the unclear + is gone.<br><b>v3.8.6</b>: Date")
open(p,'w',encoding='utf-8').write(s)
i=s.rindex('})();');s=s[:i]+'window.__t={get S(){return S},go,render};\n'+s[i:]
open(d+'otiagen/sw_test.html','w',encoding='utf-8').write(s)
