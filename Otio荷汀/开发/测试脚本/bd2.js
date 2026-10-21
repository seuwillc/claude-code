const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1300,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(800);await p.click('#ctl-lang [data-v="zh"]');await p.click('#ctl-care [data-v="solo"]');
const sh=async(n,id,pre,scroll)=>{await p.evaluate(([id,pre])=>{if(pre)eval(pre);__t.S.stack=['today'];__t.go(id)},[id,pre]);await p.waitForTimeout(400);if(scroll)await p.$eval('#scroll',(e,y)=>e.scrollTop=y,scroll);await p.waitForTimeout(250);await p.screenshot({path:`otiagen/bd2-${n}.png`,clip:{x:640,y:40,width:400,height:840}})};
await sh('health','health',null,700);await sh('steps','trend:steps');await sh('hrv','trend:hrv',null,620);await sh('sleep','trend:sleep','__t.S.own.env=true',560);await sh('bp','bp',null,260);await sh('ecg','ecg');await sh('glu','glucose','__t.S.cgm=true');
await p.click('[data-act="mealsnap"]');await p.waitForTimeout(500);await sh('glu2','glucose');await sh('apnea','apnea');
console.log(JSON.stringify(errs));await b.close()})();
