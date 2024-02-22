@echo off
SET scriptPath=C:\Users\dream\OneDrive\Desktop\HAHA\main.py
SET pythonExe=python

:: Change to the script's directory
cd /d C:\Users\dream\OneDrive\Desktop\HAHA

:: Install required Python packages
echo Installing required Python packages...
%pythonExe% -m pip install psutil tqdm --user

:: Check for privileges
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running with administrative privileges
    %pythonExe% "%scriptPath%"
) else (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process cmd -ArgumentList '/c cd /d C:\Users\dream\OneDrive\Desktop\HAHA && %pythonExe% \"%scriptPath%\"' -Verb RunAs"
)
