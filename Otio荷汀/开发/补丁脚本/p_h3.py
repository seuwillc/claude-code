d='/tmp/claude-0/-home-user-claude-code/5304f462-4324-55e0-ae4d-a872d232e3d9/scratchpad/'
p=d+'sgtob/vera-care-sg.html';s=open(p,encoding='utf-8').read()
def R(a,b):
    global s
    assert s.count(a)==1,(a[:70],s.count(a));s=s.replace(a,b)
# 2 compact metric rows
a=s.index(" const rows=[\n  vrow({go:'trend:vit'");b=s.index(" ];",a)+3
s=s[:a]+r""" const mrow=(go,icn,k,st,v,u,bad)=>`<button class="li" data-go="${go}"><span class="ic">${ic(icn)}</span><span class="t">${k}<small style="${bad?'color:var(--tLow)':''}">${st}</small></span><span class="r"><b class="num" style="font-size:22px;font-weight:500;color:var(--tx)">${v}</b>${u?` <span class="sm mu">${u}</span>`:''}</span><span class="chev">${ic('chev',16)}</span></button>`;
 const rows=[
  mrow('trend:vit','leaf',L('元气','Vitality'),n?L('比平常低','Below usual'):L('和平常差不多','About usual'),vit(),'',n),
  mrow('trend:sleep','moon',L('睡眠','Sleep'),n?L('醒了 3 次','Woke 3 times'):L('比平时多 15 分钟','15 min more than usual'),n?'6:05':'6:48','',n),
  mrow('trend:rhr','heart',L('心率','Heart rate'),n?L('静息心率偏高 · HRV 偏低','Resting HR high · HRV low'):L('静息心率、HRV 和平常差不多','Resting HR and HRV about usual'),n?71:62,L('次/分','bpm'),n),
  mrow('oxygen','wind',L('夜间呼吸与血氧','Night breathing & oxygen'),n?L('血氧最低 88%','Oxygen low 88%'):L('和过去 30 晚差不多','Like the last 30 nights'),n?'13.2':'14.6',L('次/分','/min'),n),
  mrow('trend:steps','run',L('活动','Activity'),L('近 7 天平均','7-day average'),'6,480',L('步','steps'),0),
 ];"""+s[b:]
R('<div class="card vitals">${rows.join(\'\')}</div>','<div class="card flush">${rows.join(\'\')}</div>')
# 1 remove sleep timing card from health
a=s.index("  ${irr?`<div class=\"card\"><div class=\"between\"><span class=\"h3\">${L('作息规律'");b=s.index("`:''}\n",a)+len("`:''}\n")
s=s[:a]+s[b:]
# add calendar card into sleep trend page + source line in trend
R("""  <div class="card"><div class="h3">${L('什么是 ','What is ')+m.n}</div>""","""  ${k==='sleep'?`<div class="card"><div class="between"><span class="h3">${L('作息规律','Sleep timing')}</span><span class="sm mu">${L('近 4 周，周五周六睡得晚','Last 4 weeks: later on Fri and Sat')}</span></div><div style="margin-top:10px">${calendar()}</div></div>`:''}
  <p class="sm mu" style="margin:0">${k==='steps'?L('戒指和手机','Ring and phone'):L('荷汀戒指 · 参考数据','Otio ring · for context')}${linked()&&['sleep','rhr','hrv','resp'].includes(k)?' · '+L('护理团队可见','care team sees'):''}</p>
  <div class="card"><div class="h3">${L('什么是 ','What is ')+m.n}</div>""")
# 3 compact lotus card in health (linked)
R("function lotusCard(){","function lotusMini(){return `<div class=\"card\" style=\"display:flex;gap:12px;align-items:center;padding:12px 14px\"><span style=\"flex:none;width:44px;height:44px;border-radius:12px;overflow:hidden;background:var(--sf2)\"><img src=\"${LOTUSIMG}\" alt=\"\" style=\"width:100%;height:100%;object-fit:cover\"></span><span style=\"flex:1;min-width:0\"><span class=\"h3\" style=\"display:block\">${L('荷息','Lotus breath')}</span><span style=\"display:flex;gap:8px;margin-top:6px\"><button class=\"btn sm\" data-go=\"breath:1\">${L('一分钟','1 min')}</button><button class=\"btn sm ghost\" data-go=\"breath:478\">4-7-8</button></span></span></div>`}\nfunction lotusCard(){")
a=s.index("P.health=()=>");b=s.index("/* generic metric page */",a)
seg=s[a:b];assert seg.count("${lotusCard()}")==1;seg=seg.replace("${lotusCard()}","${lotusMini()}");s=s[:a]+seg+s[b:]
R("L('<b>v3.8.16</b>：","L('<b>v3.8.17</b>：身体页缩短：指标改成一行一个（名字、状态、数值），范围和来源放进趋势页；作息规律从身体页移到“睡眠”趋势页；连诊所时荷息改成小卡。<br><b>v3.8.16</b>：")
R("'<b>v3.8.16</b>: How","'<b>v3.8.17</b>: Health shortened: one line per number (name, status, value), with ranges and sources on the trend page; sleep timing moved to the Sleep trend; a small lotus card when linked.<br><b>v3.8.16</b>: How")
open(p,'w',encoding='utf-8').write(s)
i=s.rindex('})();');s=s[:i]+'window.__t={get S(){return S},go,render};\n'+s[i:]
open(d+'otiagen/sw_test.html','w',encoding='utf-8').write(s)
print('ok')
