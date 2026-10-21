import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
UNI_ZH='设备自动分析（MD100C，注册证号待填）· 连诊所后另有医生判读'
UNI_EN='Device analysis (MD100C, reg. no. TBC) · read by a doctor once linked'
# ---- ECG records: state-driven ----
R("""function ecgRecs(){const a=[];
  if(S.ecgSent)a.push({id:'new',at:L('今天 8:31','Today 8:31'),hr:74,st:'await',seed:21});""",
"""function ecgRecs(){const a=[];
  if(!linked()){const sin=L('窦性心律','Sinus rhythm');
   if(S.ecgSent)a.push({id:'new',at:L('今天 8:31','Today 8:31'),hr:74,st:'dev',res:sin,seed:21});
   a.push({id:'e3',at:L('10月9日 21:05','9 Oct 9:05 pm'),hr:69,st:'dev',res:sin,seed:9});
   a.push({id:'e2b',at:L('10月2日 20:40','2 Oct 8:40 pm'),hr:70,st:'dev',res:sin,seed:7});
   a.push({id:'e2',at:L('10月2日 7:50','2 Oct 7:50 am'),hr:null,st:'dev',bad:1,res:L('信号差，无法分析（当天已重录）','Poor signal, not analysed (retaken the same day)'),seed:4,noise:.5});
   a.push({id:'e1',at:L('9月29日 8:10','29 Sep 8:10 am'),hr:68,st:'dev',res:sin,seed:12});
   return a}
  if(S.ecgSent)a.push({id:'new',at:L('今天 8:31','Today 8:31'),hr:74,st:'await',seed:21});""")
R("""  a.push({id:'e2',at:L('10月2日 7:50','2 Oct 7:50 am'),hr:null,st:'retake',by:NUs(),""","""  a.push({id:'e2b',at:L('10月2日 20:40','2 Oct 8:40 pm'),hr:70,st:'done',res:L('窦性心律','Sinus rhythm'),by:DRs(),note:L('重录的这条节律正常。','The retaken ECG shows a normal rhythm.'),seed:7});
  a.push({id:'e2',at:L('10月2日 7:50','2 Oct 7:50 am'),hr:null,st:'retook',by:NUs(),""")
R("""function ecgSt(r){return r.st==='await'?""","""function ecgSt(r){return r.st==='dev'?`<span class="tag ${r.bad?'warn':'ok'}">${r.bad?L('信号差','Poor signal'):L('设备分析：','Device: ')+r.res}</span>`:r.st==='retook'?`<span class="tag mu">${L('已重录','Retaken')}</span>`:r.st==='await'?""")
R("""L('每一条心电都由诊所医生判读。App 不做自动判断，也不会自动给出房颤结论。','Every ECG is read by a doctor at your clinic. The app doesn’t interpret ECGs and won’t give an automatic AF result.'):L('没有连诊所时，心电只保存在你这里，可以导出 PDF 给医生看。','Without a clinic linked, ECGs stay with you; export a PDF for any doctor.')""",
"""L('每一条心电由'+DRs()+'判读。设备自动分析（MD100C，注册证号待填）只作参考。','Every ECG is read by '+DRs()+'. The device analysis (MD100C, reg. no. TBC) is for reference only.'):L('"""+UNI_ZH+"""。心电保存在你的手机上，可以导出 PDF 给医生看。','"""+UNI_EN+""". ECGs stay on your phone; export a PDF for any doctor.')""")
R("""${r.st==='retake'?L('陈','C'):L(r.by.slice(0,1),r.by.split(' ')[1].slice(0,1))}""","""${r.st==='retake'||r.st==='retook'?L('陈','C'):(S.lang==='zh'?r.by.slice(0,1):(r.by.split(' ')[1]||r.by).slice(0,1))}""")
R("""<div class="sm mu">${r.st==='retake'?L('请你重录','asked for a retake'):L('判读','read this ECG')}</div>""","""<div class="sm mu">${r.st==='retake'||r.st==='retook'?L('请你重录','asked for a retake'):L('判读','read this ECG')}</div>""")
R("""  ${r.st==='await'?`<div class="banner care">""","""  ${r.st==='dev'?`<div class="card"><div class="h3">${L('设备分析：','Device analysis: ')}${r.res}</div><p class="sm mu" style="margin:6px 0 0">${L('"""+UNI_ZH+"""。不是诊断。','"""+UNI_EN+""". Not a diagnosis.')}</p></div>`:r.st==='await'?`<div class="banner care">""")
R("""  <button class="btn ghost" data-act="pdf">${ic('upload',18)} ${L('导出 PDF','Export PDF')}</button>
 </div>`}};""","""  ${linked()?'':`<button class="btn ghost" data-act="pdf">${ic('upload',18)} ${L('导出 PDF','Export PDF')}</button>`}
 </div>`}};""")
R("""${L('记录 30 秒，结束后自动上传。','It records for 30 seconds, then uploads.')}""","""${linked()?L('记录 30 秒，结束后自动上传。','It records for 30 seconds, then uploads.'):L('记录 30 秒，结束后保存在手机上。','It records for 30 seconds, then saves on your phone.')}""")
R("""L('已保存','Saved')}</h1>""","""L('已保存在手机上','Saved on your phone')}</h1>""")
R("""L('App 不会自动判断心电。医生看完后，结果会出现在“心电”里，并通知你。','The app doesn’t interpret your ECG. When the doctor has read it, the result appears under ECG and you’ll be notified.'):L('可以导出 PDF 给医生看。','You can export a PDF for a doctor.')""",
"""L('医生看完后，结果会出现在“心电”里，并通知你。','When the doctor has read it, the result appears under ECG and you’ll be notified.'):L('设备分析：窦性心律。"""+UNI_ZH+"""。可以导出 PDF 给医生看。','Device analysis: sinus rhythm. """+UNI_EN+""". You can export a PDF for a doctor.')""")
# summary / sumdoc dates
R("""L('MD100C 心电卡 · 注册证号待填 · 设备自动分析','MD100C ECG card · reg. no. TBC · device analysis'),[['v',L('9 月 20 日：窦性心律','20 Sep: sinus rhythm')]""","""L('"""+UNI_ZH+"""','"""+UNI_EN+"""'),[['v',L('9 月 29 日：窦性心律','29 Sep: sinus rhythm')]""")
R("""['20 Sep sinus · 2 Oct poor signal""","""['29 Sep sinus · 2 Oct poor signal""")
# ---- alert ----
R("""<div class="kv" style="margin-top:4px"><div><span style="text-align:left">${L('坐下，背靠椅背，双脚平放','Sit back in a chair, feet flat')}</span><span>${ic('check',16,2)}</span></div><div><span style="text-align:left">${L('手臂放在桌上，和心脏一样高','Rest your arm on a table at heart level')}</span><span>${ic('check',16,2)}</span></div><div><span style="text-align:left">${L('安静休息 5 分钟，再量一次','Rest quietly for 5 minutes, then measure again')}</span><span>${ic('clock',16,2)}</span></div></div></div>
  <button class="btn" data-act="bpre">${L('已休息 5 分钟，再量一次','I’ve rested 5 minutes, measure again')}</button>${safety()}`;""",
"""<div class="kv" style="margin-top:4px"><div><span>1</span><span style="text-align:left;flex:1;margin-left:12px">${L('坐下，背靠椅背，双脚平放','Sit back in a chair, feet flat')}</span></div><div><span>2</span><span style="text-align:left;flex:1;margin-left:12px">${L('手臂放在桌上，和心脏一样高','Rest your arm on a table at heart level')}</span></div><div><span>3</span><span style="text-align:left;flex:1;margin-left:12px">${L('安静休息 5 分钟，再量一次','Rest quietly for 5 minutes, then measure again')}</span></div></div></div>
  <button class="btn" data-act="bpre" id="bpre-btn" disabled style="opacity:.5">${L('已休息 5 分钟，再量一次','I’ve rested 5 minutes, measure again')} · <span id="bpcd" class="num">5:00</span></button><button class="link" data-act="bpskip" style="color:var(--mu);font-weight:500;font-size:13px">${L('（演示）跳过等待','(Demo) skip the wait')}</button>${safety()}`;""")
R("""<div class="card"><div class="h3">${L('昨晚和今早的药吃了吗？','Did you take last night’s and this morning’s medicine?')}</div><div class="qr" style="margin-top:10px">${[L('都吃了','Yes, both'),L('昨晚忘了','Missed last night'),L('今早忘了','Missed this morning')]""",
"""<div class="card"><div class="h3">${L('今早的氨氯地平吃了吗？','Did you take this morning’s amlodipine?')}</div><div class="qr" style="margin-top:10px">${[L('吃了','Taken'),L('还没吃','Not yet')]""")
R("""  ${safety()}<button class="btn ghost" data-act="call995">${ic('phone',18)} ${L('拨打 995','Call 995')}</button>`;""","""  ${safety()}`;""")
R("""P.alert=()=>{const st=S.bp.step;""","""P.alert=()=>{const st=S.bp.step;if(st===0&&!S.bp.t0)S.bp.t0=Date.now();""")
R("""return{calm:1,html:`${nav(L('血压偏高','High blood pressure'))}""","""return{calm:1,after(){if(S.bp.step!==0)return;const tick=()=>{const b=document.getElementById('bpre-btn'),c=document.getElementById('bpcd');if(!b){clearInterval(id);return}const r=Math.max(0,300-Math.floor((Date.now()-S.bp.t0)/1000));if(c)c.textContent=Math.floor(r/60)+':'+String(r%60).padStart(2,'0');if(!r){b.disabled=false;b.style.opacity='';clearInterval(id)}};const id=setInterval(tick,1000);tick()},html:`${nav(L('血压偏高','High blood pressure'))}""")
R("""    bpre(){S.bp.step=1;""","""    bpskip(){S.bp.t0=Date.now()-300000;render()},
    bpre(){S.bp.t0=0;S.bp.step=1;""")
# ---- care ----
R("""   ${taskRow('bpam',L('早上量血压','Morning BP'),S.scen==='bp'?L('172/104 · 已通知护士','172/104 · nurse notified'):'128/80','7:42')}""",
"""   ${devRow(L('早上量血压','Morning BP'),L('7:42 · 血压计自动记下','7:42 · recorded by your BP monitor')+(S.scen==='bp'?L(' · 已通知护士',' · nurse notified'):''),S.scen==='bp'?'172/104':'128/80',S.scen==='bp')}""")
R("""   ${taskRow('ring',L('戴戒指睡觉','Wear ring overnight'),L('记录到 6 小时 48 分','6 h 48 min recorded'),'')}""",
"""   ${devRow(L('戴戒指睡觉','Wear ring overnight'),L('戒指自动记下','Recorded by your ring'),L('6 小时 48 分','6 h 48 min'))}""")
R("""   ${taskRow('bppm',L('晚上量血压','Evening BP'),L('晚饭后 1 小时','1 hour after dinner'),'20:00')}""",
"""   ${devRow(L('晚上量血压','Evening BP'),L('20:00 · 晚饭后 1 小时 · 量完自动记上','8 pm · 1 hour after dinner · recorded automatically'),'')}""")
R("""function taskRow(k,t,sub,tm){""","""function devRow(t,sub,val,hi){return `<div class="task ${val?'done':''}"><span class="bx" style="${val?'':'border-style:dashed'}">${val?ic('check',14,2.6):''}</span><span class="t"><span>${t}</span><small>${sub}</small></span><span class="num" style="font-size:15px;${hi?'color:var(--tLow)':''}">${val}</span></div>`}
function taskRow(k,t,sub,tm){""")
R("""  <div class="card"><div class="between"><span class="h3">${L('我自己的习惯','My own habits')}</span><button class="link" data-act="mpchg">${L('改一改','Change')}</button></div>${focusCard(true)}<p class="sm mu" style="margin:8px 0 0">${L('医生安排了运动时，以医生的为准。','If your doctor sets exercise, follow that instead.')}</p></div>""",
"""  <div class="card flush">${li('leaf',L('我自己的习惯','My own habits'),FOC()[MP().focus].t+' · '+L('这周 '+focCnt()+' 天','this week: '+focCnt()+' days'),'myhab')}</div>""")
# message feed: latest only
i=s.index("""  <div class="card"><div class="h3">${L('护理团队的消息','From your care team')}</div><div style="margin-top:4px">""")
j=s.index("""  </div></div>""",i)+len("""  </div></div>""")
s=s[:i]+"""  <div class="card"><div class="between"><span class="h3">${L('护理团队的消息','From your care team')}</span><button class="link" data-go="msgs">${L('全部消息 ›','All messages ›')}</button></div><div style="margin-top:4px">
   ${unread||S.scen==='msg'?`<div class="feed"><span class="av sm2">${L('陈','C')}</span><span class="t"><b>${NUs()}</b> ${L('周医生看了你 10/9 的心电，节律正常。下午 2 点电话见。','Dr Zhou read your 9 Oct ECG: normal rhythm. Speak at 2 pm.')}<span class="w">${L('刚刚','Just now')}</span></span></div>`
   :S.ecgSent?`<div class="feed"><span class="av sm2">${ic('ecg',14)}</span><span class="t">${L('你的心电已进入'+DRs()+'的判读队列。','Your ECG is in '+DRs()+'’s review queue.')}<span class="w">${L('今天 8:31','Today 8:31')}</span></span></div>`
   :`<div class="feed"><span class="av sm2">${L('周','Z')}</span><span class="t"><b>${DRs()}</b> ${L('签发了 9 月监测报告：早上血压 30 天里 24 天在目标内，9 月的 1 条心电是窦性心律；夜间血氧最低 88%，复诊时讨论要不要做睡眠检查。','signed your September report: morning BP was on target on 24 of 30 days, and your 1 ECG in September showed sinus rhythm. Overnight oxygen was as low as 88%; we’ll discuss whether you need a sleep study at your next visit.')}<span class="w">${L('10月3日','3 Oct')}</span></span></div>`}
  </div></div>"""+s[j:]
# myhab page + count helper
R("""P.connect=(asTab)=>""","""P.myhab=()=>({calm:1,html:`${nav(L('我自己的习惯','My own habits'))}<div class="pad stack">${focusCard(false)}<p class="sm mu">${L('医生安排了运动时，以医生的为准。','If your doctor sets exercise, follow that instead.')}</p></div>`});
P.connect=(asTab)=>""")
R("""function focusCard(inCare){""","""function focCnt(){const m=MP(),f=FOC()[m.focus],TD=2,today=isDone(m.focus)?1:0,st0=TD-(m.fday-1);return f.wk.concat([today]).map((v,i)=>i<st0?0:v).filter(v=>v>0).length}
function focusCard(inCare){""")
R("""report:'care',summary:'health',""","""report:'care',myhab:'care',summary:'health',""")
# ---- appt ----
R("""   ${row('a',S.scen==='night'?L('夜里血氧低到 88%','Oxygen dipped to 88% overnight'):L('早上偶尔头有点胀','Some mornings my head feels heavy'))}
   ${row('b',L('阿托伐他汀晚上有时忘吃','Sometimes I forget the atorvastatin at night'))}
   ${row('c',L('想问能不能恢复游泳','Can I go back to swimming?'))}</div>""",
"""   ${row('a',L('夜里血氧最低 88%，要紧吗？（戒指数据）','Overnight oxygen fell to 88%: is that a concern? (from your ring)'))}</div>
   <button class="mpchip" data-act="apvoice" style="margin-top:8px">${ic('mic',14)} ${L('说一句','Say it')}</button>""")
R("prep:{a:1,b:0,c:0}","prep:{a:0}")
R("""    resched(){""","""    apvoice(){toast(L('按住说话，说完会加到这里（原型）','Hold to speak; it’s added here (prototype)'))},
    resched(){""")
# ---- plan ----
R("""  <div class="h2">${L('可以加上','Add on')}</div>
  <div class="card flush">${li('gauge',L('血压管理计划','BP care plan'),L('+S$29/月 · 护士每周看血压','+S$29/month · weekly nurse BP review'),null,null,{act:'addon'})}${li('drop',L('14 天血糖检查','14-day glucose check'),L('一次性 S$199','One-off S$199'),'check14')}</div>
""","")
R("""<button class="link" data-act="stopplan" style="color:var(--tLow)">""","""<button class="link" data-act="withdraw" style="color:var(--tLow)">""")
# ---- share ----
R("""L('戒指 · 低于 90% 超过 5 分钟会提醒护士','Ring · under 90% for 5+ min alerts the nurse')""","""L('戒指估算 · 护士每天查看时参考','Ring estimate · your nurse reviews it daily as a reference')""")
R("""   ${row('stress',L('压力（实验）','Stress (beta)'),L('默认不分享','Off by default'))}
""","")
# ---- report ----
R("""<span>${L('血压（早上平均）','BP, morning average')}</span><span class="num">131/82</span>""","""<span>${L('血压（早上平均）','BP, morning average')}</span><span class="num">133/83</span>""")
R("""L('3 条 · 窦性心律','3 · sinus rhythm')""","""L('1 条（9/29）· 窦性心律','1 (29 Sep) · sinus rhythm')""")
R("""<div><span>${L('夜间血氧低于 90% 的晚上','Nights with oxygen under 90%')}</span><span class="num">2</span></div>""","""<div><span>${L('夜间血氧（戒指估算，仅供参考）','Overnight oxygen (ring estimate, for reference)')}</span><span class="num">${L('最低 88%','Lowest 88%')}</span></div>""")
R("""L('血压控制良好，继续现在的用药。夜间血氧有 2 晚低于 90%，下次复诊讨论是否需要做睡眠检查。','BP is well controlled; keep your current medicines. Oxygen fell below 90% on 2 nights; we’ll discuss whether you need a sleep study at your next visit.')""",
"""L('血压控制良好，继续现在的用药。夜间血氧最低到 88%，下次复诊讨论是否需要做睡眠检查。','BP is well controlled; keep your current medicines. Overnight oxygen fell as low as 88%; we’ll discuss whether you need a sleep study at your next visit.')""")
# ---- survey ----
R("""  <button class="btn" data-act="svsend">${L('发给陈护士','Send to Nurse Chen')}</button></div>`}};""",
"""  ${S.survey[0]===2||S.survey[1]===2?`<div class="card" style="border:1.5px solid var(--tLow)"><div class="h3" style="color:var(--tLow)">${L('今天就打给诊所','Call your clinic today')}</div><p class="sm mu" style="margin:6px 0 10px">${L('经常胸闷或气短，需要护士今天就了解。这份问卷会标为优先。','Frequent chest tightness or breathlessness: your nurse should know today. This check will be marked urgent.')}</p><button class="btn sm" data-act="callclinic">${ic('phone',16)} ${L('打给诊所','Call the clinic')}</button></div>${safety()}`:''}
  <button class="btn" data-act="svsend" ${Object.keys(S.survey).length<4?'disabled style="opacity:.5"':''}>${L('发给陈护士','Send to Nurse Chen')}</button></div>`}};""")
R("""    svsend(){S.tasks.survey=true;toast(L('已发给陈护士','Sent to Nurse Chen'));back()},""","""    svsend(){if(Object.keys(S.survey).length<4)return;const u=S.survey[0]===2||S.survey[1]===2;S.tasks.survey=true;toast(u?L('已发给陈护士，标为优先','Sent to Nurse Chen, marked urgent'):L('已发给陈护士','Sent to Nurse Chen'));back()},""")
open(p,'w',encoding='utf-8').write(s); print('ok')
