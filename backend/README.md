# Albert Heijn Automation Backend

Backend service for automating Albert Heijn mobile app using Appium.

## Prerequisites

1. **Appium Server**: Install and run Appium server
   ```bash
   npm install -g appium
   appium
   ```

2. **iOS Setup** (for iOS devices):
   - Xcode installed
   - iOS device connected via USB
   - WebDriverAgent installed on device
   - Device UDID

3. **Android Setup** (for Android devices):
   - Android SDK installed
   - ADB configured
   - Android device connected via USB or emulator running
   - Albert Heijn app installed

## Installation

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

1. Copy `.env.example` to `.env`
2. Update configuration based on your device:
   - For iOS: Set `IOS_UDID`, `IOS_VERSION`, etc.
   - For Android: Set `AH_PACKAGE`, `AH_ACTIVITY`, etc.

## Running

```bash
python src/main.py
```

Or with uvicorn:
```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

- `GET /`: Health check
- `GET /health`: Detailed health status
- `POST /automate`: Start automation (HTTP)
- `WebSocket /ws/automate`: Start automation with real-time updates
- `POST /disconnect`: Disconnect Appium driver

## Notes

- The app selectors (IDs, XPaths) need to be customized based on the actual Albert Heijn app structure
- Use Appium Inspector to find the correct selectors for UI elements
- Device must be connected and Appium server running before starting automation

