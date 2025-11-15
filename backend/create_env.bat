@echo off
REM Script to create .env file from template (Windows)

if exist .env (
    echo .env file already exists
    exit /b 0
)

echo Creating .env file from template...

(
echo # Appium Server Configuration
echo APPIUM_SERVER_URL=http://localhost:4723
echo.
echo # iOS Configuration
echo IOS_DEVICE_NAME=iPhone
echo IOS_VERSION=17.0
echo IOS_UDID=
echo AH_BUNDLE_ID=nl.ah.ahapp
echo.
echo # Android Configuration
echo ANDROID_DEVICE_NAME=Android Device
echo AH_PACKAGE=nl.ah.app
echo AH_ACTIVITY=nl.ah.app.MainActivity
echo.
echo # Backend Configuration
echo BACKEND_PORT=8000
) > .env

echo .env file created successfully!
echo Please edit .env and update with your device configuration
pause

