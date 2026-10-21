import sys,re
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# 1 welcome
R("""  <button class="btn ghost" data-go="login">${L('我有账号，登录','I have an account')}</button>
""","")
R("""<p class="p sm mu">${L('戒指看睡眠和心率；血压计、心电卡、连续血糖仪的读数，按你的同意交给你的诊所。','Your ring follows sleep and heart rate. Readings from your BP monitor, ECG card and CGM go to your clinic, with your consent.')}</p>""",
  """<p class="p sm mu">${L('戒指看睡眠和心率，家人和诊所可以一起照看。','Your ring follows sleep and heart rate; family and your clinic can look in too.')}</p>""")
# 2 login
i=s.index('<button class="chk" role="checkbox" aria-checked="${S.agree}" data-act="agree">');j=s.index('</button>',i)+len('</button>')
s=s[:i]+"""<p class="sm mu" style="margin:0">${L('继续即表示同意《使用条款》和《隐私声明》（依据新加坡 PDPA）。','By continuing you agree to the Terms of Use and the Privacy Notice (under Singapore’s PDPA).')}</p>"""+s[j:]
R("""<button class="btn ghost sm" data-act="otp">""","""<button class="btn ghost sm" data-act="otp" style="flex:none;min-width:88px;white-space:nowrap">""")
R("singpass(){if(!S.agree){toast(L('请先勾选同意条款','Please accept the terms first'));return}toast(","singpass(){toast(")
R("login(){if(!S.agree){toast(L('请先勾选同意条款','Please accept the terms first'));return}go('join')},","login(){go('join')},")
R("    agree(){S.agree=!S.agree;render()},\n","")
# 3 join
R("""<button class="btn ghost sm" data-act="scan">""","""<button class="btn ghost sm" data-act="scan" style="flex:none;min-width:88px;white-space:nowrap">""")
R("""<div><span class="mu">${L('推荐来源','Referred by')}</span><span>${CL()}</span></div>""","")
R("""<button class="btn" data-go="consent">${L('就是这家，继续','That’s my clinic, continue')}</button>""","""<button class="btn" data-act="tolinkc">${L('就是这家，继续','That’s my clinic, continue')}</button>""")
R("scan(){S.code='BFC-0317';S.codeOk=true;render()},","scan(){S.code='BFC-1003';S.codeOk=true;render()},")
R("verify(){const el=$('#code');S.code=(el&&el.value||'BFC-0317').toUpperCase()||'BFC-0317';S.codeOk=true;S.care='linked';render()},","verify(){const el=$('#code');S.code=((el&&el.value.trim())||'BFC-1003').toUpperCase();S.codeOk=true;render()},\n    tolinkc(){go('linkc')},")
# 4 delete consent page + actions
i=s.index("P.consent=()=>");j=s.index("P.pair=()=>")
s=s[:i]+s[j:]
R("    cons(){S.consent[v]=S.consent[v]?0:1;render()},\n","")
R("    consentok(){S.care='linked';go('pair')},\n","")
R("const ONB=['splash','welcome','login','join','consent','pair','checkout'];","const ONB=['splash','welcome','login','join','linkc','pair','checkout'];")
R("['consent',L('同意书','Consent')]","['linkc',L('确认诊所','Confirm clinic')]")
# linkc
R("P.linkc=()=>{const c=S.lk||(S.lk={a:0});return{","P.linkc=()=>{return{")
R("""${li('gauge',L('读数超过医生定的线会通知护士','Readings past your doctor’s limits alert the nurse'),L('血压、夜间血氧','Blood pressure, overnight oxygen'),null,null,{c:'care'})}""",
  """${li('gauge',L('血压计、心电卡的读数超过医生定的线，会通知护士','BP monitor and ECG card readings past your doctor’s limits alert the nurse'),L('戒指的睡眠、夜间血氧供护士参考','Ring sleep and overnight oxygen are for your nurse’s reference'),null,null,{c:'care'})}""")
R("""${li('ecg',L('心电由医生判读','A doctor reads every ECG'),L('App 自己不下结论','The app never interprets it'),null,null,{c:'care'})}
  </div></div>""","""${li('ecg',L('心电由医生判读','A doctor reads every ECG'),L('App 自己不下结论','The app never interprets it'),null,null,{c:'care'})}
   ${li('shield',L('周日和公众假期由荷汀护士代看告警','Otio nurses cover alerts on Sundays and public holidays'),L('诊所不开门时','When your clinic is closed'),null,null,{c:'care'})}
  </div></div>""")
i=s.index('<button class="chk" role="checkbox" aria-checked="${!!c.a}" data-act="lkchk">');j=s.index('</button>',i)+len('</button>')
s=s[:i]+"""<p class="sm mu" style="margin:0">${L('点下面的按钮，即表示你同意按新加坡《个人数据保护法》（PDPA）把上述数据分享给 '+CL()+'，可以随时撤回。','By tapping below, you agree to share the data above with '+CL()+' under Singapore’s PDPA. You can withdraw at any time.')}</p>"""+s[j:]
R("""<button class="btn" data-act="linkdo" ${c.a?'':'disabled'}>""","""<button class="btn" data-act="linkdo">""")
R("    lkchk(){S.lk.a=S.lk.a?0:1;render()},\n","")
R("relink(){const el=document.getElementById('code2');S.code=(el&&el.value.trim().toUpperCase())||'BFC-1003';S.lk={a:0};S.stack.push('linkc');render(true)},","relink(){const el=document.getElementById('code2');S.code=(el&&el.value.trim().toUpperCase())||'BFC-1003';S.stack.push('linkc');render(true)},")
# 5 flow: agree -> pair -> checkout -> paid
R("linkdo(){S.care='linked';S.stack=['care'];toast(L('欢迎加入 Otio Care · '+CL(),'Welcome to Otio Care · '+CL()));render(true);buildPanel()},","linkdo(){S.joining=true;go('pair')},")
R("paid(){toast(L('已支付，欢迎加入 '+CL(),'Paid. Welcome to '+CL()));S.stack=['today'];render(true)},","paid(){S.joining=false;S.care='linked';S.stack=['care'];toast(L('欢迎加入 Otio Care · '+CL(),'Welcome to Otio Care · '+CL()));render(true);buildPanel()},")
R("solo(){S.care='solo';go('pair')},","solo(){S.care='solo';S.joining=false;go('pair')},")
# 6 pair
R("P.pair=()=>{const p=S.paired;","P.pair=()=>{const p=S.paired,lk=linked()||S.joining;")
R("""<p class="p mu">${linked()?L('医生的计划需要心电卡和血压计。打开设备，靠近手机。','Your plan uses the ECG card and the BP monitor. Switch them on and hold them near your phone.'):L('戒指或手环就够了；有血压计、心电卡也可以连。','Your ring or band is enough. You can add a BP monitor or ECG card too.')}</p>""",
  """<p class="p mu">${lk?L('医生的计划需要心电卡和血压计。打开设备，靠近手机。','Your plan uses the ECG card and the BP monitor. Switch them on and hold them near your phone.'):L('戒指或手环就够了。','Your ring or band is all you need.')}</p>""")
R("""   ${item('ecg','ecg',L('心电卡 MD100C','ECG card MD100C'),linked()?L('诊所借给你 · SN-52018','On loan from your clinic · SN-52018'):L('蓝牙','Bluetooth'),L('连接','Pair'))}
   ${item('bp','gauge',L('上臂式血压计','Upper-arm BP monitor'),L('蓝牙','Bluetooth'),L('连接','Pair'))}
   ${item('cgm','drop',L('Sinocare 连续血糖仪','Sinocare CGM'),L('登录 Sinocare 账号关联，读数由厂商云端直接传来','Sign in to your Sinocare account; readings come straight from Sinocare’s cloud'),L('关联','Link'))}
  </div>
  <p class="sm mu">${L('手机的“健康”/Health Connect 里的步数也可以同步，在“我的 › 设备与数据来源”里开。','You can also sync steps from Apple Health or Health Connect in Me › Devices.')}</p>
  <button class="btn" data-go="${linked()?'checkout':'today'}">""",
"""   ${lk?item('ecg','ecg',L('心电卡 MD100C','ECG card MD100C'),L('诊所借给你 · SN-52018','On loan from your clinic · SN-52018'),L('连接','Pair'))+item('bp','gauge',L('上臂式血压计','Upper-arm BP monitor'),L('蓝牙','Bluetooth'),L('连接','Pair')):''}
  </div>
  ${lk?'':`<p class="sm mu">${L('有血压计？以后在“我的 › 设备”里加。','Have a BP monitor? Add it later in Me › Devices.')}</p>`}
  <button class="btn" data-go="${lk?'checkout':'today'}">""")
# 7 connect
i=s.index("""  <div class="h2">${L('附近的合作机构','Partners near you')}</div>""");j=s.index("</div>\n",s.index('<div class="card flush">',i))+len("</div>\n")
s=s[:i]+"""  <p class="sm mu" style="margin:0">${L('还没有护理码？问你的家庭医生。','No care code? Ask your family doctor.')}</p>\n"""+s[j:]
# 8 billCard dup subtotal
R("""  <div><span>${L('心律监测计划','Heart rhythm plan')}</span><span class="num">S$39.00</span></div>
  <div class="sub">""","""  <div class="sub">""")
# 9 withdraw
R("""${li('ring',L('你的戒指数据都留着','All your ring data stays with you'),""","""${li('ecg',L('心电卡请交还诊所','Please return the ECG card'),L('交回 '+CL(),'To '+CL()),null,null,{c:'care'})}${li('ring',L('你的戒指数据都留着','All your ring data stays with you'),""")
open(p,'w',encoding='utf-8').write(s); print('ok')
