import sys,re
S=sys.argv[1]; p=S+'/sgtob/vera-care-sg.html'
s=open(p,encoding='utf-8').read()
cn=open(S+'/proto/vera-prototype.html',encoding='utf-8').read()
i=cn.index('荷息 · 跟着荷花呼吸'); j=cn.rfind('<img src="',0,i)+len('<img src="'); k=cn.index('"',j)
LOTUS=cn[j:k]; assert LOTUS.startswith('data:image/jpeg;base64,')
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a)); s=s.replace(a,b)
CSS="""
.pnow{display:flex;align-items:center;gap:8px;margin:6px 0;color:var(--alr);font-size:13px;font-weight:600}.pnow::before,.pnow::after{content:"";flex:1;height:1px;background:currentColor;opacity:.45}
.pfold{display:flex;justify-content:space-between;align-items:center;width:100%;background:var(--sf2);border:0;border-radius:12px;padding:10px 12px;margin:4px 0 6px;color:var(--mu);font:inherit;font-size:14px;cursor:pointer}
.mpi{display:flex;gap:12px;padding:11px 0;border-bottom:1px solid var(--line)}.mpi:last-child{border-bottom:0}
.mpi .tm{width:50px;flex:none;font-size:15px;color:var(--mu);padding-top:1px}.mpi .bd{flex:1;min-width:0}
.mpi .tt{font-size:16px;font-weight:600;line-height:1.35}.mpi .ss{font-size:13px;color:var(--mu);margin-top:2px;line-height:1.45}
.mpi.done .tt{opacity:.5;text-decoration:line-through}.mpi.skip .tt{opacity:.4}.mpi.miss .tm{color:var(--tLow)}
.mpi .adj{font-size:13px;color:var(--act);margin-top:3px;line-height:1.45}
.mpi .acts{display:flex;gap:16px;margin-top:4px}.mpi .acts button{background:none;border:0;color:var(--vit);font:inherit;font-size:14px;font-weight:600;padding:4px 0;cursor:pointer;min-height:34px}
.mpi .tag{margin-left:6px;vertical-align:2px}
.mpchips{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}.mpchip{border:1px solid var(--line);background:var(--sf2);color:var(--tx);border-radius:999px;padding:8px 13px;font:inherit;font-size:14px;cursor:pointer;min-height:38px}.mpchip.on{background:var(--vit);color:var(--bg);border-color:var(--vit)}
.lotus2{display:flex;gap:14px;align-items:stretch}.lotus2 img{width:96px;border-radius:16px;object-fit:cover;flex:none}
.wk{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin-top:10px}.wk span{display:flex;flex-direction:column;align-items:center;gap:4px;font-size:12px;color:var(--mu)}.wk i{display:block;width:100%;height:30px;border-radius:8px;background:var(--sf2)}.wk i.on{background:var(--vit)}.wk i.half{background:color-mix(in srgb,var(--vit) 35%,transparent)}
.prog2{height:6px;border-radius:3px;background:var(--line);overflow:hidden;margin-top:8px}.prog2 i{display:block;height:100%;background:var(--slp)}
.brw{display:flex;flex-direction:column;align-items:center;gap:16px;padding-top:24px;text-align:center}
.brorb{width:230px;height:230px;border-radius:50%;background:radial-gradient(circle,color-mix(in srgb,var(--vit) 34%,transparent),color-mix(in srgb,var(--vit) 6%,transparent) 70%);display:grid;place-items:center;transform:scale(.62)}
.brorb img{width:130px;height:130px;border-radius:50%;object-fit:cover;opacity:.92}
.mpstep{display:flex;gap:6px}.mpstep i{flex:1;height:4px;border-radius:2px;background:var(--line)}.mpstep i.on{background:var(--vit)}
"""
i=s.index('</style>'); s=s[:i]+CSS+s[i:]
JS=r"""
const LOTUSIMG='__LOTUS__';
const MP=()=>S.mp||(S.mp={setup:false,step:1,wake:'06:30',bed:'22:30',where:'outdoor',when:'evening',fam:false,voice:'en',cal:false,done:[],skip:[],later:{},past:false,hab:[],meds:[],h365:false,course:3});
const mpT=t=>{const [h,m]=t.split(':').map(Number);return h+m/60},mpS=h=>{h=(h+24)%24;const H=Math.floor(h),M=Math.round((h-H)*60);return String(H+(M===60?1:0)).padStart(2,'0')+':'+String(M%60).padStart(2,'0')};
function mpItems(){const m=MP(),low=S.scen==='night',out=[];
 out.push({id:'wake',t:m.wake,k:'base',a:L('起床，先喝一杯水','Up, and a glass of water'),b:m.fam?L('家人也会收到提醒','Your family gets a nudge too'):L('按你设的时间','At the time you set')});
 out.push({id:'bpam',t:mpS(mpT(m.wake)+.33),k:'med',a:L('早上量血压','Morning BP'),b:L('坐下休息 5 分钟再量 · 自己记录','Sit for 5 minutes first · for your own record')});
 m.meds.forEach((x,i)=>out.push({id:'med'+i,t:x.t,k:'med',a:x.n,b:L('只是提醒，不给用药建议','Reminder only, no dosing advice')}));
 let wt=m.when==='morning'?'07:00':'17:30',adj='';
 if(m.where==='outdoor'&&mpT(wt)>=16){wt='07:00';adj=L('下午 4 点后可能有雷雨，挪到早上','Thunderstorms likely after 4 pm, moved to the morning')}
 const wa=low?L('慢走 20 分钟','Slow walk, 20 minutes'):m.where==='indoor'?L('社区中心健身操 30 分钟','Exercise class at the community centre, 30 minutes'):L('公园连道快走 30 分钟','Brisk walk on the park connector, 30 minutes');
 const wb=low?L('昨晚血氧有一段偏低，今天轻松一点','Your oxygen dipped last night, so take it easy today'):L('心率 100–125 次/分，能说话不能唱歌','Heart rate 100–125, enough to talk but not sing');
 out.push({id:'walk',t:wt,k:'sug',a:wa,b:wb,adj});
 out.push({id:'nap',t:'13:30',k:'sug',a:L('午休，不超过 30 分钟','Afternoon rest, under 30 minutes'),b:L('躲开中午最热的时候','Out of the midday heat')});
 out.push({id:'breath',t:'15:00',k:'sug',a:L('1 分钟呼吸','1-minute breathing'),b:L('点开跟着荷花呼吸','Tap to breathe with the lotus'),go:'breath:1'});
 out.push({id:'phone',t:mpS(mpT(m.bed)-.75),k:'sug',a:L('放下手机，调暗灯光','Phone down, lights low'),b:L('上床前 45 分钟','45 minutes before bed')});
 out.push({id:'bed',t:m.bed,k:'base',a:L('上床','In bed'),b:L('你的目标 '+m.bed,'Your goal '+m.bed)});
 out.forEach(x=>{if(m.later[x.id])x.t=mpS(mpT(x.t)+m.later[x.id])});
 return out.sort((a,b)=>mpT(a.t)-mpT(b.t))}
function mpRow(x,now){const m=MP(),past=mpT(x.t)<=now,done=m.done.includes(x.id)||(past&&x.k==='base'),skip=m.skip.includes(x.id),miss=past&&!done&&!skip&&x.k!=='base';
 const acts=done||skip||x.k==='base'?'':`<div class="acts"><button data-act="mpdone" data-v="${x.id}">${x.k==='med'?L('做了','Done'):L('完成','Done')}</button>${past?'':`<button data-act="mplater" data-v="${x.id}">${L('晚 1 小时','1 hour later')}</button>`}<button data-act="mpskip" data-v="${x.id}">${L('今天不做','Not today')}</button></div>`;
 const tg=x.k==='med'?`<span class="tag mu">${L('固定','Fixed')}</span>`:x.k==='sug'?`<span class="tag">${L('建议','Suggested')}</span>`:'';
 return `<div class="mpi ${done?'done':skip?'skip':miss?'miss':''}"><span class="tm num">${x.t}</span><div class="bd"><div class="tt">${x.go&&!done?`<button class="link" data-go="${x.go}" style="font-size:16px;padding:0;min-height:0;color:var(--tx);font-weight:600">${x.a} ${ic('chev',14)}</button>`:x.a}${tg}</div><div class="ss">${skip?L('今天不做了','Skipped today'):x.b}</div>${x.adj?`<div class="adj">↻ ${x.adj}</div>`:''}${acts}</div></div>`}
function mpTL(){const m=MP(),now=S.hour,L2=mpItems();let h='',nowDone=false;const past=L2.filter(x=>mpT(x.t)<=now);
 if(past.length&&!m.past){const nd=past.filter(x=>m.done.includes(x.id)||x.k==='base').length;h+=`<button class="pfold" data-act="mppast"><span>${L('已过 '+past.length+' 项 · 完成 '+nd+'/'+past.length,'Earlier: '+past.length+' items · '+nd+' of '+past.length+' done')}</span><span class="chev">${ic('chev',16)}</span></button>`}
 for(const x of L2){if(past.length&&!m.past&&past.includes(x))continue;if(!nowDone&&mpT(x.t)>now){h+=`<div class="pnow"><span>${L('现在 ','Now ')+clk()}</span></div>`;nowDone=true}h+=mpRow(x,now)}
 if(!nowDone)h+=`<div class="pnow"><span>${L('现在 ','Now ')+clk()}</span></div>`;
 return h}
P.mpsetup=()=>{const m=MP(),st=m.step;const ch=(f,v,t)=>`<button class="mpchip ${m[f]===v?'on':''}" data-act="mpset" data-v="${f}=${v}">${t}</button>`;
 const body=st===1?`<h1 class="h1" style="font-size:26px">${L('几点起床，几点上床？','When do you get up and go to bed?')}</h1><div class="h3">${L('起床','Get up')}</div><div class="mpchips">${['06:00','06:30','07:00','07:30'].map(v=>ch('wake',v,v)).join('')}</div><div class="h3">${L('上床','Go to bed')}</div><div class="mpchips">${['21:30','22:00','22:30','23:00'].map(v=>ch('bed',v,v)).join('')}</div><p class="sm mu">${L('固定起床时间，比早睡更重要。','A steady wake-up time matters more than an early bedtime.')}</p>`
 :st===2?`<h1 class="h1" style="font-size:26px">${L('你喜欢怎么动？','How do you like to move?')}</h1><div class="h3">${L('在哪','Where')}</div><div class="mpchips">${ch('where','outdoor',L('户外：公园连道、组屋楼下','Outdoors: park connector, round the block'))}${ch('where','indoor',L('室内：社区中心、家里','Indoors: community centre, at home'))}</div><div class="h3">${L('什么时候','When')}</div><div class="mpchips">${ch('when','morning',L('早上','Morning'))}${ch('when','evening',L('傍晚','Evening'))}</div><p class="sm mu">${L('下雨、空气不好（PSI 超过 100）或太热时，会自动帮你挪时间或换室内。','When it rains, the air is poor (PSI above 100) or it is too hot, we move it or switch indoors for you.')}</p>`
 :st===3?`<h1 class="h1" style="font-size:26px">${L('怎么提醒你？','How should we remind you?')}</h1><div class="card" style="padding:4px 16px"><div class="devcard"><span class="t">${L('手机通知','Phone notification')}<small>${L('戒指不会震动，提醒都在手机上','The ring doesn’t vibrate, so reminders come to your phone')}</small></span>${sw('on',1,{dis:1,lab:'phone'})}</div><div class="devcard"><span class="t">${L('也提醒家人','Remind my family too')}<small>${L('起床、上床、吃药没做时','If wake-up, bedtime or medicines are missed')}</small></span>${sw('fam',m.fam,{act:'mpsw',lab:'family'})}</div></div><div class="h3">${L('“读给我听”用什么语言','Read-aloud voice')}</div><div class="mpchips">${ch('voice','en','English')}${ch('voice','zh','华语')}</div>`
 :`<h1 class="h1" style="font-size:26px">${L('连上日历？（可跳过）','Connect your calendar? (optional)')}</h1><p class="p mu">${L('连上后，有事的时段不排建议，空档里插 1 分钟呼吸。只读，标题只留在这台手机上。','Busy times get no suggestions, and a 1-minute breather goes in the gaps. Read-only; titles stay on this phone.')}</p><div class="mpchips">${ch('cal',true,L('连上日历','Connect calendar'))}${ch('cal',false,L('先不用','Not now'))}</div>`;
 return{calm:1,html:`${nav(L('排好你的每一天','Set up your day'))}<div class="pad stack"><div class="mpstep">${[1,2,3,4].map(i=>`<i class="${i<=st?'on':''}"></i>`).join('')}</div><div class="sm mu">${L('第 '+st+' 步，共 4 步','Step '+st+' of 4')}</div>${body}<div class="row2" style="margin-top:8px">${st>1?`<button class="btn ghost" data-act="mpstep" data-v="-1">${L('上一步','Back')}</button>`:'<span></span>'}<button class="btn" data-act="${st<4?'mpstep':'mpfin'}" data-v="1">${st<4?L('下一步','Next'):L('完成','Done')}</button></div></div>`}};
P.breath=(k)=>{const f=k==='478';return{theme:'mo',calm:1,html:`${nav(f?L('4-7-8 助眠','4-7-8 for sleep'):L('1 分钟静心','1-minute calm'))}<div class="pad brw"><div class="brorb" id="br-orb"><img src="${LOTUSIMG}" alt=""></div><div class="h2" id="br-lab" style="font-family:var(--serif);font-weight:500;font-size:22px">${L('准备','Get ready')}</div><div class="num" id="br-t" style="font-size:32px">${f?'1:16':'1:00'}</div><p class="p mu" style="max-width:300px">${f?L('用鼻子吸气 4 秒，屏住 7 秒，用嘴慢慢呼气 8 秒，一共 4 组。','Breathe in through your nose for 4, hold for 7, breathe out slowly through your mouth for 8. Four rounds.'):L('吸气 5 秒，呼气 5 秒，一分钟 6 次。','In for 5, out for 5: six breaths a minute.')}</p><button class="btn ghost" data-act="back" style="max-width:240px">${L('结束','Finish')}</button></div>`,
 after(){const PH=f?[[L('吸气','Breathe in'),4,1],[L('屏住','Hold'),7,1],[L('呼气','Breathe out'),8,.62]]:[[L('吸气','Breathe in'),5,1],[L('呼气','Breathe out'),5,.62]];const cyc=PH.reduce((a,x)=>a+x[1],0),tot=f?cyc*4:60;let e=0;
  const orb=$('#br-orb'),lab=$('#br-lab'),tt=$('#br-t');
  const set=()=>{const c=e%cyc;let a=0;for(const [n,len,sc] of PH){if(c<a+len){lab.textContent=n+' · '+(a+len-c);if(c===a){orb.style.transition=`transform ${len}s ease-in-out`;orb.style.transform=`scale(${sc})`}break}a+=len}const r=tot-e;tt.textContent=Math.floor(r/60)+':'+String(r%60).padStart(2,'0')};
  set();const id=setInterval(()=>{if(!document.getElementById('br-orb')){clearInterval(id);return}e++;if(e>=tot){clearInterval(id);lab.textContent=L('做完了','Done');orb.style.transform='scale(.62)';tt.textContent='0:00';return}set()},1000)}}};
"""
JS=JS.replace('__LOTUS__',LOTUS)
MYPLAN_NEW=r"""P.myplan=()=>{if(linked())return P.care();
 const m=MP(),now=S.hour,L2=mpItems(),nx=L2.find(x=>mpT(x.t)>now&&!m.done.includes(x.id)&&!m.skip.includes(x.id)&&x.k!=='base'),nt=now>=20.5||now<4;
 const H=[['nap',L('午睡','Nap')],['kopi',L('下午 3 点后喝咖啡','Kopi after 3 pm')],['supper',L('宵夜','Late supper')],['late',L('熬夜','Up late')],['sit',L('久坐','Long sitting')],['drink',L('喝酒','Alcohol')]];
 const wk=[1,2,0,1,0,.5,0];
 return{tab:'myplan',html:`<div class="pad stack">
  <div class="between" style="padding-top:8px"><span class="sm mu">${L('我的计划 · 自己定的，随时可改','My plan · set by you, change any time')}</span><button class="link" data-act="mpread">${ic('sound',16)} ${L('读给我听','Read to me')}</button></div>
  <h1 class="h1" style="font-size:28px">${L('今天怎么过','How today goes')}</h1>
  <div class="card"><div class="between" style="gap:10px"><span class="ic" style="color:var(--slp)">${ic('rain',20)}</span><span style="flex:1;min-width:0"><span class="h3" style="display:block">25–32° · ${L('午后雷雨','afternoon thunderstorms')} · PSI 42</span><span class="sm mu">${L('11 点到下午 3 点最热，户外活动避开这段 · 天气：NEA','Hottest 11 am–3 pm, so keep outdoor activity outside it · Weather: NEA')}</span></span></div></div>
  ${m.setup?'':`<button class="card tap" data-go="mpsetup" style="text-align:left;--c:var(--vit)"><div class="between"><span class="h3">${L('用 4 步排好你的每一天','Set up your day in 4 steps')}</span><span class="chev">${ic('chev',16)}</span></div><p class="sm mu" style="margin:4px 0 0">${L('起床和上床、怎么运动、怎么提醒、日历（可跳过）。没设置前，先按默认排了一版。','Wake and bed times, how you move, reminders, calendar (optional). Until then, here’s a default day.')}</p></button>`}
  <div class="card" style="padding:20px"><div class="sm mu">${L('下一件事','Next up')}</div>${nx?`<div class="num" style="font-size:34px;margin-top:6px">${nx.t}</div><div class="h2" style="margin-top:2px">${nx.a}</div><p class="p mu" style="margin-top:4px">${nx.adj||nx.b}</p><div class="row2" style="margin-top:12px"><button class="btn" data-act="mpdone" data-v="${nx.id}">${L('做完了','Done')}</button><button class="btn ghost" data-act="mpread">${ic('sound',18)} ${L('读给我听','Read to me')}</button></div>`:`<div class="h2" style="margin-top:6px">${L('今天的事都做完了','All done for today')}</div><p class="p mu" style="margin-top:4px">${L('明天第一件事：'+m.wake+' 起床','First thing tomorrow: up at '+m.wake)}</p>`}</div>
  <div class="card"><div class="between"><span class="h3">${L('今天','Today')}</span><span class="sm mu">${L('建议最多 5 条','Up to 5 suggestions')}</span></div><div class="ptl" style="margin-top:6px">${mpTL()}</div></div>
  <div class="card"><div class="between"><span class="h3">${L('今天的习惯','Today’s habits')}</span><span class="sm mu">${L('点一下记下来','Tap what happened')}</span></div><div class="mpchips">${H.map(([k,t])=>`<button class="mpchip ${m.hab.includes(k)?'on':''}" data-act="mphab" data-v="${k}">${t}</button>`).join('')}</div><p class="sm mu" style="margin:8px 0 0">${L('记几天以后，“身体”里会告诉你哪件事最影响你的睡眠。','After a few days, Health shows which of these affects your sleep most.')}</p></div>
  <div class="card"><div class="between"><span class="h3">${L('吃药提醒','Medicine reminders')}</span><button class="link" data-act="mpmed">${ic('plus',14,2.2)} ${L('添加','Add')}</button></div>${m.meds.length?`<div class="kv" style="margin-top:4px">${m.meds.map(x=>`<div><span>${x.n}</span><span class="num">${x.t}</span></div>`).join('')}</div>`:`<p class="sm mu" style="margin:6px 0 0">${L('自己添加药名和时间，到点提醒你。','Add a medicine and a time, and we’ll remind you.')}</p>`}<p class="sm mu" style="margin:8px 0 0">${L('只是提醒，不给用药建议。连上诊所后，由医生的护理计划接管。','Reminders only, no dosing advice. If you link a clinic, your doctor’s care plan takes over.')}</p></div>
  <div class="card"><div class="lotus2"><img src="${LOTUSIMG}" alt=""><div style="flex:1;min-width:0"><span class="eyebrow">${L('荷息 · 跟着荷花呼吸','Lotus breath')}</span><div class="h3" style="margin-top:4px">${nt?L('睡前 4-7-8 呼吸','4-7-8 before sleep'):L('1 分钟呼吸','1-minute breathing')}</div><p class="sm mu" style="margin:4px 0 0">${nt?L('吸 4 秒、屏 7 秒、呼 8 秒，做 4 组，帮你慢下来入睡。','In 4, hold 7, out 8, four rounds, to slow down for sleep.'):L('一分钟 6 次，心里紧的时候做一组。','Six breaths a minute, whenever you feel tense.')}</p><div class="mpchips"><button class="btn sm${nt?' ghost':''}" data-go="breath:1">${L('一分钟 · 静心','1 min · calm')}</button><button class="btn sm${nt?'':' ghost'}" data-go="breath:478">${L('4-7-8 · 助眠','4-7-8 · sleep')}</button></div></div></div></div>
  <div class="card"><div class="between"><span class="h3">${L('睡得更好 · 第 '+m.course+' 课','Better sleep · Lesson '+m.course)}</span><span class="sm mu">${L('共 8 课','of 8')}</span></div><div class="prog2"><i style="width:${m.course/8*100}%"></i></div><p class="p mu" style="margin-top:8px">${L('固定起床时间比早睡更重要。这周先把起床定在 '+m.wake+'，周末也别晚过一小时。','A fixed wake-up time matters more than an early night. This week, get up at '+m.wake+', and no more than an hour later at weekends.')}</p><button class="btn ghost sm" data-act="mpcourse" style="margin-top:10px">${ic('sound',16)} ${L('听 3 分钟（'+(m.voice==='zh'?'华语':'English')+'）','Listen, 3 min ('+(m.voice==='zh'?'华语':'English')+')')}</button></div>
  <div class="card"><div class="between"><span class="h3">${L('运动','Exercise')}</span><button class="link" data-act="mplog">${L('本周 2/3 次 · 记录','2 of 3 this week · Log')}</button></div><div class="wk">${[L('一','M'),L('二','T'),L('三','W'),L('四','T'),L('五','F'),L('六','S'),L('日','S')].map((d,i)=>`<span><i class="${wk[i]===1?'on':wk[i]?'half':''}"></i>${d}</span>`).join('')}</div><p class="sm mu" style="margin:8px 0 0">${L('可以这样动：公园连道散步、社区中心健身操、组屋楼下快走。','Ideas: a park connector walk, an exercise class at the community centre, a brisk walk round your block.')}</p></div>
  <div class="card"><div class="between"><span class="h3">${L('我的目标','My goals')}</span><button class="link" data-act="mpedit">${L('改一改','Change')}</button></div><div class="kv" style="margin-top:4px">
   <div><span>${L('睡眠','Sleep')}</span><span class="num">7–8 h</span></div><div><span>${L('上床时间','Bedtime')}</span><span class="num">${m.bed}</span></div><div><span>${L('每天步数','Daily steps')}</span><span class="num">6,000</span></div><div><span>${L('血压（自己的目标）','Blood pressure (your own goal)')}</span><span class="num">&lt; 135/85</span></div></div>
   <p class="sm mu" style="margin:8px 0 0">${L('这些是你自己定的参考目标，不是医生的处方。','These are goals you set for yourself, not a doctor’s prescription.')}</p></div>
  <div class="card"><div class="h3">${L('这一周','This week')}</div><div class="kv" style="margin-top:4px"><div><span>${L(m.bed+' 前上床','In bed by '+m.bed)}</span><span class="num">5 / 7 ${L('晚','nights')}</span></div><div><span>${L('平均步数','Average steps')}</span><span class="num">5,420</span></div><div><span>${L('计划完成','Plan done')}</span><span class="num">74%</span></div></div><p class="sm mu" style="margin:8px 0 0">${L('和你自己的上周比，上床更规律了。','More regular bedtimes than your own last week.')}</p></div>
  <div class="card" style="padding:4px 16px"><div class="devcard"><span class="t">Healthy 365 · ${L('国家步数挑战赛','National Steps Challenge')}<small>${L('把每天步数同步过去，攒积分换奖励。','Send your daily steps across to earn points and rewards.')} <span class="tag warn">${L('接口待与保健促进局确认','Integration to be confirmed with HPB')}</span></small></span>${sw('h365',m.h365,{act:'mph365',lab:'Healthy 365'})}</div></div>
  <button class="card tap" data-go="connect" style="text-align:left"><div class="between"><span class="h3">${L('想让护士一起看着吗？','Want a nurse to keep an eye on it too?')}</span><span class="chev">${ic('chev',16)}</span></div><p class="sm mu" style="margin:4px 0 0">${L('连上诊所后，这个标签会变成“护理”：医生定的计划接管目标，你自己的习惯会保留。','Link a clinic and this tab becomes Care: your doctor’s plan takes over the goals, and your own habits stay.')}</p></button>
 </div>`}};
"""
a=s.index('P.myplan=()=>{if(linked())return P.care();'); b=s.index('P.linkc=()=>',a)
s=s[:a]+JS+MYPLAN_NEW+s[b:]
ACTS=r"""    mpdone(){const m=MP();if(!m.done.includes(v))m.done.push(v);m.skip=m.skip.filter(x=>x!==v);render()},
    mplater(){const m=MP();m.later[v]=(m.later[v]||0)+1;toast(L('挪到 1 小时后','Moved 1 hour later'));render()},
    mpskip(){const m=MP();if(!m.skip.includes(v))m.skip.push(v);render()},
    mppast(){MP().past=!MP().past;render()},
    mpread(){toast(MP().voice==='zh'?'正在用华语读下一件事（原型）':L('正在用英语读下一件事（原型）','Reading your next step aloud (prototype)'))},
    mphab(){const m=MP();m.hab=m.hab.includes(v)?m.hab.filter(x=>x!==v):m.hab.concat(v);render()},
    mpmed(){const m=MP();const opts=[['Amlodipine 5 mg','08:00'],['Metformin 500 mg','19:00']];const n=opts[m.meds.length%2];m.meds.push({n:n[0],t:n[1]});toast(L('已添加 '+n[0]+' · '+n[1]+'（原型）','Added '+n[0]+' at '+n[1]+' (prototype)'));render()},
    mpcourse(){const m=MP();toast(L('播放第 '+m.course+' 课（原型）','Playing lesson '+m.course+' (prototype)'));if(m.course<8)m.course++;setTimeout(render,600)},
    mplog(){toast(L('记一次运动：类型、时长（原型）','Log exercise: type and time (prototype)'))},
    mph365(){const m=MP();m.h365=!m.h365;toast(m.h365?L('已打开同步（接口待确认，原型）','Sync on (integration to be confirmed, prototype)'):L('已关闭同步','Sync off'));render()},
    mpset(){const m=MP(),[f,x]=v.split('=');m[f]=x==='true'?true:x==='false'?false:x;render()},
    mpsw(){const m=MP();m[v]=!m[v];render()},
    mpstep(){const m=MP();m.step=Math.max(1,Math.min(4,m.step+(+v)));render()},
    mpfin(){const m=MP();m.setup=true;m.step=1;m.later={};S.stack.pop();toast(L('已按你的习惯排好','Your day is set up'));render(true)},
"""
R("    mpedit(){",ACTS+"    mpedit(){")
# linked care: personal habits rows use taskRow with mpwalk/mpbed: keep
# index entries
R("['linkc',L('确认诊所','Confirm clinic')],","['linkc',L('确认诊所','Confirm clinic')],['mpsetup',L('计划设置','Plan setup')],['breath:1',L('荷息','Lotus breath')],")
# changelog
R("<b>v2.4</b>：自己用也有","<b>v2.5 计划页</b>：按国内版重做并换成新加坡内容——4 步设置（起床上床、怎么运动、提醒和读音语言、日历可跳过）；时间线带“现在”线，已过事项折叠，每项可“完成 / 晚 1 小时 / 今天不做”；雷雨自动把户外运动挪到早上，昨晚血氧偏低改成慢走，避开 11–15 点暑热；“读给我听”（英语/华语）；今天的习惯（午睡、下午咖啡、宵夜、熬夜、久坐、喝酒）；吃药提醒（只提醒）；荷息呼吸（1 分钟、4-7-8）；睡眠课程 8 课；运动一周格子；Healthy 365 步数同步（接口待确认）。<br><b>v2.4</b>：自己用也有")
R("'<b>v2.4</b>: On my own","'<b>v2.5 Plan page</b>: rebuilt on the China version with Singapore content: 4-step setup (wake and bed, how you move, reminders and read-aloud voice, optional calendar); timeline with a Now line, earlier items folded, each item Done / 1 hour later / Not today; thunderstorms move outdoor exercise to the morning, an overnight oxygen dip turns it into a slow walk, and the 11 am–3 pm heat is avoided; Read to me (English/华语); today’s habits (nap, kopi after 3 pm, late supper, up late, long sitting, alcohol); medicine reminders (reminders only); Lotus breath (1 minute, 4-7-8); an 8-lesson sleep course; a weekly exercise grid; Healthy 365 steps sync (integration to be confirmed).<br><b>v2.4</b>: On my own")
open(p,'w',encoding='utf-8').write(s); print('ok', len(s))
