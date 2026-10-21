import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# ---- vera
i=s.index("const VQ=()=>[[L('夜里血氧为什么会低？'");j=s.index("P.vera=q=>")
s=s[:i]+r"""const VQ=()=>linked()?[[L('夜里血氧为什么会低？','Why was my oxygen low overnight?'),L('可能和睡姿、鼻塞或睡眠呼吸暂停有关。戒指不能诊断，只能告诉你哪一晚、几点、多久。你的医生设了规则，低于 90% 超过 5 分钟会让护士看一下。','It can be sleeping position, a blocked nose or sleep apnoea. The ring can’t diagnose it; it can only show which night, what time and for how long. Your doctor’s rule has a nurse look when it stays under 90% for more than 5 minutes.')],
 [L('128/80 算好吗？','Is 128/80 okay?'),L('在你医生定的家庭目标（135/85 以下）里面。早晚各量一次、坐着休息 5 分钟后再量，数更准。','It’s within the home target your doctor set (under 135/85). Measuring morning and evening, after 5 minutes of sitting, gives the most reliable numbers.')],
 [L('下午电话要问陈护士什么？','What should I ask Nurse Chen at 2 pm?'),L('可以问：最近早上头胀要不要紧；漏吃药要不要告诉护士；能不能恢复游泳。我已经帮你放进“想提的事”。','You could ask: whether the heavy-head mornings matter; whether to tell the nurse about missed doses; and whether you can swim again. I’ve added them to “Things to bring up”.')]]
 :[[L('夜里血氧为什么会低？','Why was my oxygen low overnight?'),L('可能和睡姿、鼻塞或睡眠呼吸暂停有关。戒指不能诊断，只能告诉你哪一晚、最低多少。可以带上复诊一页纸问医生。','It can be sleeping position, a blocked nose or sleep apnoea. The ring can’t diagnose it; it can only show which night and how low. Bring your visit summary to your doctor.')],
 [L('128/80 算好吗？','Is 128/80 okay?'),L('在常用的家庭血压参考（135/85 以下）里面。适合你的目标请听医生的。早晚各量一次、坐着休息 5 分钟后再量，数更准。','It’s under the usual home reference of 135/85; your own target is for your doctor to set. Measuring morning and evening, after 5 minutes of sitting, gives the most reliable numbers.')],
 [L('明天看诊要问什么？','What should I ask at tomorrow’s visit?'),L('可以问：能不能恢复游泳；早上有几次血压偏高怎么办。我已经帮你加进复诊一页纸的“我想问”，看诊时给医生看。','You could ask whether you can swim again, and what to do about the few high morning readings. I’ve added them to My questions in your visit summary to show the doctor.')]];
"""+s[j:]
R("""${L(MR()+'，想问什么？我能解释你的数字，但不做诊断。要紧的事我会建议你直接找陈护士。','Hi '+MR()+', what would you like to know? I can explain your numbers but I don’t diagnose. For anything important I’ll point you to Nurse Chen.')}""",
"""${linked()?L(MR()+'，想问什么？我能解释你的数字，但不做诊断。要紧的事我会建议你直接找陈护士。','Hi '+MR()+', what would you like to know? I can explain your numbers but I don’t diagnose. For anything important I’ll point you to Nurse Chen.'):L(MR()+'，想问什么？我能解释你的数字，但不做诊断。要紧的事请找你的医生；胸痛、呼吸困难请拨 995。','Hi '+MR()+', what would you like to know? I can explain your numbers but I don’t diagnose. For anything important, see your doctor; for chest pain or trouble breathing, call 995.')}""")
R("    vq(){const x=VQ()[+v];S.vera.push(['u',x[0]],['v',x[1]]);render()},","    vq(){const x=VQ()[+v];S.vera.push(['u',x[0]],['v',x[1]]);if(!linked()&&+v===2){const q=SQ();['swim','ambp'].forEach(k=>{if(!q.includes(k)&&q.length<3)q.push(k)})}render()},")
# ---- notify
i=s.index("P.notify=()=>");j=s.index("P.privacy=()=>")
s=s[:i]+r"""P.notify=()=>{const n=S.notif,m=MP();const row=(k,t,sub,dis)=>`<div class="devcard"><span class="t">${t}<small>${sub}</small></span>${sw(k,dis?1:n[k],{dis,act:'notif',lab:t})}</div>`;
 const quiet=row('quiet',L('勿扰：上床到起床（'+m.bed+'–'+m.wake+'）','Quiet: bedtime to wake-up ('+m.bed+'–'+m.wake+')'),L('跟着你的作息；起床、上床提醒不受影响','Follows your routine; wake-up and bedtime reminders still come through')+(linked()?L('，护理团队的紧急联系也不受影响','; urgent care team contact too'):''));
 return{calm:1,html:`${nav(L('提醒与通知','Reminders & notifications'))}<div class="pad stack">
  <div class="card" style="padding:4px 16px">
   ${linked()?row('care',L('护理团队的消息和告警','Care team messages & alerts'),L('计划期间不能关','Always on while on a plan'),1)+row('bp',L('量血压提醒','BP reminders'),L('7:30 · 20:00'))+row('med',L('吃药提醒','Medicine reminders'),L('8:00 氨氯地平 · 22:30 阿托伐他汀','8:00 amlodipine · 22:30 atorvastatin')):''}
   ${row('ecg',L('提示记录心电','Prompts to record an ECG'),L('夜里血氧或心率异常后','After an overnight oxygen or heart rate change'))}
   ${quiet}
  </div>
  ${linked()?`<p class="sm mu" style="margin:0">${L('护理计划的提醒由诊所设置。','Care plan reminders are set by your clinic.')}</p>`:`<div class="card flush">${li('plan',L('吃药和习惯提醒','Medicine and habit reminders'),L('在计划设置里改','Change them in Plan settings'),null,null,{act:'notifplan'})}</div>`}
 </div>`}};
"""+s[j:]
R("    notif(){","    notifplan(){MP().step=3;go('mpsetup')},\n    notif(){")
# ---- me
R("""<div class="card tap" data-go="plan"><div class="team"><span class="av" style="--c:var(--vit)">${L('吴','G')}</span><div style="flex:1"><div class="h2">${NM()}</div><div class="sm mu">${linked()?L('心律监测计划 · '+CL(),'Heart rhythm plan · '+CL()):L('自己使用 · 未连诊所','On my own · no clinic linked')}</div></div><span class="chev">${ic('chev',16)}</span></div></div>""",
"""<div class="card ${linked()?'tap':''}" ${linked()?'data-go="plan"':''}><div class="team"><span class="av" style="--c:var(--vit)">${L('吴','G')}</span><div style="flex:1"><div class="h2">${NM()}</div><div class="sm mu">${linked()?L('心律监测计划 · '+CL(),'Heart rhythm plan · '+CL()):L('自己使用 · 未连诊所','On my own · no clinic linked')}</div></div>${linked()?`<span class="chev">${ic('chev',16)}</span>`:''}</div></div>""")
R("""   ${linked()?li('dollar',L('计划与账单','Plan & bill'),null,'plan',null,{c:'care'}):''}
""","")
R("L('起床上床、运动、提醒','Wake and bed, exercise, reminders')","L('作息、正在养成的习惯、提醒','Routine, current habit, reminders')")
# ---- privacy
R("dpo@veracare.sg","dpo@otio.sg")
R("${li('upload',L('导出我的数据','Export my data'),L('CSV + 心电 PDF','CSV plus ECG PDFs'),null,null,{act:'pdf'})}","${li('upload',L('导出我的数据','Export my data'),L('CSV + 心电 PDF','CSV plus ECG PDFs'),null,null,{act:'expx'})}")
R("    pdfgo(){","""    expx(){sheet(`<div class="stack" style="gap:10px"><h2 class="h2" style="font-size:20px">${L('导出我的数据','Export my data')}</h2><p class="p">${L('文件含健康数据，请只分享给信任的人。','This file contains your health data. Share it only with people you trust.')}</p><div class="kv"><div><span>${L('格式','Format')}</span><span>${L('CSV 表格 + 心电 PDF','CSV plus ECG PDFs')}</span></div><div><span>${L('范围','Range')}</span><span>${L('全部记录','All records')}</span></div></div><p class="sm mu" style="margin:0">${L('文件只存到这台手机，生成时间写在文件里。','Saved to this phone only; the file shows when it was made.')}</p><button class="btn" data-act="expgo">${L('导出','Export')}</button></div>`);const kb=document.querySelector('.sheet [data-act="sheetclose"]');if(kb)kb.textContent=L('取消','Cancel')},
    expgo(){const s2=document.querySelector('.sheet-bg');if(s2)s2.remove();toast(L('已导出（原型）','Exported (prototype)'))},
    pdfgo(){""")
# ---- about
R("L('不自动诊断，不自动判读心电，不估算血压和血糖，不是急救服务（紧急请拨 995）。','No automatic diagnosis, no automatic ECG reading, no BP or glucose estimates from the ring, and no emergency service (call 995).')",
  "L('不自动诊断，不估算血压和血糖，不是急救服务（紧急请拨 995）。心电结论来自心电卡自带的分析（注册办理中），App 不另做判读。','No automatic diagnosis, no BP or glucose estimates from the ring, and no emergency service (call 995). ECG results come from the card’s own analysis (registration in progress); the app adds no reading of its own.')")
# ---- family
R("fam:{hm:1}","fam:{hm:1,sl:0,hr:0,bp:0,ox:0}")
R("""${L('家人只看到“在不在平常范围”，看不到具体数值，也看不到你和护理团队的消息、心电。','Family only see whether things are in your usual range. They never see numbers, your care team messages or your ECGs.')}""",
"""${L('家人默认只看到总状态：“都和平常差不多”或“有一项需要留意”。看不到具体数值，也看不到你和护理团队的消息、心电。','By default family see one overall status: “About the same as usual” or “One thing to keep an eye on”. Never numbers, care team messages or ECGs.')}""")
R("""<div class="devcard"><span class="ic">${ic('users')}</span><span class="t">${L('女儿 · 吴慧敏','Goh Hui Min · daughter')}<small>${L('睡眠、静息心率、夜间血氧、血压在不在目标 · 到 2027.4.13','Sleep, resting HR, overnight oxygen, BP on target · until 13 Apr 2027')}</small></span>${sw('hm',S.fam.hm,{act:'fam',lab:'Hui Min'})}</div>""",
"""<div class="devcard"><span class="ic">${ic('users')}</span><span class="t">${L('女儿 · 吴慧敏','Goh Hui Min · daughter')}<small>${L('看到总状态 · 到 2027.4.13','Sees overall status · until 13 Apr 2027')}</small></span>${sw('hm',S.fam.hm,{act:'fam',lab:'Hui Min'})}</div>
   ${S.fam.hm?`<div class="sm mu" style="margin:8px 0 2px">${L('想让她多看一项，可以单独打开（只看在不在平常范围）：','To let her see more, switch items on one by one (in-range status only):')}</div>${[['sl',L('睡眠','Sleep')],['hr',L('静息心率','Resting heart rate')],['bp',L('血压','Blood pressure')],['ox',L('夜间血氧','Overnight oxygen')]].map(([k,t])=>`<div class="devcard"><span class="t">${t}</span>${sw(k,S.fam[k],{act:'fam',lab:t})}</div>`).join('')}`:''}""")
R("""${L('只有连续 3 天离开平常范围才提醒，例如“血压连续 3 天高于目标，可以问问最近怎么样”。荷汀康护不会替你呼救。','Only when something stays outside your usual range for 3 days, e.g. “BP above target 3 days running, maybe check in.” Otio Care never calls for help on your behalf.')}""",
"""${linked()?L('只有连续 3 天离开平常范围才提醒，例如“血压连续 3 天高于目标，可以问问最近怎么样”。荷汀康护不会替你呼救。','Only when something stays outside your usual range for 3 days, e.g. “BP above target 3 days running, maybe check in.” Otio Care never calls for help on your behalf.'):L('只有连续 3 天离开平常范围才提醒，例如“有一项连续 3 天和平常不一样，可以问问最近怎么样”。荷汀不会替你呼救。','Only when something stays outside your usual range for 3 days, e.g. “Something has been different from usual 3 days running, maybe check in.” Otio never calls for help on your behalf.')}""")
# ---- devices
R("""  <div class="card" style="padding:4px 16px"><div class="devcard"><span class="t">Healthy 365 · ${L('国家步数挑战赛','National Steps Challenge')}<small>${L('同步每天步数攒积分 · 接口待与保健促进局确认','Send daily steps for points · integration to be confirmed with HPB')}</small></span>${sw('h365',MP().h365,{act:'mph365',lab:'Healthy 365'})}</div></div>
  <div class="card flush">${li('link','Apple Health / Health Connect',L('同步步数、体重；不回写医疗读数','Sync steps and weight; medical readings aren’t written back'),null,null,{act:'hk'})}</div>""",
"""  <div class="card" style="padding:4px 16px"><div class="h3" style="padding-top:12px">${L('同步到其他 App','Sync with other apps')}</div><div class="devcard"><span class="t">Healthy 365<small>${L('每天步数攒积分 · 接口待与保健促进局确认','Daily steps for points · integration to be confirmed with HPB')}</small></span>${sw('h365',MP().h365,{act:'mph365',lab:'Healthy 365'})}</div>${li('link','Apple Health / Health Connect',L('步数、体重；不回写医疗读数','Steps and weight; medical readings aren’t written back'),null,null,{act:'hk'})}</div>""")
open(p,'w',encoding='utf-8').write(s); print('ok')
