const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1300,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(800);await p.click('#ctl-lang [data-v="zh"]');await p.click('#ctl-care [data-v="solo"]');await p.click('.tab[data-tab="today"]');await p.waitForTimeout(300);
const line=()=>p.$eval('.app',e=>{const l=e.querySelector('.sline');return l?l.innerText.replace(/\s+/g,' '):'(none)'});
console.log('morning:',await line());await p.click('.sline [data-act="qoff"]');await p.waitForTimeout(200);console.log('after x:',await line(),'ack=',await p.evaluate(()=>__t.S.ntAck));
await p.click('#ctl-tm [data-v="afternoon"]');await p.waitForTimeout(200);console.log('afternoon:',await line());
await p.click('#ctl-nt [data-v="none"]');await p.click('#ctl-tm [data-v="morning"]');await p.waitForTimeout(200);console.log('morning no note:',await line());
await p.click('#ctl-scen [data-v="night"]');await p.evaluate(()=>{__t.S.own.ecg=false;__t.render(true)});await p.waitForTimeout(200);console.log('alert:',await line(),'x?',await p.$('.sline [data-act="qoff"]')!==null);
console.log(JSON.stringify(errs));await b.close()})();
