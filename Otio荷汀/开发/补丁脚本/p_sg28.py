import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
def cut(a,b):
    i=s.index(a); j=s.index(b,i); return i,j
# voice follows UI language unless set
R("fam:false,voice:'en',","fam:false,voice:null,")
R("const mpT=t=>","const VOICE=()=>MP().voice||(S.lang==='zh'?'zh':'en');\nconst mpT=t=>")
R("${ch('voice','en','English')}${ch('voice','zh','华语')}","${['en','zh'].map(v=>`<button class=\"mpchip ${VOICE()===v?'on':''}\" data-act=\"mpset\" data-v=\"voice=${v}\">${v==='en'?'English':'华语'}</button>`).join('')}")
R("mpread(){toast(MP().voice==='zh'?","mpread(){toast(VOICE()==='zh'?")
# meds move into setup step 3
R("""<div class="h3">${L('“读给我听”用什么语言','Read-aloud voice')}</div>""","""<div class="between"><span class="h3">${L('吃药提醒','Medicine reminders')}</span><button class="link" data-act="mpmed">${ic('plus',14,2.2)} ${L('添加','Add')}</button></div>${m.meds.length?`<div class="kv">${m.meds.map(x=>`<div><span>${x.n}</span><span class="num">${x.t}</span></div>`).join('')}</div>`:''}<p class="sm mu" style="margin:0">${L('只是提醒，不给用药建议。','Reminders only, no dosing advice.')}</p><div class="h3">${L('“读给我听”用什么语言','Read-aloud voice')}</div>""")
# walk remedy when missed
R("""out.push({id:'walk',t:wt,k:'sug',a:wa,b:wb,adj});""","""if(m.fix){out.push({id:'walk',t:'18:30',k:'sug',a:L('社区中心健身操 30 分钟','Exercise class at the community centre, 30 minutes'),b:L('早上错过了，改成室内','Missed this morning, moved indoors'),adj:''})}else out.push({id:'walk',t:wt,k:'sug',a:wa,b:wb,adj});""")
# row: med wording, daily tag, remedy
a,b=cut("function mpRow(x,now){","\nfunction mpTL(){")
s=s[:a]+r"""function mpRow(x,now){const m=MP(),past=mpT(x.t)<=now,done=m.done.includes(x.id)||(past&&x.k==='base'),skip=m.skip.includes(x.id),miss=past&&!done&&!skip&&x.k!=='base',med=x.k==='med';
 const acts=done||skip||x.k==='base'?'':`<div class="acts"><button data-act="mpdone" data-v="${x.id}">${med?L('做了','Done'):L('完成','Done')}</button>${past?'':`<button data-act="mplater" data-v="${x.id}">${med?L('晚一点','A bit later'):L('晚 1 小时','1 hour later')}</button>`}<button data-act="mpskip" data-v="${x.id}">${med?L('没做','Didn’t'):L('今天不做','Not today')}</button></div>`;
 const tg=med?`<span class="tag mu">${L('每天','Daily')}</span>`:'';
 const fix=miss&&x.id==='walk'&&!m.fix?`<div class="adj">${L('错过了。傍晚有雷雨，改成室内健身操？','Missed. Rain this evening: switch to an indoor class?')} <button class="link" data-act="mpfix" style="font-size:13px;min-height:0;padding:0 0 0 4px">${L('改到 18:30','Move to 6:30 pm')}</button></div>`:'';
 return `<div class="mpi ${done?'done':skip?'skip':miss?'miss':''}"><span class="tm num">${x.t}</span><div class="bd"><div class="tt">${x.go&&!done?`<button class="link" data-go="${x.go}" style="font-size:16px;padding:0;min-height:0;color:var(--tx);font-weight:600">${x.a} ${ic('chev',14)}</button>`:x.a}${tg}</div><div class="ss">${skip?(med?L('记下了：没做','Noted: not done'):L('今天不做了','Skipped today')):x.b}</div>${x.adj?`<div class="adj">↻ ${x.adj}</div>`:''}${fix}${miss&&x.id==='walk'&&!m.fix?'':acts}</div></div>`}"""+s[b:]
# tomorrow line at end of timeline
R("""if(!nowDone)h+=`<div class="pnow"><span>${L('现在 ','Now ')+clk()}</span></div>`;""","""if(!nowDone)h+=`<div class="pnow"><span>${L('现在 ','Now ')+clk()}</span></div>`;
 if(now>=20)h+=`<p class="sm mu" style="margin:8px 0 0">${L('明天第一件事：'+MP().wake+' 起床','First thing tomorrow: up at '+MP().wake)}</p>`;""")
# new lean plan page
a,b=cut("P.myplan=()=>{if(linked())return P.care();","\nP.linkc=()=>")
s=s[:a]+r"""P.myplan=()=>{if(linked())return P.care();
 const m=MP(),now=S.hour,L2=mpItems(),nx=L2.find(x=>mpT(x.t)>now&&!m.done.includes(x.id)&&!m.skip.includes(x.id)&&x.k!=='base'),nt=now>=20.5||now<4;
 const H=[['nap',L('午睡','Nap')],['kopi',L('下午 3 点后喝咖啡','Kopi after 3 pm')],['supper',L('宵夜','Late supper')],['late',L('熬夜','Up late')],['sit',L('久坐','Long sitting')],['drink',L('喝酒','Alcohol')]];
 const wk=[1,2,0,1,0,.5,0];
 const row=(icn,t,sub,attr)=>`<button class="li" ${attr}><span class="ic">${ic(icn)}</span><span class="t">${t}<small>${sub}</small></span><span class="chev">${ic('chev',16)}</span></button>`;
 return{tab:'myplan',html:`<div class="pad stack">
  <div style="padding-top:8px"><h1 class="h1" style="font-size:28px">${L('今天怎么过','How today goes')}</h1><div class="sm mu" style="margin-top:4px">${ic('rain',14)} 25–32° · ${L('午后雷雨','afternoon storms')} · PSI 42 · ${L('11–15 点最热','hottest 11–3')}</div></div>
  ${m.setup?'':`<button class="card tap" data-go="mpsetup" style="text-align:left"><div class="between"><span class="h3">${L('用 4 步排好你的每一天','Set up your day in 4 steps')}</span><span class="chev">${ic('chev',16)}</span></div></button>`}
  <div class="card" style="padding:20px"><div class="sm mu">${L('下一件事','Next up')}</div>${nx?`<div class="num" style="font-size:34px;margin-top:6px">${nx.t}</div><div class="h2" style="margin-top:2px">${nx.a}</div><p class="p mu" style="margin-top:4px">${nx.adj||nx.b}</p><div class="row2" style="margin-top:12px"><button class="btn" data-act="mpdone" data-v="${nx.id}">${L('做完了','Done')}</button><button class="btn ghost" data-act="mpread">${ic('sound',18)} ${L('读给我听','Read to me')}</button></div>`:`<div class="h2" style="margin-top:6px">${L('今天的事都做完了','All done for today')}</div><p class="p mu" style="margin-top:4px">${L('明天第一件事：'+m.wake+' 起床','First thing tomorrow: up at '+m.wake)}</p>`}</div>
  <div class="card"><div class="h3">${L('今天','Today')}</div><div class="ptl" style="margin-top:6px">${mpTL()}</div></div>
  <div class="card flush">
   ${row('wind',L('荷息 · '+(nt?'4-7-8 助眠':'1 分钟静心'),'Lotus breath · '+(nt?'4-7-8 for sleep':'1-minute calm')),L('跟着荷花呼吸','Breathe with the lotus'),`data-go="breath:${nt?'478':'1'}"`)}
   ${row('moon',L('睡得更好 · 第 '+m.course+' 课','Better sleep · Lesson '+m.course),L('听 3 分钟 · '+(VOICE()==='zh'?'华语':'English'),'Listen, 3 min · '+(VOICE()==='zh'?'华语':'English')),'data-act="mpcourse"')}
   ${row('leaf',L('今天的习惯','Today’s habits'),m.hab.length?L('已记 '+m.hab.length+' 项','Noted '+m.hab.length):L('午睡、咖啡、宵夜…点一下记下来','Nap, kopi, late supper… tap to note'),'data-act="mphabopen"')}
   ${m.habOpen?`<div style="padding:4px 0 14px"><div class="mpchips" style="margin-top:0">${H.map(([k,t])=>`<button class="mpchip ${m.hab.includes(k)?'on':''}" data-act="mphab" data-v="${k}">${t}</button>`).join('')}</div><p class="sm mu" style="margin:8px 0 0">${L('记几天以后，“身体”里会告诉你哪件事最影响睡眠。','After a few days, Health shows which affects your sleep most.')}</p></div>`:''}
  </div>
  <div class="card"><div class="between"><span class="h3">${L('这一周','This week')}</span><button class="link" data-act="mplog">${L('记运动','Log exercise')}</button></div>
   <div class="wk">${[L('一','M'),L('二','T'),L('三','W'),L('四','T'),L('五','F'),L('六','S'),L('日','S')].map((d,i)=>`<span><i class="${wk[i]===1?'on':wk[i]?'half':''}"></i>${d}</span>`).join('')}</div>
   <div class="kv" style="margin-top:8px"><div><span>${L('运动','Exercise')}</span><span class="num">2 / 3 ${L('次','times')}</span></div><div><span>${L(m.bed+' 前上床','In bed by '+m.bed)}</span><span class="num">5 / 7 ${L('晚','nights')}</span></div><div><span>${L('平均步数','Average steps')}</span><span class="num">5,420</span></div></div>
   <button class="link" data-go="mpsetup" style="margin-top:6px;font-weight:500;color:var(--mu);font-size:13px;text-align:left">${L('我的目标：睡 7–8 小时 · '+m.bed+' 上床 · 每天 6,000 步 · 血压 <135/85','My goals: sleep 7–8 h · bed '+m.bed+' · 6,000 steps · BP <135/85')} · <span style="color:var(--vit);font-weight:600">${L('改一改','Change')}</span></button></div>
  ${m.ctaOff?'':`<div class="card"><div class="between"><span class="h3">${L('想让护士一起看着吗？','Want a nurse to keep an eye on it too?')}</span><button class="link" data-act="mpctaoff" style="color:var(--mu);font-weight:500">${L('不用了','No thanks')}</button></div><button class="link" data-go="connect" style="text-align:left">${L('连上诊所 ›','Link a clinic ›')}</button></div>`}
 </div>`}};"""+s[b:]
# actions
R("    mpedit(){","""    mpfix(){MP().fix=true;toast(L('已改到 18:30 室内','Moved to 6:30 pm, indoors'));render()},
    mpctaoff(){MP().ctaOff=true;toast(L('好的，需要时在“我的 › 连上诊所”','OK. You can still link in Me › Link a clinic'));render()},
    mphabopen(){MP().habOpen=!MP().habOpen;render()},
    mpedit(){""")
R("mpcourse(){const m=MP();toast(L('播放第 '+m.course+' 课（原型）','Playing lesson '+m.course+' (prototype)'))","mpcourse(){const m=MP();toast((VOICE()==='zh'?'用华语':'In English')+' · '+L('播放第 '+m.course+' 课（原型）','lesson '+m.course+' (prototype)'))")
# changelog
R("<b>v2.7</b>：连上诊所后","<b>v2.8 计划页做减法</b>：12 张卡减到 6 块，约 2 屏——标题带一行天气；下一件事；今天的时间线；一张“随手可做”（荷息、睡眠课程、今天的习惯，习惯点开才展开）；“这一周”合并运动格子、按时上床、平均步数，目标收成底部一行；连诊所卡可点“不用了”关掉。删掉：页头重复的“读给我听”、Healthy 365（在“我的 › 设备与数据来源”）、吃药卡（添加挪到计划设置第 3 步）、“建议最多 5 条”。修正：朗读默认跟界面语言；吃药和量血压改成“做了 / 晚一点 / 没做”，标签“每天”；错过的户外运动给出“改到 18:30 室内”；晚上显示明天第一件事。<br><b>v2.7</b>：连上诊所后")
R("'<b>v2.7</b>: once linked,","'<b>v2.8 Plan page, trimmed</b>: 12 cards down to 6 blocks, about two screens: title with one weather line; Next up; Today’s timeline; one Any time card (Lotus breath, sleep course, today’s habits, which open only when tapped); This week merges the exercise grid, bedtimes and steps, with goals as one line at the bottom; the clinic card can be dismissed. Removed: the duplicate Read to me, Healthy 365 (now in Me › Devices & data sources), the medicines card (adding moves to setup step 3) and “Up to 5 suggestions”. Fixed: read-aloud follows the app language; medicines and BP use Done / A bit later / Didn’t, tagged Daily; a missed outdoor walk offers “Move to 6:30 pm, indoors”; evenings show tomorrow’s first step.<br><b>v2.7</b>: once linked,")
open(p,'w',encoding='utf-8').write(s); print('ok',len(s))
