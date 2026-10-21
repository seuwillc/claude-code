#!/usr/bin/env bash
# 打开所有页面（自己用 / 连诊所 两种模式），报告脚本错误。需要 Node 和 Playwright（npm i -g playwright && npx playwright install chromium）
set -e
cd "$(dirname "$0")"
mkdir -p sw otiagen
python3 make_test.py "../../原型/新加坡版/$(ls ../../原型/新加坡版 | grep html | tail -1)" sw_test.html
NODE_PATH=$(npm root -g) node sweep.js "$PWD/sw_test.html"
