# Script to create .env file from template (PowerShell)

if (Test-Path .env) {
    Write-Host ".env file already exists"
    exit
}

Write-Host "Creating .env file from template..."

$envContent = @"
# Appium Server Configuration
APPIUM_SERVER_URL=http://localhost:4723

# iOS Configuration
IOS_DEVICE_NAME=iPhone
IOS_VERSION=17.0
IOS_UDID=
AH_BUNDLE_ID=nl.ah.ahapp

# Android Configuration
ANDROID_DEVICE_NAME=Android Device
AH_PACKAGE=nl.ah.app
AH_ACTIVITY=nl.ah.app.MainActivity

# Backend Configuration
BACKEND_PORT=8000
"@

$envContent | Out-File -FilePath .env -Encoding utf8

Write-Host ".env file created successfully!"
Write-Host "Please edit .env and update with your device configuration"

