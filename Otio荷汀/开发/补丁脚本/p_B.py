import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
def SEG(start,end,new):
    global s
    i=s.index(start);j=s.index(end,i);s=s[:i]+new+s[j:]
# whyText
R("L('凌晨 4:40 最低 88%，低于 90% 约 6 分钟；早上心率也比平常高。'+(linked()?'护理团队已经能看到。':''),'Lowest 88% at 4:40 am, about 6 minutes below 90%. Your heart rate was also higher than usual this morning.'+(linked()?' Your care team can already see this.':''))",
  "L('凌晨 4:40 最低 88%（戒指估算）；早上心率也比平常高。'+(linked()?'护理团队已经能看到。':''),'Lowest 88% at 4:40 am (ring estimate). Your heart rate was also higher than usual this morning.'+(linked()?' Your care team can already see this.':''))")
R("L('静息心率 62、HRV 31，都在你平常的范围里。','Resting heart rate 62 and HRV 31, both within your usual range.')","L('静息心率 62，心跳的细微变化也和平常一样。','Resting heart rate 62, and the small changes in your heartbeat look like your usual.')")
# oneThing / oneRow
SEG("function oneThing(){","function triNums(){",r"""function oneThing(){
  if(S.scen==='bp'&&linked())return S.bp.step>=2?{t:L('已通知护理团队，陈护士 10:30 前联系你','Care team notified. Nurse Chen will contact you by 10:30'),done:1,go:'alert'}:{t:L('静坐 5 分钟后再量一次','Rest 5 minutes, then measure again'),go:'alert',cta:L('开始','Start')};
  if(linked()){const C=[['bppm',20,L('20:00 晚上量血压','8 pm · Evening BP')],['med2',22.5,L('22:30 阿托伐他汀 20 mg','10:30 pm · Atorvastatin 20 mg')]],n=C.find(([k,h])=>!S.tasks[k]&&h>S.hour);
   return n?{t:n[2],tab:'care'}:{t:L('今天的护理计划都做完了','Today’s care plan is done'),done:1,tab:'care'}}
  const m=MP(),nx=mpItems().find(x=>mpT(x.t)>S.hour&&!isDone(x.id)&&!m.skip.includes(x.id)&&x.id!=='wake');
  return nx?{t:nx.t+' '+nx.a+(nx.auto?L(' · 戒指自动记',' · the ring records it'):''),tab:'myplan'}:{t:L('今天的事都做完了','All done for today'),done:1,tab:'myplan'}}
function oneRow(){const o=oneThing();
  return `<div class="onerow"><span class="t">${o.t}</span>${o.go?`<button class="btn sm ${o.done?'ghost':''}" data-go="${o.go}">${o.cta||L('查看','View')}</button>`:`<button class="btn sm ghost" data-tab="${o.tab}">${L('查看','View')}</button>`}</div>`}
""")
# careStrip
R("""  if(!linked())return `<div class="card flush">${li('team',L('连上你的诊所','Bring in your care team'),L('护士看你的血压和心电，有事会联系你','A nurse checks your BP and ECG and reaches out when needed'),'connect',null,{c:'care'})}</div>`;""","  if(!linked())return '';")
R("""  rows.push(li('phone',L('陈护士今天 14:00 给你打电话'""","""  if(S.scen!=='night')rows.push(li('phone',L('陈护士今天 14:00 给你打电话'""")
R("""  const left=['bppm','med2','survey'].filter(k=>!S.tasks[k]).length;
  rows.push(li('check',L(`今天的护理计划还剩 ${left} 项`,`${left} care plan task${left===1?'':'s'} left today`),S.tm==='night'?L('阿托伐他汀 · 睡前','Atorvastatin · at bedtime'):L('晚上量血压 · 20:00','Evening BP · 8 pm'),'care',null,{c:'care'}));
""","")
R("""   ${seasonLine()}
   <div style="flex:1"></div>""","""   <div style="flex:1"></div>""")
R("""  ${careStrip()}
  ${entries()}
 </div>`});""","""  ${careStrip()}
 </div>`});""")
# health
R("st:n?L('最低 88%，低于 90% 约 6 分钟','Low 88%, about 6 min under 90%'):L('平稳','Steady')","st:n?L('最低 88%（戒指估算）','Low 88% (ring estimate)'):L('平稳','Steady')")
R("""<h1 class="h1" style="font-size:28px">${L('睡眠更规律了，血压大多在目标内。','Sleep is steadier, and BP is mostly on target.')}</h1>""",
  """<h1 class="h1" style="font-size:28px">${b?L('血压近 14 天 12 天在目标内，今早偏高。','BP was on target 12 of 14 days; high this morning.'):n?L('睡眠和血压大多平稳，昨夜血氧有一段偏低。','Sleep and BP are mostly steady; oxygen dipped last night.'):L('睡眠更规律了，血压大多在目标内。','Sleep is steadier, and BP is mostly on target.')}</h1>""")
R("""L('关联 Sinocare 连续血糖仪，或预约 14 天血糖检查','Link a Sinocare CGM, or book a 14-day glucose check'),'glucose')}</div>`}""","""linked()?L('关联 Sinocare 连续血糖仪，或预约 14 天血糖检查','Link a Sinocare CGM, or book a 14-day glucose check'):L('关联连续血糖仪，读数显示在 App 里，看医生时可以带上','Link a CGM; readings show here to bring to your doctor'),'glucose')}</div>`}""")
SEG("""  ${linked()?`<div class="h2" style="margin-top:4px">${L('我自己的放松和记录'""",""" </div>`}};""",r"""  ${linked()?`<div class="h2" style="margin-top:4px">${L('只给自己看','Just for you')}</div>
  <div class="card flush">${li('wind',L('荷息 · 跟着荷花呼吸','Lotus breath'),L('1 分钟静心 · 4-7-8 助眠','1-minute calm · 4-7-8 for sleep'),'breath:1')}<button class="li" data-act="mphabopen"><span class="ic">${ic('leaf')}</span><span class="t">${L('今天记一笔','Quick note on today')}<small>${MP().hab.length?L('已记 '+MP().hab.length+' 项','Noted '+MP().hab.length):L('午睡、咖啡、宵夜…点一下记下来','Nap, kopi, late supper… tap to note')}</small></span><span class="chev">${ic('chev',16)}</span></button>${MP().habOpen?`<div style="padding:4px 0 14px"><div class="mpchips" style="margin-top:0">${[['nap',L('午睡','Nap')],['kopi',L('下午 3 点后喝咖啡','Kopi after 3 pm')],['supper',L('宵夜','Late supper')],['late',L('熬夜','Up late')],['sit',L('久坐','Long sitting')],['drink',L('喝酒','Alcohol')]].map(([k,t])=>`<button class="mpchip ${MP().hab.includes(k)?'on':''}" data-act="mphab" data-v="${k}">${t}</button>`).join('')}</div><p class="sm mu" style="margin:8px 0 0">${L('不会分享给护理团队，除非你在“护理团队能看到什么”里打开。','Not shared with your care team unless you switch it on in What my care team sees.')}</p></div>`:''}</div>`:''}
""")
# metric
R("L('元气看昨夜的静息心率、HRV、体温和睡眠，和你自己的平常比。不是医疗指标。','Vitality looks at last night’s resting heart rate, HRV, temperature and sleep, compared with your own usual. It isn’t a medical measure.')",
  "L('元气看昨夜的静息心率、心跳的细微变化、体温和睡眠，和你自己的平常比。不是医疗指标。','Vitality looks at last night’s resting heart rate, small changes in your heartbeat, temperature and sleep, compared with your own usual. It isn’t a medical measure.')")
R("p:L('雷雨多在午后，上午或傍晚出门更合适。PSI 42，空气良好。','Thunderstorms tend to come in the afternoon, so mornings or evenings are better for walks. PSI 42, air is good.')",
  "p:L('近 7 天平均 6,480 步。有快走的那天，大约多 2,000 步。','7-day average 6,480 steps. Days with a brisk walk add about 2,000.')")
# oxygen
R("""<path d="M8 ${Y(90).toFixed(1)}H${W-8}" stroke="var(--tLow)" stroke-dasharray="3 4" stroke-opacity=".6"/><text x="${W-8}" y="${(Y(90)-4).toFixed(1)}" text-anchor="end">90%</text>""","")
R("L('凌晨 4:30–4:46 血氧低于 90%，最低 88%。这段时间呼吸频率也变慢了。','Between 4:30 and 4:46 am your oxygen was below 90%, lowest 88%. Your breathing also slowed during that time.')",
  "L('凌晨 4:40 最低 88%（戒指估算），这段时间呼吸也变慢了。','Lowest 88% at 4:40 am (ring estimate); your breathing also slowed then.')")
R("L('这条已同步给 '+CL()+'。你的医生设的规则是“低于 90% 超过 5 分钟”提醒护士，陈护士今天中午前会看。','This has been shared with '+CL()+'. Your doctor’s rule flags oxygen under 90% for more than 5 minutes to the nurse; Nurse Chen will look at it before noon.')",
  "L('已同步给护理团队，护士每天查看时参考。','Shared with your care team; the nurse uses it for context in the daily review.')")
R("""  ${dip?`<button class="btn" data-go="ecgrec">${L('记录一次心电','Record an ECG')}</button>`:''}""",
  """  ${dip&&!linked()?`<p class="sm mu">${L('常打鼾或白天犯困，看医生时带上复诊一页纸。','If you snore or feel sleepy by day, bring your visit summary to your doctor.')}</p>`:''}
  ${dip?`<button class="btn ghost" data-go="ecgrec">${L('有心慌就记录一次心电','Feeling palpitations? Record an ECG')}</button>`:''}""")
# bp
R("${linked()?L('医生给你定的目标','Targets set by '+DRs()):L('你的目标','Your targets')}","${linked()?L('医生给你定的目标','Targets set by '+DRs()):L('参考值','Reference')}")
R("""<div><span>${L('家里量的目标','Home target')}</span><span class="num">&lt; 135/85</span></div>""","""<div><span>${linked()?L('家里量的目标','Home target'):L('家庭血压参考','Home BP reference')}</span><span class="num">&lt; 135/85</span></div>""")
# glucose
R("L('Sinocare 传感器贴在上臂，戴 14 天。读数由 Sinocare 云端直接传到你的护理团队，App 里也能看。','A Sinocare sensor sits on your upper arm for 14 days. Readings flow from Sinocare’s cloud to your care team, and show here too.')",
  "linked()?L('Sinocare 传感器贴在上臂，戴 14 天。读数由 Sinocare 云端直接传到你的护理团队，App 里也能看。','A Sinocare sensor sits on your upper arm for 14 days. Readings flow from Sinocare’s cloud to your care team, and show here too.'):L('Sinocare 传感器贴在上臂，戴 14 天。读数显示在 App 里，看医生时可以带上。','A Sinocare sensor sits on your upper arm for 14 days. Readings show here, to bring to your doctor.')")
R("""<div><span>${L('数据来源','Data from')}</span><span>${L('Sinocare 云端 → RPM 平台','Sinocare cloud → RPM platform')}</span></div><div><span>${L('低血糖提醒','Low alert')}</span><span>${L('低于 3.9 通知护士','Below 3.9 alerts nurse')}</span></div>""",
  """${linked()?`<div><span>${L('数据来源','Data from')}</span><span>${L('Sinocare 云端 → RPM 平台','Sinocare cloud → RPM platform')}</span></div><div><span>${L('低血糖提醒','Low alert')}</span><span>${L('低于 3.9 通知护士','Below 3.9 alerts nurse')}</span></div>`:''}""")
R("L('午饭后升得最高（9.8）。吃饭时记一笔，护士复盘时更容易看出原因。','Your highest rise was after lunch (9.8). Logging meals helps your nurse see why at the review.')",
  "linked()?L('午饭后升得最高（9.8）。吃饭时记一笔，护士复盘时更容易看出原因。','Your highest rise was after lunch (9.8). Logging meals helps your nurse see why at the review.'):L('午饭后升得最高（9.8）。吃饭时记一笔，更容易看出原因。','Your highest rise was after lunch (9.8). Logging meals makes the reason easier to see.')")
# panel
R("if(S.care!=='linked'&&v!=='normal')S.care='linked';","if(S.care!=='linked'&&(v==='bp'||v==='msg'))S.care='linked';")
open(p,'w',encoding='utf-8').write(s); print('ok')
