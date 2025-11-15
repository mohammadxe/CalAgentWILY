# Quick Start: Running Appium Server

## ✅ Appium is Now Installed!

Appium version: **3.1.1**
Android driver (uiautomator2): **Installed**

## How to Start Appium Server

### Option 1: Use Command Line (Recommended)

**Windows (PowerShell/Command Prompt):**
```bash
appium
```

**macOS/Linux:**
```bash
appium
```

### Option 2: Use the Start Script

**Windows:**
```bash
cd backend
start_appium.bat
```

**macOS/Linux:**
```bash
cd backend
chmod +x start_appium.sh
./start_appium.sh
```

### Option 3: Use npx (No Installation Required)

```bash
npx appium
```

## What Happens When You Start Appium?

When you run `appium`, you should see:

```
[Appium] Welcome to Appium v3.1.1
[Appium] Appium REST http interface listener started on 0.0.0.0:4723
```

**Keep this terminal window open!** Appium needs to keep running.

## Verify Appium is Running

### Test Connection (in another terminal)

**Windows (PowerShell):**
```powershell
Invoke-WebRequest -Uri http://localhost:4723/wd/hub/status -Method GET
```

**macOS/Linux:**
```bash
curl http://localhost:4723/wd/hub/status
```

**Or use a browser:**
- Open: http://localhost:4723/wd/hub/status
- You should see a JSON response

## Common Commands

### Start Appium
```bash
appium
```

### Start on Specific Port
```bash
appium --port 4723
```

### Start with Logging
```bash
appium --log-level debug
```

### Stop Appium
- Press `Ctrl+C` in the terminal
- Or close the terminal window

## Next Steps

1. **Start Appium Server**
   ```bash
   appium
   ```

2. **Keep it Running** (don't close the terminal)

3. **Connect Your Device**
   - Connect Android device via USB
   - Enable USB debugging
   - Trust the computer

4. **Open Appium Inspector**
   - Download from: https://github.com/appium/appium-inspector/releases
   - Or use: `npx appium-inspector`

5. **Find Selectors**
   - Connect to device in Appium Inspector
   - Inspect Albert Heijn app
   - Find selectors for automation

## Troubleshooting

### Issue: "appium: command not found"

**Solution: Use npx**
```bash
npx appium
```

### Issue: "Driver not found"

**Solution: Install drivers**
```bash
# For Android
appium driver install uiautomator2

# For iOS (macOS only)
appium driver install xcuitest
```

### Issue: "Port 4723 already in use"

**Solution: Use different port**
```bash
appium --port 4724
```

### Issue: "Cannot connect to device"

**Solution: Check device connection**
```bash
# For Android
adb devices

# For iOS (macOS only)
xcrun simctl list devices
```

## Verify Installation

### Check Appium Version
```bash
appium --version
```

**Expected output**: `3.1.1`

### Check Drivers
```bash
appium driver list
```

**Expected output**: `uiautomator2 [installed]` (for Android)

### Test Appium Server
```bash
# Start Appium (in one terminal)
appium

# In another terminal, test connection
curl http://localhost:4723/wd/hub/status
# Or
Invoke-WebRequest -Uri http://localhost:4723/wd/hub/status -Method GET
```

## Quick Reference

### Start Appium
```bash
appium
```

### Stop Appium
- Press `Ctrl+C`

### Test Connection
```bash
# Windows
Invoke-WebRequest -Uri http://localhost:4723/wd/hub/status -Method GET

# macOS/Linux
curl http://localhost:4723/wd/hub/status
```

### Install Drivers
```bash
appium driver install uiautomator2  # Android
appium driver install xcuitest      # iOS (macOS only)
```

## Resources

- **Appium Documentation**: https://appium.io/docs/en/2.1/
- **Appium GitHub**: https://github.com/appium/appium
- **Appium Inspector**: https://github.com/appium/appium-inspector

