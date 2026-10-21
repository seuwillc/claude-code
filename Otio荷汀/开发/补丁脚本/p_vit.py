p='sgtob/vera-care-sg.html';s=open(p).read()
def R(a,b,n=1):
    global s;assert s.count(a)==n,(s.count(a),a[:70]);s=s.replace(a,b)
# alert tint (A: 赭红, same as the app's "below usual" colour)
R(" function inkPaint(W,v,l,dark,lw){"," function inkPaint(W,v,l,dark,lw,al){")
R("  const key=[W,v.toFixed(2),l.toFixed(2),dark,lw].join();if(inkCache.has(key))return inkCache.get(key);",
  "  const key=[W,v.toFixed(2),l.toFixed(2),dark,lw,al?1:0].join();if(inkCache.has(key))return inkCache.get(key);")
R("C.qing=C.qing.map((x,i)=>Math.round(x+(tq[i]-x)*kq))}",
  "C.qing=C.qing.map((x,i)=>Math.round(x+(tq[i]-x)*kq))}\n  /* 需要留意的那天：彩换成提醒色（赭红），墨骨不变 */\n  if(al)Object.assign(C,dark?{qing:[226,140,110],lv:[232,170,132],dan:[240,202,172]}:{qing:[164,73,42],lv:[178,108,66],dan:[214,164,132]});")
R("  const Q=inkPaint(W,v,l,dark,+lw.toFixed(2)),c=el.getContext('2d')","  const Q=inkPaint(W,v,l,dark,+lw.toFixed(2),el.dataset.t==='alert'),c=el.getContext('2d')")
R('data-v="${vit}" data-l="${load}" data-s="ink" aria-hidden="true">','data-v="${vit}" data-l="${load}" data-s="ink" data-t="${opt.alert?\'alert\':\'\'}" aria-hidden="true">')
# vitality demo override
R("function vit(){return S.scen==='night'?61:68}","function vit(){return S.vitD!=null?S.vitD:S.scen==='night'?61:68}\nconst vitAlert=()=>S.scen==='night'||S.scen==='bp';")
# hero: vitality only, number in the middle, tap for one line
R("""   ${S.viz==='aura'?aura(168,vit(),S.tm==='morning'?4:9,{label:L('光漩：泼彩是元气，洒金是活动','Light swirl: wash = vitality, gold = activity')}):`<div class="enso">${enso(vit()/100,S.scen==='night'?'var(--tLow)':null)}</div>`}""",
  """   <button class="vitorb" data-act="vitwhy" aria-label="${L('元气 '+vit(),'Vitality '+vit())}">${S.viz==='aura'?aura(168,vit(),0,{label:L('元气 '+vit(),'Vitality '+vit()),alert:vitAlert()}):`<div class="enso">${enso(vit()/100,vitAlert()?'var(--tLow)':null)}</div>`}<span class="vnum num" ${vitAlert()?'style="color:var(--tLow)"':''}>${vit()}</span></button>""")
R(".enso{width:150px;height:150px;margin:6px 0 0 -6px;position:relative}",
  ".enso{width:150px;height:150px;margin:6px 0 0 -6px;position:relative}\n.vitorb{position:relative;display:block;align-self:flex-start;background:none;border:0;padding:0;margin:0;color:inherit;font:inherit;cursor:pointer}\n.vitorb .vnum{position:absolute;left:calc(50% - 3px);top:50%;transform:translate(-50%,-50%);font-family:var(--num);font-size:40px;line-height:1;color:var(--tx);pointer-events:none}")
R("    qoff(){","    vitwhy(){toast(L('这是你今天的元气，圈越满越足。','This is your vitality today. The fuller the circle, the more you have.'))},\n    qoff(){")
# three rings: resting heart rate replaces vitality
R("""  const T=[{k:L('元气','Vitality'),v:v,rv:v,o:{lo:65,hi:69,mn:55,mx:79,c:'var(--c-sq)'},t:low?'low':'ok',st:low?L('比平常低','Below usual'):'',go:'trend:vit'},""",
  """  const T=[{k:L('静息心率','Resting HR'),v:low?71:62,rv:low?71:62,o:{lo:61,hi:63,mn:54,mx:74,c:'var(--c-oh)'},t:low?'low':'ok',st:low?L('比平常高','Above usual'):'',go:'trend:rhr',u:L('次/分','bpm')},""")
# panel slider
R("""    <div class="grp"><span class="lbl" data-l="家人捎话|Family note">""","""    <div class="grp"><span class="lbl" data-l="元气（演示墨圈粗细）|Vitality (demo: ink circle)"></span><div class="hr-row"><input type="range" id="ctl-vit" min="40" max="95" step="1" aria-label="Vitality"><b id="vit-lab"></b></div></div>
    <div class="grp"><span class="lbl" data-l="家人捎话|Family note">""")
R("  const hr=$('#ctl-hour');hr.value=S.hour;","  {const vs=$('#ctl-vit');vs.value=vit();vs.oninput=()=>{S.vitD=+vs.value;render()}}\n  const hr=$('#ctl-hour');hr.value=S.hour;")
R("  {const hr=$('#ctl-hour');if(hr&&document.activeElement!==hr)hr.value=S.hour;const hl=$('#hour-lab');if(hl)hl.textContent=clk()}",
  "  {const hr=$('#ctl-hour');if(hr&&document.activeElement!==hr)hr.value=S.hour;const hl=$('#hour-lab');if(hl)hl.textContent=clk()}\n  {const vs=$('#ctl-vit');if(vs&&document.activeElement!==vs)vs.value=vit();const vl=$('#vit-lab');if(vl)vl.textContent=vit()}")
R("v=>{S.ecgSent=false;S.bp.step=0;S.msgSeen=false;S.qOff={};","v=>{S.ecgSent=false;S.bp.step=0;S.msgSeen=false;S.qOff={};S.vitD=null;")
R("$('#p-chg').innerHTML=L('<b>v3.8.33</b>","$('#p-chg').innerHTML=L('<b>v3.8.34</b>：首页墨圈只表达元气：去掉金沙，元气数字放在圈中间；元气越高圈越满、墨越润，低时墨淡、笔画收短；身体需要留意的那天（血氧偏低、血压超上限）彩换成提醒色赭红；点墨圈出一行“这是你今天的元气，圈越满越足。”。下面三个圆环改成静息心率、睡眠、活动。面板加“元气”滑杆演示墨圈变化。<br><b>v3.8.33</b>")
R("   '<b>v3.8.33</b>: Afternoon","   '<b>v3.8.34</b>: Today’s ink circle now shows vitality only: no gold dust, the vitality number sits in the middle; higher vitality means a fuller, richer circle, lower means paler ink and a shorter stroke; on a day that needs a look (oxygen dip, high BP) the colour turns to the alert red-ochre; tap the circle for one line. The three rings are now resting heart rate, sleep and activity. New panel slider to demo vitality.<br><b>v3.8.33</b>: Afternoon")
open(p,'w').write(s)
s=open(p).read();i=s.rfind('})();')
open('otiagen/sw_test.html','w').write(s[:i]+'window.__t={get S(){return S},go,render,tband,tseries};'+s[i:])
