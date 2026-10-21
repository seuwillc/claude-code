p='sgtob/vera-care-sg.html';s=open(p).read()
def R(a,b,n=1):
    global s;assert s.count(a)==n,(s.count(a),a[:70]);s=s.replace(a,b)
# remove wave strokes
R("""  for(let i=0;i<7;i++){const y=hz+8+i*i*7.5;s+=`<path d="M${(r()*120).toFixed(0)} ${y} h${(80+r()*180).toFixed(0)}" stroke="${dk?'#F5E6C0':'#FFFFFF'}" stroke-opacity="${dk?.1:.28}" stroke-width="${(1+i*.25).toFixed(1)}" stroke-linecap="round"/>`}
""","")
# boat reflection instead of white line
R("""<path d="M-26 6 h56" stroke="${dk?'#F5E6C0':'#fff'}" stroke-opacity=".35"/></g>`;""",
  """</g><g transform="translate(300 ${hz+238}) scale(1 -1)" fill="${ink}" opacity="${dk?.16:.1}" filter="url(#ffar)"><path d="M-22 0 Q0 5 24 0 L20 -3 L-18 -3Z"/><path d="M-6 -3 v-7 h12 v7" fill="none" stroke="${ink}" stroke-width="1"/></g>`;""")
# rain tree only on Today
R("""  s+=`<g filter="url(#fink)" opacity="${dk?.6:.16}"><path d="M40""","""  if(today)s+=`<g filter="url(#fink)" opacity="${dk?.6:.16}"><path d="M40""")
# frangipani lower, clear of battery chip
R("""s+=`<g opacity="${dk?.75:1}" transform="translate(0 46)">""","""s+=`<g opacity="${dk?.75:1}" transform="translate(8 92)">""")
open(p,'w').write(s)
