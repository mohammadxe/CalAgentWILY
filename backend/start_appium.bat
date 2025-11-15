@echo off
REM Script to start Appium server on Windows

echo ==========================================
echo Starting Appium Server
echo ==========================================

REM Check if Node.js is installed
where node >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Node.js is not installed!
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)

REM Check if npm is installed
where npm >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] npm is not installed!
    echo Please install npm (comes with Node.js)
    pause
    exit /b 1
)

REM Check if Appium is installed
where appium >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [WARNING] Appium is not installed globally
    echo Attempting to install Appium...
    
    REM Try to install Appium
    call npm install -g appium
    
    REM Check again
    where appium >nul 2>nul
    if %ERRORLEVEL% NEQ 0 (
        echo [WARNING] Failed to install Appium globally
        echo Trying with npx...
        echo.
        echo Starting Appium with npx (no installation required)...
        call npx appium %*
        pause
        exit /b 0
    )
)

REM Check if drivers are installed
echo Checking for Appium drivers...
appium driver list | findstr /i "xcuitest uiautomator2" >nul
if %ERRORLEVEL% NEQ 0 (
    echo [WARNING] Drivers not found. Installing drivers...
    
    REM Install iOS driver
    echo Installing XCUITest driver (iOS)...
    call appium driver install xcuitest
    
    REM Install Android driver
    echo Installing UiAutomator2 driver (Android)...
    call appium driver install uiautomator2
)

REM Start Appium server
echo.
echo ==========================================
echo Starting Appium Server on port 4723
echo ==========================================
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start Appium with default options
appium %*

pause

