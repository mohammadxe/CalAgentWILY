# How to Install and Run Appium Server

## Step-by-Step Installation Guide

### Prerequisites

1. **Node.js and npm** must be installed
   - Check if installed: `node --version` and `npm --version`
   - If not installed: Download from https://nodejs.org/

2. **For iOS**: Xcode must be installed (macOS only)
3. **For Android**: Android SDK must be installed

### Installation Methods

## Method 1: Install Appium Globally (Recommended)

### Install Appium
```bash
npm install -g appium
```

### Verify Installation
```bash
appium --version
```

You should see something like: `3.x.x` or `2.x.x`

### Start Appium Server
```bash
appium
```

### If `appium` command doesn't work:

#### Option 1: Use npx (No Installation Required)
```bash
npx appium
```

#### Option 2: Install Appium Doctor (Helps diagnose issues)
```bash
npm install -g appium-doctor
appium-doctor
```

#### Option 3: Check PATH
```bash
# Check if appium is in PATH
which appium

# If not found, find where npm installs global packages
npm root -g

# Add to PATH (if needed)
export PATH=$PATH:$(npm root -g)/../bin
```

## Method 2: Install Appium via npx (No Installation)

### Run Appium without installing
```bash
npx appium
```

This will download and run Appium temporarily.

### Install Appium Drivers

After Appium is running, you need to install drivers:

```bash
# For iOS
appium driver install xcuitest

# For Android
appium driver install uiautomator2
```

### If using npx:
```bash
npx appium driver install xcuitest
npx appium driver install uiautomator2
```

## Method 3: Install Appium 2.0 (Latest Version)

### Install Appium 2.0
```bash
npm install -g appium@next
```

### Or install specific version
```bash
npm install -g appium@2.0.0
```

### Verify Installation
```bash
appium --version
```

## Troubleshooting

### Issue 1: "appium: command not found"

**Solution 1: Use npx**
```bash
npx appium
```

**Solution 2: Install globally**
```bash
npm install -g appium
```

**Solution 3: Check npm global path**
```bash
# Find npm global path
npm root -g

# Add to PATH (macOS/Linux)
export PATH=$PATH:$(npm root -g)/../bin

# Add to PATH (Windows)
# Add to System Environment Variables
```

### Issue 2: "Permission denied"

**Solution: Use sudo (macOS/Linux)**
```bash
sudo npm install -g appium
```

**Or fix npm permissions:**
```bash
# Create .npm directory
mkdir ~/.npm-global

# Configure npm to use new directory
npm config set prefix '~/.npm-global'

# Add to PATH
export PATH=~/.npm-global/bin:$PATH

# Install Appium
npm install -g appium
```

### Issue 3: "EACCES: permission denied"

**Solution: Fix npm permissions**
```bash
# Option 1: Use sudo (not recommended)
sudo npm install -g appium

# Option 2: Fix npm permissions (recommended)
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
npm install -g appium
```

### Issue 4: Appium starts but can't connect to device

**Solution: Install drivers**
```bash
# For iOS
appium driver install xcuitest

# For Android
appium driver install uiautomator2
```

### Issue 5: "Driver not found"

**Solution: List and install drivers**
```bash
# List available drivers
appium driver list

# Install driver
appium driver install xcuitest
appium driver install uiautomator2
```

## Quick Start Commands

### 1. Install Appium
```bash
npm install -g appium
```

### 2. Install Drivers
```bash
appium driver install xcuitest      # For iOS
appium driver install uiautomator2  # For Android
```

### 3. Start Appium Server
```bash
appium
```

### 4. Verify Appium is Running
```bash
# In another terminal
curl http://localhost:4723/wd/hub/status
```

You should see a JSON response with status information.

## Alternative: Use Appium Desktop (GUI)

### Download Appium Desktop
1. Go to: https://github.com/appium/appium-desktop/releases
2. Download for your OS (macOS/Windows/Linux)
3. Install and run

### Start Appium Desktop
1. Open Appium Desktop
2. Click "Start Server"
3. Server will start on port 4723

## Platform-Specific Instructions

### macOS (iOS)

1. **Install Xcode**
   ```bash
   xcode-select --install
   ```

2. **Install CocoaPods**
   ```bash
   sudo gem install cocoapods
   ```

3. **Install Appium**
   ```bash
   npm install -g appium
   ```

4. **Install iOS Driver**
   ```bash
   appium driver install xcuitest
   ```

### Windows (Android)

1. **Install Node.js**
   - Download from: https://nodejs.org/

2. **Install Appium**
   ```bash
   npm install -g appium
   ```

3. **Install Android Driver**
   ```bash
   appium driver install uiautomator2
   ```

### Linux (Android)

1. **Install Node.js**
   ```bash
   sudo apt-get update
   sudo apt-get install nodejs npm
   ```

2. **Install Appium**
   ```bash
   npm install -g appium
   ```

3. **Install Android Driver**
   ```bash
   appium driver install uiautomator2
   ```

## Verify Installation

### Check Appium Version
```bash
appium --version
```

### Check Drivers
```bash
appium driver list
```

### Test Appium Server
```bash
# Start Appium
appium

# In another terminal, test connection
curl http://localhost:4723/wd/hub/status
```

## Start Appium with Options

### Start on Specific Port
```bash
appium --port 4723
```

### Start with Logging
```bash
appium --log-level debug
```

### Start with Specific IP
```bash
appium --address 0.0.0.0 --port 4723
```

## Common Commands

### Start Appium
```bash
appium
```

### Stop Appium
- Press `Ctrl+C` in the terminal
- Or close the terminal window

### Check if Appium is Running
```bash
curl http://localhost:4723/wd/hub/status
```

### List Installed Drivers
```bash
appium driver list
```

### Install Driver
```bash
appium driver install <driver-name>
```

### Uninstall Driver
```bash
appium driver uninstall <driver-name>
```

## Next Steps

After Appium is installed and running:

1. **Install Appium Inspector** (for finding selectors)
   ```bash
   npm install -g appium-inspector
   ```

2. **Connect Device** (iOS or Android)

3. **Start Appium Server**
   ```bash
   appium
   ```

4. **Open Appium Inspector** and connect to device

5. **Find Selectors** for Albert Heijn app

## Resources

- **Appium Documentation**: https://appium.io/docs/en/2.1/
- **Appium GitHub**: https://github.com/appium/appium
- **Appium Desktop**: https://github.com/appium/appium-desktop
- **Node.js**: https://nodejs.org/

