p='sgtob/vera-care-sg.html';s=open(p).read()
a=s.index("P.welcome=()=>");b=s.index("function langSw(){")
s=s[:a]+r"""P.welcome=()=>({dark:1,full:1,html:`<div class="pad above" style="min-height:780px;display:flex;flex-direction:column;align-items:center;text-align:center;padding-top:14px;padding-bottom:30px">
  <div style="align-self:flex-end">${langSw()}</div>
  <div style="flex:1.1"></div>
  <div>${olloMark(240,{ink:'#F4F6F1',paper:'var(--bg)',label:'Otio'})}</div>
  <div style="font-family:var(--serif);font-size:20px;letter-spacing:.06em;margin-top:18px">${L('安时而处顺','At ease with time, in tune with the flow.')}</div>
  <p class="p mu" style="margin-top:12px;font-size:16px">${L('懂你的节律，只在需要时出现。','Knows your rhythm. Shows up only when it matters.')}</p>
  <div style="flex:1"></div>
  <button class="btn" data-go="login" style="width:100%">${L('开始使用','Get started')}</button>
  <button class="link" data-go="login" style="margin-top:12px;color:inherit;opacity:.85">${L('我有账号，登录','I have an account')}</button>
  <div class="bvby" style="margin-top:22px;justify-content:center">${bvMark(16)}<span>by BioVision AI</span></div>
  <div class="sm mu" style="margin-top:6px">${L('新加坡设计 · 数据存放在新加坡','Designed in Singapore · Data stays in Singapore')}</div>
 </div>`});
"""+s[b:]
def R(a,b,n=1):
    global s;assert s.count(a)==n,(s.count(a),a[:60]);s=s.replace(a,b)
R("$('#p-chg').innerHTML=L('<b>v3.8.27</b>","$('#p-chg').innerHTML=L('<b>v3.8.28</b>：欢迎页去掉“荷汀康护”大字，标志本身就是名字，居中；只留一句“懂你的节律，只在需要时出现。”；护理团队和诊所的说明移出欢迎页；登录改成文字链接，语言切换放右上角。<br><b>v3.8.27</b>")
R("   '<b>v3.8.27</b>: Today","   '<b>v3.8.28</b>: Welcome drops the big “Otio Care” name; the centred mark is the name, with one line “Knows your rhythm. Shows up only when it matters.” Care-team and clinic copy moved off Welcome; sign-in is a text link; language switch top right.<br><b>v3.8.27</b>: Today")
open(p,'w').write(s)
