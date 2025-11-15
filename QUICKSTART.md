# Quick Start Guide

## Overview

This app automates adding products to Albert Heijn shopping basket via mobile app using Agentic AI.

**Architecture:**
- **Backend (Python)**: Runs on MacBook, controls mobile app via Appium
- **Frontend (Expo)**: Runs on phone, sends commands to backend
- **Communication**: WebSocket for real-time updates

## 5-Minute Setup

### 1. Backend Setup (MacBook)

```bash
# Install dependencies
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Install Appium
npm install -g appium

# Create .env file
python find_ip.py  # Find your MacBook's IP address
# Manually create .env with device configuration
# See SETUP.md for details
```

### 2. Frontend Setup (Mobile)

```bash
# Install dependencies
cd frontend
npm install

# Update API_BASE_URL in App.tsx with your MacBook's IP
# See SETUP.md for finding IP address
```

### 3. Device Setup

1. **Connect device** to MacBook via USB
2. **Trust computer** on device
3. **Install Albert Heijn app** on device
4. **Update .env** with device configuration

### 4. Find App Selectors (IMPORTANT!)

**This is the most critical step!**

1. Start Appium server: `appium`
2. Open Appium Inspector
3. Connect to device
4. Find selectors for:
   - Search input field
   - Product results
   - Add to basket button
   - Navigation buttons
5. Update selectors in `backend/src/main.py`

See `CUSTOMIZATION.md` for detailed instructions.

## Running

### 1. Start Appium Server

```bash
appium
```

### 2. Start Backend Server

```bash
cd backend
source venv/bin/activate
python src/main.py
```

### 3. Start Frontend

```bash
cd frontend
npm start
```

Scan QR code with Expo Go app on your phone.

## Testing

### Test Connection

```bash
cd backend
python test_connection.py
```

This will test:
- Backend API
- Appium server
- Device connection

### Test Automation

1. Open Expo app on phone
2. Add products to list
3. Select device type (iOS/Android)
4. Tap "Start Automation"
5. Watch real-time progress

## Common Issues

### Connection Issues

- **Backend not reachable**: Check if backend is running, update IP address in App.tsx
- **Appium not connecting**: Check if Appium is running, verify device connection
- **Device not detected**: Check USB connection, trust settings, device configuration

### Selector Issues

- **Selectors not working**: Use Appium Inspector to find correct selectors
- **App updated**: Re-inspect app and update selectors
- **Element not found**: Add waits, check element visibility

### WebSocket Issues

- **WebSocket connection failed**: Check firewall, network connectivity
- **Fallback to HTTP**: Already implemented, should work automatically

## Next Steps

1. **Customize App Selectors**: Most important step - see `CUSTOMIZATION.md`
2. **Test with One Product**: Start with a single product to verify setup
3. **Add Error Handling**: Improve error handling and recovery
4. **Add Logging**: Improve logging and monitoring
5. **Add Testing**: Add unit and integration tests

## Documentation

- **SETUP.md**: Detailed setup instructions
- **CUSTOMIZATION.md**: Guide for customizing app selectors
- **README.md**: Full documentation
- **backend/README.md**: Backend-specific documentation
- **frontend/README.md**: Frontend-specific documentation

## Getting Help

1. **Check Documentation**: Read SETUP.md and CUSTOMIZATION.md
2. **Test Connection**: Run `python test_connection.py`
3. **Check Logs**: Check backend and Appium logs
4. **Use Appium Inspector**: Inspect app structure
5. **Test Selectors**: Test selectors individually

## Important Notes

- **App Selectors**: Must be customized based on actual Albert Heijn app structure
- **Device Connection**: Device must be connected via USB
- **Network**: MacBook and phone must be on same Wi-Fi network
- **Appium Server**: Must be running before starting backend
- **Backend Server**: Must be running before using frontend
- **Albert Heijn App**: Must be installed on target device

## Troubleshooting

### Backend Not Starting

1. Check Python version: `python3 --version`
2. Check dependencies: `pip list`
3. Check port 8000: `lsof -i :8000`
4. Check .env file: Verify configuration

### Appium Not Starting

1. Check Node.js version: `node --version`
2. Check Appium installation: `appium --version`
3. Check port 4723: `lsof -i :4723`
4. Check device connection: `adb devices` (Android) or `xcrun simctl list` (iOS)

### Frontend Not Connecting

1. Check backend is running: `curl http://localhost:8000/health`
2. Check IP address: Update API_BASE_URL in App.tsx
3. Check network: Ensure MacBook and phone are on same Wi-Fi
4. Check firewall: Allow connections on port 8000

### Device Not Detected

1. Check USB connection
2. Check device trust settings
3. Check device configuration in .env
4. Check Appium logs for errors

## Support

For issues or questions:
1. Check documentation first
2. Test connection with `test_connection.py`
3. Check logs for errors
4. Use Appium Inspector to debug selectors

