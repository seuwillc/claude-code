d='/tmp/claude-0/-home-user-claude-code/5304f462-4324-55e0-ae4d-a872d232e3d9/scratchpad/'
p=d+'sgtob/vera-care-sg.html';s=open(p,encoding='utf-8').read()
def R(a,b):
    global s
    assert s.count(a)==1,(a[:70],s.count(a));s=s.replace(a,b)
# metrics: vrow style, split oxygen
a=s.index(" const mbar=");b=s.index(" ];",a)+3
s=s[:a]+r""" const ring=sh=>`${ic('ring',12)} ${L('荷汀戒指 · 参考数据','Otio ring · for context')}${sh&&lk?' '+seeTag():''}`,lowC=c=>n?'var(--tLow)':c;
 const rows=[
  vrow({go:'trend:vit',c:n?'var(--tLow)':'var(--c-sq)',ic:'leaf',k:L('元气','Vitality'),st:n?L('比平常低','Below usual'):L('和平常差不多','About usual'),v:vit(),bar:rbar('var(--c-sq)',65,69,45,90,vit(),[65,69]),src:ring(0)}),
  vrow({go:'trend:sleep',c:n?'var(--tLow)':'var(--c-dl)',ic:'moon',k:L('睡眠','Sleep'),st:n?L('醒了 3 次','Woke 3 times'):L('比平时多 15 分钟','15 min more than usual'),v:n?'6:05':'6:48',bar:rbar('var(--c-dl)',6.5,6.75,4,9,n?6.08:6.8,['6:29','6:44']),src:ring(1)}),
  vrow({go:'trend:rhr',c:n?'var(--tLow)':'var(--c-oh)',ic:'heart',k:L('心率','Heart rate'),st:n?L('静息心率偏高 · HRV 偏低','Resting HR high · HRV low'):L('静息心率、HRV 和平常差不多','Resting HR and HRV about usual'),v:n?71:62,u:L('次/分 · HRV ','bpm · HRV ')+(n?24:31),bar:rbar('var(--c-oh)',61,63,50,80,n?71:62,[61,63]),src:ring(1)}),
  vrow({go:'trend:resp',c:n?'var(--tLow)':'var(--c-tsb)',ic:'wind',k:L('夜间呼吸','Night breathing'),st:n?L('比平常慢一点','A little slower'):L('近 30 晚相近','Like the last 30 nights'),v:n?'13.2':'14.6',u:L('次/分','/min'),bar:rbar('var(--c-tsb)',13.8,15.4,12,17,n?13.2:14.6,['13.8','15.4']),src:ring(1)}),
  vrow({go:'trend:spo2',c:n?'var(--tLow)':'var(--c-qb)',ic:'drop',k:L('血氧','Oxygen'),st:n?L('最低 88%，比平常低','Lowest 88%, below usual'):L('平均 95% · 最低 92%','Average 95% · lowest 92%'),v:n?'93':'95',u:'% '+L('平均','avg'),bar:rbar('var(--c-qb)',95,97,88,100,n?93:95,['95','97']),src:ring(1)}),
  vrow({go:'trend:steps',c:'var(--c-zs)',ic:'run',k:L('活动','Activity'),st:L('近 7 天平均','7-day average'),v:'6,480',u:L('步','steps'),bar:rbar('var(--c-zs)',5800,6700,3000,10000,6480,['5,800','6,700']),src:ring(0)}),
 ];"""+s[b:]
R("""<div class="card flush crows cm">${rows.join('')}</div>""","""<div class="card vitals">${rows.join('')}</div>""")
# checks: vrow style
a=s.index("""  <div class="card flush crows">\n   ${cli('var(--c-jz)'""");b=s.index("\n  </div>",a)+len("\n  </div>")
s=s[:a]+r"""  <div class="card vitals">
   ${vrow({go:'bp',c:b?'var(--tLow)':'var(--c-jz)',ic:'gauge',k:L('血压','Blood pressure'),st:b?L('今早高于上限','Above limit this morning'):lk?L('早上 · 近 14 天 12 天在目标内','Morning · on target 12 of 14 days'):L('早上 · 在参考值内','Morning · within reference'),v:b?'172/104':'128/80',u:'mmHg',bar:rbar('var(--c-jz)',110,135,95,180,b?172:128,[lk?L('目标','target'):L('参考','ref'),'<135']),src:`${ic('gauge',12)} ${L('血压计 · 医疗器械','BP monitor · medical device')}${lk?' '+seeTag():''}`})}
   ${lk?vrow({go:'ecg',c:'var(--c-ts)',ic:'ecg',k:L('心电','ECG'),st:L('最近一条：窦性心律 · 医生判读','Latest: sinus rhythm · doctor-read'),v:3,u:L('条 · 本月','this month'),src:`${ic('ecg',12)} ${L('心电卡 MD100C','ECG card MD100C')} ${seeTag()}`}):''}
   ${vrow({go:'rhythm',c:'var(--c-oh)',ic:'heart',k:L('夜间心律提示','Night rhythm alerts'),st:L('心跳规不规律（不是快慢）','Whether beats are regular (not how fast)'),v:'',u:L('即将开放','Coming soon'),src:`${ic('ring',12)} ${L('荷汀戒指','Otio ring')}`})}
   ${S.cgm?vrow({go:'glucose',c:'var(--c-xs)',ic:'drop',k:L('血糖','Glucose'),st:L('今天 81% 在范围内','81% in range today'),v:'6.2',u:'mmol/L',bar:rbar('var(--c-xs)',3.9,10,2.5,14,6.2,['3.9','10']),src:`${ic('drop',12)} Sinocare CGM${lk?' '+seeTag():''}`}):vrow({go:'glucose',c:'var(--c-xs)',ic:'drop',k:L('血糖','Glucose'),st:L('关联 Sinocare 连续血糖仪','Link a Sinocare CGM'),v:'',u:L('加上 ›','Add ›')})}
   ${lk?vrow({go:'fundus',c:'var(--c-zq)',ic:'eye',k:L('眼底筛查','Eye screening'),st:L('医生已审阅 · 明年 9 月再拍','Reviewed · next photo Sep next year'),v:'',u:L('9 月 26 日','26 Sep'),src:`${ic('clinic',12)} ${CL()}`}):''}
   ${lk?vrow({go:'report',c:'var(--c-mo)',ic:'doc',k:L('9 月监测报告','September report'),st:L('周医生 10/3 签发','Signed by Dr Zhou 3 Oct'),v:'',u:CL()}):vrow({go:'summary',c:'var(--c-mo)',ic:'file',k:L('复诊一页纸','Visit summary'),st:L('近 30 天的事实和趋势，看诊时给医生看','Your last 30 days, to show your doctor'),v:'',u:''})}
  </div>"""+s[b:]
# new colour 青碧 for oxygen
R(".app{--c-sq:#2E6E7E;",".app{--c-qb:#4A7FB0;--c-sq:#2E6E7E;")
R(".app.mo{--c-sq:#8FC7CF;",".app.mo{--c-qb:#9EC2E6;--c-sq:#8FC7CF;")
# spo2 trend metric
i=s.index("const TMT_=()=>({")+len("const TMT_=()=>({")
s=s[:i]+"""
 spo2:{n:L('夜间血氧','Overnight oxygen'),u:'%',c:'var(--c-qb)',base:95.4,amp:.5,seed:16,lo:88,hi:100,
  what:L('每晚睡着期间逐分钟记录后的平均值，显示每晚的实际数值，并和你过去 30 晚比较。戒指估算，非医疗器械。','The average of minute-by-minute readings while you sleep each night, shown as actual values and compared with your last 30 nights. A ring estimate; not a medical device.'),
  up:L('夜间平均血氧和过去 30 晚差不多。','Similar to your last 30 nights.'),down:L('夜间平均血氧和过去 30 晚差不多。','Similar to your last 30 nights.')},"""+s[i:]
R(" if(k==='vit')out[N-1]=68;"," if(k==='spo2')out[N-1]=S.scen==='night'?93:95;if(k==='vit')out[N-1]=68;")
R("['vit','sleep','rhr','hrv','resp','temp','steps'].map(k=>`<button class=\"li\" data-act=\"tpick\"","['vit','sleep','rhr','hrv','resp','spo2','temp','steps'].map(k=>`<button class=\"li\" data-act=\"tpick\"")
# trend page: night detail link for resp/spo2
R("""  ${k==='rhr'||k==='hrv'?`<div class="card flush">""","""  ${k==='resp'||k==='spo2'?`<div class="card flush">${li('wind',L('看某一晚的详情','See one night in detail'),L('一整晚的血氧、呼吸和睡眠，按住拖动看任一时刻','Oxygen, breathing and sleep across the night; drag to any moment'),'oxygen')}</div>`:''}
  ${k==='rhr'||k==='hrv'?`<div class="card flush">""")
R("['sleep','rhr','hrv','resp'].includes(k)","['sleep','rhr','hrv','resp','spo2'].includes(k)")
# how for spo2
R(" steps:{t:L('步数','Steps'),c:[[L('怎么测'",""" spo2:{t:L('夜间血氧','Overnight oxygen'),c:[[L('怎么测','How it’s measured'),L('戒指用红光和红外光照手指，估算血液里的氧含量。','The ring shines red and infrared light into your finger to estimate oxygen in your blood.')],
   [L('怎么算','How'),L('睡着期间逐分钟记录，取整晚的平均值和最低值。戴松、手凉、压着手的时段不算。','Recorded minute by minute while asleep; the night’s average and lowest. Loose-ring, cold-hand or lying-on-hand stretches are left out.')],
   [L('平常范围','Usual range'),L('你过去 30 晚的常见平均值。只和自己比，不按固定数值判断。','Your typical nightly average over 30 nights. Compared only with yourself, not against a fixed number.')],
   [L('注意','Note'),L('戒指估算，非医疗器械，不能诊断睡眠呼吸暂停。常打鼾或白天犯困，带上复诊一页纸问医生。','A ring estimate, not a medical device, and can’t diagnose sleep apnoea. If you snore or feel sleepy by day, ask a doctor with your visit summary.')]]},
 steps:{t:L('步数','Steps'),c:[[L('怎么测'""")
R("L('<b>v3.8.19</b>：","L('<b>v3.8.20</b>：身体页两块都回到中国版风格（大数字、平常范围条、来源行，各自传统色）；“夜间呼吸与血氧”拆成“夜间呼吸”“血氧”两行，各有趋势页和“如何计算”，趋势页可进某一晚详情；检查与测量用同样风格。<br><b>v3.8.19</b>：")
R("'<b>v3.8.19</b>: Compact","'<b>v3.8.20</b>: Both Health sections back in the China style (large number, usual-range bar, source line, traditional colours); Night breathing and Oxygen are now separate rows, each with its own trend and How it’s calculated, linking to the one-night view; Checks & readings use the same style.<br><b>v3.8.19</b>: Compact")
open(p,'w',encoding='utf-8').write(s)
i=s.rindex('})();');s=s[:i]+'window.__t={get S(){return S},go,render,tband,tseries};\n'+s[i:]
open(d+'otiagen/sw_test.html','w',encoding='utf-8').write(s)
print('ok')
