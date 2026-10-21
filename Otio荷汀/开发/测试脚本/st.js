const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1300,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(1000);await p.click('#ctl-lang [data-v="zh"]');await p.click('#ctl-care [data-v="solo"]');await p.click('.tab[data-tab="today"]');await p.waitForTimeout(300);
const full=async n=>{const H=await p.$eval('#scroll',e=>e.scrollHeight);let i=0;for(let y=0;y<H;y+=700){await p.$eval('#scroll',(e,y)=>e.scrollTop=y,y);await p.waitForTimeout(150);await p.screenshot({path:`st-${n}-${i++}.png`,clip:{x:640,y:40,width:400,height:840}})}};
await full('m');
await p.click('#ctl-tm [data-v="afternoon"]');await p.waitForTimeout(300);await full('a');
await p.click('#ctl-tm [data-v="night"]');await p.waitForTimeout(300);await full('n');
await p.click('#ctl-tm [data-v="morning"]');await p.click('#ctl-scen [data-v="night"]');await p.waitForTimeout(300);await p.evaluate(()=>{__t.S.stack=['today'];__t.render(true)});await p.waitForTimeout(300);await full('o');
await p.evaluate(()=>{__t.S.scen='normal';__t.S.own.thermo=true;__t.S.temp={v:38.4,at:1};__t.S.cgm=true;__t.S.cgmDay=13;__t.S.stack=['today'];__t.render(true)});await p.waitForTimeout(300);await full('f');
console.log(errs);await b.close()})();
