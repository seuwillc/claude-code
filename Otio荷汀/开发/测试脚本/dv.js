const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1300,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(1000);await p.click('#ctl-lang [data-v="zh"]');await p.click('#ctl-care [data-v="solo"]');
const g=async(id,f,y=0)=>{await p.evaluate(i=>{__t.S.stack=["me"];__t.go(i)},id);await p.waitForTimeout(250);await p.$eval('#scroll',(e,y)=>e.scrollTop=y,y);await p.waitForTimeout(120);await p.screenshot({path:f,clip:{x:640,y:40,width:400,height:840}})};
await g('devices','v1.png');await g('store','v2.png');
await p.click('.app [data-act="devconn"][data-v="thermo"]');await p.click('.app [data-act="devconn"][data-v="cgm"]');await p.waitForTimeout(200);
await p.evaluate(()=>{__t.S.stack=['health'];__t.render(true)});await p.waitForTimeout(300);await p.$eval('#scroll',e=>e.scrollTop=900);await p.waitForTimeout(150);await p.screenshot({path:'v3.png',clip:{x:640,y:40,width:400,height:840}});
await g('thermo','v4.png');await p.click('.app [data-act="tempnow"]');await p.waitForTimeout(200);await p.screenshot({path:'v5.png',clip:{x:640,y:40,width:400,height:840}});
console.log(errs);await b.close()})();
