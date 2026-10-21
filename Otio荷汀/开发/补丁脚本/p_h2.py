d='/tmp/claude-0/-home-user-claude-code/5304f462-4324-55e0-ae4d-a872d232e3d9/scratchpad/'
p=d+'sgtob/vera-care-sg.html';s=open(p,encoding='utf-8').read()
def R(a,b):
    global s
    assert s.count(a)==1,(a[:70],s.count(a));s=s.replace(a,b)
# 5 sleep page night text
R("   p:L('23:28 入睡，6:16 醒。深睡 1 小时 05 分。','Asleep 11:28 pm, awake 6:16 am. Deep sleep 1 h 05 min.')}),",
  "   p:S.scen==='night'?L('0:11 入睡，6:16 醒，夜里醒了 3 次。深睡 52 分。','Asleep 12:11 am, awake 6:16 am, woke 3 times. Deep sleep 52 min.'):L('23:28 入睡，6:16 醒。深睡 1 小时 05 分。','Asleep 11:28 pm, awake 6:16 am. Deep sleep 1 h 05 min.')}),")
# 8 trend metrics: vit, sleep, steps
i=s.index("const TMT_=()=>({")+len("const TMT_=()=>({")
s=s[:i]+"""
 vit:{n:L('元气','Vitality'),u:'',c:'var(--vit)',base:66,amp:5,seed:11,lo:40,hi:100,
  what:L('元气综合了整夜 HRV、静息心率、呼吸、体温偏差和睡眠，每一项都和你自己最近 30 天的平常比，0–100。不是医疗指标。','Vitality combines overnight HRV, resting heart rate, breathing, temperature change and sleep, each against your own last 30 days, 0–100. Not a medical measure.'),
  up:L('这段时间睡得更规律，元气跟着往上走。','Steadier sleep has lifted your vitality.'),down:L('睡眠不足或累积疲劳都可能让元气走低，先从固定起床时间开始。','Short sleep or tiredness can lower it; start with a steady wake-up time.')},
 sleep:{n:L('睡眠时长','Sleep'),u:'',c:'var(--slp)',base:405,amp:20,seed:12,lo:300,hi:540,fmt:v=>Math.floor(v/60)+':'+String(Math.round(v%60)).padStart(2,'0'),
  what:L('从入睡到最后一次醒来，扣除夜里醒着的时间。只统计戴着戒指的晚上。','From falling asleep to waking, minus time awake in the night. Only nights wearing the ring.'),
  up:L('这段时间睡得更久了。','You have been sleeping longer.'),down:L('这段时间睡得比之前少，周末入睡偏晚是主要原因。','You have slept less, mostly from later weekend nights.')},
 steps:{n:L('步数','Steps'),u:L('步','steps'),c:'var(--act)',base:6300,amp:900,seed:17,lo:0,hi:14000,fmt:v=>Math.round(v).toLocaleString('en-US'),
  what:L('戒指和手机里同一分钟只取一个来源，避免重复计算。','For each minute only one source (ring or phone) is counted, so nothing is double-counted.'),
  up:L('这段时间走得更多了。','You have been walking more.'),down:L('这段时间走得比之前少。','You have walked a little less lately.')},"""+s[i:]
R(" if(k==='rhr')out[N-1]=62;"," if(k==='vit')out[N-1]=68;if(k==='sleep')out[N-1]=408;if(k==='steps')out[N-1]=6480;if(k==='rhr')out[N-1]=62;")
R("${['rhr','hrv','resp','temp'].map(x=>`<button class=\"${x===k?'on':''}\" data-act=\"tpick\" data-v=\"${x}\">${TMT_()[x].n}</button>`).join('')}",
  "${['vit','sleep','rhr','hrv','resp','temp','steps'].map(x=>`<button class=\"${x===k?'on':''}\" data-act=\"tpick\" data-v=\"${x}\">${TMT_()[x].n}</button>`).join('')}")
R("<div class=\"segm\">${['vit'","<div class=\"segm tchips\">${['vit'")
R("const tband=k=>bandAt(k,tseries(k).length);","const tband=k=>bandAt(k,tseries(k).length);\nconst tlast=k=>tseries(k)[tseries(k).length-1];")
# health page rewrite (title, rows, calendar, mgmt, footer)
a=s.index("P.health=()=>{");b=s.index("/* generic metric page */")
H=r"""function healthTitle(){const n=S.scen==='night',b=S.scen==='bp';
 if(b)return L('血压近 14 天 12 天在目标内，今早偏高。','BP was on target 12 of 14 days; high this morning.');
 if(n)return L('睡眠和血压大多平稳，昨夜血氧有一段偏低。','Sleep and BP mostly steady; oxygen dipped last night.');
 if(MP().focus==='walk'&&MP().fday>=28)return L('这个月走得最稳，睡眠也更规律了。','Your steadiest month of walking, and steadier sleep.');
 return linked()?L('睡眠更规律了，血压大多在目标内。','Sleep is steadier, and BP is mostly on target.'):L('睡眠更规律了，血压大多在参考值内。','Sleep is steadier, and BP mostly within the reference.')}
function calendar(){const pat='aaaabba'.repeat(4).split('');
 let s=`<div class="cal4">`;[L('一','M'),L('二','T'),L('三','W'),L('四','T'),L('五','F'),L('六','S'),L('日','S')].forEach(d=>s+=`<span class="sm mu" style="text-align:center">${d}</span>`);
 pat.forEach(c=>s+=`<i class="${c}"></i>`);
 return s+`</div><div class="sm mu" style="display:flex;gap:14px;margin-top:8px;flex-wrap:wrap"><span style="display:flex;gap:5px;align-items:center"><i style="width:10px;height:10px;border-radius:50%;background:color-mix(in srgb,var(--tx) 14%,transparent)"></i>${L('平常时段入睡','Usual bedtime')}</span><span style="display:flex;gap:5px;align-items:center"><i style="width:10px;height:10px;border-radius:50%;background:var(--slp)"></i>${L('晚于平常 1 小时以上','1 h+ later')}</span></div>`}
P.health=()=>{const n=S.scen==='night',b=S.scen==='bp',lk=linked(),ring=sh=>`${ic('ring',12)} ${L('荷汀戒指 · 参考数据','Otio ring · for context')}${sh&&lk?' '+seeTag():''}`;
 const rows=[
  vrow({go:'trend:vit',c:n?'var(--tLow)':'var(--vit)',ic:'leaf',k:L('元气','Vitality'),st:n?L('比平常低','Below usual'):L('和平常差不多','About usual'),v:vit(),bar:rbar('var(--vit)',62,76,45,90,vit(),[62,76]),src:ring(0)}),
  vrow({go:'trend:sleep',c:'var(--slp)',ic:'moon',k:L('睡眠','Sleep'),st:n?L('醒了 3 次','Woke 3 times'):L('比平时多 15 分钟','15 min more than usual'),v:n?'6:05':'6:48',bar:rbar('var(--slp)',6.3,7.2,4,9.5,n?6.08:6.8,['6:18','7:12']),src:ring(1)}),
  vrow({go:'trend:rhr',c:n?'var(--tLow)':'var(--vit)',ic:'heart',k:L('心率','Heart rate'),st:n?L('静息心率偏高 · HRV 偏低','Resting HR high · HRV low'):L('静息心率和 HRV 都和平常差不多','Resting HR and HRV about usual'),v:n?71:62,u:L('次/分 · HRV ','bpm · HRV ')+(n?24:31),bar:rbar('var(--vit)',58,66,50,80,n?71:62,[58,66]),src:ring(1)}),
  vrow({go:'oxygen',c:'var(--slp)',ic:'wind',k:L('夜间呼吸与血氧','Night breathing & oxygen'),st:n?L('血氧最低 88%','Oxygen low 88%'):L('和过去 30 晚差不多','Like the last 30 nights'),v:n?'13.2':'14.6',u:L('次/分','/min'),bar:rbar('var(--slp)',13.8,15.4,12,17,n?13.2:14.6,['13.8','15.4']),src:ring(1)}),
  vrow({go:'trend:steps',c:'var(--act)',ic:'run',k:L('活动','Activity'),st:L('近 7 天平均','7-day average'),v:'6,480',u:L('步','steps'),bar:rbar('var(--act)',5000,7000,0,10000,6480,['5,000','7,000']),src:ring(0)}),
 ];
 const r=t=>`<span class="sm mu" style="white-space:nowrap">${t}</span>`,vis=lk?' · '+L('护理团队可见','care team sees'):'';
 const wakeHint=MP().focus!=='wake'?`<button class="link" data-act="mpchg" style="text-align:left;margin-top:8px;font-size:14px">${L('起床时间前后差了 1 个半小时。要不要先养成按时起床？','Wake-up times vary by an hour and a half. Make getting up on time your next habit?')} ›</button>`:'';
 return{tab:'health',html:`<div class="pad stack">
  <div class="sm mu" style="padding-top:8px">${L('长期看，我在变好吗','Am I doing better over time?')}</div>
  <h1 class="h1" style="font-size:28px">${healthTitle()}</h1>
  <div><button class="chip" data-go="vera" style="cursor:pointer;color:var(--tx);padding:8px 12px">${ic('spark',14)} ${L('问小鸥 展开说说','Ask Ollie to explain')}</button></div>
  <div class="between" style="margin-top:4px"><span class="h2">${L('各项指标','Your numbers')}</span><span class="sm mu">${L('亮段是你的平常范围','Shaded = your usual range')}</span></div>
  <div class="card vitals">${rows.join('')}</div>
  <div class="card flush">${li('wave',L('全部趋势','All trends'),L('周 / 月 / 6 个月，每项都和你自己的平常比','Week / month / 6 months, each against your own usual'),'trend')}</div>
  <div class="card"><div class="between"><span class="h3">${L('作息规律','Sleep timing')}</span><span class="sm mu">${L('近 4 周，周五周六睡得晚','Last 4 weeks: later on Fri and Sat')}</span></div><div style="margin-top:10px">${calendar()}</div>${wakeHint}</div>
  <div class="h2" style="margin-top:6px">${L('健康管理','Health checks')}</div>
  <div class="card flush">
   ${li('gauge',L('血压','Blood pressure'),L('血压计 · 医疗器械','BP monitor · medical device')+vis,'bp',r(b?'<b style="color:var(--tLow)">172/104</b>':lk?L('早上 128/80 · 在目标内','Morning 128/80 · on target'):L('早上 128/80 · 在参考值内','Morning 128/80 · within reference')))}
   ${lk?li('ecg',L('心电','ECG'),L('心电卡 MD100C','ECG card MD100C')+vis,'ecg',r(L('本月 3 条 · 医生判读','3 this month · doctor-read'))):''}
   ${li('heart',L('夜间心律提示','Night rhythm alerts'),L('荷汀戒指','Otio ring'),'rhythm',r(L('即将开放','Coming soon')))}
   ${S.cgm?li('drop',L('血糖','Glucose'),'Sinocare CGM'+vis,'glucose',r(L('今天 81% 在范围内','81% in range today'))):li('drop',L('加上血糖','Add glucose'),L('Sinocare 连续血糖仪','Sinocare CGM'),'glucose',null)}
   ${lk?li('eye',L('眼底筛查','Eye screening'),CL(),'fundus',r(L('9 月 · 医生已审阅','Sep · reviewed'))):''}
  </div>
  <div class="h2" style="margin-top:6px">${L('报告','Reports')}</div>
  <div class="card flush">
   ${lk?li('doc',L('9 月监测报告','September report'),L(CL()+' · 周医生 10/3 签发',CL()+' · signed by Dr Zhou 3 Oct'),'report',null,{c:'care'}):''}
   ${lk?'':li('file',L('复诊一页纸','Visit summary'),L('近 30 天的事实和趋势，看诊时给医生看','Your last 30 days, facts and trends, to show your doctor'),'summary')}
  </div>
  ${lk?`<div class="h2" style="margin-top:4px">${L('我自己的放松和记录','My own wellbeing tools')}</div>
  <div class="card flush">${li('wind',L('荷息 · 跟着荷花呼吸','Lotus breath'),L('1 分钟静心 · 4-7-8 助眠','1-minute calm · 4-7-8 for sleep'),'breath:1')}</div>
  <div class="card"><div class="between"><span class="h3">${L('今天记一笔','Quick note on today')}</span><span class="sm mu">${L('只给你自己看','Just for you')}</span></div><div class="mpchips">${[['nap',L('午睡','Nap')],['kopi',L('下午 3 点后喝咖啡','Kopi after 3 pm')],['supper',L('宵夜','Late supper')],['late',L('熬夜','Up late')],['sit',L('久坐','Long sitting')],['drink',L('喝酒','Alcohol')]].map(([k,t])=>`<button class="mpchip ${MP().hab.includes(k)?'on':''}" data-act="mphab" data-v="${k}">${t}</button>`).join('')}</div><p class="sm mu" style="margin:8px 0 0">${L('这些不会分享给护理团队，除非你在“护理团队能看到什么”里打开。','Not shared with your care team unless you switch it on in What my care team sees.')}</p></div>`:''}
  <p class="sm mu" style="padding-bottom:12px">${L('戒指数据不是医疗器械读数，只和你自己的平常比。','Ring data is not a medical-device reading; it is compared only with your own usual.')}</p>
 </div>`}};

"""
s=s[:a]+H+s[b:]
# remove old calendar (from hport) — now duplicate
i=s.index("function calendar(){const pat='aaabbaaabaaabaaaaabbaaaaab'");j=s.index("P.rhythm=()=>",i);s=s[:i]+s[j:]
i=s.index('</style>');s=s[:i]+".tchips{overflow-x:auto;scrollbar-width:none}.tchips button{flex:none;padding:7px 12px;white-space:nowrap}\n"+s[i:]
R("L('<b>v3.8.10</b>：","L('<b>v3.8.11</b>：身体页按审核全部修改：标题按情况变（自己用写“参考值”）；指标收成 5 行（元气、睡眠、心率含 HRV、夜间呼吸与血氧、活动），每行带来源，连诊所时标“护理团队可见”，点进去统一到趋势页；趋势页补齐 7 项；作息规律和副标题对上，并提示“要不要先养成按时起床”；健康管理去掉重复行，自己用不显示心电，血压自己用写“参考值”，心律提示写“即将开放”；页脚改为“戒指数据不是医疗器械读数”；夜间血氧偏低那天睡眠页时间对上。<br><b>v3.8.10</b>：")
R("'<b>v3.8.10</b>: Health","'<b>v3.8.11</b>: Health page fixes from the review: the title follows the situation (reference, not target, on your own); five numbers (vitality, sleep, heart rate with HRV, night breathing & oxygen, activity) with sources and care-team marks, each opening the trend page; trends cover seven measures; sleep timing matches its caption and suggests the wake-up habit; no duplicate row, no ECG on your own, reference wording for BP, coming soon for rhythm alerts; footer clarified; sleep times match on the oxygen-dip day.<br><b>v3.8.10</b>: Health")
open(p,'w',encoding='utf-8').write(s)
i=s.rindex('})();');s=s[:i]+'window.__t={get S(){return S},go,render};\n'+s[i:]
open(d+'otiagen/sw_test.html','w',encoding='utf-8').write(s)
print('ok')
