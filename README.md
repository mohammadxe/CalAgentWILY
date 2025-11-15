# Albert Heijn Mobile App Automation

Agentic AI-powered automation system for adding products to Albert Heijn shopping basket via mobile app.

## Architecture

- **Backend (Python)**: FastAPI server with Appium for mobile app automation
- **Frontend (Expo)**: React Native mobile app for controlling automation
- **Communication**: WebSocket for real-time updates, HTTP API as fallback
- **Automation**: Appium for iOS/Android app automation

## Project Structure

```
.
├── backend/           # Python FastAPI backend
│   ├── src/
│   │   └── main.py   # Main automation server
│   ├── requirements.txt
│   └── README.md
└── frontend/          # Expo React Native frontend
    ├── App.tsx       # Main app component
    ├── components/   # UI components
    ├── hooks/        # Custom hooks
    ├── types.ts      # TypeScript types
    └── README.md
```

## Prerequisites

### Backend (MacBook)

1. **Python 3.9+**
2. **Appium Server**
   ```bash
   npm install -g appium
   appium
   ```

3. **iOS Setup** (if using iOS):
   - Xcode installed
   - iOS device connected via USB
   - WebDriverAgent installed
   - Device UDID

4. **Android Setup** (if using Android):
   - Android SDK installed
   - ADB configured
   - Android device connected or emulator running

### Frontend (Mobile)

1. **Node.js 18+**
2. **Expo CLI**
3. **Physical device** with Albert Heijn app installed
4. **Expo Go app** installed on device (for development)

## Setup

### 1. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your device configuration
```

### 2. Frontend Setup

```bash
cd frontend
npm install

# Update API_BASE_URL in App.tsx with your MacBook's IP address
```

### 3. Configure Device

1. Connect your iOS/Android device to MacBook via USB
2. Ensure Appium server is running
3. Update `.env` file with device details:
   - iOS: `IOS_UDID`, `IOS_VERSION`, `AH_BUNDLE_ID`
   - Android: `AH_PACKAGE`, `AH_ACTIVITY`

## Running

### 1. Start Appium Server

```bash
appium
```

### 2. Start Backend Server

```bash
cd backend
python src/main.py
# Or: uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Start Frontend

```bash
cd frontend
npm start
```

Scan QR code with Expo Go app on your phone.

## Usage

1. Open the Expo app on your phone
2. Add products you want to purchase
3. Select device type (iOS/Android)
4. Tap "Start Automation"
5. Watch real-time progress as products are added to Albert Heijn basket

## Important Notes

### App Selectors (CRITICAL!)

**The app selectors in `backend/src/main.py` are placeholder values and MUST be customized!**

The most critical step is finding the correct selectors for the Albert Heijn app:

1. Use **Appium Inspector** to inspect the Albert Heijn app
2. Find the correct selectors for:
   - Search input field
   - Product results
   - Add to basket button
   - Navigation buttons

3. Update the selectors in `main.py`

See `CUSTOMIZATION.md` for detailed instructions on finding and updating selectors.

### Network Configuration

- Ensure MacBook and phone are on the same Wi-Fi network
- Update `API_BASE_URL` in `frontend/App.tsx` with MacBook's IP address
- Firewall may need to allow connections on port 8000

### Device Connection

- iOS: Device must be connected via USB and trusted
- Android: Device must be connected via USB with USB debugging enabled
- Appium must be able to connect to the device

## Troubleshooting

### Connection Issues

- Check if backend is running: `curl http://localhost:8000/health`
- Check if Appium is running: `curl http://localhost:4723/wd/hub/status`
- Verify device connection: `adb devices` (Android) or `xcrun simctl list` (iOS)

### App Selector Issues

- Use Appium Inspector to find correct selectors
- Check if app structure has changed
- Verify bundle ID/package name is correct

### WebSocket Issues

- Check firewall settings
- Verify network connectivity
- Check browser console for WebSocket errors
- Fallback to HTTP API if WebSocket fails

## Development

### Backend

- API documentation: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

### Frontend

- Hot reload enabled
- TypeScript for type safety
- Expo Router for navigation (if needed)

## Next Steps

1. **Customize App Selectors**: Use Appium Inspector to find correct selectors for Albert Heijn app
2. **Add Error Handling**: Improve error handling and recovery
3. **Add Product Search**: Implement smarter product search and selection
4. **Add Authentication**: Handle Albert Heijn app login if needed
5. **Add Testing**: Add unit and integration tests
6. **Add Logging**: Improve logging and monitoring

## License

MIT

