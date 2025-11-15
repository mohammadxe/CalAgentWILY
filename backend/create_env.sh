#!/bin/bash
# Script to create .env file from template

if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cat > .env << EOF
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
EOF
    echo ".env file created successfully!"
    echo "Please edit .env and update with your device configuration"
else
    echo ".env file already exists"
fi

