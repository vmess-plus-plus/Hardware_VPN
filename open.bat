@echo off

title Vmess++ Connect USBClient ver-Beta1.0

reg query "hklm\software\Python\pythoncore\3.7>2 nul>nul
if %errorlevel% == 0(goto client) else (echo 请安装python3.7后运行)

:while1
pause>nul
goto while1


:client
python init.py