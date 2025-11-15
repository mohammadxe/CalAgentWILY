# Quick iOS Configuration for Appium Inspector

## Copy This Configuration

### Step 1: Get Your Device UDID

**Using Xcode (Easiest):**
1. Open Xcode
2. Window > Devices and Simulators
3. Connect iPhone via USB
4. Copy the **Identifier** (UDID)

**Using Terminal:**
```bash
xcrun simctl list devices
```

### Step 2: Get Your iOS Version

**On iPhone:**
- Settings > General > About > Software Version
- Note the version (e.g., 17.0, 17.1)

### Step 3: Copy This JSON

**Replace `YOUR_DEVICE_UDID` with your actual UDID:**
**Replace `17.0` with your iOS version if different:**

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

### Step 4: Paste in Appium Inspector

1. Open Appium Inspector
2. Click "Edit Configurations" or find "Desired Capabilities"
3. Paste the JSON above
4. Replace `YOUR_DEVICE_UDID` with your device UDID
5. Update `platformVersion` if needed
6. Click "Start Session"

## Example Configuration

**iPhone 14 Pro, iOS 17.0:**

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

## Important Fields

- **platformName**: `"iOS"` (required)
- **platformVersion**: Your iOS version (required)
- **deviceName**: Your iPhone name (required)
- **udid**: Your device UDID (required)
- **bundleId**: `"nl.ah.ahapp"` (Albert Heijn app)
- **automationName**: `"XCUITest"` (required for iOS)
- **noReset**: `true` (keeps app state)
- **fullReset**: `false` (doesn't uninstall app)

## Troubleshooting

### Can't find UDID?
- Use Xcode: Window > Devices and Simulators
- Connect iPhone via USB
- Copy the Identifier

### Bundle ID not found?
- Check if Albert Heijn app is installed
- Verify bundle ID: `nl.ah.ahapp`

### Device not found?
- Check if device is connected via USB
- Check if device is trusted
- Try disconnecting and reconnecting

## Next Steps

After Appium Inspector connects:

1. **Verify app is open** on iPhone
2. **Inspect elements** in Appium Inspector
3. **Find selectors** for automation
4. **Update code** with found selectors


