const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1300,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(800);await p.click('#ctl-lang [data-v="zh"]');await p.click('#ctl-care [data-v="solo"]');await p.click('.tab[data-tab="today"]');
const V=[['n68','normal',null],['v45','normal',45],['v90','normal',90],['night','night',null],['bp','bp',null]];
for(const [n,sc,vd] of V){await p.evaluate(([sc,vd])=>{__t.S.scen=sc;__t.S.vitD=vd;__t.S.stack=['today'];__t.render(true)},[sc,vd]);await p.waitForTimeout(1600);await p.evaluate(()=>{document.querySelectorAll('.pushn,.push').forEach(e=>e.remove())});
 await p.screenshot({path:`otiagen/vt-${n}.png`,clip:{x:640,y:90,width:400,height:560}})}
await p.click('#ctl-viz [data-v="enso"]');await p.evaluate(()=>{__t.S.scen='night';__t.S.vitD=null;__t.render(true)});await p.waitForTimeout(800);await p.screenshot({path:`otiagen/vt-enso.png`,clip:{x:640,y:90,width:400,height:560}});
await p.click('#ctl-viz [data-v="aura"]');await p.evaluate(()=>{__t.S.scen='normal';__t.render(true)});await p.click('.vitorb');await p.waitForTimeout(400);await p.screenshot({path:`otiagen/vt-tap.png`,clip:{x:640,y:40,width:400,height:840}});
console.log(JSON.stringify(errs));await b.close()})();
