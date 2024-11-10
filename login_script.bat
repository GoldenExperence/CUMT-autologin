@echo off
chcp 65001 > nul
echo CUMT校园网自动连接脚本启动，按Ctrl + C 终止
cd /d "D:\SeeYoung\Documents\python\projects\autoLogin\autoLogin" 
python login.py >> log.txt