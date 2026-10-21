import re
d='/tmp/claude-0/-home-user-claude-code/5304f462-4324-55e0-ae4d-a872d232e3d9/scratchpad/'
cn=open(d+'proto/vera-prototype.html',encoding='utf-8').read().split('\n')
p=d+'sgtob/vera-care-sg.html';s=open(p,encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a));s=s.replace(a,b)
zen='\n'.join(cn[1939:2113])  # lines 1940..2113
assert zen.startswith('const Zen=')
br='\n'.join(cn[2114:2139])   # P.breathe .. before 守护
assert br.startswith('P.breathe=')
# take only pond branch: from "):({theme:'xuan'" 
i=br.index("({theme:'xuan',light:true,html:")
pond=br[i:]
pond=pond.rstrip()
assert pond.endswith('}});'),pond[-20:]
pond=pond[:-1]  # drop ;
# bilingual
rep=[("nav(k==='478'?'荷息 · 4-7-8':'荷息 · 一分钟')","nav(k==='478'?L('荷息 · 4-7-8','Lotus breath · 4-7-8'):L('荷息 · 一分钟','Lotus breath · 1 minute'))"),
 ("${k==='478'?'吸气 4 秒，屏住 7 秒，呼气 8 秒':'吸气时水面起涟漪，呼气时慢慢平下来'}","${k==='478'?L('吸气 4 秒，屏住 7 秒，呼气 8 秒','In 4, hold 7, out 8'):L('吸气时水面起涟漪，呼气时慢慢平下来','Breathe in and the water ripples; breathe out and it settles')}"),
 ('<span id="breath-lab">吸气</span>','<span id="breath-lab">${L(\'吸气\',\'In\')}</span>'),
 ("${k==='478'?'第一组　共四组':'第一息　共六息'}","${k==='478'?L('第一组　共四组','Round 1 of 4'):L('第一息　共六息','Breath 1 of 6')}"),
 ('data-act="redo">再来一组</button>','data-act="redo">${L(\'再来一组\',\'Once more\')}</button>'),
 ('data-act="back">返回</button>','data-act="back">${L(\'返回\',\'Back\')}</button>'),
 ("cur()!=='breathe'","cur()!=='breath'"),
 ("lab.textContent='做完了'","lab.textContent=L('做完了','Done')"),
 ("const C=k==='478'?{T:76,cyc:19,P:[['吸气',4,'in'],['屏住',7,'hold'],['呼气',8,'out']],u:'组',N:'四',fin:'四组　做完'}:{T:60,cyc:10,P:[['吸气',5,'in'],['呼气',5,'out']],u:'息',N:'六',fin:'一分钟　六息'};",
  "const C=k==='478'?{T:76,cyc:19,P:[[L('吸气','In'),4,'in'],[L('屏住','Hold'),7,'hold'],[L('呼气','Out'),8,'out']],u:'组',N:'四',fin:L('四组　做完','Four rounds done')}:{T:60,cyc:10,P:[[L('吸气','In'),5,'in'],[L('呼气','Out'),5,'out']],u:'息',N:'六',fin:L('一分钟　六息','One minute, six breaths')};"),
 ("nn.textContent=`第${'一二三四五六'[Math.min(5,Math.floor(el/C.cyc))]}${C.u}　共${C.N}${C.u}`","nn.textContent=S.lang==='zh'?`第${'一二三四五六'[Math.min(5,Math.floor(el/C.cyc))]}${C.u}　共${C.N}${C.u}`:(k==='478'?'Round ':'Breath ')+(Math.min(5,Math.floor(el/C.cyc))+1)+' of '+(k==='478'?4:6)"),
]
for a,b in rep:
    assert pond.count(a)>=1,(a[:50]);pond=pond.replace(a,b)
# replace SG P.breath
a=s.index("P.breath=(k)=>{");b=s.index("\nP.myplan=",a)
s=s[:a]+zen+"\nconst BD={speed:1,jump:null};\nP.breath=(k)=>"+pond+";\n"+s[b+1:]
# lotus card
cardline=cn[1913]
m=re.search(r'data:image/jpeg;base64,[A-Za-z0-9+/=]+',cardline);img=m.group(0)
card=r"""function lotusCard(){const nt=S.hour>=20.5||S.hour<4;return `<div class="card lotuscard"><img src="LOTUSCARDIMG" alt="" aria-hidden="true"><span class="lc"><span class="eyebrow">${L('荷息 · 跟着荷花呼吸','Lotus breath')}</span><span class="h3" style="display:block;margin-top:4px">${nt?L('睡前 4-7-8 呼吸','4-7-8 before sleep'):L('1 分钟呼吸','1-minute breathing')}</span><span class="sm mu" style="display:block;margin-top:6px;line-height:1.6">${nt?L('吸 4 秒、屏 7 秒、呼 8 秒，做 4 组，帮你慢下来入睡。','In 4, hold 7, out 8, four rounds, to slow down for sleep.'):L('每分钟 6 次，六息一分钟，心里紧的时候做一组。','Six breaths a minute; one round when you feel tense.')}</span>
   <span style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap"><button class="btn sm${nt?' ghost':''}" data-go="breath:1">${L('一分钟 · 静心','1 min · calm')}</button><button class="btn sm${nt?'':' ghost'}" data-go="breath:478">${L('4-7-8 · 助眠','4-7-8 · sleep')}</button></span></span></div>`}
""".replace('LOTUSCARDIMG',img)
s=s.replace("const BD={speed:1,jump:null};","const BD={speed:1,jump:null};\n"+card,1)
# entries: solo plan row -> card ; linked health row -> card
i=s.index("   ${row('wind',L('荷息 · '");j=s.index("\n",i);s=s[:i]+s[j+1:]
R("""  ${focusCard(false)}
  <div class="card flush">""","""  ${focusCard(false)}
  ${lotusCard()}
  <div class="card flush">""")
R("""<div class="card flush">${li('wind',L('荷息 · 跟着荷花呼吸','Lotus breath'),L('1 分钟静心 · 4-7-8 助眠','1-minute calm · 4-7-8 for sleep'),'breath:1')}</div>""","""${lotusCard()}""")
# redo action
if "    redo(){" not in s: R("    qoff(){","    redo(){render()},\n    qoff(){")
# CSS
css=open(d+'pondcss.txt',encoding='utf-8').read()
css+="\n.app .card.lotuscard{display:grid!important;grid-template-columns:98px 1fr;gap:16px;align-items:center;text-align:left}.lotuscard img{width:98px;height:220px;object-fit:cover;border-radius:14px;display:block}.lotuscard .lc{display:block}\n"
i=s.index('</style>');s=s[:i]+css+s[i:]
# today line: night & HR high
R("night:[[L('月','☾'),L('今晚早点歇，明天的元气多半看这一觉。','Rest early; tomorrow’s energy mostly comes from tonight.')],[L('静','~'),L('关灯前，慢慢呼吸几次。','A few slow breaths before lights out.')]]}[S.tm]||[];",
  "night:[[L('荷','❀'),L('关灯前，跟荷花慢慢呼吸一分钟。','Before lights out, breathe with the lotus for a minute.'),'breath:478'],[L('月','☾'),L('今晚早点歇，明天的元气多半看这一觉。','Rest early; tomorrow’s energy mostly comes from tonight.')]]}[S.tm]||[];\n if(S.scen==='night'&&S.tm!=='night')Q.unshift([L('荷','❀'),L('心跳比平常快一点，要不要跟荷花呼吸一分钟？','Heart rate a little higher than usual. Breathe with the lotus for a minute?'),'breath:1']);")
R("return `<div class=\"sline\"><span class=\"sk\">${q[0]}</span><span class=\"t\">${q[1]}</span>","return `<div class=\"sline\"><span class=\"sk\">${q[0]}</span><span class=\"t\">${q[2]?`<button class=\"link\" data-go=\"${q[2]}\" style=\"text-align:left;padding:0;min-height:0;font:inherit;color:inherit\">${q[1]} ›</button>`:q[1]}</span>")
R("L('<b>v3.8.13</b>：","L('<b>v3.8.14</b>：荷息按中国版恢复：整屏荷塘动画（吸气花开、涟漪，切换轻震，做完小鱼游过、可再来一组）；入口换成荷花卡片（自己用在计划页，连诊所在身体页）；首页今日一句在夜里、心率偏高时引导去荷息。<br><b>v3.8.13</b>：")
R("'<b>v3.8.13</b>: Health","'<b>v3.8.14</b>: Lotus breath restored from the China version: full-screen lotus pond (blooms and ripples as you breathe, a light buzz at each switch, fish at the end, once more); the entry is the lotus card (Plan on your own, Health when linked); the line of the day points to it at night and when heart rate is up.<br><b>v3.8.13</b>: Health")
open(p,'w',encoding='utf-8').write(s)
i=s.rindex('})();');s=s[:i]+'window.__t={get S(){return S},go,render};\n'+s[i:]
open(d+'otiagen/sw_test.html','w',encoding='utf-8').write(s)
print('ok')
