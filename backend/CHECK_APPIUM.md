# Quick Check: Is Appium Installed?

## Quick Check Commands

### 1. Check if Node.js is installed
```bash
node --version
```

**Expected output**: `v18.x.x` or similar

**If not installed**: Download from https://nodejs.org/

### 2. Check if npm is installed
```bash
npm --version
```

**Expected output**: `9.x.x` or similar

**If not installed**: Comes with Node.js, reinstall Node.js if missing

### 3. Check if Appium is installed
```bash
appium --version
```

**Expected output**: `3.x.x` or `2.x.x`

**If not installed**: See installation instructions below

### 4. Try using npx (No Installation Required)
```bash
npx appium --version
```

**This works even if Appium is not installed globally!**

## Quick Installation

### Option 1: Install Globally (Recommended)
```bash
npm install -g appium
```

### Option 2: Use npx (No Installation)
```bash
npx appium
```

This downloads and runs Appium temporarily without installing.

### Option 3: Use the Start Scripts

**macOS/Linux:**
```bash
cd backend
chmod +x start_appium.sh
./start_appium.sh
```

**Windows:**
```bash
cd backend
start_appium.bat
```

## Common Issues

### Issue: "appium: command not found"

**Solution 1: Use npx**
```bash
npx appium
```

**Solution 2: Install globally**
```bash
npm install -g appium
```

**Solution 3: Check PATH**
```bash
# Check npm global path
npm root -g

# Add to PATH if needed
export PATH=$PATH:$(npm root -g)/../bin
```

### Issue: "Permission denied"

**Solution: Use sudo (macOS/Linux)**
```bash
sudo npm install -g appium
```

### Issue: "EACCES: permission denied"

**Solution: Fix npm permissions**
```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
npm install -g appium
```

## Verify Installation

### Test Appium Server
```bash
# Start Appium (in one terminal)
appium
# Or
npx appium

# In another terminal, test connection
curl http://localhost:4723/wd/hub/status
```

**Expected output**: JSON response with status information

## Next Steps

1. **Install Appium** (if not installed)
2. **Install Drivers** (if needed)
   ```bash
   appium driver install xcuitest      # For iOS
   appium driver install uiautomator2  # For Android
   ```
3. **Start Appium Server**
   ```bash
   appium
   # Or
   npx appium
   ```
4. **Verify it's running**
   ```bash
   curl http://localhost:4723/wd/hub/status
   ```

