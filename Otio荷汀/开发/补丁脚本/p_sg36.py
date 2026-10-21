import sys,re
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
mp=open('newmp.js',encoding='utf-8').read(); pl=open('newplan.js',encoding='utf-8').read()
i=s.index('const MP=()=>');j=s.index('P.breath=(k)=>');s=s[:i]+mp+s[j:]
i=s.index('P.myplan=()=>');j=s.index('P.linkc=()=>');s=s[:i]+pl+s[j:]
i=s.index("""<div class="card"><div class="between"><span class="h3">${L('我自己的习惯','My own habits')}</span><button class="link" data-go="mpsetup:own">""")
j=s.index("""</p></div>""",i)+len("</p></div>")
s=s[:i]+"""<div class="card"><div class="between"><span class="h3">${L('我自己的习惯','My own habits')}</span><button class="link" data-act="mpchg">${L('改一改','Change')}</button></div>${focusCard(true)}<p class="sm mu" style="margin:8px 0 0">${L('医生安排了运动时，以医生的为准。','If your doctor sets exercise, follow that instead.')}</p></div>"""+s[j:]
R("""${li('run',L('运动记录','Exercise log'),L('本周 2 次','2 this week'),null,null,{act:'mplog'})}""","")
R("    mpdone(){","    mptog(){const m=MP();m.done=m.done.includes(v)?m.done.filter(x=>x!==v):m.done.concat(v);m.skip=m.skip.filter(x=>x!==v);render()},\n    mpauto(){toast(L('这一项戒指会自动记下','The ring records this one for you'))},\n    mpchg(){MP().step=2;go(linked()?'mpsetup:own':'mpsetup')},\n    mpdone(){")
R("mpstep(){const m=MP();m.step=Math.max(1,Math.min(linked()?4:5,m.step+(+v)));render()},","mpstep(){const m=MP();m.step=Math.max(1,Math.min(3,m.step+(+v)));render()},")
R("mpfin(){const m=MP();m.setup=true;m.step=1;m.later={};","mpfin(){const m=MP();m.setup=true;m.step=1;")
R("mpfocus(){const m=MP();if(m.focus!==v){m.focus=v;m.fday=1;m.lvl=null}render()},","mpfocus(){const m=MP();if(m.focus!==v){if(m.fday>=14&&!m.grad.includes(m.focus))m.grad.push(m.focus);m.grad=m.grad.filter(x=>x!==v);m.focus=v;m.fday=1;m.lvl=null}render()},")
R("mpnext(){MP().step=3;","mpnext(){MP().step=2;")
i=s.index("    mplvl(){");j=s.index("\n",i)
s=s[:i]+"""    mplvl(){const m=MP();m.lvl=v;if(v==='up'){m.min=String(Math.min(60,+m.min+5));toast(L('从明天起，每次走 '+m.min+' 分钟','From tomorrow: '+m.min+' minutes each time'))}else toast(L('好，先保持。两周后再问你','OK, keeping it. We’ll ask again in two weeks'));render()},"""+s[j:]
for dead in ["    mplater(){","    mppast(){","    mpfix(){","    mppart(){","    mpstp(){","    mplog(){"]:
    i=s.index(dead);j=s.index("\n",i);s=s[:i]+s[j+1:]
R("L('圆环满一圈、点一下“完成”，就是记录。','A full ring or one tap on Done is your record.')","L('快走和起床戒指自动记下，满一圈就是做到了。','The ring records walks and wake-ups; a full ring means done.')")
R("L('先定大多数日子做得到的量。不想动的日子，走 5 分钟也算。','Pick an amount you can do on most days. On off days, 5 minutes counts.')","L('先定大多数日子做得到的量。不想动的日子，做一点也算。','Pick an amount you can do on most days. On off days, a little still counts.')")
R("你说了算。','Changing","你说了算。做稳的习惯会继续提醒。','Changing")
R("Your call.')","Your call. Habits you’ve built keep their reminders.')")
i=s.index('</style>'); s=s[:i]+".task.miss .tm{color:var(--tLow)}.task .t>span .tag{margin-left:4px;vertical-align:1px}\n"+s[i:]
R("L('<b>v3.5</b>：","L('<b>v3.6</b>：按场景重审“我的习惯”，做减法。设置从 5 步减到 3 步（作息 → 先养成哪一个 → 提醒），快走的时间和分钟数只在选中快走时展开；去掉日历、朗读语言、在哪走和步数目标两处设置。时间线只留起床、量血压、吃药、正在养成的习惯、看诊提醒和上床，每行一个勾，去掉三连按钮和“晚 1 小时”；午休、呼吸不再排进时间线。快走和起床由戒指自动记下；下雨不挪时间，就地改在组屋走廊走。周环只看正在养成的这一个（满圈做到、半圈做了一点）；做稳后问你“多走 5 分钟”或“开始下一个”，养成的习惯继续提醒。连上诊所后护理页只显示这一张卡；身体页去掉运动记录。<br><b>v3.5</b>：")
R("'<b>v3.5</b>: How long","'<b>v3.6</b>: My habits re-reviewed by scenario, with cuts. Setup goes from 5 steps to 3 (routine → which habit first → reminders); walk time and minutes only open when walking is chosen; calendar, voice, where-to-walk and steps-goal settings removed. The timeline keeps wake, BP, medicines, the habit being built, visit reminders and bed, one tick per row (no triple buttons, no 1 hour later); nap and breathing no longer scheduled. The ring records walks and wake-ups; rain keeps the time and moves the walk to the HDB corridor. The week rings track only the habit being built (full = done, half = a bit). When steady we offer 5 more minutes or the next habit; built habits keep reminding. Linked Care shows just this one card; Health drops the exercise log.<br><b>v3.5</b>: How long")
open(p,'w',encoding='utf-8').write(s); print('ok')
