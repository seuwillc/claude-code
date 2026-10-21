import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
R("focus:'walk',fday:16,grad:[],","focus:'walk',fday:16,grad:[],more:false,cu:{anc:'bf',what:'',tiny:''},")
i=s.index("const FOC=()=>");j=s.index("const isDone=")
s=s[:i]+r"""/* every habit is the same shape: a cue (after what), one small action, a fallback, and how it is recorded */
const ANC=()=>{const m=MP();return {wake:[L('起床后','After waking'),mpS(mpT(m.wake)+.1)],bf:[L('早饭后','After breakfast'),mpS(mpT(m.wake)+1)],lunch:[L('午饭后','After lunch'),'13:00'],dinner:[L('晚饭后','After dinner'),'19:00'],bed:[L('睡前','Before bed'),mpS(mpT(m.bed)-.5)]}};
const HREC=['walk','wake','phone'],HMORE=['water','stretch','veg','call'];
const CUBAD=/药|停药|减药|断食|禁食|节食|不吃饭|medic|pill|dose|fast/i;
const FOC=()=>{const m=MP(),mn=+m.min,am=m.when==='morning',A=ANC(),cu=m.cu,ca=A[cu.anc]||A.bf;return {
 walk:{t:L((am?'早饭后':'晚饭后')+'快走 '+mn+' 分钟','Brisk walk for '+mn+' min after '+(am?'breakfast':'dinner')),s:L('约 '+(mn*100).toLocaleString('en-US')+' 步 · 有点喘、还能说话','About '+(mn*100).toLocaleString('en-US')+' steps · a little out of breath, still able to talk'),at:am?A.bf[1]:'19:00',auto:1,wk:[1,.5]},
 wake:{t:L('每天 '+m.wake+' 起床，周末也一样','Up at '+m.wake+' every day, weekends too'),s:L('前后半小时内都算 · 戒指自动记下','Within half an hour counts · the ring records it'),at:m.wake,auto:1,wk:[1,1]},
 phone:{t:L(mpS(mpT(m.bed)-.75)+' 放下手机，调暗灯光','Phone down, lights low at '+mpS(mpT(m.bed)-.75)),a:L('放下手机，调暗灯光','Phone down, lights low'),s:L('手机放到卧室外面充电','Charge it outside the bedroom'),at:mpS(mpT(m.bed)-.75),wk:[1,0]},
 water:{t:L('起床后先喝一杯温水','A glass of warm water after waking'),a:L('喝一杯温水','A glass of warm water'),s:L('睡前把杯子放在床头','Leave a cup by the bed the night before'),at:A.wake[1],wk:[1,1]},
 stretch:{t:L('午饭后拉伸 5 分钟','Stretch for 5 min after lunch'),a:L('拉伸 5 分钟','Stretch, 5 min'),s:L('扶着椅背慢慢来，不痛为度','Hold a chair back, go slowly, stop before it hurts'),at:A.lunch[1],wk:[1,1]},
 veg:{t:L('晚饭先吃一碗菜','Start dinner with a bowl of vegetables'),a:L('先吃一碗菜','Vegetables first'),s:L('先吃菜，再吃饭和肉','Vegetables first, then rice and meat'),at:'18:30',wk:[1,1]},
 call:{t:L('下午 4 点给亲友打个电话','Call family or a friend at 4 pm'),a:L('给亲友打个电话','Call family or a friend'),s:L('聊几分钟就好','A few minutes is enough'),at:'16:00',wk:[1,1]},
 custom:{t:cu.what?ca[0]+L('，','')+' '+cu.what:L('自己写一个','Write your own'),a:cu.what||L('我的小习惯','My habit'),s:cu.tiny?L('不想做时，至少'+cu.tiny,'On off days, at least: '+cu.tiny):L('做完点一下','Tap when done'),at:ca[1],wk:[0,0]}}};
"""+s[j:]
R(" if(on('phone'))out.push({id:'phone',t:F.phone.at,k:'hab',a:L('放下手机，调暗灯光','Phone down, lights low'),b:F.phone.s});",
  " for(const k of [m.focus,...m.grad])if(k!=='wake'&&k!=='walk'&&F[k])out.push({id:k,t:F[k].at,k:'hab',a:F[k].a,b:F[k].s});")
# step 2
i=s.index(":st===2?`<h1 class=\"h1\" style=\"font-size:26px\">${L('先养成哪一个？'");j=s.index(":`<h1 class=\"h1\" style=\"font-size:26px\">${L('怎么提醒你？'")
s=s[:i]+r""":st===2?`<h1 class="h1" style="font-size:26px">${L('先养成哪一个？','Which habit first?')}</h1><p class="p mu">${L('一次只养成一个。','One at a time.')}</p>${(()=>{const opt=k=>{const f=F[k],on=m.focus===k;return `<button class="fopt ${on?'on':''}" data-act="mpfocus" data-v="${k}"><span class="rd"></span><span><b>${f.t}</b><small>${f.s}</small></span></button>`};
  const walkX=`<div class="stack" style="gap:10px;padding:0 4px 6px"><div class="h3">${L('接在哪件事后面','Right after')}</div><div class="mpchips" style="margin-top:0">${ch('when','morning',L('早饭后','Breakfast'))}${ch('when','evening',L('晚饭后','Dinner'))}</div>${msl()}<p class="sm mu" style="margin:0">${L('下雨或太热，就在组屋走廊、商场或家里走。','If it rains or it’s too hot, walk the HDB corridor, a mall or at home.')}</p></div>`;
  const A=ANC(),cu=m.cu,ip='font:inherit;font-size:17px;padding:12px 14px;border-radius:14px;border:1px solid var(--line);background:var(--sf);color:var(--tx);width:100%;box-sizing:border-box';
  const cuX=`<div class="stack" style="gap:10px;padding:0 4px 6px"><div class="h3">${L('接在哪件事后面','Right after')}</div><div class="mpchips" style="margin-top:0">${Object.keys(A).map(a=>`<button class="mpchip ${cu.anc===a?'on':''}" data-act="mpcu" data-v="${a}">${A[a][0]}</button>`).join('')}</div><div class="h3">${L('我会……','I will…')}</div><input id="cu-what" maxlength="20" value="${cu.what.replace(/"/g,'&quot;')}" placeholder="${L('比如：靠墙站 2 分钟','e.g. Stand against the wall for 2 min')}" style="${ip}" aria-label="${L('我会','I will')}"><div class="h3">${L('不想做时，至少……（可不填）','On off days, at least… (optional)')}</div><input id="cu-tiny" maxlength="16" value="${cu.tiny.replace(/"/g,'&quot;')}" placeholder="${L('比如：站 30 秒','e.g. 30 seconds')}" style="${ip}" aria-label="${L('最少版本','Smallest version')}"><div class="sm" id="cu-warn" style="color:var(--tLow);${CUBAD.test(cu.what)?'':'display:none'}">${L('和吃药、节食有关的，请先问医生。吃药提醒在下一步设。','Anything about medicines or dieting: ask your doctor first. Medicine reminders are in the next step.')}</div><p class="sm mu" style="margin:0">${L('写一件小到不用下决心、做完就能打勾的事。','Pick something small enough to need no willpower, and clear enough to tick off.')}</p></div>`;
  const list=HREC.concat(HMORE.includes(m.focus)&&!m.more?[m.focus]:[]);
  return list.map(k=>opt(k)+(k==='walk'&&m.focus==='walk'?walkX:'')).join('')
   +(m.more?HMORE.map(opt).join(''):'')
   +`<button class="link" data-act="mpmore" style="text-align:left;font-size:15px">${m.more?L('收起','Show fewer'):L('更多习惯 ›','More habits ›')}</button>`
   +opt('custom')+(m.focus==='custom'?cuX:'')})()}<p class="sm mu">${L('时间跟着你的作息走。做稳了，我们再问你要不要开始下一个。','Times follow your routine. Once it’s steady, we’ll ask about the next one.')}</p>`
 """+s[j:]
R("return{calm:1,after(){const ms=document.querySelector('[data-msl]');","return{calm:1,after(){const cw=document.getElementById('cu-what'),ct=document.getElementById('cu-tiny');if(cw)cw.oninput=()=>{MP().cu.what=cw.value.trim();const w=document.getElementById('cu-warn');if(w)w.style.display=CUBAD.test(cw.value)?'':'none'};if(ct)ct.oninput=()=>{MP().cu.tiny=ct.value.trim()};const ms=document.querySelector('[data-msl]');")
R("    mpchg(){","    mpmore(){MP().more=!MP().more;render()},\n    mpcu(){MP().cu.anc=v;render()},\n    mpchg(){")
R("mpstep(){const m=MP();m.step=","mpstep(){const m=MP();if(m.step===2&&+v>0&&m.focus==='custom'&&(!m.cu.what||CUBAD.test(m.cu.what))){toast(m.cu.what?L('这一条请先问医生','Please check this one with your doctor first'):L('写下你要做的那件小事','Write the small thing you’ll do'));return}m.step=")
R("L('<b>v3.6</b>：","L('<b>v3.7</b>：习惯可以换成别的。每个习惯都是同一个结构：接在哪件事后面、做一件小事、不想做时的最少版本、怎么记录；界面按这个结构生成，所以卡片、时间线、周环对任何习惯都一样。默认推荐 3 个，“更多习惯”里有 4 个（起床喝水、午饭后拉伸、晚饭先吃菜、下午给亲友打电话），也可以“自己写一个”：选接在哪件事后面，写“我会……”和“至少……”。涉及吃药、节食的会提示先问医生，不能保存。<br><b>v3.6</b>：")
R("'<b>v3.6</b>: My habits","'<b>v3.7</b>: Any habit. Every habit has the same shape (a cue, one small action, a smallest version, how it is recorded) and the UI is generated from it, so the card, timeline and rings work for any habit. Three recommended, four more under More habits (water on waking, stretch after lunch, vegetables first, a 4 pm call), or Write your own: pick the cue, write I will… and At least…. Anything about medicines or dieting asks you to check with your doctor and can’t be saved.<br><b>v3.6</b>: My habits")
open(p,'w',encoding='utf-8').write(s); print('ok')
