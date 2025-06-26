@echo off
:: run_user_setup.bat
cls

echo === User Setup Tool (Windows) ===

:: Prompt for username
set /p username=Enter username: 

:: Check if user exists
net user %username% >nul 2>&1
if %errorlevel% equ 0 (
  echo User %username% already exists.
  goto end
)

:: Prompt for email & phone
set /p email=Enter email: 
set /p phone=Enter phone number: 

:: Departments list
setlocal enabledelayedexpansion
set departments=IT,HR,Accounting,Business,Telesale,Sales,Logistics,CustomerService,R&D,Marketing
for /l %%i in (1,1,10) do (
  for /f "tokens=%%i delims=," %%d in ("%departments%") do echo %%i. %%d
)
set /p idx=Select department (1-10): 
for /f "tokens=%idx% delims=," %%d in ("%departments%") do set department=%%d
endlocal & set department=%department%

echo Selected department: %department%

:: Simulate Chrome install
echo Installing Chrome (simulated)...
timeout /t 2 >nul

echo timestamp,username,email,phone,department>>user_creation_log.csv
for /f %%t in ('powershell -command "Get-Date -Format o"') do (
  set timestamp=%%t
)
echo %timestamp%,%username%,%email%,%phone%,%department%>>user_creation_log.csv

echo Log saved to user_creation_log.csv

:end
pause