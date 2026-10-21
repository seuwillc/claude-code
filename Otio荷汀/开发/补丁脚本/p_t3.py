p='sgtob/vera-care-sg.html';s=open(p).read()
def R(a,b,n=1):
    global s;assert s.count(a)==n,(s.count(a),a[:60]);s=s.replace(a,b)
R("L('外面下着雨，适合在家泡杯茶。','Rain outside: a good time for a pot of tea.')","L('午后下雨，慢一点，不赶。','Rain this afternoon. Take it slow, no rush.')")
R("if(S.scen==='night'&&S.tm!=='night')Q.unshift(","if(S.scen==='night'&&S.tm!=='night'&&!(linked()||S.own.ecg))Q.unshift(")
R("$('#p-chg').innerHTML=L('<b>v3.8.26</b>","$('#p-chg').innerHTML=L('<b>v3.8.27</b>：首页午后一句改成“午后下雨，慢一点，不赶。”，不再假设人在家；夜间血氧偏低那天只提一件事：有心电卡时只留“记录 30 秒心电”，今日一句换成普通的一句；没有心电卡时才出现荷花呼吸。<br><b>v3.8.26</b>")
R("   '<b>v3.8.26</b>: Family","   '<b>v3.8.27</b>: Today’s afternoon line is now “Rain this afternoon. Take it slow, no rush.” and no longer assumes you are home. On an oxygen-dip day Today asks for one thing only: with an ECG card, just the 30-second ECG and an ordinary line; the lotus breath appears only without a card.<br><b>v3.8.26</b>: Family")
open(p,'w').write(s)
