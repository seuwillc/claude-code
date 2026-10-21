d='/tmp/claude-0/-home-user-claude-code/5304f462-4324-55e0-ae4d-a872d232e3d9/scratchpad/'
p=d+'sgtob/vera-care-sg.html';s=open(p,encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a));s=s.replace(a,b)
# state
R("const S={lang:'en',care:'linked',scen:'normal',dev:'ring',cgm:false,","const S={lang:'en',care:'linked',scen:'normal',dev:'ring',cgm:false,own:{bp:true,ecg:true,thermo:false,mat:false},temp:{v:36.8,at:0},sick:false,cgmDay:9,")
# devices + store + thermo pages
a=s.index("P.devices=()=>({calm:1,");b=s.index("\nP.notify=",a)
s=s[:a]+r"""const DEVS=()=>[
 {k:'bp',ic:'gauge',n:L('上臂式血压计','Upper-arm BP monitor'),who:L('有高血压，或医生让你在家量血压','You have high blood pressure, or your doctor wants home readings'),no:L('血压一直正常，不必买','Your BP has always been normal'),diff:L('戒指不测血压，血压只能靠它','The ring can’t measure BP; this can')},
 {k:'ecg',ic:'ecg',n:L('心电卡','ECG card'),who:L('常心慌、心跳忽快忽慢','You often feel palpitations or an uneven heartbeat'),no:L('从没心慌过','You’ve never had palpitations'),diff:L('戒指看心率快慢，心电卡看每一下的节律','The ring sees how fast; the card sees each beat’s rhythm')},
 {k:'cgm',ic:'drop',n:L('连续血糖仪（CGM）','Continuous glucose monitor (CGM)'),who:L('有糖尿病或血糖偏高，想看吃什么让血糖升高','You have diabetes or high glucose and want to see what raises it'),no:L('血糖正常，也没有医生建议','Normal glucose and no doctor’s advice'),diff:L('贴在上臂 14 天，每几分钟测一次','Worn on the arm for 14 days, reading every few minutes')},
 {k:'thermo',ic:'temp',n:L('智能蓝牙体温计','Smart Bluetooth thermometer'),who:L('家里需要一支体温计，生病时想记下体温变化','You need a thermometer at home and want a record when unwell'),no:L('家里已有好用的体温计','You already have one you like'),diff:L('量的是真实体温；戒指只看和平常比的变化','Measures actual temperature; the ring only shows change from usual')},
 {k:'mat',ic:'moon',n:L('睡眠监测床垫','Sleep-monitoring mat'),who:L('不喜欢戴着戒指睡觉','You don’t like wearing the ring to bed'),no:L('戴戒指睡得惯','You’re fine sleeping with the ring'),diff:L('放在床垫下，不用戴；没戴戒指的晚上自动补上睡眠和呼吸','Goes under the mattress; fills in sleep and breathing on nights without the ring')}];
const owns=k=>k==='cgm'?S.cgm:k==='ecg'?(S.own.ecg||linked()):S.own[k];
P.devices=()=>({calm:1,html:`${nav(L('设备与数据来源','Devices & data sources'))}<div class="pad stack">
  <div class="card flush">
   <div class="devcard"><span class="ic">${ic(S.dev==='ring'?'ring':'band')}</span><span class="t">${devName()}<small>${S.dev==='ring'?'SN-60233 · '+L('电量 12%','battery 12%'):'SN-71102 · '+L('电量 68%','battery 68%')}</small></span><span class="tag ${S.dev==='ring'?'low':'ok'}">${S.dev==='ring'?L('电量低','Low'):L('已连接','Connected')}</span></div>
   ${DEVS().filter(x=>owns(x.k)).map(x=>`<div class="devcard"><span class="ic">${ic(x.ic)}</span><span class="t">${x.n}<small>${x.k==='ecg'&&linked()&&!S.own.ecg?L('诊所借用','On loan from clinic'):x.k==='cgm'?L('传感器第 '+S.cgmDay+'/14 天','Sensor day '+S.cgmDay+' of 14'):L('型号待定','Model TBC')}</small></span><span class="tag ok">${L('已连接','Connected')}</span></div>`).join('')}
  </div>
  <div class="card flush">${li('plus',L('加设备 · BioVision 严选','Add a device · BioVision picks'),L('血压计、心电卡、血糖仪、体温计、睡眠床垫','BP monitor, ECG card, CGM, thermometer, sleep mat'),'store')}${li('users',L('请家人帮我连','Ask family to help me connect'),L('发给女儿一张图文步骤卡','Send your daughter a step-by-step card'),null,null,{act:'famhelp'})}</div>
  <div class="card" style="padding:4px 16px"><div class="devcard"><span class="t">Healthy 365<small>${L('每天步数攒积分','Daily steps for points')}</small></span>${sw('h365',MP().h365,{act:'mph365',lab:'Healthy 365'})}</div></div>
  <div class="card flush">${li('link','Apple Health / Health Connect',L('同步步数、体重；不回写医疗读数','Sync steps and weight; medical readings aren’t written back'),null,null,{act:'hk'})}</div>
 </div>`});
P.store=()=>({calm:1,html:`${nav(L('BioVision 严选','BioVision picks'))}<div class="pad stack">
  <p class="p">${L('先用戒指。只有医生建议，或你确实有需要，再加设备。','Start with the ring. Add a device only if your doctor suggests it or you really need it.')}</p>
  ${DEVS().map(x=>`<div class="card"><div class="between"><span style="display:flex;gap:10px;align-items:center"><span class="ic" style="width:30px;height:30px;border-radius:50%;display:grid;place-items:center;background:var(--sf2)">${ic(x.ic,16)}</span><span class="h3">${x.n}</span></span>${owns(x.k)?`<span class="tag ok">${L('已连接','Connected')}</span>`:''}</div>
   <div class="kv" style="margin-top:6px"><div><span class="sm mu">${L('谁需要','Who it’s for')}</span><span class="sm" style="text-align:right;max-width:62%">${x.who}</span></div><div><span class="sm mu">${L('谁不需要','Who doesn’t need it')}</span><span class="sm" style="text-align:right;max-width:62%">${x.no}</span></div><div><span class="sm mu">${L('和戒指的区别','vs the ring')}</span><span class="sm" style="text-align:right;max-width:62%">${x.diff}</span></div></div>
   ${owns(x.k)?'':`<div class="row2" style="margin-top:10px"><button class="btn sm" data-act="devconn" data-v="${x.k}">${L('我已经有，连接','I have one, connect')}</button><button class="btn sm ghost" data-act="devbuy">${L('去购买 ›','Buy ›')}</button></div>`}</div>`).join('')}
  <p class="sm mu">${L('型号在选定中。购买会跳到官方商城，App 里不收款。','Models are being chosen. Buying opens the official store; the app takes no payment.')}</p></div>`});
P.thermo=()=>{const t=S.temp.v,fev=t>=38;return{calm:1,html:`${nav(L('体温','Temperature'))}<div class="pad stack">
  <div class="card"><div class="eyebrow">${S.temp.at?L('刚刚','Just now'):L('今天 7:10','Today 7:10')} · ${L('蓝牙体温计','Bluetooth thermometer')}</div><div class="bign" ${fev?'style="color:var(--tLow)"':''}>${t.toFixed(1)}<small>°C</small></div></div>
  ${fev?`<div class="card"><div class="h3">${L('有点发烧','A bit of a fever')}</div><p class="p" style="margin-top:6px">${L('多喝水、多休息，过几小时再量一次。','Drink plenty, rest, and check again in a few hours.')}</p>${S.sick?`<p class="sm mu" style="margin-top:8px">${L('已标成生病：这几天不算进你的平常范围。','Marked as unwell: these days won’t count toward your usual range.')}</p>`:`<button class="btn sm ghost" data-act="marksick" style="margin-top:10px">${L('把这几天标成生病','Mark these days as unwell')}</button><p class="sm mu" style="margin-top:6px">${L('标了以后，这几天不算进平常范围，元气不会被拉低。','Then these days won’t count toward your usual range, so vitality isn’t pulled down.')}</p>`}</div>
   <div class="banner alr">${ic('sos',16)}<span>${L('气促、胸痛、意识不清，请马上拨打 995。','Breathless, chest pain or confused: call 995 now.')}</span></div>`:''}
  <button class="btn ghost" data-act="tempnow">${L('量一次（演示）','Take a reading (demo)')}</button>
  <p class="sm mu">${L('这是体温计的实测值。戒指的“体温偏差”是和你平常比的变化，两者不同。','This is the thermometer’s actual reading. The ring’s temperature change is a difference from your usual; they’re not the same.')}</p></div>`}};"""+s[b:]
# actions
R("    qoff(){","""    devconn(){if(v==='cgm')S.cgm=true;else S.own[v]=true;toast(L('已连接（演示）','Connected (demo)'));render()},
    devbuy(){toast(L('打开官方商城（原型）','Opening the official store (prototype)'))},
    famhelp(){sheet(`<h2 class="h2" style="font-size:20px">${L('请家人帮我连','Ask family to help')}</h2><p class="p" style="margin-top:8px">${L('会发给慧敏一张图文步骤卡：打开设备、靠近手机、在荷汀里点“连接”。她也可以下次来家里时，用你的手机帮你连。','We’ll send Hui Min a picture card: switch the device on, hold it near the phone, tap Connect in Otio. She can also do it on your phone next visit.')}</p><button class="btn" data-act="sheetclose" style="margin-top:12px">${L('发给慧敏','Send to Hui Min')}</button>`)},
    tempnow(){S.temp={v:S.temp.v>=38?36.8:38.4,at:1};render()},
    marksick(){S.sick=true;toast(L('已标成生病','Marked as unwell'));render()},
    qoff(){""")
# health checks section rebuild
a=s.index("""  <div class="card vitals2">\n   ${vrow2({go:'bp'""");b=s.index("\n  </div>",a)+len("\n  </div>")
s=s[:a]+r"""  <div class="card vitals2">
   ${owns('bp')?vrow2({go:'bp',c:b?'var(--tLow)':'var(--c-jz)',ic:'gauge',k:L('血压','Blood pressure'),st:b?L('今早高于上限','Above limit this morning'):lk?L('早上 · 在目标内','Morning · on target'):L('早上 · 在参考值内','Morning · within reference'),v:b?'172/104':'128/80',u:'mmHg',bar:rbar('var(--c-jz)',110,135,100,175,b?172:128,[lk?L('目标','target'):L('参考','ref'),'<135'])}):''}
   ${owns('ecg')?vrow2({go:'ecg',c:'var(--c-ts)',ic:'ecg',k:L('心电','ECG'),st:lk?L('最近一条窦性心律','Latest: sinus rhythm'):L('设备分析：窦性心律','Device: sinus rhythm'),v:3,u:L('条/月','/mo')}):''}
   ${vrow2({go:'rhythm',c:'var(--c-oh)',ic:'heart',k:L('夜间心律提示','Night rhythm alerts'),st:L('看规律，不看快慢','Regularity, not speed'),v:'',u:L('即将开放','Coming soon')})}
   ${S.cgm?vrow2({go:'glucose',c:'var(--c-xs)',ic:'drop',k:L('血糖','Glucose'),st:S.cgmDay>=13?`<span style="color:var(--tLow)">${L('明天该换贴片了','Change sensor tomorrow')}</span>`:L('贴片第 '+S.cgmDay+'/14 天','Sensor day '+S.cgmDay+' of 14'),v:'6.2',u:'mmol/L',bar:rb('var(--c-xs)',3.9,10,6.2)}):''}
   ${owns('thermo')?vrow2({go:'thermo',c:S.temp.v>=38?'var(--tLow)':'var(--c-ts)',ic:'temp',k:L('体温','Temperature'),st:S.temp.v>=38?L('有点发烧','A bit of a fever'):S.temp.at?L('刚刚量的','Just now'):L('今天 7:10 量的','Today 7:10'),v:S.temp.v.toFixed(1),u:'°C'}):''}
   ${lk?vrow2({go:'fundus',c:'var(--c-zq)',ic:'eye',k:L('眼底筛查','Eye screening'),st:L('医生已审阅','Reviewed'),v:'',u:L('9 月 26 日','26 Sep')}):''}
   ${lk?vrow2({go:'report',c:'var(--c-mo)',ic:'doc',k:L('9 月报告','Sep report'),st:L('周医生签发','Signed by Dr Zhou'),v:'',u:'10/3'}):vrow2({go:'summary',c:'var(--c-mo)',ic:'file',k:L('复诊一页纸','Visit summary'),st:L('看诊时给医生看','Show your doctor'),v:'',u:''})}
  </div>
  ${DEVS().some(x=>!owns(x.k))?`<button class="link" data-go="store" style="text-align:left;color:var(--mu);font-weight:500;padding:4px 2px">${L('加血压计、体温计等设备 ›','Add a BP monitor, thermometer or more ›')}</button>`:''}"""+s[b:]
# glucose page solo copy + change reminder
R("""<div><span>${L('数据来源','Data from')}</span><span>${L('Sinocare 云端 → RPM 平台','Sinocare cloud → RPM platform')}</span></div><div><span>${L('低血糖提醒','Low alert')}</span><span>${L('低于 3.9 通知护士','Below 3.9 alerts nurse')}</span></div>""",
  """${linked()?`<div><span>${L('数据来源','Data from')}</span><span>${L('Sinocare 云端 → RPM 平台','Sinocare cloud → RPM platform')}</span></div><div><span>${L('低血糖提醒','Low alert')}</span><span>${L('低于 3.9 通知护士','Below 3.9 alerts nurse')}</span></div>`:`<div><span>${L('参考范围','Reference')}</span><span>3.9–10.0 mmol/L</span></div>`}""")
R("""<div><span>${L('传感器','Sensor')}</span><span>${L('第 9/14 天','Day 9 of 14')}</span></div>""","""<div><span>${L('传感器','Sensor')}</span><span>${L('第 '+S.cgmDay+'/14 天','Day '+S.cgmDay+' of 14')}${S.cgmDay>=13?' · '+L('明天该换了','change tomorrow'):''}</span></div>""")
R("L('午饭后升得最高（9.8）。吃饭时记一笔，护士复盘时更容易看出原因。','Your highest rise was after lunch (9.8). Logging meals helps your nurse see why at the review.')","linked()?L('午饭后升得最高（9.8）。吃饭时记一笔，护士复盘时更容易看出原因。','Your highest rise was after lunch (9.8). Logging meals helps your nurse see why at the review.'):L('午饭后升得最高（9.8）。吃饭时记一笔，自己更容易看出是哪顿饭。','Your highest rise was after lunch (9.8). Logging meals helps you see which meal did it.')")
# mattress source in trend
R("${k==='steps'?L('戒指和手机','Ring and phone'):L('荷汀戒指 · 参考数据','Otio ring · for context')}","${k==='steps'?L('戒指和手机','Ring and phone'):(S.own.mat&&['sleep','resp'].includes(k)?L('荷汀戒指 / 睡眠床垫 · 参考数据','Otio ring / sleep mat · for context'):L('荷汀戒指 · 参考数据','Otio ring · for context'))}")
# summary rows
R("""   ${row(L('夜间血氧','Overnight oxygen'),L('戒指估算 · 26/30 晚'""","""   ${S.cgm?row(L('血糖','Glucose'),L('连续血糖仪 · 型号待定','CGM · model TBC'),[['v',L('14 天里 81% 的时间在 3.9–10.0','81% of 14 days within 3.9–10.0')],['v',L('最高 9.8（午饭后）','Highest 9.8, after lunch')]]):''}
   ${S.own.thermo?row(L('体温','Temperature'),L('蓝牙体温计 · 型号待定','Bluetooth thermometer · model TBC'),[['v',S.temp.v>=38?L('最高 '+S.temp.v.toFixed(1)+'°C','Highest '+S.temp.v.toFixed(1)+'°C'):L('近 30 天没有发烧','No fever in 30 days')]]):''}
   ${row(L('夜间血氧','Overnight oxygen'),L('戒指估算 · 26/30 晚'""")
# summary missing BP hint (solo)
R("""<div style="padding-top:10px;font-size:14px;line-height:1.55;color:#2E3B44">${L('戒指非医疗器械""","""${owns('bp')?'':`<button class="link" data-go="store" style="text-align:left;font-size:14px;padding:8px 0 0">${L('没有血压计？看医生前在家量几次更有用 ›','No BP monitor? A few home readings before the visit help ›')}</button>`}<div style="padding-top:10px;font-size:14px;line-height:1.55;color:#2E3B44">${L('戒指非医疗器械""")
# checkout: own ECG card
R("""    <div><span>${L('心电卡（计划期内借用）','ECG card, on loan')}</span><span>${ic('check',16,2)}</span></div>""","""    <div><span>${S.own.ecg?L('心电卡：用你自己的','ECG card: your own'):L('心电卡（计划期内借用）','ECG card, on loan')}</span><span>${ic('check',16,2)}</span></div>""")
R("""  <div class="tot"><span>${L('合计（含 GST）','Total (incl. GST)')}</span><span class="num">S$39.00</span></div></div>""","""  ${S.own.ecg&&!linked()?`<div class="sub"><span>${L('已有心电卡，不收借用费（金额待定）','You have an ECG card, so no loan fee (amount TBC)')}</span><span class="num">−S$5.00</span></div>`:''}
  <div class="tot"><span>${L('合计（含 GST）','Total (incl. GST)')}</span><span class="num">${S.own.ecg&&!linked()?'S$34.00':'S$39.00'}</span></div></div>""")
# pair page solo copy
R("L('戒指或手环就够了；有血压计、心电卡也可以连。','Your ring or band is enough. You can add a BP monitor or ECG card too.')","L('戒指就够了。有 BioVision 严选设备，现在连，或以后在“我的 › 设备”里加。','The ring is enough. Have a BioVision device? Connect it now or later in Me › Devices.')")
# today: ECG prompt in solo if own ecg
R("  if(S.scen==='night'&&linked())return S.ecgSent?","  if(S.scen==='night'&&(linked()||S.own.ecg))return S.ecgSent?")
R("L('<b>v3.8.24</b>：","L('<b>v3.8.25</b>：自己用也能接 BioVision 严选设备（血压计、心电卡、连续血糖仪、蓝牙体温计、睡眠床垫）：“我的 › 设备”只列已连设备，加设备进严选页（每样写谁需要、谁不需要、和戒指的区别，去购买跳官方商城，可请家人帮忙连）；身体页只显示已连设备，最后一行“加设备”；体温计量到 38°C 以上给一句建议和 995，并可把这几天标成生病；血糖仪显示贴片第几天、第 13 天提醒换；床垫作为睡眠和呼吸的备用来源；复诊一页纸带上血糖和体温；没有血压计时提醒一次；连诊所时已有心电卡不收借用费。<br><b>v3.8.24</b>：")
R("'<b>v3.8.24</b>: Today","'<b>v3.8.25</b>: On your own you can add BioVision picks (BP monitor, ECG card, CGM, Bluetooth thermometer, sleep mat): Devices lists only connected ones; a picks page says who each is for and not for and how it differs from the ring, buying opens the official store, family can help connect; Health shows only connected devices with one Add line; a thermometer reading of 38°C+ gets advice, 995 and an option to mark the days unwell; the CGM shows its sensor day and a day-13 change reminder; the mat backs up sleep and breathing; the visit summary includes glucose and temperature; a one-time nudge if there’s no BP monitor; linking a clinic with your own ECG card drops the loan fee.<br><b>v3.8.24</b>: Today")
open(p,'w',encoding='utf-8').write(s)
i=s.rindex('})();');s=s[:i]+'window.__t={get S(){return S},go,render,tband,tseries};\n'+s[i:]
open(d+'otiagen/sw_test.html','w',encoding='utf-8').write(s)
print('ok')
