# Albert Heijn Automation - Expo Frontend

React Native mobile app built with Expo for controlling Albert Heijn automation.

## Prerequisites

- Node.js (v18 or higher)
- Expo CLI
- iOS Simulator (for iOS) or Android Emulator (for Android)
- Physical device with Expo Go app installed

## Installation

```bash
cd frontend
npm install
```

## Configuration

Update the `API_BASE_URL` in `App.tsx` to point to your MacBook's IP address:

```typescript
const API_BASE_URL = __DEV__ 
  ? 'http://YOUR_MACBOOK_IP:8000'  // Replace with your MacBook's IP
  : 'http://your-server.com:8000';
```

To find your MacBook's IP address:
- macOS: System Preferences > Network > Wi-Fi > Advanced > TCP/IP

## Running

### Development

```bash
npm start
```

Then:
- Press `i` for iOS simulator
- Press `a` for Android emulator
- Scan QR code with Expo Go app on physical device

### Build

```bash
# iOS
expo build:ios

# Android
expo build:android
```

## Features

- Add/remove products
- Adjust quantities
- Select device type (iOS/Android)
- Real-time automation status
- Progress tracking
- WebSocket connection for live updates

## Notes

- Make sure your MacBook and phone are on the same network
- Backend server must be running on your MacBook
- Appium server must be running and connected to device
- Albert Heijn app must be installed on the target device

