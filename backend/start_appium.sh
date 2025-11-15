#!/bin/bash
# Script to start Appium server with proper configuration

echo "=========================================="
echo "Starting Appium Server"
echo "=========================================="

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed!"
    echo "Please install Node.js from https://nodejs.org/"
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed!"
    echo "Please install npm (comes with Node.js)"
    exit 1
fi

# Check if Appium is installed
if ! command -v appium &> /dev/null; then
    echo "⚠️  Appium is not installed globally"
    echo "Attempting to install Appium..."
    
    # Try to install Appium
    npm install -g appium
    
    if ! command -v appium &> /dev/null; then
        echo "❌ Failed to install Appium"
        echo "Trying with npx..."
        echo ""
        echo "Starting Appium with npx (no installation required)..."
        npx appium "$@"
        exit 0
    fi
fi

# Check if drivers are installed
echo "Checking for Appium drivers..."
if ! appium driver list | grep -q "xcuitest\|uiautomator2"; then
    echo "⚠️  Drivers not found. Installing drivers..."
    
    # Install iOS driver
    echo "Installing XCUITest driver (iOS)..."
    appium driver install xcuitest
    
    # Install Android driver
    echo "Installing UiAutomator2 driver (Android)..."
    appium driver install uiautomator2
fi

# Start Appium server
echo ""
echo "=========================================="
echo "Starting Appium Server on port 4723"
echo "=========================================="
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start Appium with default options
appium "$@"

