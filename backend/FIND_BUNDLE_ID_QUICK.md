# Quick Guide: Find Albert Heijn Bundle ID

## Albert Heijn Bundle ID (iOS)

**Most Common:**
```
nl.ah.ahapp
```

**Alternative:**
```
nl.ah.app
```

## How to Find It

### Method 1: Test in Appium Inspector

**Try this first:**
```json
{
  "bundleId": "nl.ah.ahapp"
}
```

**If it doesn't work, try:**
```json
{
  "bundleId": "nl.ah.app"
}
```

### Method 2: Check on iPhone

1. **Settings > General > iPhone Storage**
2. Find **Albert Heijn** app
3. Tap on it
4. Check app details

### Method 3: Use Terminal (macOS)

```bash
# List all apps
xcrun simctl listapps booted | grep -i albert

# Or
instruments -s devices
```

### Method 4: Check in Xcode

1. **Xcode > Window > Devices and Simulators**
2. Connect iPhone via USB
3. Select your iPhone
4. Check installed apps

## Verify Bundle ID

### If Bundle ID is Correct:
- ✅ Albert Heijn app will launch
- ✅ Appium Inspector will show the app

### If Bundle ID is Wrong:
- ❌ Error: "Bundle ID not found"
- ❌ Error: "App not installed"
- ❌ Error: "Cannot find application"

## Use in Desired Capabilities

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

## Quick Test

1. **Try `nl.ah.ahapp` first** in Appium Inspector
2. **If error, try `nl.ah.app`**
3. **Check if app is installed** on iPhone
4. **Update if needed**


