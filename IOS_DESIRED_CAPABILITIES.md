# iOS/iPhone Desired Capabilities for Appium Inspector

## Quick Copy-Paste Configuration

### For iPhone (iOS)

**Copy this JSON into Appium Inspector:**

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

## Step-by-Step: How to Get Your Device Information

### 1. Get Your iPhone's UDID

**Option A: Using Xcode (Easiest)**
1. Open Xcode
2. Go to: **Window > Devices and Simulators**
3. Connect your iPhone via USB
4. Select your iPhone
5. Copy the **Identifier** (this is your UDID)

**Option B: Using Terminal**
```bash
# macOS only
xcrun simctl list devices
```

**Option C: Using Instruments**
```bash
# macOS only
instruments -s devices
```

**Option D: Using libimobiledevice (if installed)**
```bash
idevice_id -l
```

### 2. Get Your iOS Version

**On iPhone:**
1. Go to: **Settings > General > About**
2. Look for: **Software Version**
3. Note the version number (e.g., 17.0, 17.1, 16.5)

### 3. Get Albert Heijn App Bundle ID

**The bundle ID is:** `nl.ah.ahapp`

**Verify it's installed:**
```bash
# macOS only
xcrun simctl listapps booted | grep -i albert
```

**Or check on iPhone:**
- Settings > General > iPhone Storage
- Look for Albert Heijn app

## Complete Desired Capabilities Configuration

### Basic Configuration (Minimum Required)

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

### Recommended Configuration (Full)

```json
{
  "platformName": "iOS",
  "platformVersion": "17.0",
  "deviceName": "iPhone",
  "udid": "YOUR_DEVICE_UDID",
  "bundleId": "nl.ah.ahapp",
  "automationName": "XCUITest",
  "noReset": true,
  "fullReset": false,
  "waitForIdleTimeout": 1000,
  "shouldUseSingletonTestManager": false
}
```

### Advanced Configuration (If Needed)

```json
{
  "platformName": "iOS",
  "platformVersion": "17.0",
  "deviceName": "iPhone",
  "udid": "YOUR_DEVICE_UDID",
  "bundleId": "nl.ah.ahapp",
  "automationName": "XCUITest",
  "noReset": true,
  "fullReset": false,
  "waitForIdleTimeout": 1000,
  "shouldUseSingletonTestManager": false,
  "wdaLaunchTimeout": 60000,
  "wdaConnectionTimeout": 60000,
  "usePrebuiltWDA": false,
  "derivedDataPath": "/tmp/derivedDataPath",
  "useSimpleBuildTest": true
}
```

## How to Use in Appium Inspector

### Step 1: Open Appium Inspector

### Step 2: Configure Connection

**Remote Connection Settings:**
- **Remote Host:** `localhost` or `127.0.0.1`
- **Remote Port:** `4723`
- **Remote Path:** `/` (for Appium 3.x)

### Step 3: Enter Desired Capabilities

1. Click **"Edit Configurations"** or find the **Desired Capabilities** section
2. Paste the JSON configuration above
3. **Replace `YOUR_DEVICE_UDID`** with your actual device UDID
4. **Update `platformVersion`** if your iOS version is different
5. **Update `deviceName`** if needed (e.g., "iPhone 14 Pro", "iPhone 15")

### Step 4: Start Session

Click **"Start Session"** button.

Appium Inspector will:
- Connect to Appium server
- Connect to your iPhone
- Launch Albert Heijn app
- Display the app screen

## Example Configuration

### Example 1: iPhone 14 Pro, iOS 17.0

```json
{
  "platformName": "iOS",
  "platformVersion": "17.0",
  "deviceName": "iPhone 14 Pro",
  "udid": "00008030-001A4D9E1E38802E",
  "bundleId": "nl.ah.ahapp",
  "automationName": "XCUITest",
  "noReset": true,
  "fullReset": false
}
```

### Example 2: iPhone 15, iOS 17.1

```json
{
  "platformName": "iOS",
  "platformVersion": "17.1",
  "deviceName": "iPhone 15",
  "udid": "00008030-001A4D9E1E38802F",
  "bundleId": "nl.ah.ahapp",
  "automationName": "XCUITest",
  "noReset": true,
  "fullReset": false
}
```

## Important Notes

### Required Fields

1. **platformName**: Must be `"iOS"`
2. **platformVersion**: Your iOS version (e.g., "17.0", "17.1", "16.5")
3. **deviceName**: Your iPhone name (e.g., "iPhone", "iPhone 14 Pro")
4. **udid**: Your device UDID (unique device identifier)
5. **bundleId**: Albert Heijn app bundle ID (`"nl.ah.ahapp"`)
6. **automationName**: Must be `"XCUITest"` for iOS

### Optional Fields

1. **noReset**: `true` - Don't reset app state between sessions
2. **fullReset**: `false` - Don't uninstall app between sessions
3. **waitForIdleTimeout**: Time to wait for app to be idle (milliseconds)
4. **shouldUseSingletonTestManager**: `false` - Use singleton test manager

### Common Issues

#### Issue 1: "Device not found"

**Solution:**
1. Check if device UDID is correct
2. Check if device is connected via USB
3. Check if device is trusted
4. Try disconnecting and reconnecting device

#### Issue 2: "Bundle ID not found"

**Solution:**
1. Check if Albert Heijn app is installed on iPhone
2. Verify bundle ID is correct: `nl.ah.ahapp`
3. Try installing the app again

#### Issue 3: "iOS version mismatch"

**Solution:**
1. Check your iOS version on iPhone
2. Update `platformVersion` in desired capabilities
3. Make sure Xcode supports your iOS version

#### Issue 4: "WebDriverAgent not found"

**Solution:**
1. This is normal - Appium will build it automatically
2. First time may take longer
3. Wait for WebDriverAgent to build and install

## Quick Reference

### Minimum Required Configuration

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

### Recommended Configuration

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

After Appium Inspector connects:

1. **Verify App is Open**
   - Albert Heijn app should be open on your iPhone
   - Appium Inspector should show the app screen

2. **Inspect Elements**
   - Click on elements in the app
   - Find selectors in the right panel

3. **Find Selectors**
   - Search button
   - Search input
   - Product results
   - "Voeg toe" button

4. **Update Code**
   - Update selectors in `backend/src/ah_automation.py`
   - Update `.env` file with your device UDID

## Resources

- **Appium iOS Capabilities**: https://appium.io/docs/en/2.1/guides/caps/
- **XCUITest Documentation**: https://developer.apple.com/documentation/xctest
- **WebDriverAgent**: https://github.com/appium/WebDriverAgent


