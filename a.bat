@echo off
cd /d "%~dp0"

set "NIC=以太网 3"
set "PY_FILE=main.py"

echo [正在检测] 网卡 "%NIC%" 的可见性...

ipconfig | findstr /C:"%NIC%" >nul

if %errorlevel% EQU 0 (
    goto ActionDisable
) else (
    goto ActionEnable
)

:ActionDisable
    netsh interface set interface "%NIC%" admin=disable
    echo [完成] 网卡已禁用。
    goto End

:ActionEnable
    netsh interface set interface "%NIC%" admin=enable
    echo [等待] 正在初始化网络 (等待5秒)...
    timeout /t 5 /nobreak >nul
    
    echo [执行] 正在运行 Python 脚本...
    python "%PY_FILE%"
    goto End

:End
    echo.
    echo 脚本执行结束