# What is Bundle ID and How to Find It

## What is Bundle ID?

**Bundle ID** is a unique identifier for an iOS app, similar to a package name for Android apps.

**Format:** Usually in reverse domain format, like:
- `com.company.appname`
- `nl.ah.ahapp` (Albert Heijn)
- `com.apple.safari`

## Albert Heijn App Bundle ID

### For Albert Heijn App (iOS):

**Bundle ID:** `nl.ah.ahapp`

**What it means:**
- `nl` = Netherlands (country code)
- `ah` = Albert Heijn (company)
- `ahapp` = Albert Heijn app

### Common Albert Heijn Bundle IDs:

- **Primary:** `nl.ah.ahapp` (most common)
- **Alternative:** `nl.ah.app` (sometimes used)
- **Web version:** `nl.ah.web` (if exists)

## How to Find Bundle ID

### Method 1: Check on iPhone (Easiest)

**Using Settings:**
1. On iPhone, go to: **Settings > General > iPhone Storage**
2. Find **Albert Heijn** app in the list
3. Tap on it
4. Look at the app details - bundle ID may be shown

**Using iTunes/Finder (macOS):**
1. Connect iPhone via USB
2. Open **Finder** (macOS Catalina+) or **iTunes** (older macOS)
3. Select your iPhone
4. Go to **Apps** tab
5. Find **Albert Heijn** app
6. Right-click > **Get Info** or **Show in Finder**
7. Bundle ID is usually in the app name or file name

### Method 2: Using Terminal (macOS)

**List all installed apps:**
```bash
# List all apps on connected iPhone
xcrun simctl listapps booted | grep -i albert

# Or using ideviceinstaller (if installed)
ideviceinstaller -l | grep -i albert
```

**Check app bundle ID:**
```bash
# Using xcrun (requires Xcode)
xcrun simctl listapps booted | grep -A 5 -i albert

# Using ideviceinstaller
ideviceinstaller -l | grep -i albert
```

### Method 3: Using Appium Inspector

**After connecting to device:**
1. Open Appium Inspector
2. Connect to your iPhone
3. Once connected, you can see installed apps
4. Find Albert Heijn app
5. Bundle ID will be shown

### Method 4: Check in Xcode (macOS)

**Using Xcode:**
1. Open Xcode
2. Go to: **Window > Devices and Simulators**
3. Connect iPhone via USB
4. Select your iPhone
5. Click on **Installed Apps** or check device logs
6. Find Albert Heijn app
7. Bundle ID should be visible

### Method 5: Check App Store

**Using App Store (web):**
1. Go to: https://apps.apple.com
2. Search for "Albert Heijn"
3. Open the app page
4. Look at the URL - it may contain bundle ID
5. Or check app details page

### Method 6: Using Python Script

**Check installed apps:**
```python
# Using appium-python-client
from appium import webdriver
from appium.options.ios import XCUITestOptions

options = XCUITestOptions()
options.platform_name = "iOS"
options.device_name = "iPhone"
options.udid = "YOUR_DEVICE_UDID"
options.automation_name = "XCUITest"

driver = webdriver.Remote("http://localhost:4723", options=options)

# Get installed apps (if supported)
# Check driver capabilities or use system commands
```

## Verify Bundle ID is Correct

### Method 1: Test with Appium Inspector

1. **Use the bundle ID in desired capabilities:**
   ```json
   {
     "platformName": "iOS",
     "platformVersion": "17.0",
     "deviceName": "iPhone",
     "udid": "YOUR_DEVICE_UDID",
     "bundleId": "nl.ah.ahapp",
     "automationName": "XCUITest"
   }
   ```

2. **Click "Start Session"**

3. **If correct:** Albert Heijn app will launch
4. **If wrong:** You'll get an error like:
   - "Bundle ID not found"
   - "App not installed"
   - "Cannot find application"

### Method 2: Check if App Installed

**Using Terminal (macOS):**
```bash
# Check if app is installed
xcrun simctl listapps booted | grep -i "nl.ah.ahapp"

# Or check all Albert Heijn related apps
xcrun simctl listapps booted | grep -i albert
```

**Using adb (Android - for comparison):**
```bash
# Android equivalent
adb shell pm list packages | grep -i albert
```

### Method 3: Try Common Bundle IDs

**If `nl.ah.ahapp` doesn't work, try:**

1. **`nl.ah.app`** (without 'ah' before 'app')
2. **`com.ah.app`** (using .com instead of .nl)
3. **`nl.ah.albertheijn`** (full company name)

**Test each one in Appium Inspector until one works.**

## Common Bundle IDs for Albert Heijn

### iOS (iPhone/iPad):
- **Primary:** `nl.ah.ahapp`
- **Alternative:** `nl.ah.app`
- **Possible:** `com.ah.app`

### Android (for reference):
- **Package Name:** `nl.ah.app`
- **Alternative:** `com.ah.app`

## Troubleshooting

### Issue 1: Bundle ID Not Found

**Error:** "Bundle ID not found" or "App not installed"

**Solutions:**
1. **Check if app is installed:**
   - On iPhone: Settings > General > iPhone Storage
   - Look for Albert Heijn app

2. **Try different bundle IDs:**
   - `nl.ah.ahapp` (primary)
   - `nl.ah.app` (alternative)
   - `com.ah.app` (alternative)

3. **Check app name:**
   - Make sure it's "Albert Heijn" (official app)
   - Not a third-party app

4. **Reinstall app:**
   - Delete app from iPhone
   - Reinstall from App Store
   - Check bundle ID again

### Issue 2: Bundle ID Changed

**If app was updated:**
- Bundle ID might have changed
- Check latest app version
- Update bundle ID in desired capabilities

### Issue 3: Multiple Versions

**If you have multiple Albert Heijn apps:**
- Check which one is the official app
- Use bundle ID for the official app
- Remove other versions if needed

## How to Find Any App's Bundle ID

### General Method:

1. **Install the app** on iPhone
2. **Connect iPhone** to Mac via USB
3. **Use Terminal:**
   ```bash
   # List all installed apps
   xcrun simctl listapps booted
   
   # Or for physical device
   instruments -s devices
   ```

4. **Search for app name** in the output
5. **Find bundle ID** in the app details

### Using Third-Party Tools:

**iOS App Installer:**
- Use tools like **iMazing** or **iFunbox**
- These show bundle IDs for installed apps

## Quick Reference

### Albert Heijn Bundle ID (iOS):

**Primary (most likely):**
```
nl.ah.ahapp
```

**Alternative:**
```
nl.ah.app
```

### Use in Desired Capabilities:

```json
{
  "platformName": "iOS",
  "platformVersion": "17.0",
  "deviceName": "iPhone",
  "udid": "YOUR_DEVICE_UDID",
  "bundleId": "nl.ah.ahapp",
  "automationName": "XCUITest",
  "noReset": true,
  "fullReset": false
}
```

## Next Steps

1. **Try `nl.ah.ahapp` first** (most common)
2. **If it doesn't work, try `nl.ah.app`**
3. **Check if app is installed** on iPhone
4. **Verify in Appium Inspector** when connecting
5. **Update desired capabilities** if needed

## Resources

- **Apple Developer Documentation**: https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleidentifier
- **Appium iOS Capabilities**: https://appium.io/docs/en/2.1/guides/caps/
- **Find Bundle ID Tools**: Various iOS device managers


