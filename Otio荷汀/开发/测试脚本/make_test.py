"""把原型复制成测试版：在最后一个 })(); 前注入 window.__t，测试脚本靠它切状态。
用法：python3 make_test.py <原型.html> <输出.html>"""
import sys
s = open(sys.argv[1], encoding='utf-8').read()
i = s.rfind('})();')
open(sys.argv[2], 'w', encoding='utf-8').write(s[:i] + 'window.__t={get S(){return S},go,render,tband,tseries};' + s[i:])
