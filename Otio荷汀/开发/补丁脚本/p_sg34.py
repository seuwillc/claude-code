import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
R("steps:'6000',min:'20',","steps:'6000',min:'20',focus:'walk',fday:12,")
# focus helpers
R("const AVG7=6480;","""const AVG7=6480;
const FOC=()=>{const m=MP(),mn=+m.min,am=m.when==='morning';return {
 walk:{t:L((am?'早饭后':'晚饭后')+(m.where==='indoor'?'做室内健身操 ':'快走 ')+mn+' 分钟',(m.where==='indoor'?'Indoor exercise class':'Brisk walk')+' for '+mn+' min after '+(am?'breakfast':'dinner')),s:L('不想动的日子，走 5 分钟也算','On off days, 5 minutes counts'),k:L('快走（到今天）','Walks so far'),v:L('2 / 3 天','2 / 3 days')},
 wake:{t:L('每天 '+m.wake+' 起床，周末也一样','Up at '+m.wake+' every day, weekends too'),s:L('前后半小时内都算。起来先拉开窗帘','Within half an hour counts. Open the curtains first thing'),k:L('按时起床（到今天）','Up on time so far'),v:L('3 / 3 天','3 / 3 days')},
 phone:{t:L(mpS(mpT(m.bed)-.75)+' 放下手机，调暗灯光',' Phone down and lights low at '+mpS(mpT(m.bed)-.75)),s:L('手机放到卧室外面充电','Charge your phone outside the bedroom'),k:L('睡前放下手机（到昨晚）','Phone down before bed so far'),v:L('2 / 2 晚','2 / 2 nights')}}};""")
R("const lvlUp=()=>{const m=MP();if(m.lvl||+m.steps>=12000)return '';",
"""const focusHd=()=>{const m=MP(),f=FOC()[m.focus];return `<div style="padding:10px 12px;border-radius:12px;background:var(--sf2);margin-top:8px"><div class="between"><span class="sm mu">${L('正在养成','Building now')}</span><span class="sm mu">${L('第 '+m.fday+' 天','Day '+m.fday)}</span></div><div class="h3" style="margin-top:2px">${f.t}</div><div class="sm mu">${f.s}</div></div>`};
const lvlUp=()=>{const m=MP();if(m.lvl)return '';if(m.focus!=='walk'){const nm={wake:L('按时起床','Getting up on time'),phone:L('睡前放下手机','Phone down before bed')}[m.focus];return `<div style="padding:12px 0 2px;border-top:1px solid var(--line);margin-top:10px"><div class="h3">${L(nm+'已经稳了',nm+' is steady')}</div><p class="p" style="margin-top:4px">${L('过去两周，每周都做到 5 天以上。要不要开始养成下一个？这个会继续提醒你。','In each of the last two weeks you did it on 5 or more days. Start the next one? This one keeps its reminder.')}</p><div class="row2" style="margin-top:10px"><button class="btn" data-act="mpnext">${L('选下一个','Choose next')}</button><button class="btn ghost" data-act="mplvl" data-v="keep">${L('先保持','Keep going')}</button></div></div>`}if(+m.steps>=12000)return '';""")
# setup: steps
R("N=own?3:4,st=Math.min(m.step,N);","N=own?4:5,st=Math.min(m.step,N),K=(own?['time','move','focus','remind']:['time','move','focus','remind','cal'])[st-1];")
R("const body=st===1?","const body=K==='time'?")
R(":st===2?",":K==='move'?")
R(":st===3?",""":K==='focus'?`<h1 class="h1" style="font-size:26px">${L('先养成哪一个？','Which one first?')}</h1><p class="p mu">${L('一次只养成一个。其他的照常提醒，但不算进度。','One at a time. The others still remind you, but don’t count toward progress.')}</p>${['walk','wake','phone'].map(k=>{const f=FOC()[k];return `<button class="fopt ${m.focus===k?'on':''}" data-act="mpfocus" data-v="${k}"><span class="rd"></span><span><b>${f.t}</b><small>${f.s}</small></span></button>`}).join('')}<p class="sm mu">${L('做稳了（两周里每周 5 天以上），我们再问你要不要开始下一个。','Once it’s steady (5+ days a week for two weeks), we’ll ask if you want to start the next.')}</p>`:K==='remind'?""")
R("mpstep(){const m=MP();m.step=Math.max(1,Math.min(linked()?3:4,m.step+(+v)));render()},","mpstep(){const m=MP();m.step=Math.max(1,Math.min(linked()?4:5,m.step+(+v)));render()},")
R("L('用 4 步排好你的每一天','Set up your day in 4 steps')","L('用 5 步排好你的每一天','Set up your day in 5 steps')")
# actions
R("    mpstp(){","""    mpfocus(){const m=MP();if(m.focus!==v){m.focus=v;m.fday=1;m.lvl=null}render()},
    mpnext(){MP().step=3;go(linked()?'mpsetup:own':'mpsetup')},
    mpstp(){""")
# tag in row
R("const tg=med?`<span class=\"tag mu\">${L('每天','Daily')}</span>`:'';","const tg=med?`<span class=\"tag mu\">${L('每天','Daily')}</span>`:m.focus===x.id?`<span class=\"tag\">${L('正在养成','Building')}</span>`:'';")
# solo week card: focus header + kv
R("""<div><span>${L('快走（到今天）','Walks so far')}</span><span class="num">2 / 3 ${L('天','days')}</span></div><div><span>${L(m.bed+' 前上床','In bed by '+m.bed)}</span><span class="num">5 / 7 ${L('晚','nights')}</span></div>""",
"""<div><span>${FOC()[m.focus].k}</span><span class="num">${FOC()[m.focus].v}</span></div>""")
R("""<div class="card"><div class="between"><span class="h3">${L('这一周','This week')}</span><button class="link" data-act="mplog">${L('记运动','Log exercise')}</button></div>""",
"""<div class="card"><div class="between"><span class="h3">${L('这一周','This week')}</span><button class="link" data-act="mplog">${L('记运动','Log exercise')}</button></div>${focusHd()}""")
# linked card
R("""<div style="margin-top:4px">${mpItems().filter(x=>['walk','phone','bed'].includes(x.id)).map(x=>mpRow(x,S.hour)).join('')}</div>${lvlUp()}""",
"""${focusHd()}<div style="margin-top:4px">${mpItems().filter(x=>['walk','phone','bed',MP().focus].includes(x.id)).map(x=>mpRow(x,S.hour)).join('')}</div>${lvlUp()}""")
# sheet point 5
R("L('5 稳了再加','5 Add more once it’s steady')","L('5 一次一个，稳了再加','5 One at a time, add once it’s steady')")
R("L('连续两周每周做到 5 天，我们会问你要不要加一点；你说了算。','After two weeks of 5+ days, we’ll ask if you want a bit more. Your call.')",
  "L('同时改好几件事最容易半途而废。连续两周每周做到 5 天，我们再问你要不要加一点或开始下一个；你说了算。','Changing several things at once is how most people stall. After two weeks of 5+ days, we’ll ask about a bit more or the next habit. Your call.')")
# css
i=s.index('</style>'); s=s[:i]+""".fopt{display:flex;gap:12px;align-items:flex-start;width:100%;text-align:left;padding:14px 16px;border-radius:16px;border:2px solid var(--line);background:var(--sf);color:var(--tx);font:inherit;cursor:pointer}
.fopt b{display:block;font-size:17px;font-weight:600}.fopt small{display:block;font-size:13px;color:var(--mu);margin-top:3px}
.fopt .rd{flex:none;width:22px;height:22px;border-radius:50%;border:2px solid var(--line);margin-top:1px}.fopt.on{border-color:var(--vit)}.fopt.on .rd{border:7px solid var(--vit)}
"""+s[i:]
# changelog
R("L('<b>v3.3</b>：","L('<b>v3.4</b>：一次只养成一个习惯。设置里多了一步“先养成哪一个？”（快走 / 每天同一时间起床 / 睡前放下手机），其他照常提醒但不算进度；计划页和护理页显示“正在养成 · 第几天”，时间线上标“正在养成”；做稳两周后问你加一点或开始下一个。设置变为 5 步（连上诊所后 4 步）。<br><b>v3.3</b>：")
R("'<b>v3.3</b>: My own","'<b>v3.4</b>: One habit at a time. Setup gains a step, Which one first? (walk / same wake-up time daily / phone down before bed); the others keep reminding but don’t count toward progress. Plan and Care show Building now · Day N, and the timeline tags it. After two steady weeks we ask about a bit more or the next habit. Setup is now 5 steps (4 when linked).<br><b>v3.3</b>: My own")
open(p,'w',encoding='utf-8').write(s); print('ok')
