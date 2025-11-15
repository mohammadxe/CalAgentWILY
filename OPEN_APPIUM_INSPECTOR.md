# How to Open Appium Inspector

## Quick Guide: 3 Ways to Open Appium Inspector

### Method 1: Download Desktop App (Recommended - Easiest!)

**This is the easiest way - no installation needed!**

1. **Go to Appium Inspector Releases:**
   - Visit: https://github.com/appium/appium-inspector/releases
   - Download the latest version for **Windows**

2. **Download:**
   - Look for: `Appium-Inspector-Windows-x.x.x.exe`
   - Or: `Appium-Inspector-x.x.x-x64-win.zip`
   - Download and extract

3. **Run:**
   - Double-click `Appium Inspector.exe`
   - Appium Inspector will open!

**No command line needed!** Just download and run.

### Method 2: Use npx (No Installation)

**This works even if you don't have Appium Inspector installed!**

1. **Start Appium Server First** (in one terminal):
   ```bash
   appium
   ```

2. **Open Appium Inspector** (in another terminal):
   ```bash
   npx appium-inspector
   ```

   This will:
   - Download Appium Inspector automatically
   - Open it in your browser
   - No installation needed!

### Method 3: Install via npm

**If you want to install it permanently:**

1. **Install Appium Inspector:**
   ```bash
   npm install -g appium-inspector
   ```

2. **Run Appium Inspector:**
   ```bash
   appium-inspector
   ```

   **Note:** This may require Electron, which can cause issues.

## Recommended: Method 1 or 2

### Quick Start: Use npx (Easiest!)

**Step 1: Start Appium Server**
```bash
# In Terminal 1
appium
```

**Step 2: Open Appium Inspector**
```bash
# In Terminal 2
npx appium-inspector
```

**That's it!** Appium Inspector will open in your browser.

## Fixing "electron is not recognized" Error

### Issue: Electron Not Found

If you see: `electron is not recognized as internal or external command`

**Solution 1: Use npx (No Electron Needed)**
```bash
npx appium-inspector
```

**Solution 2: Download Desktop App**
- Go to: https://github.com/appium/appium-inspector/releases
- Download Windows version
- Run the .exe file directly

**Solution 3: Install Electron**
```bash
c```

Then try:
```bash
appium-inspector
```

## Step-by-Step: Using npx (Recommended)

### 1. Start Appium Server (Terminal 1)

Open PowerShell or Command Prompt:

```bash
appium
```

Keep this terminal open! You should see:
```
[Appium] Welcome to Appium v3.1.1
[Appium] Appium REST http interface listener started on 0.0.0.0:4723
```

### 2. Open Appium Inspector (Terminal 2)

Open **another** PowerShell or Command Prompt:

```bash
npx appium-inspector
```

This will:
- Download Appium Inspector automatically
- Open it in your default browser
- Connect to Appium server on port 4723

### 3. Configure Connection

In Appium Inspector, you'll see:

**Remote Host:** `localhost` or `127.0.0.1`
**Remote Port:** `4723`
**Remote Path:** `/wd/hub` (for Appium 1.x) or `/` (for Appium 2.x)

**Desired Capabilities:**

**For Android:**
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

### 4. Start Session

Click **"Start Session"** button.

Appium Inspector will:
- Connect to Appium server
- Connect to your device
- Launch Albert Heijn app
- Display the app screen

## Troubleshooting

### Issue 1: "electron is not recognized"

**Solution: Use npx**
```bash
npx appium-inspector
```

**Or download desktop app:**
- Go to: https://github.com/appium/appium-inspector/releases
- Download Windows .exe file
- Run directly

### Issue 2: Appium Inspector won't connect

**Check:**
1. Is Appium server running?
   ```bash
   appium
   ```

2. Test connection:
   ```powershell
   Invoke-WebRequest -Uri http://localhost:4723/wd/hub/status -Method GET
   ```

3. Check port:
   - Default: `4723`
   - If different, update in Appium Inspector

### Issue 3: Can't find device

**Check:**
1. Device connected via USB?
   ```bash
   adb devices
   ```

2. USB debugging enabled?

3. Device trusted?

### Issue 4: App won't launch

**Check:**
1. App installed on device?
   ```bash
   adb shell pm list packages | findstr ah
   ```

2. Bundle ID/Package name correct?

3. Activity name correct?

## Quick Reference

### Start Appium Inspector (Easiest Way)

```bash
# Terminal 1: Start Appium
appium

# Terminal 2: Open Inspector
npx appium-inspector
```

### Download Desktop App

1. Go to: https://github.com/appium/appium-inspector/releases
2. Download Windows version
3. Run .exe file

### Install Permanently

```bash
npm install -g appium-inspector
appium-inspector
```

## Next Steps

After Appium Inspector is open:

1. **Connect to Device**
   - Enter desired capabilities
   - Click "Start Session"

2. **Inspect Albert Heijn App**
   - Click on elements in the app
   - Find selectors in the right panel

3. **Find Selectors**
   - Search button
   - Search input
   - Product results
   - "Voeg toe" button

4. **Test Selectors**
   - Use the helper script: `backend/find_selectors_guide.py`

5. **Update Code**
   - Update selectors in `backend/src/ah_automation.py`

## Resources

- **Appium Inspector Releases**: https://github.com/appium/appium-inspector/releases
- **Appium Inspector Docs**: https://github.com/appium/appium-inspector
- **Appium Documentation**: https://appium.io/docs/en/2.1/

