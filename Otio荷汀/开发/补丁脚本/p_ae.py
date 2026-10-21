import re
p='sgtob/vera-care-sg.html';s=open(p).read()
def R(a,b,n=1):
    global s;assert s.count(a)==n,(s.count(a),a[:70]);s=s.replace(a,b)
# metric colour tokens, one per metric across the app
R(".ic.care{color:var(--care)}",".ic.care{color:var(--care)}\n.ic.mc{color:var(--c);background:color-mix(in srgb,var(--c) 14%,transparent)}")
R("const DEVS=()=>[","const MC={ring:'var(--c-sq)',bp:'var(--c-jz)',ecg:'var(--c-oh)',cgm:'var(--c-xs)',thermo:'var(--c-ts)',mat:'var(--c-dl)'};\nconst DEVS=()=>[")
# devices
R("""<div class="devcard"><span class="ic">${ic(S.dev==='ring'?'ring':'band')}</span>""","""<div class="devcard"><span class="ic mc" style="--c:${MC.ring}">${ic(S.dev==='ring'?'ring':'band')}</span>""")
R("""map(x=>`<div class="devcard"><span class="ic">${ic(x.ic)}</span>""","""map(x=>`<div class="devcard"><span class="ic mc" style="--c:${MC[x.k]}">${ic(x.ic)}</span>""")
# store: coloured icon, stacked Q/A
R("""<span class="ic" style="width:30px;height:30px;border-radius:50%;display:grid;place-items:center;background:var(--sf2)">${ic(x.ic,16)}</span>""",
  """<span class="ic mc" style="--c:${MC[x.k]};width:30px;height:30px;border-radius:50%">${ic(x.ic,16)}</span>""")
R("""   <div class="kv" style="margin-top:6px"><div><span class="sm mu">${L('谁需要','Who it’s for')}</span><span class="sm" style="text-align:right;max-width:62%">${x.who}</span></div><div><span class="sm mu">${L('谁不需要','Who doesn’t need it')}</span><span class="sm" style="text-align:right;max-width:62%">${x.no}</span></div><div><span class="sm mu">${L('和戒指的区别','vs the ring')}</span><span class="sm" style="text-align:right;max-width:62%">${x.diff}</span></div></div>""",
  """   <div class="stack" style="gap:10px;margin-top:12px">${[[L('谁需要','Who it’s for'),x.who],[L('谁不需要','Who doesn’t need it'),x.no],[L('和戒指的区别','vs the ring'),x.diff]].map(([k,t])=>`<div><div class="sm mu">${k}</div><div class="p" style="font-size:15px;margin-top:2px">${t}</div></div>`).join('')}</div>""")
# ECG list icons
R("""<span class="ic care">${ic('ecg')}</span><span class="t">${r.at}""","""<span class="ic mc" style="--c:${MC.ecg}">${ic('ecg')}</span><span class="t">${r.at}""")
# BP chart: 绛紫 systolic, 黛蓝 diastolic
s=s.replace("'#B83227'","'var(--c-jz)'").replace("'#35589C'","'var(--c-dl)'")
R('<i style="background:#B83227"></i>','<i style="background:var(--c-jz)"></i>')
R('<i style="background:#35589C"></i>','<i style="background:var(--c-dl)"></i>')
# oxygen tiles label size
R(".oxt .k{font-size:13px;",".oxt .k{font-size:14px;")
# thermometer: last 7 days sparkline in 檀
R("""<div class="bign" ${fev?'style="color:var(--tLow)"':''}>${t.toFixed(1)}<small>°C</small></div></div>""",
  """<div class="bign" ${fev?'style="color:var(--tLow)"':''}>${t.toFixed(1)}<small>°C</small></div>${(()=>{const d=[36.6,36.7,36.5,36.8,36.6,36.7,t],W=300,H=70,mn=36,mx=39,X=i=>10+i/6*(W-20),Y=v=>6+(1-(v-mn)/(mx-mn))*(H-22);return `<svg class="chart" viewBox="0 0 ${W} ${H}" style="margin-top:8px"><path d="M6 ${Y(38).toFixed(1)}H${W-6}" stroke="var(--tLow)" stroke-dasharray="2 4" stroke-opacity=".6"/><text x="${W-6}" y="${(Y(38)-4).toFixed(1)}" text-anchor="end">38°</text><path d="${d.map((v,i)=>(i?'L':'M')+X(i).toFixed(1)+' '+Y(v).toFixed(1)).join('')}" fill="none" stroke="var(--c-ts)" stroke-width="1.6"/>${d.map((v,i)=>`<circle cx="${X(i).toFixed(1)}" cy="${Y(v).toFixed(1)}" r="${i===6?4:2.2}" fill="${i===6&&fev?'var(--tLow)':'var(--c-ts)'}"/>`).join('')}<text x="10" y="${H-2}">${L('7 天前','7 days ago')}</text><text x="${W-10}" y="${H-2}" text-anchor="end">${L('今天','Today')}</text></svg>`})()}</div>""")
# rhythm: no repeated page name in the headline
R("""<h1 class="h1" style="font-size:24px">${L('夜间心律提示在等注册证','Night rhythm alerts are awaiting registration')}</h1>""",
  """<h1 class="h1" style="font-size:24px">${L('还在等注册证','Awaiting registration')}</h1>""")
# metric pages merge into Trends
R("P.metric=k=>{if(k==='hr')return P.trend('rhr');","P.metric=k=>{const TK={hr:'rhr',vit:'vit',sleep:'sleep',act:'steps'}[k||'vit'];if(TK)return P.trend(TK);")
# privacy contact: old brand
s=s.replace("dpo@veracare.sg","dpo@otio.sg")
open(p,'w').write(s)
