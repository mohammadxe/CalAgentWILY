# Setup Guide

## Quick Start

### 1. Backend Setup (MacBook)

```bash
# Install Python dependencies
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Install Appium globally
npm install -g appium

# Create .env file (copy from .env.example and update)
cp .env.example .env
# Edit .env with your device configuration
```

### 2. Frontend Setup (Mobile)

```bash
# Install Node.js dependencies
cd frontend
npm install

# Update API_BASE_URL in App.tsx with your MacBook's IP address
# Find your MacBook IP: System Preferences > Network > Wi-Fi > Advanced > TCP/IP
# Or run: ifconfig | grep "inet " | grep -v 127.0.0.1
```

### 3. Device Setup

#### iOS:
1. Connect iPhone to MacBook via USB
2. Trust the computer on iPhone
3. Install WebDriverAgent (via Appium Doctor)
4. Get device UDID: `xcrun simctl list devices` or `instruments -s devices`
5. Update `.env` with UDID and iOS version

#### Android:
1. Connect Android device to MacBook via USB
2. Enable USB debugging on Android device
3. Trust the computer on Android device
4. Verify connection: `adb devices`
5. Update `.env` with package name and activity

### 4. Albert Heijn App

1. Install Albert Heijn app on target device
2. **iOS**: Bundle ID is typically `nl.ah.ahapp`
3. **Android**: Package name is typically `nl.ah.app`

### 5. Appium Inspector (For Finding Selectors)

1. Start Appium server: `appium`
2. Open Appium Inspector
3. Connect to device
4. Find selectors for:
   - Search input field
   - Product results
   - Add to basket button
   - Navigation buttons
5. Update selectors in `backend/src/main.py`

## Running

### 1. Start Appium Server

```bash
appium
```

Keep this running in a terminal.

### 2. Start Backend Server

```bash
cd backend
source venv/bin/activate
python src/main.py
# Or: uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Keep this running in another terminal.

### 3. Start Frontend

```bash
cd frontend
npm start
```

Scan QR code with Expo Go app on your phone.

## Configuration

### Backend (.env)

```env
# Appium Server
APPIUM_SERVER_URL=http://localhost:4723

# iOS Configuration
IOS_DEVICE_NAME=iPhone
IOS_VERSION=17.0
IOS_UDID=YOUR_DEVICE_UDID
AH_BUNDLE_ID=nl.ah.ahapp

# Android Configuration
ANDROID_DEVICE_NAME=Android Device
AH_PACKAGE=nl.ah.app
AH_ACTIVITY=nl.ah.app.MainActivity
```

### Frontend (App.tsx)

```typescript
const API_BASE_URL = __DEV__ 
  ? 'http://YOUR_MACBOOK_IP:8000'  // Replace with your MacBook's IP
  : 'http://your-server.com:8000';
```

## Finding Your MacBook's IP Address

### macOS:
1. System Preferences > Network > Wi-Fi > Advanced > TCP/IP
2. Or run: `ifconfig | grep "inet " | grep -v 127.0.0.1`
3. Look for IP address (usually starts with 192.168.x.x or 10.x.x.x)

### Command Line:
```bash
# macOS/Linux
ifconfig | grep "inet " | grep -v 127.0.0.1

# Or
ipconfig getifaddr en0  # For Wi-Fi
ipconfig getifaddr en1  # For Ethernet
```

## Troubleshooting

### Connection Issues

1. **Backend not reachable**:
   - Check if backend is running: `curl http://localhost:8000/health`
   - Check firewall settings
   - Ensure MacBook and phone are on same Wi-Fi network
   - Update API_BASE_URL in App.tsx with correct IP address

2. **Appium not connecting**:
   - Check if Appium is running: `curl http://localhost:4723/wd/hub/status`
   - Verify device connection: `adb devices` (Android) or `xcrun simctl list` (iOS)
   - Check device trust settings
   - Verify USB connection

3. **App selectors not working**:
   - Use Appium Inspector to find correct selectors
   - Check if app structure has changed
   - Verify bundle ID/package name is correct
   - Update selectors in `backend/src/main.py`

### WebSocket Issues

1. **WebSocket connection failed**:
   - Check if backend supports WebSocket (FastAPI does by default)
   - Verify firewall allows WebSocket connections
   - Check network connectivity
   - Fallback to HTTP API (already implemented)

### Device Issues

1. **iOS device not detected**:
   - Trust computer on iPhone
   - Check USB connection
   - Verify Xcode is installed
   - Check device UDID: `xcrun simctl list devices`

2. **Android device not detected**:
   - Enable USB debugging
   - Trust computer on Android
   - Check ADB: `adb devices`
   - Verify USB connection

## Next Steps

1. **Customize App Selectors**: Use Appium Inspector to find correct selectors for Albert Heijn app
2. **Test Automation**: Run automation with a single product first
3. **Add Error Handling**: Improve error handling and recovery
4. **Add Logging**: Improve logging and monitoring
5. **Add Testing**: Add unit and integration tests

## Important Notes

- App selectors need to be customized based on actual Albert Heijn app structure
- Device must be connected via USB for automation to work
- Appium server must be running before starting backend
- Backend server must be running before using frontend
- MacBook and phone must be on same Wi-Fi network
- Albert Heijn app must be installed on target device

