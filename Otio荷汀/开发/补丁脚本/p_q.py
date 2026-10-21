p='sgtob/vera-care-sg.html';s=open(p).read()
def R(a,b,n=1):
    global s;assert s.count(a)==n,(s.count(a),a[:70]);s=s.replace(a,b)
R("""'Heart rate a little higher than usual. Breathe with the lotus for a minute?'),'breath:1']);
 const n=(S.qOff&&typeof S.qOff==='object'?S.qOff[S.tm]:0)||0,q=Q[n];if(!q)return '';""",
"""'Heart rate a little higher than usual. Breathe with the lotus for a minute?'),'breath:1','alert']);
 /* one line per time slot, highest priority first: body alert > family note > weather > season/Zhuangzi. × hides it until the next slot; resets daily. Body alerts have no × */
 const q=Q[0];if(!q||(q[3]!=='alert'&&S.qOff&&S.qOff[S.tm]))return '';""")
R("""<button class="link" data-act="qoff" aria-label="${L('换一句','Next')}" style="min-height:0;padding:0 4px;color:var(--mu)">×</button></div>`}""",
  """${q[3]==='alert'?'':`<button class="link" data-act="qoff" data-v="${q[3]||''}" aria-label="${L('今天先不看','Hide for now')}" style="min-height:0;padding:0 4px;color:var(--mu)">×</button>`}</div>`}""")
R("""    qoff(){const k=S.tm;S.qOff=S.qOff&&typeof S.qOff==='object'?S.qOff:{};S.qOff[k]=(S.qOff[k]||0)+1;render()},""",
  """    qoff(){S.qOff=S.qOff&&typeof S.qOff==='object'?S.qOff:{};S.qOff[S.tm]=1;if(v==='note')S.ntAck=true;render()},""")
R("""seg('ctl-nt','nt',[['hm',L('慧敏捎来一句','Note from Hui Min')],['none',L('没有','None')]],()=>{S.ntAck=false});""",
  """seg('ctl-nt','nt',[['hm',L('慧敏捎来一句','Note from Hui Min')],['none',L('没有','None')]],()=>{S.ntAck=false;S.qOff={}});""")
open(p,'w').write(s)
