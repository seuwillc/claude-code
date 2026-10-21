const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1300,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(1000);await p.click('#ctl-lang [data-v="zh"]');await p.click('#ctl-care [data-v="solo"]');await p.click('.tab[data-tab="today"]');await p.waitForTimeout(300);
const sh=async f=>{await p.$eval('#scroll',e=>e.scrollTop=330);await p.waitForTimeout(150);await p.screenshot({path:f,clip:{x:640,y:40,width:400,height:840}})};
await sh('d1.png');
await p.click('#ctl-scen [data-v="night"]');await p.waitForTimeout(300);await p.click('.tab[data-tab="today"]').catch(()=>{});await p.waitForTimeout(300);await sh('d2.png');
await p.click('#ctl-scen [data-v="bp"]');await p.waitForTimeout(300);await p.click('.tab[data-tab="today"]').catch(()=>{});await p.waitForTimeout(300);await sh('d3.png');
await p.click('#ctl-scen [data-v="normal"]');await p.click('#ctl-tm [data-v="night"]');await p.waitForTimeout(300);await p.click('.tab[data-tab="today"]').catch(()=>{});await p.waitForTimeout(300);await sh('d4.png');
console.log(errs);await b.close()})();
