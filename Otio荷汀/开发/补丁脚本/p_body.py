p='sgtob/vera-care-sg.html';s=open(p).read()
def R(a,b,n=1):
    global s;assert s.count(a)==n,(s.count(a),a[:70]);s=s.replace(a,b)
# --- state
R("hour:8.33,va:'auto',","hour:8.33,va:'auto',meals:{b:1,l:0},")
R("own:{bp:true,ecg:true,thermo:false,mat:false}","own:{bp:true,ecg:true,thermo:false,mat:false,env:false}")
# --- 1 distance in Activity trend (no calories)
R("""   <p class="p sm" style="margin-top:14px">${say}</p>""","""   <p class="p sm" style="margin-top:14px">${say}</p>${k==='steps'?(()=>{const t=S.tm==='morning'?1240:3920;return `<p class="p sm mu" style="margin-top:4px">${L('今天约 '+(t*.7/1000).toFixed(1)+' 公里 · 近 7 天平均每天约 4.5 公里','About '+(t*.7/1000).toFixed(1)+' km today · about 4.5 km a day over 7 days')}</p>`})():''}""")
# --- 3 HRV: today's tension timeline
R("""  ${k==='sleep'?`<div class="card"><div class="between"><span class="h3">${L('作息规律','Sleep timing')}</span>""","""  ${k==='hrv'?songjin():''}
  ${k==='sleep'&&S.own.env?`<div class="card"><div class="between"><span class="h3">${L('昨晚的卧室','Your bedroom last night')}</span><span class="sm mu">${L('卧室环境监测仪','Bedroom monitor')}</span></div><div class="kv" style="margin-top:4px"><div><span>${L('温度','Temperature')}</span><span class="num">27.5°C</span></div><div><span>${L('湿度','Humidity')}</span><span class="num">78%</span></div><div><span>PM2.5</span><span class="num">12</span></div></div><p class="sm mu" style="margin:8px 0 0">${L('偏潮。空调开除湿或调到 25–26°C，夜里容易睡得更稳。','On the humid side. Dry mode or 25–26°C on the aircon tends to help sleep.')}</p></div>`:''}
  ${k==='sleep'?`<div class="card"><div class="between"><span class="h3">${L('作息规律','Sleep timing')}</span>""")
R("/* 夜间呼吸与血氧：按中国版移植","""/* 今天的松紧：白天按小时看 HRV 相对自己的平常，低 = 绷得紧。不打分，只标出哪段紧，紧的时候引到荷息呼吸 */
function songjin(){const today=S.tm!=='morning',H0=7,T=[.2,.3,.55,.85,.7,.35,.25,.3,.6,.75,.4,.3,.2,.15,.2],n=today?Math.min(T.length,Math.floor(S.hour)-H0+1):T.length,W=300,Hh=46,bw=(W-8)/T.length;
 const bars=T.map((v,i)=>i<n?`<rect x="${(4+i*bw+1).toFixed(1)}" y="${(Hh-6-v*(Hh-14)).toFixed(1)}" width="${(bw-2).toFixed(1)}" height="${(v*(Hh-14)+2).toFixed(1)}" rx="2" fill="var(--c-oh)" opacity="${(.25+.75*v).toFixed(2)}"/>`:'').join('');
 return `<div class="card"><div class="between"><span class="h3">${today?L('今天的松紧','Today: tense or at ease'):L('昨天的松紧','Yesterday: tense or at ease')}</span><span class="sm mu">${L('柱子越高越紧','Taller = more tense')}</span></div>
  <svg class="chart" viewBox="0 0 ${W} ${Hh+14}" style="margin-top:8px">${bars}<text x="4" y="${Hh+12}">7:00</text><text x="${W/2}" y="${Hh+12}" text-anchor="middle">14:00</text><text x="${W-4}" y="${Hh+12}" text-anchor="end">21:00</text></svg>
  <p class="p sm" style="margin-top:6px">${L('10:00–11:00 和 15:00–16:00 比较紧，其余时间都松。','Tenser around 10–11 am and 3–4 pm; at ease the rest of the day.')}</p></div>
  <div class="card flush">${li('lotus',L('绷紧的时候，跟荷花呼吸一分钟','When you feel tense, breathe with the lotus for a minute'),L('荷息 · 一分钟','Lotus breath · 1 minute'),'breath:1')}</div>`}
/* 夜间呼吸与血氧：按中国版移植""")
# --- 4 BP rule insight from cuff readings
R("""  ${hi?`<button class="btn" data-go="alert">${L('按医生的指引处理','Follow your doctor’s steps')}</button>`:''}""","""  ${hi?`<button class="btn" data-go="alert">${L('按医生的指引处理','Follow your doctor’s steps')}</button>`:''}
  ${(()=>{const am=BPD.slice(),pm=BPE;if(hi)am[13]=[172,104];const ok=am.filter(x=>x[0]<135&&x[1]<85).length,dd=Math.round(am.reduce((a,x)=>a+x[0],0)/14-pm.reduce((a,x)=>a+x[0],0)/14);
    return `<div class="card"><div class="h3">${L('这两周的规律','Last two weeks')}</div><p class="p" style="margin-top:6px">${L('早上 14 天里有 '+ok+' 天在目标内。','Mornings: '+ok+' of 14 days on target.')}${Math.abs(dd)>=3?L('早上收缩压比晚上平均'+(dd>0?'高':'低')+' '+Math.abs(dd)+'。',' Morning systolic averages '+Math.abs(dd)+' '+(dd>0?'higher':'lower')+' than evening.'):L('早晚差不多。',' Mornings and evenings are similar.')}</p><p class="sm mu" style="margin:6px 0 0">${L('只按血压计的实测值统计，复诊时可以给医生看。','From your monitor readings only; worth showing your doctor.')}</p></div>`})()}""")
# --- 6 ECG monthly summary
R("""  <button class="btn" data-go="ecgrec">${ic('ecg',18)} ${L('记录 30 秒心电','Record a 30-second ECG')}</button>""","""  <button class="btn" data-go="ecgrec">${ic('ecg',18)} ${L('记录 30 秒心电','Record a 30-second ECG')}</button>
  ${(()=>{const R0=ecgRecs(),sin=R0.filter(r=>r.st==='done').length,rt=R0.filter(r=>r.st==='retake').length,aw=R0.filter(r=>r.st==='await').length;return `<div class="card"><div class="between"><span class="h3">${L('近 30 天','Last 30 days')}</span><span class="sm mu">${linked()?L('医生判读','Read by your doctor'):L('心电卡设备分析','ECG card’s own analysis')}</span></div><p class="p" style="margin-top:6px">${L('共 '+R0.length+' 条：'+sin+' 条窦性心律'+(rt?'，'+rt+' 条请重录':'')+(aw?'，'+aw+' 条等判读':'')+'。',R0.length+' recordings: '+sin+' sinus rhythm'+(rt?', '+rt+' retake':'')+(aw?', '+aw+' awaiting':'')+'.')}</p></div>`})()}""")
# --- 2 meal photo on the glucose curve
R("""${[[7.5,L('早餐','Breakfast')],[12.8,L('午餐','Lunch')],[19.2,L('晚餐','Dinner')]].map(([h,t])=>`<text x="${X(h*4).toFixed(1)}" y="${H-14}" text-anchor="middle">${t}</text>`).join('')}""",
  """${[[7.5,L('早餐','Breakfast'),'b'],[12.8,L('午餐','Lunch'),'l'],[19.2,L('晚餐','Dinner'),'d']].map(([h,t,mk])=>{const i=Math.round(h*4),x=X(i).toFixed(1),y=Y(d[Math.min(d.length-1,i+4)]).toFixed(1),has=S.meals[mk];return `<text x="${x}" y="${H-14}" text-anchor="middle">${t}</text>${has?`<circle cx="${x}" cy="${(+y-14).toFixed(1)}" r="7" fill="var(--c-xs)"/><circle cx="${x}" cy="${(+y-14).toFixed(1)}" r="2.6" fill="#fff"/>`:''}`}).join('')}""")
R("""  <p class="sm mu">${linked()?L('午饭后升得最高（9.8）。吃饭时记一笔，护士复盘时更容易看出原因。','Your highest rise was after lunch (9.8). Logging meals helps your nurse see why at the review.'):L('午饭后升得最高（9.8）。吃饭时记一笔，自己更容易看出是哪顿饭。','Your highest rise was after lunch (9.8). Logging meals helps you see which meal did it.')}</p>""",
  """  <div class="card"><div class="between"><span class="h3">${L('这几顿饭','Today’s meals')}</span><span class="sm mu">${L('照片标在曲线上','Shown on the curve')}</span></div>
   <div class="kv" style="margin-top:4px"><div><span>${L('早餐 7:30','Breakfast 7:30')}</span><span>${L('咖椰吐司、半熟蛋','Kaya toast, soft eggs')}</span></div><div><span>${L('午餐 12:50','Lunch 12:50')}</span><span>${S.meals.l?L('海南鸡饭','Chicken rice'):`<span class="mu">${L('还没拍','No photo yet')}</span>`}</span></div></div>
   ${S.meals.l?'':`<button class="btn sm ghost" data-act="mealsnap" style="margin-top:10px">${ic('camera',16)} ${L('拍一下这顿饭','Snap this meal')}</button>`}</div>
  <p class="sm mu">${S.meals.l?L('午饭（海南鸡饭）后升得最高，到 9.8。','The biggest rise, to 9.8, came after lunch (chicken rice).'):L('午饭后升得最高（9.8）。拍一下这顿饭，就知道是哪顿饭让血糖升高。','Your highest rise was after lunch (9.8). Snap the meal to see which one did it.')}${linked()?L('护士复盘时也能看到。',' Your nurse sees it at the review too.'):''}</p>""")
R("    vitwhy(){","    mealsnap(){S.meals.l=1;toast(L('已拍下午餐 · 标在曲线上','Lunch photo added to the curve'));render()},\n    vitwhy(){")
# --- 8 sleep breathing alerts row + page
R("""   ${vrow2({go:'rhythm',c:'var(--c-oh)',ic:'heart',k:L('夜间心律提示','Night rhythm alerts'),st:L('看规律，不看快慢','Regularity, not speed'),v:'',u:L('即将开放','Coming soon')})}""",
  """   ${vrow2({go:'rhythm',c:'var(--c-oh)',ic:'heart',k:L('夜间心律提示','Night rhythm alerts'),st:L('看规律，不看快慢','Regularity, not speed'),v:'',u:L('即将开放','Coming soon')})}
   ${vrow2({go:'apnea',c:'var(--c-tsb)',ic:'wind',k:L('睡眠呼吸提示','Sleep breathing alerts'),st:L('看夜里呼吸有没有停顿','Pauses in breathing at night'),v:'',u:L('即将开放','Coming soon')})}""")
R("P.fundus=()=>({calm:1,","""P.apnea=()=>({calm:1,html:`${nav(L('睡眠呼吸提示','Sleep breathing alerts'))}<div class="pad stack">
  <h1 class="h1" style="font-size:24px">${L('还在等注册证','Awaiting registration')}</h1>
  <p class="p sm mu">${L('戒指整晚都在看血氧和呼吸。拿到注册证后，如果连续几晚看到呼吸停顿的迹象，会建议你去做一次睡眠检查。','Your ring watches oxygen and breathing all night. Once registered, if it sees signs of pauses in breathing several nights running, it will suggest a sleep study.')}</p>
  <div class="card"><div class="h3">${L('获批后怎么用','How it will work')}</div><div class="list">${[[L('不用操作','Nothing to do'),L('睡着时自动分析','Analysed while you sleep')],[L('少打扰','Rarely'),L('连续几晚都有迹象才提醒','Only when several nights show signs')],[linked()?L('护理团队也能看到','Your care team sees it too'):L('给医生看','Show a doctor'),linked()?L('提醒会同时进入周医生的查看列表','The alert also goes to Dr Zhou’s review list'):L('提醒附带那几晚的记录，放进复诊一页纸','The nights are added to your visit summary')]].map(([k,v])=>`<div class="li" style="cursor:default;min-height:0;padding:10px 0"><span class="t"><span class="sm" style="display:block">${k}</span><span class="sm mu">${v}</span></span></div>`).join('')}</div></div>
  <div class="card flush">${li('wind',L('先看看昨晚的夜间呼吸与血氧','See last night’s breathing and oxygen'),L('参考数据，不是诊断','For context, not a diagnosis'),'oxygen')}</div>
  <p class="sm mu">${L('能提示什么、适合谁用，以注册证批准的范围为准。睡眠呼吸暂停要由睡眠检查确诊。','What it can flag, and for whom, will follow the approved registration. Sleep apnoea is diagnosed by a sleep study.')}</p></div>`});
P.fundus=()=>({calm:1,""")
# --- 7 bedroom monitor device
R("const MC={ring:'var(--c-sq)',","const MC={env:'var(--c-mo)',ring:'var(--c-sq)',")
R(""" {k:'mat',ic:'moon',""",""" {k:'env',ic:'wind',n:L('卧室环境监测仪','Bedroom air monitor'),who:L('卧室闷、潮，或烟霾季想知道夜里空气怎么样','Your bedroom feels stuffy or humid, or you want to know the air at night in haze season'),no:L('睡得好，卧室也舒服','You sleep well and the room is comfortable'),diff:L('看温度、湿度和 PM2.5；戒指看不到房间','Reads temperature, humidity and PM2.5; the ring can’t see the room')},
 {k:'mat',ic:'moon',""")
R("$('#p-chg').innerHTML=L('<b>v3.8.36</b>","$('#p-chg').innerHTML=L('<b>v3.8.37</b>：身体页补功能：活动趋势加距离（不做卡路里）；血糖页加“拍一下这顿饭”，照片标在曲线上；HRV 趋势加“今天的松紧”时间线，链到荷息呼吸；血压页加“这两周的规律”（只用血压计实测值）；心电页加近 30 天小结；睡眠趋势在有卧室环境监测仪时加一句卧室温湿度；检查与测量加“睡眠呼吸提示 · 即将开放”（在等注册证）；严选加卧室环境监测仪。<br><b>v3.8.36</b>")
R("   '<b>v3.8.36</b>: New ink","   '<b>v3.8.37</b>: Health additions: distance in the Activity trend (no calories); Snap this meal on the glucose page, shown on the curve; Today: tense or at ease timeline in HRV, linking to lotus breath; Last two weeks pattern on BP (monitor readings only); 30-day ECG summary; bedroom temperature and humidity in Sleep when a bedroom monitor is connected; Sleep breathing alerts row (awaiting registration); bedroom air monitor in Picks.<br><b>v3.8.36</b>: New ink")
open(p,'w').write(s)
s=open(p).read();i=s.rfind('})();')
open('otiagen/sw_test.html','w').write(s[:i]+'window.__t={get S(){return S},go,render,tband,tseries};'+s[i:])
