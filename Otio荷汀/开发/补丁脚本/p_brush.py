p='sgtob/vera-care-sg.html';s=open(p).read()
def R(a,b,n=1):
    global s;assert s.count(a)==n,(s.count(a),a[:70]);s=s.replace(a,b)
R(" function inkPaint(W,v,l,dark,lw,al){"," function inkPaint(W,v,l,dark,lw,al,nv){")
R("  const key=[W,v.toFixed(2),l.toFixed(2),dark,lw,al?1:0].join();","  const key=[W,v.toFixed(2),l.toFixed(2),dark,lw,al?1:0,nv?1:0].join();")
R("  const d=Math.PI*.55*(v-.5),IA=-Math.PI*.37+d,ISW=Math.PI*.88-d,CS=Math.PI*.80,sc=(Math.PI*1.1+d)/(Math.PI*1.1),A=a=>CS+(a-CS)*sc;",
  """  const d=Math.PI*.55*(v-.5),IA=-Math.PI*.37+d,CS=Math.PI*.80,sc=(Math.PI*1.1+d)/(Math.PI*1.1);let ISW=Math.PI*.88-d,A=a=>CS+(a-CS)*sc;
  /* 新笔法：元气主要落在“圆满度”上。元气足，缺口几乎合拢；元气亏，彩起得晚、墨收得早，缺口变大 */
  const G=nv?Math.PI*.5*(.55-v):0;
  if(nv){const E=IA+2*Math.PI,A0=A,k2=(E-(CS+G/2))/(E-CS);A=a=>E-(E-A0(a))*k2;ISW-=G/2}""")
# splashes
R("for(let i=0;i<Math.round(4+8*v);i++){const a=A(","for(let i=0;i<Math.round(4+8*v)+(nv?4:0);i++){const a=A(")
# water rim + paper fibres
R("  /* 水流丝：几缕细淡的拖尾 */","""  /* 新笔法：水渍线（颜料干时边缘积起的一道深线）+ 宣纸纤维（颜色像渗进纸里） */
  if(nv){const [Le,ge]=mk();ge.drawImage(Lp,0,0);ge.globalCompositeOperation='destination-out';ge.filter=`blur(${(W*.007).toFixed(1)}px)`;for(let i=0;i<3;i++)ge.drawImage(Lp,0,0);ge.filter='none';ge.globalCompositeOperation='source-in';ge.fillStyle=`rgb(${C.qing.map(x=>Math.round(x*(dark?1.1:.75)))})`;ge.fillRect(0,0,W,W);gp.save();gp.globalAlpha=dark?.45:.7;gp.drawImage(Le,0,0);gp.restore();
   const fr=rng(77);gp.save();gp.globalCompositeOperation='destination-out';gp.lineCap='round';for(let i=0;i<Math.round(W*.6);i++){const x=fr()*W,y=fr()*W,a=fr()*Math.PI,l2=W*(.01+.03*fr());gp.strokeStyle=`rgba(0,0,0,${(.05+.12*fr()).toFixed(3)})`;gp.lineWidth=Math.max(.6,W*.0012);gp.beginPath();gp.moveTo(x,y);gp.quadraticCurveTo(x+Math.cos(a)*l2*.5+(fr()-.5)*W*.01,y+Math.sin(a)*l2*.5+(fr()-.5)*W*.01,x+Math.cos(a)*l2,y+Math.sin(a)*l2);gp.stroke()}gp.restore()}
  /* 水流丝：几缕细淡的拖尾 */""")
# 提按: thick-thin-thick rhythm
R("return head*(.78+.32*pz(s*1.4))*taper};","return head*(.78+.32*pz(s*1.4))*taper*(nv?1-.26*Math.exp(-Math.pow((s-.30)/.12,2))+.22*Math.exp(-Math.pow((s-.54)/.10,2)):1)};")
# 飞白: irregular bristles
R("al=(dark?.16:.24)*(.45+.8*br());","al=(dark?.16:.24)*(.45+.8*br()),endS=nv?.80+.2*br():2;")
R("o=Math.max(-1,Math.min(1,o0+.22*(drift(s*1.2)-.5)));","o=Math.max(-1,Math.min(1,o0+(nv?.5:.22)*(drift(s*1.2)-.5)));")
R("     if(gap||left<-.15){dn=false;continue}","     if(nv&&(s>endS||(s>dryAt*.55&&own(s*5.3+b*.1)<.16))){dn=false;continue}\n     if(gap||left<-.15){dn=false;continue}")
# ink grows out of colour: longer transition
R("ramp=Math.PI*.88*(.13+.10*(1-v))","ramp=Math.PI*.88*(.13+.10*(1-v))*(nv?1.7:1)")
# plumbing
R("  const Q=inkPaint(W,v,l,dark,+lw.toFixed(2),el.dataset.t==='alert'),","  const Q=inkPaint(W,v,l,dark,+lw.toFixed(2),el.dataset.t==='alert',el.dataset.nv==='1'),")
R("""data-t="${opt.alert?'alert':''}" aria-hidden="true">""","""data-t="${opt.alert?'alert':''}" data-nv="${opt.nv?1:0}" aria-hidden="true">""")
R("""${aura(168,vit(),0,{label:L('元气 '+vit(),'Vitality '+vit()),alert:vitAlert()})}<span class="vnum num" """,
  """${aura(168,vit(),0,{label:L('元气 '+vit(),'Vitality '+vit()),alert:vitAlert(),nv:S.brush!=='v1'})}<span class="vnum num${S.brush!=='v1'?' v2':''}" """)
R(".vitorb .vnum{",".vitorb .vnum.v2{font-size:34px;font-weight:300;top:calc(50% + 6px);opacity:.9}\n.vitorb .vnum{")
R("hour:8.33,va:'auto',","hour:8.33,va:'auto',brush:'v2',")
R("""    <div class="grp"><span class="lbl" data-l="墨圈颜色（演示）|Ink circle colour (demo)"></span><div class="seg" id="ctl-va"></div></div>""",
  """    <div class="grp"><span class="lbl" data-l="墨圈颜色（演示）|Ink circle colour (demo)"></span><div class="seg" id="ctl-va"></div></div>
    <div class="grp"><span class="lbl" data-l="光漩笔法|Ink brushwork"></span><div class="seg" id="ctl-brush"></div></div>""")
R("""  seg('ctl-va','va',""","""  seg('ctl-brush','brush',[['v2',L('新笔法','New')],['v1',L('原版','Original')]]);
  seg('ctl-va','va',""")
R("['lang','care','scen','tm','dev','va','nt'].forEach(k=>{const m={lang:'ctl-lang',care:'ctl-care',scen:'ctl-scen',tm:'ctl-tm',dev:'ctl-dev',va:'ctl-va',nt:'ctl-nt'}[k]",
  "['lang','care','scen','tm','dev','va','nt','brush'].forEach(k=>{const m={lang:'ctl-lang',care:'ctl-care',scen:'ctl-scen',tm:'ctl-tm',dev:'ctl-dev',va:'ctl-va',nt:'ctl-nt',brush:'ctl-brush'}[k]")
open(p,'w').write(s)
s=open(p).read();i=s.rfind('})();')
open('otiagen/sw_test.html','w').write(s[:i]+'window.__t={get S(){return S},go,render,tband,tseries};'+s[i:])
