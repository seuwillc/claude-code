p='sgtob/vera-care-sg.html';s=open(p).read()
def R(a,b,n=1):
    global s;assert s.count(a)==n,(s.count(a),a[:70]);s=s.replace(a,b)
# state
R("safe:false,greet:true,","safe:false,nt:'hm',ntAck:false,sent:{},")
# today line
R("morning:[S.greet&&S.scen==='normal'?[L('敏','♡'),L('慧敏说：周末回来看你。','Hui Min says: coming to see you this weekend.')]:null,S.scen==='normal'?","morning:[S.scen==='normal'?")
R(" if(S.scen==='night'&&S.tm!=='night'&&!(linked()||S.own.ecg))Q.unshift(",
  " if(S.nt==='hm')Q.unshift([L('敏','H'),L('慧敏说：周末回来看你。','Hui Min: coming to see you this weekend.'),null,'note']);\n if(S.scen==='night'&&S.tm!=='night'&&!(linked()||S.own.ecg))Q.unshift(")
R("""<button class="link" data-act="qoff" aria-label="${L('换一句','Next')}" style="min-height:0;padding:0 4px;color:var(--mu)">×</button></div>`}""",
  """${q[3]==='note'?(S.ntAck?`<span class="sm mu" style="flex:none">${L('已回 ♡','Replied ♡')}</span>`:`<button class="btn sm ghost" data-act="ntack" style="flex:none;min-height:34px;padding:0 12px">${L('收到 ♡','Got it ♡')}</button>`):''}<button class="link" data-act="qoff" aria-label="${L('换一句','Next')}" style="min-height:0;padding:0 4px;color:var(--mu)">×</button></div>`}""")
# family note box
R("const FAMITEMS=()=>","""function noteBox(w,n){const s=S.sent[w],P0=w==='w'?[L('记得喝水','Drink some water'),L('早点休息','Rest early'),L('我出门走走','Out for a walk')]:[L('我很好','I’m fine'),L('周末等你','See you this weekend'),L('别太累','Don’t overdo it')];
 return `<div class="card"><div class="between"><span class="h3">${L('捎句话给'+n,'A note for '+n)}</span><span class="sm mu">${L('每天一句','One a day')}</span></div>${s?`<div class="sm" style="margin-top:6px;color:var(--c-zq);font-weight:600">${L('今天捎了：','Sent today: ')}${s}</div>`:''}<div class="mpchips" style="margin-top:10px">${P0.map(t=>`<button class="mpchip ${s===t?'on':''}" data-act="famhi" data-v="${w}|${t}">${t}</button>`).join('')}<button class="mpchip" data-act="famnote" data-v="${w}">${L('自己写','Write my own')}</button></div></div>`}
const FAMITEMS=()=>""")
R("""  <div class="row2"><button class="btn sm ghost" data-act="famhi" data-v="${L('记得喝水','Remember to drink water')}">${L('记得喝水','Drink water')}</button><button class="btn sm ghost" data-act="famhi" data-v="${L('早点休息','Rest early')}">${L('早点休息','Rest early')}</button></div>
""","""  ${noteBox('w',L('秀兰','Siew Lan'))}
""")
R("""  <button class="btn" data-act="famcall" data-v="d">${ic('phone',16)} ${L('打电话给慧敏','Call Hui Min')}</button>""",
  """  ${noteBox('d',L('慧敏','Hui Min'))}
  <button class="btn" data-act="famcall" data-v="d">${ic('phone',16)} ${L('打电话给慧敏','Call Hui Min')}</button>""")
# actions
R("""    famhi(){toast(L('已发给秀兰：','Sent to Siew Lan: ')+v)},""",
  """    famhi(){const [w,t]=v.split('|');S.sent[w]=t;toast(L('已捎给'+(w==='w'?'秀兰':'慧敏')+'：','Sent to '+(w==='w'?'Siew Lan':'Hui Min')+': ')+t);render()},
    famnote(){sheet(`<h2 class="h2" style="font-size:20px">${L('自己写一句','Write your own')}</h2><div class="field" style="margin-top:12px"><div class="ph"><input id="ntin" maxlength="20" placeholder="${L('最多 20 个字','Up to 20 characters')}" aria-label="${L('一句话','Note')}"></div></div><button class="btn" style="margin-top:14px;width:100%" data-act="famnotesend" data-v="${v}">${L('捎过去','Send')}</button>`)},
    famnotesend(){const i=document.getElementById('ntin'),t=(i&&i.value.trim())||'';const b=document.querySelector('.sheet-bg');if(b)b.remove();if(!t)return;S.sent[v]=t;toast(L('已捎过去：','Sent: ')+t);render()},
    ntack(){S.ntAck=true;toast(L('慧敏会看到：爸爸看到了 · '+clk(),'Hui Min will see: Dad saw it · '+clk()));render()},""")
# daughter's phone preview
R("""<div class="sm mu" style="margin-top:6px">${S.safe?L('今天报了平安 ❀','Sent “all well” today ❀'):L('今天还没报平安','No “all well” yet today')}</div></div>""",
  """<div class="sm mu" style="margin-top:6px">${S.safe?L('今天报了平安 ❀','Sent “all well” today ❀'):L('今天还没报平安','No “all well” yet today')}</div>${S.nt==='hm'?`<div class="sm mu" style="margin-top:4px">${L('你捎的“周末回来看你”：','Your note “coming this weekend”: ')}${S.ntAck?L('爸爸看到了 ♡','Dad saw it ♡'):L('还没看到','not seen yet')}</div>`:''}${S.sent.d?`<div class="sm" style="margin-top:4px">${L('爸爸捎来：','From Dad: ')}${S.sent.d}</div>`:''}</div>""")
# panel
R("""    <div class="grp"><span class="lbl" data-l="首页画面|Home visual">""","""    <div class="grp"><span class="lbl" data-l="家人捎话|Family note"></span><div class="seg" id="ctl-nt"></div></div>
    <div class="grp"><span class="lbl" data-l="首页画面|Home visual">""")
R("""  seg('ctl-viz','viz',""","""  seg('ctl-nt','nt',[['hm',L('慧敏捎来一句','Note from Hui Min')],['none',L('没有','None')]],()=>{S.ntAck=false});
  seg('ctl-viz','viz',""")
R("['lang','care','scen','tm','dev','viz'].forEach(k=>{const m={lang:'ctl-lang',care:'ctl-care',scen:'ctl-scen',tm:'ctl-tm',dev:'ctl-dev',viz:'ctl-viz'}[k]",
  "['lang','care','scen','tm','dev','viz','nt'].forEach(k=>{const m={lang:'ctl-lang',care:'ctl-care',scen:'ctl-scen',tm:'ctl-tm',dev:'ctl-dev',viz:'ctl-viz',nt:'ctl-nt'}[k]")
R("$('#p-chg').innerHTML=L('<b>v3.8.29</b>","$('#p-chg').innerHTML=L('<b>v3.8.30</b>：家人“捎句话”：家人每天可以捎一句（常用句或自己写，最多 20 字），出现在首页“今日一句”里，排在身体提醒之后、天气之前，旁边一个“收到 ♡”，对方会看到“爸爸看到了”；不是聊天，没有对话框和红点。家人页里也能给秀兰、慧敏各捎一句。面板加“家人捎话”开关。<br><b>v3.8.29</b>")
R("   '<b>v3.8.29</b>: The name","   '<b>v3.8.30</b>: Family notes: each family member can send one line a day (a ready phrase or up to 20 characters). It shows in Today’s line, after body alerts and before weather, with a “Got it ♡” button; the sender sees “Dad saw it”. Not a chat: no thread, no badges. You can send Siew Lan and Hui Min a note from Family. New panel switch: Family note.<br><b>v3.8.29</b>: The name")
open(p,'w').write(s)
