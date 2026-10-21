import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
def DEL(key,tag='p'):
    global s
    assert s.count(key)==1,(key,s.count(key))
    k=s.index(key);i=s.rindex('<'+tag,0,k);j=s.index('</'+tag+'>',k)+len(tag)+3
    while s[j:j+1]=='\n' or s[i-1:i]==' ':
        if s[i-1:i]==' ': i-=1
        else: break
    s=s[:i]+s[j:]
for k in ['戒指看睡眠和心率，家人','通过 Myinfo 自动带入','诊所按实际提供的服务收固定费用','戒指和手环不估算血压','带去给医生看的记录。看诊时','周日和公众假期：荷汀集中护士','家人默认只看到总状态']:
    DEL(k)
# join: shorter
R("L('护理码在诊所或体检中心给你的单张上，也可以扫码。连上后，你的读数会交给护理团队看。','It’s on the slip from your clinic or screening centre, or scan the QR code. Once linked, your care team can see your readings.')","L('在诊所给你的单张上。','It’s on the slip from your clinic.')")
# vitality
R("L('元气看昨夜的静息心率、心跳的细微变化、体温和睡眠，和你自己的平常比。不是医疗指标。','Vitality looks at last night’s resting heart rate, small changes in your heartbeat, temperature and sleep, compared with your own usual. It isn’t a medical measure.')","L('和你自己的平常比，不是医疗指标。','Compared with your own usual. Not a medical measure.')")
R("L('戒指的血氧是参考数据，不是医疗器械读数，不能用来诊断睡眠呼吸暂停。','Ring oxygen readings are for context. They are not a medical device reading and can’t diagnose sleep apnoea.')","L('戒指估算，仅供参考，不能诊断。','Ring estimate, for reference only; not a diagnosis.')")
R("linked()?L('目标和告警线由医生在诊所端设定，更新后这里会同步。','Your doctor sets these in the clinic portal; changes show up here.'):L('连上诊所后，由医生设定你的目标。','Once you link a clinic, your doctor sets your targets.')","linked()?L('由医生设定。','Set by your doctor.'):L('参考值，不是医生定的目标。','A reference, not a target set by a doctor.')")
R("L('每一条心电由'+DRs()+'判读。设备自动分析（MD100C，注册证号待填）只作参考。','Every ECG is read by '+DRs()+'. The device analysis (MD100C, reg. no. TBC) is for reference only.'):L('设备自动分析（MD100C，注册证号待填）· 连诊所后另有医生判读。心电保存在你的手机上，可以导出 PDF 给医生看。','Device analysis (MD100C, reg. no. TBC) · read by a doctor once linked. ECGs stay on your phone; export a PDF for any doctor.')","L('每条心电由'+DRs()+'判读。','Every ECG is read by '+DRs()+'.'):L('设备自动分析，仅供参考（MD100C）。','Device analysis, for reference only (MD100C).')")
R("L('连上诊所后，护士每天看你的血压和心电，读数超出医生定的线会联系你；每条心电由医生判读。','Once linked, a nurse checks your BP and ECG every day and reaches out when a reading crosses the line your doctor set. Every ECG is read by a doctor.')","L('护士每天看你的血压和心电，医生判读每条心电。','A nurse checks your BP and ECG daily; a doctor reads every ECG.')")
R("L('血压计划 S$29/月，心律计划 S$39/月，血糖计划 S$149/月起。账单会列明诊所的临床服务费。不连诊所，戒指的功能照常免费用。','BP plan S$29/month, heart rhythm S$39/month, glucose from S$149/month. Your bill itemises the clinic’s service fee. Without a clinic, your ring features stay free.')","L('血压 S$29/月 · 心律 S$39/月 · 血糖 S$149/月起。不连诊所，戒指照常免费。','BP S$29/month · heart rhythm S$39 · glucose from S$149. Without a clinic, the ring stays free.')")
R("L('拖动滑轨，或按 ±5 分钟微调。固定起床时间，比早睡更重要。','Drag the slider, or fine-tune with ±5 min. A steady wake-up time matters more than an early bedtime.')","L('固定起床时间，比早睡更重要。','A steady wake-up time matters more than an early bedtime.')")
R("L('这周做到 '+cnt+' 天。满圈：做到了；半圈：做了一点，也算。','Done on '+cnt+' days this week. Full ring: done; half ring: a bit, which still counts.')","L('这周做到 '+cnt+' 天 · 半圈也算','Done on '+cnt+' days this week · half rings count')")
R("L('过去两周，每周都做到 5 天以上。下一步你来定：','Five or more days in each of the last two weeks. Your call what’s next:')","L('两周都做到 5 天以上。','5+ days in each of the last two weeks.')")
R("L('戒指估算，不是诊断。可以带上复诊一页纸问问医生','A ring estimate, not a diagnosis. Worth asking your doctor; bring your visit summary')","L('戒指估算 · 带上复诊一页纸问医生','Ring estimate · ask your doctor, bring your visit summary')")
R("L('连上诊所后，复诊资料由 '+CL()+' 的护理团队负责：医生在病历里能看到你的全部读数，每月签发监测报告。需要看其他医生时，请诊所出具转诊信。'","L('复诊资料由 '+CL()+' 负责。看其他医生，请诊所出转诊信。'")
i=s.index("'While you’re linked, '+CL()+'’s care team looks after your visit records");j=s.index("')",i)
s=s[:i]+"CL()+' handles your visit records. For another doctor, ask the clinic for a referral letter."+s[j:]
# devices: drop registered-device paragraph (both branches) and dev note
k=s.index("有注册证的设备（血压计、心电卡、连续血糖仪）读数会进入你的病历");i=s.rindex('<p',0,k);j=s.index('</p>',k)+4;s=s[:i]+s[j:]
R("L('每天步数攒积分 · 接口待与保健促进局确认','Daily steps for points · integration to be confirmed with HPB')","L('每天步数攒积分','Daily steps for points')")
R("L('跟着你的作息；起床、上床提醒不受影响','Follows your routine; wake-up and bedtime reminders still come through')+(linked()?L('，护理团队的紧急联系也不受影响','; urgent care team contact too'):'')","L('起床、上床提醒照常','Wake-up and bedtime reminders still come')")
R("<div class=\"banner alr\" style=\"margin-top:8px\">${ic('sos',16)}<span>${L('消息不是急救渠道。紧急情况请拨 995。','Messages aren’t for emergencies. Call 995.')}</span></div>","<div class=\"banner alr\" style=\"margin-top:8px\">${ic('sos',16)}<span>${L('紧急情况请拨 995','Emergencies: call 995')}</span></div>")
# family: drop "what family hear" card, simplify toggles label + sub
k=s.index("有事时，家人会收到什么");i=s.rindex('<div class="card">',0,k);j=s.index('</p></div>',k)+10;s=s[:i]+s[j:]
R("L('想让她多看一项，可以单独打开（只看在不在平常范围）：','To let her see more, switch items on one by one (in-range status only):')","L('还可以给她看','She can also see')")
R("L('看到总状态 · 到 2027.4.13','Sees overall status · until 13 Apr 2027')","L('看到：好不好','Sees: OK or not')")
R("L('<b>v3.9</b>：","L('<b>v3.10</b>：说明文字做减法。删掉解释系统如何运作、用户读不读都不影响操作的段落（家人页三段、登录 Myinfo 说明、提成说明、血压计说明、复诊一页纸开头等），其余压到一句；只保留法律和安全必需的（PDPA 同意、995、不能诊断）。<br><b>v3.9</b>：")
R("'<b>v3.9</b>: All 40","'<b>v3.10</b>: Fewer words. Paragraphs explaining how the system works, which don’t change what you do, are gone (three on Family, the Myinfo note, the commission note, the BP monitor note, the visit summary intro and more); the rest are cut to one line. Only what law and safety need stays (PDPA consent, 995, not a diagnosis).<br><b>v3.9</b>: All 40")
open(p,'w',encoding='utf-8').write(s); print('ok')
