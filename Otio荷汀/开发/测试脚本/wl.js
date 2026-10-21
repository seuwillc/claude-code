const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1300,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(1000);
for(const l of ['zh','en']){await p.click(`#ctl-lang [data-v="${l}"]`);await p.evaluate(()=>{__t.S.stack=['welcome'];__t.render(true)});await p.waitForTimeout(400);await p.screenshot({path:`otiagen/wl-${process.argv[3]||'x'}-${l}.png`,clip:{x:640,y:40,width:400,height:840}})}
console.log(JSON.stringify(errs));await b.close()})();
