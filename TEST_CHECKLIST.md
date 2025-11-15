# Test Checklist - What's Missing

## 🔴 Critical Missing Items

### 1. **Environment Configuration File (.env)**
- ❌ **Missing**: `.env` file in `backend/` directory
- **Required variables**:
  ```
  APPIUM_SERVER_URL=http://localhost:4723
  IOS_DEVICE_NAME=iPhone
  IOS_VERSION=17.0
  IOS_UDID=                    # REQUIRED: Your device UDID
  AH_BUNDLE_ID=nl.ah.ahapp     # Verify this is correct
  ANDROID_DEVICE_NAME=Android Device
  AH_PACKAGE=nl.ah.app         # Verify this is correct
  AH_ACTIVITY=nl.ah.app.MainActivity  # Verify this is correct
  BACKEND_PORT=8000
  ```
- **Action**: Create `.env` file using `backend/create_env.sh` or manually

### 2. **Appium Server URL Inconsistency**
- ⚠️ **Issue**: `test_connection.py` uses `/wd/hub` but `main.py` doesn't
- **Location**: 
  - `backend/test_connection.py:40` uses `http://localhost:4723/wd/hub/status`
  - `backend/test_connection.py:60` uses `http://localhost:4723/wd/hub`
  - `backend/src/main.py:85` uses `http://localhost:4723` (no `/wd/hub`)
- **Action**: Standardize Appium URL format (Appium 2.x uses `/` not `/wd/hub`)

### 3. **App Selectors (CRITICAL)**
- ❌ **Missing**: Actual working selectors for Albert Heijn app
- **Current status**: All selectors in `backend/src/ah_automation.py` are placeholders
- **Required selectors**:
  - Search button/icon
  - Search input field
  - Product results (first product)
  - "Voeg toe" (Add to cart) button
  - Plus (+) button for quantities
  - Back/navigation buttons
- **Action**: 
  1. Open Appium Inspector (see `OPEN_APPIUM_INSPECTOR.md`)
  2. Connect to device
  3. Find actual selectors
  4. Test with `backend/find_selectors_guide.py`
  5. Update `backend/src/ah_automation.py`

### 4. **Frontend API Configuration**
- ⚠️ **Missing**: Actual MacBook IP address in frontend
- **Location**: `frontend/App.tsx:22-24`
- **Current**: `http://192.168.1.XXX:8000` (placeholder)
- **Action**: Replace `XXX` with your MacBook's actual IP address

### 5. **Device-Specific Configuration**
- ❌ **Missing**: Device UDID (for iOS)
- ❌ **Missing**: Verified bundle ID/package name
- ❌ **Missing**: Verified activity name (for Android)
- **Action**: 
  - iOS: Get UDID using `xcrun simctl list devices` or `instruments -s devices`
  - Verify bundle ID: `nl.ah.ahapp` (iOS) or `nl.ah.app` (Android)
  - Verify activity name for Android

## 🟡 Prerequisites to Verify

### 6. **Appium Server**
- ⚠️ **Status**: Need to verify installation
- **Check**: Run `appium --version`
- **Action**: Install if missing: `npm install -g appium`

### 7. **Appium Inspector**
- ⚠️ **Status**: Need to verify can be opened
- **Check**: Try `npx appium-inspector` or download desktop app
- **Action**: Follow `OPEN_APPIUM_INSPECTOR.md` guide

### 8. **Python Dependencies**
- ⚠️ **Status**: Need to verify installation
- **Check**: Run `pip list` in backend virtual environment
- **Action**: Install if missing: `pip install -r backend/requirements.txt`

### 9. **Device Connection**
- ⚠️ **Status**: Need to verify device is connected
- **Check**: 
  - iOS: Device appears in Xcode or `xcrun simctl list devices`
  - Android: `adb devices` shows device
- **Action**: Connect device via USB and trust computer

### 10. **Albert Heijn App**
- ⚠️ **Status**: Need to verify app is installed
- **Check**: App should be visible on device
- **Action**: Install Albert Heijn app from App Store/Play Store

### 11. **Backend Server Running**
- ⚠️ **Status**: Need to verify can start
- **Check**: Run `python backend/src/main.py`
- **Action**: Fix any import or configuration errors

### 12. **Frontend Dependencies**
- ⚠️ **Status**: Need to verify installation
- **Check**: Run `npm list` in frontend directory
- **Action**: Install if missing: `npm install` in frontend directory

## 🟢 Code Issues to Fix

### 13. **Appium URL Path Inconsistency**
- **Issue**: Mixed use of `/wd/hub` (Appium 1.x) vs `/` (Appium 2.x)
- **Files affected**:
  - `backend/test_connection.py:40` - uses `/wd/hub/status`
  - `backend/test_connection.py:60` - uses `/wd/hub`
  - `backend/src/main.py:85` - uses base URL only
- **Action**: Determine Appium version and standardize

### 14. **Missing Error Handling**
- **Issue**: Some error cases not handled gracefully
- **Action**: Review and add error handling where needed

## 📋 Test Execution Checklist

Before running `backend/test_connection.py`, ensure:

1. ✅ `.env` file exists and is configured
2. ✅ Appium server is running (`appium`)
3. ✅ Device is connected via USB
4. ✅ Device is trusted
5. ✅ Albert Heijn app is installed
6. ✅ Python virtual environment is activated
7. ✅ All Python dependencies are installed
8. ✅ Backend can start without errors

## 🎯 Priority Order

1. **HIGHEST PRIORITY**:
   - Create `.env` file with device configuration
   - Fix Appium URL inconsistency
   - Find actual app selectors using Appium Inspector

2. **HIGH PRIORITY**:
   - Configure frontend API_BASE_URL
   - Verify device connection
   - Verify Appium server is running

3. **MEDIUM PRIORITY**:
   - Verify all dependencies installed
   - Test individual components
   - Update selectors in code

4. **LOW PRIORITY**:
   - Improve error handling
   - Add logging improvements
   - Documentation updates

## 🔧 Quick Fixes Needed

1. **Create .env file**:
   
   **Windows (PowerShell):**
   ```powershell
   cd backend
   .\create_env.ps1
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   cd backend
   create_env.bat
   ```
   
   **macOS/Linux:**
   ```bash
   cd backend
   bash create_env.sh
   ```
   
   **Or manually create** `backend/.env` with the template content.
   
   Then edit `.env` with your device details (especially `IOS_UDID` for iOS devices).

2. **Fix Appium URL** (if using Appium 2.x):
   - Update `test_connection.py` to remove `/wd/hub` paths
   - Or update `main.py` to add `/wd/hub` if using Appium 1.x

3. **Configure Frontend**:
   - Find MacBook IP: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
   - Update `frontend/App.tsx:23` with actual IP

4. **Find Selectors**:
   - Start Appium: `appium`
   - Open Inspector: `npx appium-inspector`
   - Connect to device
   - Find and test selectors
   - Update `backend/src/ah_automation.py`

