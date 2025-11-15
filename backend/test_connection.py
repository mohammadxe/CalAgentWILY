#!/usr/bin/env python3
"""
Test script to verify backend and Appium connections
"""

import requests
import sys
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options
import os
from dotenv import load_dotenv

load_dotenv()

def test_backend():
    """Test backend API"""
    print("Testing backend API...")
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            print("✓ Backend API is running")
            print(f"  Response: {response.json()}")
            return True
        else:
            print(f"✗ Backend API returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("✗ Backend API is not running")
        print("  Start it with: python src/main.py")
        return False
    except Exception as e:
        print(f"✗ Error testing backend: {e}")
        return False

def test_appium_server():
    """Test Appium server"""
    print("\nTesting Appium server...")
    # Try both Appium 2.x/3.x (/) and Appium 1.x (/wd/hub) endpoints
    endpoints = [
        "http://localhost:4723/status",  # Appium 2.x/3.x
        "http://localhost:4723/wd/hub/status",  # Appium 1.x
    ]
    
    for endpoint in endpoints:
        try:
            response = requests.get(endpoint, timeout=5)
            if response.status_code == 200:
                print("✓ Appium server is running")
                data = response.json()
                # Handle both response formats
                if 'value' in data:
                    print(f"  Status: {data.get('value', {}).get('ready', False)}")
                else:
                    print(f"  Status: {data}")
                return True
        except requests.exceptions.ConnectionError:
            continue
        except Exception as e:
            continue
    
    print("✗ Appium server is not running")
    print("  Start it with: appium")
    return False

def test_device_connection(device_type="ios"):
    """Test device connection"""
    print(f"\nTesting {device_type} device connection...")
    # Get URL from env, default to Appium 2.x/3.x format
    appium_url = os.getenv("APPIUM_SERVER_URL", "http://localhost:4723")
    
    try:
        if device_type.lower() == "ios":
            options = XCUITestOptions()
            options.platform_name = "iOS"
            options.device_name = os.getenv("IOS_DEVICE_NAME", "iPhone")
            options.platform_version = os.getenv("IOS_VERSION", "17.0")
            options.bundle_id = os.getenv("AH_BUNDLE_ID", "nl.ah.ahapp")
            options.udid = os.getenv("IOS_UDID", "")
            options.automation_name = "XCUITest"
            options.no_reset = True
        else:  # Android
            options = UiAutomator2Options()
            options.platform_name = "Android"
            options.device_name = os.getenv("ANDROID_DEVICE_NAME", "Android Device")
            options.app_package = os.getenv("AH_PACKAGE", "nl.ah.app")
            options.app_activity = os.getenv("AH_ACTIVITY", "nl.ah.app.MainActivity")
            options.automation_name = "UiAutomator2"
            options.no_reset = True
        
        driver = webdriver.Remote(appium_url, options=options)
        print(f"✓ Successfully connected to {device_type} device")
        print(f"  Device capabilities: {driver.capabilities}")
        driver.quit()
        return True
    except Exception as e:
        print(f"✗ Failed to connect to {device_type} device: {e}")
        print("  Make sure:")
        print("    1. Device is connected via USB")
        print("    2. Device is trusted")
        print("    3. Appium server is running")
        print("    4. .env file is configured correctly")
        return False

def main():
    print("=" * 50)
    print("Albert Heijn Automation - Connection Test")
    print("=" * 50)
    print()
    
    backend_ok = test_backend()
    appium_ok = test_appium_server()
    
    if backend_ok and appium_ok:
        print("\n" + "=" * 50)
        print("Testing device connection...")
        print("=" * 50)
        
        device_type = input("\nDevice type (ios/android): ").strip().lower() or "ios"
        device_ok = test_device_connection(device_type)
        
        if device_ok:
            print("\n" + "=" * 50)
            print("✓ All tests passed!")
            print("=" * 50)
            print("\nYou're ready to run the automation!")
        else:
            print("\n" + "=" * 50)
            print("✗ Device connection failed")
            print("=" * 50)
            print("\nPlease fix the device connection issues before running automation.")
            sys.exit(1)
    else:
        print("\n" + "=" * 50)
        print("✗ Some tests failed")
        print("=" * 50)
        print("\nPlease fix the issues above before running automation.")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        sys.exit(1)

