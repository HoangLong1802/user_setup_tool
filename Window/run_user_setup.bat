@echo off
REM Usage: run_user_setup.bat <username> <department>

if "%~1"=="" (
    echo Usage: %~nx0 ^<username^> ^<department^>
    goto :eof
)
if "%~2"=="" (
    echo Usage: %~nx0 ^<username^> ^<department^>
    goto :eof
)

set "USERNAME=%~1"
set "DEPARTMENT=%~2"
set "LOGFILE=%~dp0user_creation_log.csv"

REM 1) Cài đặt công cụ cơ bản: Chrome và mos bằng Chocolatey
choco install googlechrome -y
choco install mos -y

REM 2) Tạo user local và gán vào nhóm phòng ban (nếu cần tạo nhóm)
net localgroup "%DEPARTMENT%" >nul 2>&1 || (
    net localgroup "%DEPARTMENT%" /add
)
net user "%USERNAME%" /add
net localgroup "%DEPARTMENT%" "%USERNAME%" /add

REM 3) Ghi log: username,timestamp,department
for /f "tokens=1-3 delims=/:. " %%a in ("%date% %time%") do (
    set "LOGTIME=%%c-%%b-%%a %%d:%%e:%%f"
)
if not exist "%LOGFILE%" (
    echo username,timestamp,department>"%LOGFILE%"
)
echo %USERNAME%,%LOGTIME%,%DEPARTMENT%>>"%LOGFILE%"

echo Da tao user "%USERNAME%" thuoc phong "%DEPARTMENT%" va ghi log tai "%LOGFILE%".