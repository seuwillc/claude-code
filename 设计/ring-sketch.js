// ring(id, metal, win) -> svg string. 3/4 view, front window centred on the band
const METAL={
 gold:['#7A4E25','#C08A4C','#F3D6A0','#D9A866','#8A5A2B'],
 xuan:['#0E0E10','#2E2E33','#77777F','#3A3A3F','#141416'],
 moon:['#7E868C','#B8C0C6','#F6F8FA','#D4DADF','#8E979E']};
function ring(id,m,win,o={}){const W=300,H=200,cx=W/2,cy=78,rx=118,ry=40,B=36,t=11,M=METAL[m];
 const g=(n,st)=>`<linearGradient id="${id}${n}" x1="0" x2="1" y1="0" y2="0">${st.map(([o,c])=>`<stop offset="${o}" stop-color="${c}"/>`).join('')}</linearGradient>`;
 const band=g('b',[[0,M[0]],[.18,M[1]],[.36,M[2]],[.52,M[3]],[.78,M[1]],[1,M[4]]]);
 const rim=g('r',[[0,M[1]],[.3,M[2]],[.7,M[3]],[1,M[1]]]);
 const inn=g('i',[[0,M[4]],[.5,M[1]],[1,M[0]]]);
 const wx=cx,wy=cy+ry+B/2-1,ww=16,wh=26;
 const W_={
  lotus:`<radialGradient id="${id}w" cx=".45" cy=".35" r=".8"><stop offset="0" stop-color="#BFE4E6"/><stop offset=".35" stop-color="#5FA3AE"/><stop offset="1" stop-color="#1F5A66"/></radialGradient>`,
  leaf:`<radialGradient id="${id}w" cx=".45" cy=".3" r=".9"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".6" stop-color="#EEE9DD"/><stop offset="1" stop-color="#CFC8B8"/></radialGradient>`,
  celadon:`<radialGradient id="${id}w" cx=".4" cy=".3" r=".9"><stop offset="0" stop-color="#D6E6D8"/><stop offset=".6" stop-color="#A9C7B0"/><stop offset="1" stop-color="#7FA48A"/></radialGradient>`}[win];
 const cap=`M${wx} ${wy-wh/2} a${ww/2} ${ww/2} 0 0 1 ${ww/2} ${ww/2} v${wh-ww} a${ww/2} ${ww/2} 0 0 1 ${-ww} 0 v${-(wh-ww)} a${ww/2} ${ww/2} 0 0 1 ${ww/2} ${-ww/2}z`;
 let deco='';
 if(win==='lotus'){const r=[[-3,-6,.9],[2,-2,.7],[-1,4,.7],[3,7,.5],[-3,1,.5]];deco=r.map(([x,y,s])=>`<circle cx="${wx+x}" cy="${wy+y}" r="${s}" fill="#fff" opacity=".85"/>`).join('')}
 if(win==='leaf'){deco=`<g stroke="#9C8E6E" stroke-width=".6" fill="none" opacity=".75"><path d="M${wx} ${wy+10} V${wy-10}"/>${[-8,-3,2,7].map((y,i)=>`<path d="M${wx} ${wy+y+2} q-4 -2 -6 -5"/><path d="M${wx} ${wy+y+2} q4 -2 6 -5"/>`).join('')}</g>`}
 if(win==='celadon'){deco=`<g stroke="#6E8F78" stroke-width=".45" fill="none" opacity=".6"><path d="M${wx-7} ${wy-4} l5 2 l3 -4 l4 3"/><path d="M${wx-2} ${wy-2} l-1 6 l5 3"/><path d="M${wx+3} ${wy-6} l2 7 l-4 6"/></g>`}
 return `<svg viewBox="0 0 ${W} ${H}" width="${o.w||W}" height="${(o.w||W)*H/W}" xmlns="http://www.w3.org/2000/svg"><defs>${band}${rim}${inn}${W_}
  <clipPath id="${id}hole"><ellipse cx="${cx}" cy="${cy}" rx="${rx-t}" ry="${ry-t*.32}"/></clipPath>
  <radialGradient id="${id}sh"><stop offset="0" stop-color="#000" stop-opacity=".18"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient></defs>
  <ellipse cx="${cx}" cy="${cy+B+ry+16}" rx="${rx*1.02}" ry="12" fill="url(#${id}sh)"/>
  <path d="M${cx-rx} ${cy} A${rx} ${ry} 0 0 0 ${cx+rx} ${cy} V${cy+B} A${rx} ${ry} 0 0 1 ${cx-rx} ${cy+B} Z" fill="url(#${id}b)"/>
  <path d="M${cx-rx+2} ${cy+B-3} A${rx-2} ${ry-1} 0 0 0 ${cx+rx-2} ${cy+B-3}" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="1.2"/>
  <ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="url(#${id}r)"/>
  <g clip-path="url(#${id}hole)"><rect x="0" y="0" width="${W}" height="${H}" fill="url(#${id}i)"/><ellipse cx="${cx}" cy="${cy+B}" rx="${rx-t}" ry="${ry-t*.32}" fill="var(--bg,#F3F1EC)"/>
   <path d="M${cx-rx+t} ${cy+B} A${rx-t} ${ry-t*.32} 0 0 1 ${cx+rx-t} ${cy+B}" fill="none" stroke="#000" stroke-opacity=".12" stroke-width="2"/></g>
  <ellipse cx="${cx}" cy="${cy}" rx="${rx-t}" ry="${ry-t*.32}" fill="none" stroke="#fff" stroke-opacity=".25"/>
  <path d="${cap}" fill="${m==='xuan'?'#2a2a2e':'#00000022'}" transform="translate(0 1.2)"/>
  <path d="${cap}" fill="url(#${id}w)" stroke="${m==='xuan'?'#55555c':'#ffffffaa'}" stroke-width="1"/>${deco}
  <path d="M${wx-5} ${wy-9} q2 -3 6 -3" stroke="#fff" stroke-width="1.6" fill="none" stroke-linecap="round" opacity=".9"/>
 </svg>`}
if(typeof module!=='undefined')module.exports={ring,METAL};
