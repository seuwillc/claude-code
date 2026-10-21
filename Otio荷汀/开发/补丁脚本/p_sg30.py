import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
CSS="""
.vs{font-size:17px;line-height:1.55;color:#10202A}.vs .row1{display:flex;flex-direction:column;gap:3px;padding:12px 0;border-bottom:1px solid rgba(17,32,42,.12)}.vs .row1:last-child{border-bottom:0}
.vs .k{font-weight:700;font-size:17px}.vs .src{font-size:13px;color:#2E3B44;font-weight:500}.vs .v{font-size:17px}.vs .tr{font-size:16px;font-weight:700}
.vqs{display:flex;flex-direction:column;gap:8px;margin-top:6px}.vq{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:12px;background:rgba(17,32,42,.06);font-size:17px}
.docm{font-size:19px;line-height:1.55;color:#10202A}.docm .k{font-weight:700}.docm .row1{padding:12px 0;border-bottom:1px solid rgba(17,32,42,.14)}
"""
i=s.index('</style>'); s=s[:i]+CSS+s[i:]
QS="""const VQ_OPTS=[['swim','还能游泳吗？','Can I swim again?'],['dose','药量要不要调整？','Should my medicine dose change?'],['oxy','夜里血氧最低到 88% 要紧吗？','Is a lowest overnight oxygen of 88% a concern?'],['ambp','早上血压有几次偏高，怎么办？','A few morning BP readings were high. What should I do?'],['ecgq','心电结果要注意什么？','Anything to note about my ECGs?']];
const VQ=()=>S.vq||(S.vq=['swim']);
"""
a=s.index("P.summary=()=>{"); b=s.index("\nP.",a+5)
SUM=QS+r"""P.summary=()=>{if(linked())return{calm:1,html:`${nav(L('复诊资料','Visit records'))}<div class="pad stack"><div class="banner care">${ic('team',18)}<span>${L('连上诊所后，复诊资料由 '+CL()+' 的护理团队负责：医生在病历里能看到你的全部读数，每月签发监测报告。需要看其他医生时，请诊所出具转诊信。','While you’re linked, '+CL()+'’s care team looks after your visit records: your doctor sees all your readings and signs a monthly report. If you need another doctor, ask the clinic for a referral letter.')}</span></div><div class="card flush">${li('doc',L('9 月监测报告','September report'),L('周医生 10/3 签发','Signed by Dr Zhou 3 Oct'),'report',null,{c:'care'})}${li('phone',L('准备随访要说的事','Prepare for your check-in'),L('今天 14:00 · 陈护士','Today 2:00 pm · Nurse Chen'),'appt',null,{c:'care'})}</div></div>`};
 const q=VQ(),row=(k,src,lines)=>`<div class="row1"><div><span class="k">${k}</span>${src?` <span class="src">· ${src}</span>`:''}</div>${lines.map(x=>`<div class="${x[0]}">${x[1]}</div>`).join('')}</div>`;
 const T=(dir,txt)=>['tr',`${dir} ${txt}`];
 return{calm:1,html:`${nav(L('复诊一页纸','Visit summary'))}<div class="pad stack">
  <p class="p">${L('带去给医生看的记录。看诊时点“给医生看”，或导出 PDF 打印。','A record to take to your doctor. At the visit, tap Show doctor, or export a PDF to print.')}</p>
  <div class="card" style="background-color:rgba(255,255,255,.95)"><div class="vs">
   <div style="padding-bottom:8px;border-bottom:2px solid rgba(17,32,42,.2)"><div class="k" style="font-size:19px">${NM()}</div><div class="v">${L('2026 年 9 月 15 日至 10 月 14 日（30 天）· 有数据 28/30 天','15 Sep – 14 Oct 2026 (30 days) · data on 28 of 30 days')}</div></div>
   <div class="row1"><div class="k">${L('我想问','My questions')}</div><div class="vqs">${q.length?q.map(k=>{const o=VQ_OPTS.find(x=>x[0]===k);return `<div class="vq">${ic('chat',18)}<span style="flex:1">${o?L(o[1],o[2]):k}</span><button class="link" data-act="vqdel" data-v="${k}" aria-label="${L('删除','Remove')}" style="color:#2E3B44">${ic('close',16)}</button></div>`}).join(''):`<div class="v">${L('还没有','None yet')}</div>`}</div>${q.length<3?`<div class="mpchips">${VQ_OPTS.filter(o=>!q.includes(o[0])).slice(0,3).map(o=>`<button class="mpchip" data-act="vqadd" data-v="${o[0]}">+ ${L(o[1],o[2])}</button>`).join('')}<button class="mpchip" data-act="vqvoice">${ic('mic',14)} ${L('说一句','Say it')}</button></div>`:`<div class="src">${L('最多 3 条','Up to 3')}</div>`}</div>
   ${row(L('血压','Blood pressure')+' (mmHg)',L('上臂血压计 · 型号与注册证号待填','Upper-arm monitor · model and reg. no. TBC'),[['v',L('早上量 28 次，平均 131/82','Morning: 28 readings, average 131/82')],T('↓',L('前 30 天 135/84','Previous 30 days 135/84')),['v',L('达到或超过 135/85 的有 6 次；最高 152/94（10 月 2 日）','6 readings at or above 135/85; highest 152/94 (2 Oct)')],['v',L('晚上量 22 次，平均 128/80','Evening: 22 readings, average 128/80')],T('＝',L('差不多（前 30 天 130/82）','About the same (previous 30 days 130/82)'))])}
   ${row(L('用药','Medicines'),L('自己记录','self-recorded'),[['v',L('氨氯地平 5 mg，每天 1 次','Amlodipine 5 mg, once a day')],['v',L('漏服 3 天：9 月 22 日、10 月 1 日、10 月 9 日','Missed 3 days: 22 Sep, 1 Oct, 9 Oct')]])}
   ${row(L('症状','Symptoms'),L('自己记录','self-recorded'),[['v',L('未记录','None recorded')]])}
   ${row(L('心电','ECG'),L('MD100C 心电卡 · 注册证号待填 · 设备自动分析','MD100C ECG card · reg. no. TBC · device analysis'),[['v',L('9 月 20 日：窦性心律','20 Sep: sinus rhythm')],['v',L('10 月 2 日：信号差，当天重测为窦性心律','2 Oct: poor signal; retaken the same day, sinus rhythm')],['v',L('10 月 9 日：窦性心律','9 Oct: sinus rhythm')],['src',L('原始波形图附在 PDF 里','Original tracings attached to the PDF')]])}
   ${row(L('夜间血氧','Overnight oxygen'),L('戒指估算 · 26/30 晚','ring estimate · 26 of 30 nights'),[['v',L('每晚平均 94–96%','Nightly average 94–96%')],['v',L('最低读数 88%（10 月 3 日夜里）','Lowest reading 88% (night of 3 Oct)')]])}
   ${row(L('夜间静息心率','Overnight resting heart rate'),L('戒指 · 26/30 晚','ring · 26 of 30 nights'),[['v',L('中位数 62 次/分（每晚 58–66）','Median 62 bpm (nightly 58–66)')],T('＝',L('差不多','About the same'))])}
   ${row(L('睡眠和步数','Sleep and steps'),L('戒指','ring'),[['v',L('平均睡 6 小时 46 分','Average sleep 6 h 46 min')],T('＝',L('差不多','About the same')),['v',L('平均每天 5,420 步','Average 5,420 steps a day')],T('＝',L('差不多','About the same'))])}
   <div style="padding-top:10px;font-size:14px;line-height:1.55;color:#2E3B44">${L('戒指非医疗器械，数据仅供参考，不用于医疗目的。血压和心电由所列设备测量，本 App 仅汇总展示。本页不构成诊断，请与医生讨论。如胸痛、呼吸困难，请拨打 995。','The ring is not a medical device; its data is for reference only, not for medical use. BP and ECG were measured by the devices listed; this app only collects and displays them. This page is not a diagnosis; please discuss it with your doctor. If you have chest pain or trouble breathing, call 995.')}</div>
  </div></div>
  <div class="row2"><button class="btn" data-go="sumdoc">${ic('heart',18)} ${L('给医生看','Show doctor')}</button><button class="btn ghost" data-act="pdfx">${ic('upload',18)} ${L('导出 PDF','Export PDF')}</button></div>
 </div>`}};
P.sumdoc=()=>{const q=VQ();const row=(k,lines)=>`<div class="row1"><div class="k">${k}</div>${lines.map(x=>`<div>${x}</div>`).join('')}</div>`;
 return{calm:1,html:`${nav('For your doctor')}<div class="pad stack"><div class="sm" style="color:#2E3B44">${ic('sun',14)} Screen stays on · English for your doctor</div>
  <div class="card" style="background-color:#fff"><div class="docm">
   <div class="row1"><div class="k" style="font-size:22px">${NM()}</div><div>15 Sep – 14 Oct 2026 · data on 28 of 30 days</div></div>
   <div class="row1"><div class="k">Questions</div>${q.map(k=>{const o=VQ_OPTS.find(x=>x[0]===k);return `<button class="chk" role="checkbox" aria-checked="${!!(S.vqok||[]).includes(k)}" data-act="vqok" data-v="${k}" style="font-size:19px;padding:6px 0"><span class="bx">${(S.vqok||[]).includes(k)?ic('check',14,3):''}</span><span>${o?o[2]:k}</span></button>`}).join('')||'<div>None</div>'}</div>
   ${row('Blood pressure (mmHg) · upper-arm monitor',['Morning ×28: avg 131/82 ↓ (prev 135/84); ≥135/85 ×6; max 152/94 (2 Oct)','Evening ×22: avg 128/80 ＝ (prev 130/82)'])}
   ${row('Medicines (self-recorded)',['Amlodipine 5 mg OD; missed 22 Sep, 1 Oct, 9 Oct'])}
   ${row('Symptoms',['None recorded'])}
   ${row('ECG · MD100C device analysis',['20 Sep sinus · 2 Oct poor signal → retaken, sinus · 9 Oct sinus'])}
   ${row('Overnight SpO₂ · ring estimate (26/30)',['Nightly avg 94–96%; lowest 88% (night of 3 Oct)'])}
   ${row('Overnight resting HR · ring (26/30)',['Median 62 bpm (58–66) ＝'])}
   ${row('Sleep / steps · ring',['6 h 46 min ＝ · 5,420/day ＝'])}
   <div style="font-size:14px;color:#2E3B44;padding-top:8px">Ring is not a medical device. Personal record, not a medical report.</div>
  </div></div></div>`}};"""
s=s[:a]+SUM+s[b:]
R("    mpedit(){","""    vqadd(){const q=VQ();if(q.length<3&&!q.includes(v))q.push(v);render()},
    vqdel(){S.vq=VQ().filter(x=>x!==v);render()},
    vqvoice(){toast(L('请说出你想问的问题（华语、英语或方言，子女可帮忙改）（原型）','Say your question (English, Mandarin or dialect; family can tidy it up) (prototype)'))},
    vqok(){const o=S.vqok||(S.vqok=[]);S.vqok=o.includes(v)?o.filter(x=>x!==v):o.concat(v);render()},
    pdfx(){sheet(`<div class="stack" style="gap:10px"><h2 class="h2" style="font-size:20px">${L('导出复诊一页纸','Export visit summary')}</h2><p class="p">${L('文件含健康数据，请只分享给信任的人。','This file contains your health data. Share it only with people you trust.')}</p><div class="kv"><div><span>${L('格式','Format')}</span><span>${L('A4 一页，英文，黑白可打印','A4, one page, English, prints in black and white')}</span></div><div><span>${L('附页','Attachment')}</span><span>${L('3 条心电原始波形','3 original ECG tracings')}</span></div><div><span>${L('个人信息','Personal details')}</span><span>${L('只有姓名','Name only')}</span></div></div><p class="sm mu" style="margin:0">${L('页脚：用户自行生成于 2026-10-14 10:32 · 个人记录，非医疗报告；带水印。底部留空白，方便记下医生的话。','Footer: generated by you on 14 Oct 2026, 10:32 am SGT · personal record, not a medical report; watermarked. Space at the bottom to note what the doctor says.')}</p><button class="btn" data-act="pdfgo">${L('导出','Export')}</button></div>`);const kb=document.querySelector('.sheet [data-act="sheetclose"]');if(kb)kb.textContent=L('取消','Cancel')},
    pdfgo(){const s2=document.querySelector('.sheet-bg');if(s2)s2.remove();toast(L('已生成 PDF（原型）','PDF created (prototype)'))},
    mpedit(){""")
R("['mpsetup',L('计划设置','Plan setup')],","['mpsetup',L('计划设置','Plan setup')],['summary',L('复诊一页纸','Visit summary')],['sumdoc',L('给医生看','Show doctor')],")
R("<b>v2.9 复诊一页纸</b>：","<b>v3.0 复诊一页纸（专家会审后）</b>：页头改“带去给医生看的记录”；日期写全并注明有数据 28/30 天；顺序为我想问 → 血压 → 用药 → 症状 → 心电 → 血氧 → 心率 → 睡眠步数；血压写早晚次数、平均、≥135/85 次数和最高值，和前 30 天比加箭头（变化小于阈值写“＝ 差不多”）；用药写药名剂量和漏服日期；心电写设备自动分析结果（力争拿证，待最终合规审核）；血氧不用 90% 切点、不做对比，只写平均和最低读数；每项标设备来源，戒指标“非医疗器械”；底部免责声明和 995；我想问可点选常见问题或说一句，最多 3 条；“给医生看”全英文大字、可逐条打勾；导出 PDF 先确认，A4 一页、只含姓名、带水印和生成时间；正文 17px，不用灰字。<br><b>v2.9 复诊一页纸</b>：")
R("'<b>v2.9 Visit summary</b>:","'<b>v3.0 Visit summary (after expert review)</b>: header now “A record to take to your doctor”; full dates and data on 28 of 30 days; order: my questions → BP → medicines → symptoms → ECG → oxygen → heart rate → sleep and steps; BP shows morning and evening counts, averages, readings at or above 135/85 and the highest, with arrows against the previous 30 days (“＝ about the same” under thresholds); medicines show name, dose and missed dates; ECG shows the device’s own analysis (pending registration and final compliance review); oxygen has no 90% cut-off or comparison, only average and lowest reading; every row names its source and the ring is marked “not a medical device”; disclaimer and 995 at the bottom; questions from quick picks or voice, up to 3; Show doctor is large-type English with tick boxes; Export PDF asks first: A4 one page, name only, watermark and timestamp; body text 17px, no grey.<br><b>v2.9 Visit summary</b>:")
open(p,'w',encoding='utf-8').write(s); print('ok')
