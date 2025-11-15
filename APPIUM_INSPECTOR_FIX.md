# Quick Fix: Appium Inspector "undefined" Error

## Quick Fix

### You have Appium 3.1.1

**Use this exact JSON (copy-paste and replace YOUR_DEVICE_UDID):**

```json
{
  "platformName": "iOS",
  "appium:platformVersion": "17.0",
  "appium:deviceName": "iPhone",
  "appium:udid": "YOUR_DEVICE_UDID",
  "appium:bundleId": "nl.ah.ahapp",
  "appium:automationName": "XCUITest",
  "appium:noReset": true
}
```

## Important: Appium 3.x Requires "appium:" Prefix

**Appium 3.x requires `appium:` prefix for Appium-specific capabilities!**

### ✅ Correct (Appium 3.x):
```json
{
  "platformName": "iOS",
  "appium:platformVersion": "17.0",
  "appium:bundleId": "nl.ah.ahapp"
}
```

### ❌ Wrong (Will cause "undefined" error):
```json
{
  "platformName": "iOS",
  "platformVersion": "17.0",
  "bundleId": "nl.ah.ahapp"
}
```

## Step-by-Step Fix

### 1. Open Appium Inspector

### 2. Clear All Capabilities

### 3. Paste This JSON:

```json
{
  "platformName": "iOS",
  "appium:platformVersion": "17.0",
  "appium:deviceName": "iPhone",
  "appium:udid": "YOUR_DEVICE_UDID",
  "appium:bundleId": "nl.ah.ahapp",
  "appium:automationName": "XCUITest",
  "appium:noReset": true
}
```

### 4. Replace YOUR_DEVICE_UDID

Replace `YOUR_DEVICE_UDID` with your actual iPhone UDID.

### 5. Click "Start Session"

## Why This Happens

**Appium 3.x uses W3C WebDriver standard:**
- Standard capabilities (like `platformName`) don't need prefix
- Appium-specific capabilities need `appium:` prefix
- Missing prefix causes "undefined" error

## Complete Working Configuration

### For Appium 3.1.1 (Your Version):

```json
{
  "platformName": "iOS",
  "appium:platformVersion": "17.0",
  "appium:deviceName": "iPhone",
  "appium:udid": "YOUR_DEVICE_UDID",
  "appium:bundleId": "nl.ah.ahapp",
  "appium:automationName": "XCUITest",
  "appium:noReset": true,
  "appium:fullReset": false
}
```

## Common Mistakes

### ❌ Wrong - Missing Prefix:
```json
{
  "platformName": "iOS",
  "platformVersion": "17.0",
  "bundleId": "nl.ah.ahapp"
}
```

### ✅ Correct - With Prefix:
```json
{
  "platformName": "iOS",
  "appium:platformVersion": "17.0",
  "appium:bundleId": "nl.ah.ahapp"
}
```

## Capabilities That Need Prefix

**These need `appium:` prefix in Appium 3.x:**
- `appium:platformVersion`
- `appium:deviceName`
- `appium:udid`
- `appium:bundleId`
- `appium:automationName`
- `appium:noReset`
- `appium:fullReset`

**These don't need prefix (W3C standard):**
- `platformName` ✅

## Quick Reference

### Minimal Configuration (Appium 3.x):

```json
{
  "platformName": "iOS",
  "appium:platformVersion": "17.0",
  "appium:deviceName": "iPhone",
  "appium:udid": "YOUR_DEVICE_UDID",
  "appium:bundleId": "nl.ah.ahapp",
  "appium:automationName": "XCUITest"
}
```

## Next Steps

1. **Copy the JSON above**
2. **Replace YOUR_DEVICE_UDID with your actual UDID**
3. **Paste into Appium Inspector**
4. **Click "Start Session"**
5. **Should work now!**


