# How to Start Appium Server

## Quick Start

### 1. Open Terminal/Command Prompt

### 2. Start Appium Server

**Windows (PowerShell/Command Prompt):**
```bash
appium
```

**macOS/Linux:**
```bash
appium
```

### 3. Keep It Running

**Don't close the terminal!** Appium needs to keep running.

You should see:
```
[Appium] Welcome to Appium v3.1.1
[Appium] Appium REST http interface listener started on 0.0.0.0:4723
```

## Alternative Methods

### Option 1: Use Start Script (Windows)

```bash
cd backend
start_appium.bat
```

### Option 2: Use npx (No Installation)

```bash
npx appium
```

### Option 3: Use Appium Desktop (GUI)

1. Download from: https://github.com/appium/appium-desktop/releases
2. Install and run
3. Click "Start Server"

## Verify Appium is Running

### Test Connection

**Windows (PowerShell):**
```powershell
Invoke-WebRequest -Uri http://localhost:4723/wd/hub/status -Method GET
```

**macOS/Linux:**
```bash
curl http://localhost:4723/wd/hub/status
```

**Or use browser:**
- Open: http://localhost:4723/wd/hub/status
- You should see JSON response

## Troubleshooting

### Issue: "appium: command not found"

**Solution:**
```bash
# Install Appium globally
npm install -g appium

# Or use npx
npx appium
```

### Issue: "Port 4723 already in use"

**Solution:**
```bash
# Use different port
appium --port 4724
```

### Issue: "Driver not found"

**Solution:**
```bash
# Install Android driver
appium driver install uiautomator2

# Install iOS driver (macOS only)
appium driver install xcuitest
```

## Next Steps

1. **Start Appium Server** (keep it running)
2. **Connect Device** (via USB)
3. **Open Appium Inspector**
4. **Find Selectors** for Albert Heijn app
5. **Test Automation**

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

