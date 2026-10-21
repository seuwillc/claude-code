const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1300,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(1000);await p.click('#ctl-lang [data-v="zh"]');await p.click('#ctl-care [data-v="solo"]');await p.click('.tab[data-tab="today"]');await p.waitForTimeout(300);
const sh=async n=>{await p.waitForTimeout(350);await p.screenshot({path:`otiagen/nt-${n}.png`,clip:{x:640,y:40,width:400,height:840}})};
await sh(1);await p.click('[data-act="ntack"]');await p.waitForTimeout(2300);await sh(2);
await p.evaluate(()=>{__t.go('famw')});await sh(3);await p.click('[data-act="famhi"]');await p.waitForTimeout(2300);await sh(4);
await p.evaluate(()=>{__t.go('famshare')});await p.click('[data-act="famnote"]');await p.fill('#ntin','下周三复诊，陪我去');await sh(5);await p.click('[data-act="famnotesend"]');await p.waitForTimeout(2300);await p.$eval('#scroll',e=>e.scrollTop=400);await sh(6);
await p.click('[data-act="fampreview"]');await sh(7);
console.log(JSON.stringify(errs));await b.close()})();
