d='/tmp/claude-0/-home-user-claude-code/5304f462-4324-55e0-ae4d-a872d232e3d9/scratchpad/'
p=d+'sgtob/vera-care-sg.html';s=open(p,encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a));s=s.replace(a,b)
R("fam:{hm:1}","fam:{hm:1,sl:0,hr:0,ox:0,bp:0},safe:false,greet:true")
a=s.index("P.family=()=>({tab:'family'");b=s.index("\n/* ---------- Me ---------- */",a)
s=s[:a]+r"""function famRow(o){return `<div class="vrow2 frow" style="--c:${o.c}" data-go="${o.go}"><span class="ic" style="font-weight:600;font-size:14px">${o.av}</span><span class="nm"><b>${o.n}</b><span class="st">${o.st}</span></span><span class="rt" style="align-items:flex-end"><button class="btn sm ghost" data-act="famcall" data-v="${o.who}" style="min-height:36px;padding:0 12px">${ic('phone',14)} ${L('打电话','Call')}</button></span><span class="chev">${ic('chev',14)}</span></div>`}
const FAMITEMS=()=>[['sl',L('睡眠','Sleep')],['hr',L('静息心率','Resting heart rate')],['ox',L('血氧','Oxygen')],['bp',L('血压','Blood pressure')]];
P.family=()=>{const on=FAMITEMS().filter(([k])=>S.fam[k]).map(x=>x[1]);return{tab:'family',html:`<div class="pad stack">
  <div class="between" style="padding-top:12px;align-items:center"><h1 class="h1">${L('家人','Family')}</h1><button class="btn sm ${S.safe?'ghost':''}" data-act="famsafe" ${S.safe?'disabled':''}>${S.safe?L('已报平安','Sent: all well'):L('报个平安','Send “all well”')}</button></div>
  <div class="between" style="margin-top:4px"><span class="h2">${L('我关心的人','People I look after')}</span><span class="sm mu">${L('只看好不好','How they’re doing')}</span></div>
  <div class="card vitals2">${famRow({c:'var(--c-oh)',av:L('兰','S'),n:L('太太 · 陈秀兰','Tan Siew Lan · wife'),st:L('都和平常差不多 · 今早报了平安','About usual · sent “all well” today'),go:'famw',who:'w'})}</div>
  <div class="between" style="margin-top:4px"><span class="h2">${L('关心我的人','People who look after me')}</span><span class="sm mu">${L('到期会再问你','Asks again when due')}</span></div>
  <div class="card vitals2">${famRow({c:'var(--c-zq)',av:L('敏','H'),n:L('女儿 · 吴慧敏','Goh Hui Min · daughter'),st:S.fam.hm?L('看到：好不好','Sees: how you are')+(on.length?L(' + '+on.join('、'),' + '+on.join(', ')):'')+L(' · 到 2027.4.13',' · until 13 Apr 2027'):L('已暂停分享','Sharing paused'),go:'famshare',who:'d'})}</div>
  <button class="btn ghost" data-act="invite">${ic('plus',18)} ${L('邀请家人','Invite family')}</button>
 </div>`}};
P.famw=()=>({calm:1,html:`${nav(L('太太 · 陈秀兰','Tan Siew Lan'))}<div class="pad stack">
  <div class="card vitals2"><div class="vrow2" style="--c:var(--c-oh)"><span class="ic">${L('兰','S')}</span><span class="nm"><b>${L('都和平常差不多','About usual')}</b><span class="st">${L('今早 6:50 同步 · 已报平安','Synced 6:50 am · sent “all well”')}</span></span><span class="rt"></span><span></span></div></div>
  <div class="card"><div class="h3">${L('她给你看的','What she shares with you')}</div><div class="kv" style="margin-top:4px"><div><span>${L('好不好','How she is')}</span><span>${ic('check',14,2.4)}</span></div><div><span>${L('睡眠','Sleep')}</span><span>${L('和平常差不多','About usual')}</span></div></div></div>
  <button class="btn" data-act="famcall" data-v="w">${ic('phone',16)} ${L('打电话给秀兰','Call Siew Lan')}</button>
  <div class="row2"><button class="btn sm ghost" data-act="famhi" data-v="${L('记得喝水','Remember to drink water')}">${L('记得喝水','Drink water')}</button><button class="btn sm ghost" data-act="famhi" data-v="${L('早点休息','Rest early')}">${L('早点休息','Rest early')}</button></div>
 </div>`});
P.famshare=()=>({calm:1,html:`${nav(L('慧敏能看到什么','What Hui Min sees'))}<div class="pad stack">
  <div class="card" style="padding:4px 16px"><div class="devcard"><span class="t">${L('分享给慧敏','Share with Hui Min')}<small>${L('到 2027.4.13，到期会再问你','Until 13 Apr 2027; we’ll ask again then')}</small></span>${sw('hm',S.fam.hm,{act:'fam',lab:'Hui Min'})}</div></div>
  ${S.fam.hm?`<div class="card" style="padding:4px 16px"><div class="devcard"><span class="t">${L('好不好','How you are')}<small>${L('“都和平常差不多”或“有一项需要留意”','“About usual” or “one thing to keep an eye on”')}</small></span><span class="tag ok">${L('一直开','Always on')}</span></div>${FAMITEMS().map(([k,t])=>`<div class="devcard"><span class="t">${t}<small>${L('只看在不在平常范围，不看数字','In-range only, no numbers')}</small></span>${sw(k,S.fam[k],{act:'fam',lab:t})}</div>`).join('')}</div>
  <div class="card flush">${li('eye',L('看看慧敏那边看到什么','See what Hui Min sees'),null,null,null,{act:'fampreview'})}</div>`:''}
  <button class="btn" data-act="famcall" data-v="d">${ic('phone',16)} ${L('打电话给慧敏','Call Hui Min')}</button>
  <p class="sm mu">${L('有一项连续 3 天和平常不一样，慧敏会收到一句“可以问问最近怎么样”。','If something stays off your usual for 3 days, Hui Min gets a note to check in.')}${linked()?L('诊所的事由护理团队跟进，她看不到你的诊所消息和心电。',' Clinic matters stay with your care team; she can’t see clinic messages or ECGs.'):''}</p>
 </div>`});
"""+s[b:]
R("famtap(){toast(L('只显示在不在平常范围（原型）','Shows in-range status only (prototype)'))}","famtap(){go('famw')}")
R("invite(){toast(L('邀请链接已复制','Invite link copied'))}","""invite(){sheet(`<h2 class="h2" style="font-size:20px">${L('邀请家人','Invite family')}</h2><p class="p" style="margin-top:6px">${L('先选给对方看什么。默认只看你好不好。','First choose what they’ll see. By default, only how you are.')}</p><div class="mpchips" style="margin-top:10px"><span class="mpchip on">${L('好不好','How I am')}</span>${FAMITEMS().map(([k,t])=>`<span class="mpchip">${t}</span>`).join('')}</div><p class="sm mu" style="margin-top:8px">${L('一年后到期，到时再问你。','Expires in a year; we’ll ask again then.')}</p><button class="btn" data-act="invitesend" style="margin-top:12px">${L('发出邀请','Send invite')}</button>`)},
    invitesend(){const b=document.querySelector('.sheet-bg');if(b)b.remove();toast(L('邀请已发出','Invite sent'))},
    famsafe(){S.safe=true;toast(L('已告诉慧敏和秀兰：今天很好','Told Hui Min and Siew Lan: all well today'));render()},
    famcall(){toast(v==='w'?L('正在打给秀兰（原型）','Calling Siew Lan (prototype)'):L('正在打给慧敏（原型）','Calling Hui Min (prototype)'))},
    famhi(){toast(L('已发给秀兰：','Sent to Siew Lan: ')+v)},
    fampreview(){const on=FAMITEMS().filter(([k])=>S.fam[k]);sheet(`<div class="sm mu">${L('慧敏的手机上：','On Hui Min’s phone:')}</div><div class="card" style="margin-top:8px"><div class="h3">${L('爸爸','Dad')}</div><p class="p" style="margin-top:4px">${L('都和平常差不多','About the same as usual')}</p>${on.map(([k,t])=>`<div class="sm mu" style="margin-top:4px">${t} · ${L('平常范围内','in usual range')}</div>`).join('')}<div class="sm mu" style="margin-top:6px">${S.safe?L('今天报了平安 ❀','Sent “all well” today ❀'):L('今天还没报平安','No “all well” yet today')}</div></div><p class="sm mu" style="margin-top:8px">${L('她看不到具体数字。','She sees no numbers.')}</p>`)},""")
# greeting in today line (morning)
R("const Q={morning:[S.scen==='normal'?[L('伞','☂')","const Q={morning:[S.greet&&S.scen==='normal'?[L('敏','♡'),L('慧敏说：周末回来看你。','Hui Min says: coming to see you this weekend.')]:null,S.scen==='normal'?[L('伞','☂')")
css=".frow{cursor:pointer}.frow .rt{justify-content:center}\n"
i=s.index('</style>');s=s[:i]+css+s[i:]
R("L('<b>v3.8.25</b>：","L('<b>v3.8.26</b>：家人页重做，风格同身体页：顶部“报个平安”；分“我关心的人”“关心我的人”，每人一行带传统色和“打电话”；点太太进她的小页面（她给你看的、打电话、发一句问候）；点女儿进分享设置（好不好一直开，睡眠、静息心率、血氧、血压默认关可单独开，可预览她那边看到什么）；邀请家人先选给对方看什么；去掉解释段落；首页今日一句会出现家人的问候。<br><b>v3.8.25</b>：")
R("'<b>v3.8.25</b>: On your","'<b>v3.8.26</b>: Family redone in the Health style: Send “all well” at the top; People I look after and People who look after me, one coloured row each with Call; your wife’s page (what she shares, call, send a note); your daughter’s sharing settings (how you are always on; sleep, resting HR, oxygen, BP off by default; preview her view); invites start by choosing what to share; explanatory paragraphs removed; a family note can appear in the line of the day.<br><b>v3.8.25</b>: On your")
open(p,'w',encoding='utf-8').write(s)
i=s.rindex('})();');s=s[:i]+'window.__t={get S(){return S},go,render,tband,tseries};\n'+s[i:]
open(d+'otiagen/sw_test.html','w',encoding='utf-8').write(s)
print('ok')
