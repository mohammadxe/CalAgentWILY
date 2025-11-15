# Project Overview - Albert Heijn Mobile App Automation

## 🎯 What We Have Now

A complete **Agentic AI-powered automation system** that allows you to control the Albert Heijn mobile app from your phone via an Expo app, while the actual automation runs on your MacBook using Python and Appium.

## 📁 Project Structure

```
agent/
├── backend/                      # Python FastAPI Backend (Runs on MacBook)
│   ├── src/
│   │   └── main.py              # Main automation server with Appium
│   ├── requirements.txt         # Python dependencies
│   ├── test_connection.py       # Test script for connections
│   ├── find_ip.py              # Helper to find MacBook IP
│   ├── create_env.sh           # Script to create .env file
│   └── README.md               # Backend documentation
│
├── frontend/                     # Expo React Native App (Runs on Phone)
│   ├── App.tsx                  # Main app component
│   ├── components/
│   │   ├── ProductList.tsx     # Product list UI component
│   │   └── AutomationControl.tsx # Automation control UI
│   ├── hooks/
│   │   └── useAutomation.ts    # Custom hook for automation logic
│   ├── types.ts                # TypeScript type definitions
│   ├── package.json            # Node.js dependencies
│   ├── app.json                # Expo configuration
│   ├── babel.config.js         # Babel configuration
│   ├── tsconfig.json           # TypeScript configuration
│   └── README.md               # Frontend documentation
│
├── README.md                    # Main project documentation
├── SETUP.md                     # Detailed setup instructions
├── CUSTOMIZATION.md            # Guide for customizing app selectors
├── QUICKSTART.md               # Quick start guide
└── .gitignore                  # Git ignore file
```

## 🏗️ Architecture

### How It Works

```
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│   Phone (Expo)  │  WebSocket │  MacBook (Backend) │  Appium  │  Phone Device │
│                 │ ◄────────► │                  │ ◄───────► │               │
│  - Add Products │  HTTP API  │  - FastAPI       │           │  Albert Heijn │
│  - Start Auto   │            │  - Appium        │           │  App          │
│  - View Status  │            │  - Automation    │           │               │
└─────────────────┘            └─────────────────┘           └─────────────────┘
```

1. **Frontend (Phone)**: Expo React Native app where you add products and start automation
2. **Backend (MacBook)**: FastAPI server that receives commands and controls the phone via Appium
3. **Device (Phone)**: Physical device with Albert Heijn app installed, controlled by Appium

### Communication Flow

1. User adds products in Expo app on phone
2. User taps "Start Automation"
3. Expo app sends WebSocket/HTTP request to MacBook backend
4. Backend connects to phone device via Appium
5. Backend automates Albert Heijn app:
   - Opens app
   - Searches for products
   - Adds products to basket
6. Backend sends real-time updates via WebSocket
7. Expo app displays progress and status

## 📦 What's Included

### Backend (Python/FastAPI)

✅ **FastAPI Server** (`backend/src/main.py`)
- REST API endpoints
- WebSocket support for real-time updates
- Appium integration for iOS/Android
- Error handling and logging

✅ **API Endpoints**
- `GET /`: Health check
- `GET /health`: Detailed health status
- `POST /automate`: Start automation (HTTP)
- `WebSocket /ws/automate`: Start automation with real-time updates
- `POST /disconnect`: Disconnect Appium driver

✅ **Automation Features**
- iOS and Android support
- Product search and selection
- Add to basket functionality
- Real-time progress updates
- Error handling

✅ **Helper Scripts**
- `find_ip.py`: Find MacBook IP address
- `test_connection.py`: Test backend and Appium connections
- `create_env.sh`: Create .env file from template

### Frontend (Expo/React Native)

✅ **Mobile App** (`frontend/App.tsx`)
- Product list management
- Add/remove products
- Quantity adjustment
- Device type selection (iOS/Android)
- Automation control

✅ **UI Components**
- `ProductList`: Display and manage products
- `AutomationControl`: Control automation with progress bar

✅ **Features**
- Real-time status updates via WebSocket
- HTTP API fallback
- Progress tracking
- Error handling
- Modern UI with React Native

✅ **Configuration**
- TypeScript support
- Expo configuration
- Babel configuration
- Package dependencies

### Documentation

✅ **Complete Documentation**
- `README.md`: Main project documentation
- `SETUP.md`: Detailed setup instructions
- `CUSTOMIZATION.md`: Guide for customizing app selectors
- `QUICKSTART.md`: Quick start guide
- `PROJECT_OVERVIEW.md`: This file

## 🚀 Features

### ✅ Implemented

1. **Backend Automation**
   - Appium integration for iOS/Android
   - Product search and selection
   - Add to basket functionality
   - Real-time progress updates
   - Error handling

2. **Frontend UI**
   - Product list management
   - Add/remove products
   - Quantity adjustment
   - Device type selection
   - Real-time status updates
   - Progress tracking

3. **Communication**
   - WebSocket for real-time updates
   - HTTP API as fallback
   - CORS support
   - Error handling

4. **Configuration**
   - Environment variables
   - Device configuration
   - Network configuration
   - App selector configuration

### ⚠️ Needs Customization

1. **App Selectors** (CRITICAL!)
   - Search input field selector
   - Product results selector
   - Add to basket button selector
   - Navigation button selectors
   - **Must be customized using Appium Inspector**

2. **Device Configuration**
   - iOS: Device UDID, iOS version, bundle ID
   - Android: Package name, activity name
   - **Must be configured in .env file**

3. **Network Configuration**
   - MacBook IP address
   - **Must be configured in frontend/App.tsx**

## 📋 Current Status

### ✅ Complete

- [x] Backend FastAPI server
- [x] Appium integration
- [x] WebSocket support
- [x] HTTP API endpoints
- [x] Frontend Expo app
- [x] Product list UI
- [x] Automation control UI
- [x] Real-time updates
- [x] Error handling
- [x] Documentation
- [x] Helper scripts

### 🔧 Needs Configuration

- [ ] App selectors (MUST be customized)
- [ ] Device configuration (.env file)
- [ ] Network configuration (IP address)
- [ ] Appium Inspector setup
- [ ] Device connection setup

### 📝 Next Steps

1. **Install Dependencies**
   - Backend: `pip install -r backend/requirements.txt`
   - Frontend: `npm install` in frontend directory
   - Appium: `npm install -g appium`

2. **Configure Environment**
   - Create `.env` file in backend directory
   - Update device configuration
   - Find MacBook IP address: `python backend/find_ip.py`
   - Update `API_BASE_URL` in `frontend/App.tsx`

3. **Find App Selectors** (CRITICAL!)
   - Install Appium Inspector
   - Connect to device
   - Inspect Albert Heijn app
   - Find selectors for:
     - Search input field
     - Product results
     - Add to basket button
     - Navigation buttons
   - Update selectors in `backend/src/main.py`

4. **Test Connection**
   - Start Appium server: `appium`
   - Start backend: `python backend/src/main.py`
   - Test connection: `python backend/test_connection.py`

5. **Run Frontend**
   - Start frontend: `npm start` in frontend directory
   - Scan QR code with Expo Go app
   - Test automation with one product

## 🎯 Key Files

### Backend
- `backend/src/main.py`: Main automation server
- `backend/requirements.txt`: Python dependencies
- `backend/test_connection.py`: Test connections
- `backend/find_ip.py`: Find IP address

### Frontend
- `frontend/App.tsx`: Main app component
- `frontend/components/ProductList.tsx`: Product list UI
- `frontend/components/AutomationControl.tsx`: Automation control UI
- `frontend/hooks/useAutomation.ts`: Automation logic
- `frontend/types.ts`: TypeScript types

### Documentation
- `README.md`: Main documentation
- `SETUP.md`: Setup instructions
- `CUSTOMIZATION.md`: Selector customization guide
- `QUICKSTART.md`: Quick start guide

## 🔍 Important Notes

1. **App Selectors Must Be Customized**
   - Current selectors are placeholders
   - Must find correct selectors using Appium Inspector
   - See `CUSTOMIZATION.md` for detailed instructions

2. **Device Connection Required**
   - Device must be connected via USB
   - Device must be trusted
   - Appium must be able to connect

3. **Network Configuration**
   - MacBook and phone must be on same Wi-Fi network
   - MacBook IP address must be configured in frontend
   - Firewall must allow connections on port 8000

4. **Appium Server Required**
   - Appium server must be running before starting backend
   - Appium must be able to connect to device
   - Device must be configured correctly

## 🚦 Getting Started

1. **Read Documentation**
   - Start with `QUICKSTART.md` for quick start
   - Read `SETUP.md` for detailed setup
   - Read `CUSTOMIZATION.md` for selector customization

2. **Install Dependencies**
   - Backend: Python dependencies
   - Frontend: Node.js dependencies
   - Appium: Global Appium installation

3. **Configure Environment**
   - Create `.env` file
   - Configure device settings
   - Find MacBook IP address

4. **Find App Selectors**
   - Use Appium Inspector
   - Find correct selectors
   - Update selectors in code

5. **Test and Run**
   - Test connections
   - Run automation
   - Verify functionality

## 📚 Documentation Links

- **Main Documentation**: `README.md`
- **Setup Guide**: `SETUP.md`
- **Customization Guide**: `CUSTOMIZATION.md`
- **Quick Start**: `QUICKSTART.md`
- **Backend Docs**: `backend/README.md`
- **Frontend Docs**: `frontend/README.md`

## 🎉 Summary

You now have a **complete automation system** that:
- ✅ Runs backend on MacBook
- ✅ Controls mobile app from phone
- ✅ Automates Albert Heijn app
- ✅ Provides real-time updates
- ✅ Handles errors gracefully
- ✅ Supports iOS and Android

**Next Critical Step**: Customize app selectors using Appium Inspector!

