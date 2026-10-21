const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1300,height:900},deviceScaleFactor:3});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(800);await p.click('#ctl-lang [data-v="zh"]');await p.click('#ctl-care [data-v="solo"]');await p.click('.tab[data-tab="today"]');
const shot=async(n,br,vd,va)=>{await p.evaluate(([br,vd,va])=>{__t.S.brush=br;__t.S.vitD=vd;__t.S.va=va;__t.render(true)},[br,vd,va]);await p.waitForTimeout(2200);await p.screenshot({path:`otiagen/a2-${n}.png`,clip:{x:650,y:150,width:200,height:200}})};
await shot('o68','v1',null,'auto');await shot('n68','v2',null,'auto');await shot('o45','v1',45,'auto');await shot('n45','v2',45,'auto');await shot('o90','v1',90,'auto');await shot('n90','v2',90,'auto');await shot('nal','v2',null,'alert');await shot('oal','v1',null,'alert');
console.log(JSON.stringify(errs));await b.close()})();
