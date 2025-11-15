# How to Open Appium Inspector - Easy Guide

## ❌ Problem: "electron is not recognized"

This happens because Appium Inspector needs Electron, which isn't installed.

## ✅ Solution: 2 Easy Ways

### Method 1: Download Desktop App (EASIEST - Recommended!)

**No command line needed! Just download and run.**

1. **Go to Appium Inspector Releases:**
   - I'll open the download page for you
   - Or go to: https://github.com/appium/appium-inspector/releases/latest

2. **Download Windows Version:**
   - Look for: `Appium-Inspector-Windows-x.x.x.exe`
   - Or: `Appium-Inspector-x.x.x-x64-win.zip`
   - Click to download

3. **Run the .exe file:**
   - Double-click the downloaded file
   - Appium Inspector will open!
   - No installation needed!

**That's it!** Just download and run.

### Method 2: Use Web-Based Inspector

**Appium 2.0+ includes a web-based inspector!**

1. **Start Appium Server:**
   ```bash
   appium
   ```

2. **Open in Browser:**
   - Open your web browser
   - Go to: http://localhost:4723
   - You should see the Appium web interface

3. **Or use Appium Inspector web version:**
   - Open: http://localhost:4723/inspector
   - This is a web-based inspector

## Step-by-Step: Download Desktop App

### 1. Open Download Page

**Option A: I'll open it for you**
```bash
start https://github.com/appium/appium-inspector/releases/latest
```

**Option B: Open manually**
- Go to: https://github.com/appium/appium-inspector/releases/latest

### 2. Download Windows Version

Look for one of these files:
- `Appium-Inspector-Windows-x.x.x.exe` (Recommended - Just double-click!)
- `Appium-Inspector-x.x.x-x64-win.zip` (Need to extract first)

### 3. Run the Application

- **If .exe file:** Just double-click it!
- **If .zip file:** Extract it, then run the .exe inside

### 4. Appium Inspector Opens!

You'll see the Appium Inspector window.

## Configure Appium Inspector

### 1. Start Appium Server First

**In Terminal/PowerShell:**
```bash
appium
```

Keep this running! You should see:
```
[Appium] Welcome to Appium v3.1.1
[Appium] Appium REST http interface listener started on 0.0.0.0:4723
```

### 2. Configure Connection in Appium Inspector

**Remote Connection Settings:**
- **Remote Host:** `localhost` or `127.0.0.1`
- **Remote Port:** `4723`
- **Remote Path:** `/` (for Appium 3.x) or `/wd/hub` (for Appium 1.x)

### 3. Enter Desired Capabilities

**For Android (Windows):**

Click "Edit Configurations" or enter JSON:

```json
{
  "platformName": "Android",
  "deviceName": "Android Device",
  "appPackage": "nl.ah.app",
  "appActivity": "nl.ah.app.MainActivity",
  "automationName": "UiAutomator2",
  "noReset": true
}
```

**For iOS (macOS only):**

```json
{
  "platformName": "iOS",
  "platformVersion": "17.0",
  "deviceName": "iPhone",
  "udid": "YOUR_DEVICE_UDID",
  "bundleId": "nl.ah.ahapp",
  "automationName": "XCUITest",
  "noReset": true
}
```

### 4. Click "Start Session"

Appium Inspector will:
- ✅ Connect to Appium server
- ✅ Connect to your device
- ✅ Launch Albert Heijn app
- ✅ Display the app screen

## Troubleshooting

### Issue: Can't download the file

**Solution:**
1. Make sure you're on the correct page
2. Look for "Assets" section
3. Download the Windows .exe file

### Issue: Appium Inspector won't connect

**Check:**
1. Is Appium server running?
   ```bash
   appium
   ```

2. Test connection:
   ```powershell
   Invoke-WebRequest -Uri http://localhost:4723/wd/hub/status -Method GET
   ```

3. Check port in Appium Inspector matches Appium server (4723)

### Issue: Device not found

**Check:**
1. Device connected via USB?
   ```bash
   adb devices
   ```

2. USB debugging enabled?

3. Device trusted on computer?

## Quick Reference

### Download Desktop App

1. Go to: https://github.com/appium/appium-inspector/releases/latest
2. Download `Appium-Inspector-Windows-x.x.x.exe`
3. Double-click to run!

### Start Appium Server

```bash
appium
```

### Configure Connection

**Remote Host:** `localhost`
**Remote Port:** `4723`
**Remote Path:** `/`

### Desired Capabilities (Android)

```json
{
  "platformName": "Android",
  "deviceName": "Android Device",
  "appPackage": "nl.ah.app",
  "appActivity": "nl.ah.app.MainActivity",
  "automationName": "UiAutomator2",
  "noReset": true
}
```

## Next Steps

After Appium Inspector is open:

1. **Connect to Device**
   - Enter desired capabilities
   - Click "Start Session"

2. **Inspect Albert Heijn App**
   - Click on elements in the app
   - Find selectors in the right panel

3. **Find Selectors:**
   - Search button
   - Search input
   - Product results
   - "Voeg toe" button

4. **Update Code:**
   - Update selectors in `backend/src/ah_automation.py`

## Summary

**Easiest Way:**
1. Download desktop app from: https://github.com/appium/appium-inspector/releases/latest
2. Run the .exe file
3. Configure connection
4. Start session!

**No command line needed!** Just download and run.

