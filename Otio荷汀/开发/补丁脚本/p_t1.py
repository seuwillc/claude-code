import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a)); s=s.replace(a,b)
# 4 why 90%
R("L('凌晨 4:40 最低 88%，低于 90% 约 6 分钟；早上心率也比平常高。'","L('凌晨 4:40 最低 88%（戒指估算）；早上心率也比平常高。'")
R("'Lowest 88% at 4:40 am, about 6 minutes below 90%. Your heart","'Lowest 88% at 4:40 am (ring estimate). Your heart")
# 2 one thing from plan
R("""  if(S.tm==='afternoon')return{t:L('晚饭后量血压','Take your BP after dinner'),act:'one'};
  return{t:L('雨前出门走 20 分钟','Walk 20 minutes before the rain'),act:'one'}}""",
"""  if(linked()){const k=S.tm==='night'?'med2':'bppm';return S.tm==='night'?{t:L('22:30 阿托伐他汀 20 mg','22:30 Atorvastatin 20 mg'),act:'one'}:{t:L('20:00 晚上量血压','8 pm evening BP'),act:'one'}}
  const m=MP(),nx=mpItems().find(x=>mpT(x.t)>S.hour&&!isDone(x.id)&&!m.skip.includes(x.id)&&x.id!=='wake');
  if(!nx)return{t:L('明天 '+m.wake+' 起床','Up at '+m.wake+' tomorrow'),act:'one'};
  const rain=nx.id==='walk'&&m.when!=='morning'&&S.tm!=='night';
  return{t:nx.t+' '+nx.a+(rain?L(' · 傍晚有雨，组屋走廊也行',' · rain later, the HDB corridor works too'):''),act:'one'}}""")
R("  if(S.tm==='night')return{t:L('23:00 前上床','In bed by 11 pm'),act:'one'};\n","")
# 7 weather
R("function dateLine(){const wx=S.tm==='afternoon'?'rain':dark()?'moon':'sun';","function dateLine(){const wx=S.tm==='afternoon'?'rain':dark()?'moon':'sun',later=S.tm==='morning'?` → ${ic('rain',14)} ${L('午后雷雨','storms later')}`:'';")
R("${ic(wx,14)} <span class=\"num\">25–32°</span>","${ic(wx,14)}${later} <span class=\"num\">25–32°</span>")
# 3 today line
R("""function seasonLine(){return `<button class="sline" data-act="season"><span class="sk">${L('雨','☂')}</span><span class="t">${L('季风转换期 · 午后多雷阵雨','Inter-monsoon · afternoon thunderstorms')}</span><span class="chev">${ic('chev',16)}</span></button>`}""",
"""function seasonLine(){if(S.qOff)return '';const q=S.tm==='night'?[L('月','☾'),L('今晚早点歇，明天的元气多半看这一觉。','Rest early; tomorrow’s energy mostly comes from tonight.')]:S.tm==='afternoon'?[L('茶','☕'),L('外面下着雨，适合在家泡杯茶。','Rain outside: a good time for a pot of tea.')]:S.scen==='normal'?[L('庄','☯'),L('昨晚睡得沉。庄子说“其寝不梦，其觉无忧”。','A deep sleep last night. Zhuangzi: “sleeping without dreams, waking without worry.”')]:[L('慢','~'),L('不急，一步一步来。','No rush, one step at a time.')];
 return `<div class="sline"><span class="sk">${q[0]}</span><span class="t">${q[1]}</span><button class="link" data-act="qoff" aria-label="${L('收起','Hide')}" style="min-height:0;padding:0 4px;color:var(--mu)">×</button></div>`}""")
R("    one(){S.oneDone=!S.oneDone;render()},","    one(){S.oneDone=!S.oneDone;render()},\n    qoff(){S.qOff=1;render()},")
# 1 HRV in hr page
R("P.metric=k=>{const m=MET[k||'vit']();return{calm:1,html:`${nav(m.t)}<div class=\"pad stack\">\n  <div class=\"card\"><div class=\"eyebrow\">${L('今天','Today')}</div><div class=\"bign\">${m.v}<small>${m.u}</small></div>${trend(m.d,m.lo,m.hi,m.mn,m.mx,m.c)}</div>",
"P.metric=k=>{const m=MET[k||'vit']();return{calm:1,html:`${nav(k==='hr'?L('静息心率与 HRV','Resting heart rate & HRV'):m.t)}<div class=\"pad stack\">\n  <div class=\"card\"><div class=\"eyebrow\">${k==='hr'?L('静息心率 · 今天','Resting heart rate · today'):L('今天','Today')}</div><div class=\"bign\">${m.v}<small>${m.u}</small></div>${trend(m.d,m.lo,m.hi,m.mn,m.mx,m.c)}</div>${k==='hr'?`<div class=\"card\"><div class=\"eyebrow\">${L('心跳的细微变化（HRV）· 昨晚','Heart rate variability (HRV) · last night')}</div><div class=\"bign\">${S.scen==='night'?24:31}<small>${L('毫秒','ms')}</small></div>${trend([30,33,29,32,31,34,30,28,32,33,31,30,32,S.scen==='night'?24:31],27,35,18,42,'var(--vit)')}<p class=\"sm mu\" style=\"margin:6px 0 0\">${L('越高通常说明身体恢复得越好。和自己的平常比，不和别人比。','Higher usually means better recovery. Compare with your own usual, not with others.')}</p></div>`:''}")
# 5 breathing rate
R("<div style=\"text-align:right\"><div class=\"eyebrow\">${L('最低','Lowest')}</div><div class=\"bign\" style=\"font-size:30px;${dip?'color:var(--tLow)':''}\">${dip?88:92}<small>%</small></div></div></div>",
"<div style=\"text-align:right\"><div class=\"eyebrow\">${L('最低','Lowest')}</div><div class=\"bign\" style=\"font-size:30px;${dip?'color:var(--tLow)':''}\">${dip?88:92}<small>%</small></div></div></div><div class=\"sm mu\" style=\"margin-top:6px\">${L('夜间呼吸 ','Breathing ')}<b class=\"num\" style=\"color:var(--tx)\">${dip?13.2:14.6}</b> ${L('次/分 · 平常 13.8–15.4','breaths/min · usual 13.8–15.4')}</div>")
# 6 appt
R("${row('a',S.scen==='night'?L('夜里血氧低到 88%','Oxygen dipped to 88% overnight'):L('早上偶尔头有点胀','Some mornings my head feels heavy'))}","${S.scen==='night'?row('a',L('夜里血氧低到 88%','Oxygen dipped to 88% overnight')):''}")
R("L('<b>v3.8.1</b>：","L('<b>v3.8.3</b>：首页梳理（只改逻辑和数据）：一件事读计划的下一件事；天气早上显示“→ 午后雷雨”；季风行换成可收起的“今日一句”；解释去掉 90%；心率页加回 HRV（同中国版）；血氧页补夜间呼吸频率；随访页不再预填症状。<br><b>v3.8.1</b>：",1)
R("'<b>v3.8.1</b>: Back","'<b>v3.8.3</b>: Today tidy-up (logic and data only): the one thing reads your plan; the weather shows storms later; the monsoon line becomes a dismissible line of the day; no 90% in the explanation; HRV back on the heart rate page; breathing rate on the oxygen page; no pre-filled symptom on the check-in.<br><b>v3.8.1</b>: Back",1)
open(p,'w',encoding='utf-8').write(s);print('ok')
