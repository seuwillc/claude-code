import sys,re
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
# remove course rows + action
R("${li('moon',L('睡得更好 · 第 '+MP().course+' 课','Better sleep · Lesson '+MP().course),L('共 8 课 · 每课 3 分钟','8 lessons · 3 minutes each'),null,null,{act:'mpcourse'})}","")
R("""   ${row('moon',L('睡得更好 · 第 '+m.course+' 课','Better sleep · Lesson '+m.course),L('听 3 分钟 · '+(VOICE()==='zh'?'华语':'English'),'Listen, 3 min · '+(VOICE()==='zh'?'华语':'English')),'data-act="mpcourse"')}
""","""   ${row('moon',L('10 月 3 日夜里血氧最低 88%','Overnight oxygen fell to 88% on 3 Oct'),L('戒指估算，不是诊断。可以带上复诊一页纸问问医生','A ring estimate, not a diagnosis. Worth asking your doctor; bring your visit summary'),'data-go="summary"')}
""")
i=s.index("    mpcourse(){");j=s.index("\n",i);s=s[:i]+s[j+1:]
R(",h365:false,course:3});",",h365:false});")
# why lines
for k,zh,en in [('walk','规律走动，白天更有精神，晚上也更容易困','Moving regularly helps you feel more awake by day and sleepier at night'),
 ('wake','起床时间固定，晚上到点自然会困','A fixed wake-up time makes you naturally sleepy at the same time each night'),
 ('phone','屏幕的光和内容会让人更清醒，放下手机更容易睡着','Screen light and content keep you alert; putting the phone away makes sleep easier'),
 ('water','一夜没喝水，起床先补一杯','After a night without water, start with a glass'),
 ('stretch','坐久了活动一下关节，下午更轻松','Moving your joints after sitting makes the afternoon easier'),
 ('veg','先吃菜，饭量自然少一点，也饱得更久','Vegetables first: you tend to eat less rice and stay full longer'),
 ('call','常和人说说话，心情会好一些','Talking with people often lifts your mood')]:
    i=s.index(" "+k+":{t:",s.index("const FOC=()=>"));j=s.index("wk:[",i)
    s=s[:j]+"w:L('"+zh+"','"+en+"'),"+s[j:]
# focus card: why line
R("""<div class="sm mu" style="margin-top:2px">${L('第 '+m.fday+' 天','Day '+m.fday)} · ${f.s}</div></div>""","""<div class="sm mu" style="margin-top:2px">${L('第 '+m.fday+' 天','Day '+m.fday)} · ${f.s}</div>${f.w?`<div class="sm" style="margin-top:4px;color:var(--vit)">${L('为什么：','Why: ')}${f.w}</div>`:''}</div>""")
# setup option: why for selected + data-based hint on wake
R("""return `<button class="fopt ${on?'on':''}" data-act="mpfocus" data-v="${k}"><span class="rd"></span><span><b>${f.t}</b><small>${f.s}</small></span></button>`};""",
"""return `<button class="fopt ${on?'on':''}" data-act="mpfocus" data-v="${k}"><span class="rd"></span><span><b>${f.t}</b><small>${f.s}</small>${on&&f.w?`<small style="color:var(--vit)">${L('为什么：','Why: ')}${f.w}</small>`:''}${k==='wake'&&!on?`<small style="color:var(--act)">${L('戒指看到：最近两周你的起床时间前后差了 1 个半小时','Your ring saw wake-up times vary by an hour and a half over two weeks')}</small>`:''}</span></button>`};""")
R("L('<b>v3.7</b>：","L('<b>v3.8</b>：去掉“睡得更好”课程（真正有效的失眠疗法需要医生参与，单讲睡眠卫生效果弱）。改为：每个习惯带一句“为什么”；戒指发现起床时间不固定时，在“按时起床”上提示；自己用时，夜里血氧偏低提示带复诊一页纸问医生（不做诊断、不按阈值计数）。<br><b>v3.7</b>：")
R("'<b>v3.7</b>: Any habit","'<b>v3.8</b>: Better-sleep course removed (insomnia treatment that works needs a clinician; sleep-hygiene talks alone do little). Instead: each habit carries a one-line why; when the ring sees irregular wake-up times it says so on Up on time; on your own, a low overnight oxygen reading suggests asking your doctor with your visit summary (no diagnosis, no threshold counts).<br><b>v3.7</b>: Any habit")
open(p,'w',encoding='utf-8').write(s); print('ok')
