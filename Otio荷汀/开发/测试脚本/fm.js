const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1300,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(1000);await p.click('#ctl-lang [data-v="zh"]');await p.click('#ctl-care [data-v="solo"]');await p.click('.tab[data-tab="family"]');await p.waitForTimeout(300);
await p.screenshot({path:'f1.png',clip:{x:640,y:40,width:400,height:840}});
await p.click('.app [data-act="famsafe"]');await p.waitForTimeout(200);
await p.click('.app [data-go="famshare"] .nm');await p.waitForTimeout(300);await p.click('.app [data-act="fam"][data-v="sl"]').catch(e=>errs.push('nosw'));await p.waitForTimeout(200);await p.screenshot({path:'f2.png',clip:{x:640,y:40,width:400,height:840}});
await p.click('.app [data-act="fampreview"]');await p.waitForTimeout(300);await p.screenshot({path:'f3.png',clip:{x:640,y:40,width:400,height:840}});
await p.click('[data-act="sheetclose"]');await p.click('.app [data-act="back"]');await p.waitForTimeout(200);await p.click('.app [data-go="famw"] .nm');await p.waitForTimeout(300);await p.screenshot({path:'f4.png',clip:{x:640,y:40,width:400,height:840}});
console.log(errs);await b.close()})();
