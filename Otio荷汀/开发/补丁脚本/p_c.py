import re
d='/tmp/claude-0/-home-user-claude-code/5304f462-4324-55e0-ae4d-a872d232e3d9/scratchpad/'
p=d+'sgtob/vera-care-sg.html';s=open(p,encoding='utf-8').read()
def R(a,b):
    global s
    assert s.count(a)==1,(a[:70],s.count(a));s=s.replace(a,b)
R("""const mrow=(go,icn,k,st,v,u,bad)=>`<button class="li" data-go="${go}"><span class="ic">${ic(icn)}</span><span class="t">${k}<small style="${bad?'color:var(--tLow)':''}">${st}</small></span>""",
  """const mrow=(go,icn,k,st,v,u,bad,c)=>`<button class="li crow" style="--c:${c}" data-go="${go}"><span class="ic">${ic(icn)}</span><span class="t">${k}<small style="${bad?'color:var(--tLow)':''}">${st}</small></span>""")
for key,c in [("vit()",'var(--c-sq)'),("n?'6:05':'6:48'",'var(--c-dl)'),("n?71:62",'var(--c-oh)'),("n?'13.2':'14.6'",'var(--c-tsb)'),("'6,480'",'var(--c-zs)')]:
    pat=re.compile(r"(mrow\('[^']*',[^\n]*?,"+re.escape(key)+r",[^\n]*?,(?:n|0))\),")
    m=pat.search(s);assert m,key
    s=s[:m.end()-2]+",'"+c+"'),"+s[m.end():]
R("""<div class="card flush">${rows.join('')}</div>""","""<div class="card flush crows">${rows.join('')}</div>""")
# checks section: colored rows
a=s.index("""<div class="between" style="margin-top:6px"><span class="h2">${L('检查与测量'""");b=s.index("\n  </div>",a)
seg=s[a:b]
seg=seg.replace('<div class="card flush">','<div class="card flush crows">',1)
for icn,c in [("gauge",'var(--c-jz)'),("ecg",'var(--c-ts)'),("heart",'var(--c-oh)'),("drop",'var(--c-xs)'),("eye",'var(--c-zq)'),("doc",'var(--c-mo)'),("file",'var(--c-mo)')]:
    seg=seg.replace("li('"+icn+"',","cli('"+c+"','"+icn+"',")
s=s[:a]+seg+s[b:]
R("function lotusMini(){","const cli=(c,...a)=>li(...a).replace('<button class=\"li\"','<button class=\"li crow\" style=\"--c:'+c+'\"');\nfunction lotusMini(){")
css="""
/* 身体页配色：中国传统色。宣（浅）/ 墨（深）各一组，颜色旁边一定有文字 */
.app{--c-sq:#2E6E7E;--c-dl:#3F5A8C;--c-oh:#9A5B70;--c-tsb:#3E8C93;--c-zs:#A0531C;--c-jz:#8C4356;--c-ts:#A35F52;--c-xs:#9C7A2E;--c-zq:#5E7A4A;--c-mo:#55606A}
.app.mo{--c-sq:#8FC7CF;--c-dl:#9DB3E0;--c-oh:#D9A3B5;--c-tsb:#8CCBD0;--c-zs:#E2A77A;--c-jz:#D49AAA;--c-ts:#E0A797;--c-xs:#E2C27E;--c-zq:#A9C495;--c-mo:#B9C2CA}
.crows .crow{background:linear-gradient(90deg,color-mix(in srgb,var(--c) 13%,transparent),color-mix(in srgb,var(--c) 3%,transparent) 70%);padding-left:14px;padding-right:12px;margin:0 -16px;width:calc(100% + 32px)}
.crows .crow .ic{color:var(--c);background:color-mix(in srgb,var(--c) 14%,transparent)}
.crows .crow .t small{color:var(--c);font-weight:600}
.crows .crow+.crow{box-shadow:inset 0 1px 0 var(--line)}
"""
i=s.index('</style>');s=s[:i]+css+s[i:]
R("L('<b>v3.8.17</b>：","L('<b>v3.8.18</b>：身体页两块改用中国版风格：每行一种中国传统色（元气石青、睡眠黛蓝、心率藕荷、夜间呼吸天水碧、活动赭石；血压绛紫、心电檀色、心律藕荷、血糖缃色、眼底竹青、报告墨灰），浅底渐变 + 同色图标和状态字，深色模式各有一组。<br><b>v3.8.17</b>：")
R("'<b>v3.8.17</b>: Health","'<b>v3.8.18</b>: Health sections in the China-version style: each row has its own traditional Chinese colour (vitality stone blue, sleep indigo, heart rate lotus-root pink, breathing water green, activity ochre; BP plum, ECG sandalwood, rhythm lotus-root, glucose pale gold, eye bamboo green, reports ink grey), with a light tint and matching icon and status text, and a dark-mode set.<br><b>v3.8.17</b>: Health")
open(p,'w',encoding='utf-8').write(s)
i=s.rindex('})();');s=s[:i]+'window.__t={get S(){return S},go,render};\n'+s[i:]
open(d+'otiagen/sw_test.html','w',encoding='utf-8').write(s)
print('ok')
