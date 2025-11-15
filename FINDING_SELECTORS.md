# How to Find Selectors Using Appium Inspector

## Step-by-Step Guide

### Step 1: Install Appium Inspector

#### Option 1: Download Appium Inspector (Recommended)
1. **Download Appium Inspector**
   - Go to: https://github.com/appium/appium-inspector/releases
   - Download the latest release for your OS (macOS/Windows/Linux)
   - Install the application

#### Option 2: Install via npm
```bash
npm install -g appium-inspector
```

#### Option 3: Use Web-based Inspector
- Appium 2.0+ includes a web-based inspector
- Access at: http://localhost:4723 (after starting Appium)

### Step 2: Install and Start Appium Server

#### Install Appium
```bash
npm install -g appium
```

#### Install Appium Drivers (if needed)
```bash
# For iOS
appium driver install xcuitest

# For Android
appium driver install uiautomator2
```

#### Start Appium Server
```bash
appium
```

You should see:
```
[Appium] Welcome to Appium v2.x.x
[Appium] Appium REST http interface listener started on 0.0.0.0:4723
```

**Keep this terminal window open!**

### Step 3: Connect Your Device

#### iOS Device
1. **Connect iPhone to MacBook via USB**
2. **Trust the computer** on iPhone
3. **Get Device UDID**:
   ```bash
   # macOS
   xcrun simctl list devices
   # Or
   instruments -s devices
   # Or
   idevice_id -l  # if you have libimobiledevice installed
   ```

4. **Get iOS Version**: Settings > General > About > Software Version

#### Android Device
1. **Connect Android device to MacBook via USB**
2. **Enable USB Debugging**:
   - Settings > About Phone > Tap "Build Number" 7 times
   - Settings > Developer Options > Enable "USB Debugging"
3. **Trust the computer** on Android device
4. **Verify connection**:
   ```bash
   adb devices
   ```
   You should see your device listed

### Step 4: Configure Appium Inspector

#### Open Appium Inspector

#### Configure Desired Capabilities

##### For iOS:
```json
{
  "platformName": "iOS",
  "platformVersion": "17.0",
  "deviceName": "iPhone",
  "udid": "YOUR_DEVICE_UDID",
  "bundleId": "nl.ah.ahapp",
  "automationName": "XCUITest",
  "noReset": true,
  "fullReset": false
}
```

##### For Android:
```json
{
  "platformName": "Android",
  "deviceName": "Android Device",
  "appPackage": "nl.ah.app",
  "appActivity": "nl.ah.app.MainActivity",
  "automationName": "UiAutomator2",
  "noReset": true,
  "fullReset": false
}
```

#### Important Settings:
- **Remote Host**: `localhost` or `127.0.0.1`
- **Remote Port**: `4723`
- **Remote Path**: `/wd/hub` (Appium 1.x) or `/` (Appium 2.x)

#### Start Session
1. Click **"Start Session"** button
2. Appium Inspector will:
   - Connect to Appium server
   - Connect to your device
   - Launch Albert Heijn app
   - Display the app screen

### Step 5: Inspect the Albert Heijn App

#### Navigate to Search Screen
1. **Look for Search Button/Icon**
   - Usually at the top of the screen
   - May have a magnifying glass icon
   - May say "Zoek" or "Search"

2. **Click on Search Button** in Appium Inspector
   - The element will be highlighted
   - Element details will appear in the right panel

3. **Find Element Properties**:
   - **Type**: Button, ImageButton, etc.
   - **Name/Label**: The text or accessibility label
   - **ID**: Element ID (if available)
   - **XPath**: Element XPath
   - **Accessibility ID**: Accessibility identifier

#### Example: Finding Search Button

**In Appium Inspector:**
- Click on the search button/icon
- Look at the element properties:
  - **iOS**: 
    - Name: "Zoek" or "Search"
    - Type: `XCUIElementTypeButton`
    - Accessibility ID: "Zoek" or "search_button"
  - **Android**:
    - Text: "Zoek" or "Search"
    - Content Description: "Zoek" or "search_button"
    - Resource ID: "nl.ah.app:id/search"

**Selector Options:**
```python
# iOS
(AppiumBy.ACCESSIBILITY_ID, "Zoek")
(AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Zoek']")

# Android
(AppiumBy.ID, "nl.ah.app:id/search")
(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Zoek']")
```

### Step 6: Find Search Input Field

#### After Clicking Search Button
1. **Search input field should appear**
2. **Click on the search input field** in Appium Inspector
3. **Find Element Properties**:
   - **Type**: TextField, EditText
   - **Placeholder**: "Zoek" or "Search"
   - **ID**: Element ID
   - **Accessibility ID**: Accessibility identifier

#### Example: Finding Search Input

**Element Properties:**
- **iOS**:
  - Type: `XCUIElementTypeSearchField` or `XCUIElementTypeTextField`
  - Placeholder: "Zoek" or "Search"
  - Accessibility ID: "search_field"
- **Android**:
  - Type: `android.widget.EditText`
  - Hint: "Zoek" or "Search"
  - Resource ID: "nl.ah.app:id/search_input"

**Selector Options:**
```python
# iOS
(AppiumBy.ACCESSIBILITY_ID, "search_field")
(AppiumBy.XPATH, "//XCUIElementTypeSearchField")
(AppiumBy.XPATH, "//XCUIElementTypeTextField[@placeholder='Zoek']")

# Android
(AppiumBy.ID, "nl.ah.app:id/search_input")
(AppiumBy.XPATH, "//android.widget.EditText[@hint='Zoek']")
```

### Step 7: Find Product Results

#### After Searching for a Product
1. **Search results should appear**
2. **Click on the first product** in Appium Inspector
3. **Find Element Properties**:
   - **Type**: Cell, ViewGroup
   - **ID**: Element ID
   - **XPath**: Element XPath

#### Example: Finding First Product

**Element Properties:**
- **iOS**:
  - Type: `XCUIElementTypeCell`
  - First cell in list
  - May have product name in it
- **Android**:
  - Type: `android.view.ViewGroup` or `android.widget.FrameLayout`
  - First item in RecyclerView
  - Resource ID: "nl.ah.app:id/product_card"

**Selector Options:**
```python
# iOS
(AppiumBy.XPATH, "//XCUIElementTypeCell[1]")
(AppiumBy.XPATH, "//XCUIElementTypeCell[@visible='true'][1]")

# Android
(AppiumBy.XPATH, "//android.widget.RecyclerView/android.view.ViewGroup[1]")
(AppiumBy.ID, "nl.ah.app:id/product_card")
```

### Step 8: Find "Voeg toe" Button

#### On Product Detail Page
1. **Navigate to product detail page**
2. **Click on "Voeg toe" button** in Appium Inspector
3. **Find Element Properties**:
   - **Type**: Button
   - **Text**: "Voeg toe" or "Voeg toe: [Product Name]"
   - **Accessibility ID**: "Voeg toe"
   - **ID**: Element ID

#### Example: Finding "Voeg toe" Button

**Element Properties:**
- **iOS**:
  - Type: `XCUIElementTypeButton`
  - Name: "Voeg toe" or "Voeg toe: Melk"
  - Accessibility ID: "Voeg toe"
- **Android**:
  - Type: `android.widget.Button`
  - Text: "Voeg toe" or "Voeg toe: Melk"
  - Content Description: "Voeg toe"
  - Resource ID: "nl.ah.app:id/add_to_basket"

**Selector Options:**
```python
# iOS
(AppiumBy.ACCESSIBILITY_ID, "Voeg toe")
(AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name, 'Voeg toe')]")

# Android
(AppiumBy.ID, "nl.ah.app:id/add_to_basket")
(AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Voeg toe')]")
```

### Step 9: Find + Button (for Quantities)

#### After Clicking "Voeg toe" Button
1. **Button may change to show quantity**
2. **Look for + button** to increment quantity
3. **Click on + button** in Appium Inspector
4. **Find Element Properties**:
   - **Type**: Button
   - **Text**: "+"
   - **Accessibility ID**: "+"
   - **ID**: Element ID

#### Example: Finding + Button

**Element Properties:**
- **iOS**:
  - Type: `XCUIElementTypeButton`
  - Name: "+"
  - Accessibility ID: "+"
- **Android**:
  - Type: `android.widget.Button`
  - Text: "+"
  - Content Description: "+"
  - Resource ID: "nl.ah.app:id/increment"

**Selector Options:**
```python
# iOS
(AppiumBy.ACCESSIBILITY_ID, "+")
(AppiumBy.XPATH, "//XCUIElementTypeButton[@name='+']")

# Android
(AppiumBy.ID, "nl.ah.app:id/increment")
(AppiumBy.XPATH, "//android.widget.Button[@text='+']")
```

### Step 10: Find Back Button

#### On Product Detail Page
1. **Look for back button** (usually top-left)
2. **Click on back button** in Appium Inspector
3. **Find Element Properties**:
   - **Type**: Button, NavigationBar
   - **Name**: "Back" or "<"
   - **Accessibility ID**: "Back"

#### Example: Finding Back Button

**Element Properties:**
- **iOS**:
  - Type: `XCUIElementTypeButton`
  - Name: "Back" or "<"
  - In NavigationBar
- **Android**:
  - Type: `android.widget.ImageButton`
  - Content Description: "Navigate up" or "Back"
  - Resource ID: "android:id/home"

**Selector Options:**
```python
# iOS
(AppiumBy.ACCESSIBILITY_ID, "Back")
(AppiumBy.XPATH, "//XCUIElementTypeNavigationBar//XCUIElementTypeButton[1]")

# Android
(AppiumBy.ID, "android:id/home")
(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
```

## Understanding Selector Types

### 1. Accessibility ID (Best Choice)
- **Most stable** across app updates
- **Works for both iOS and Android** (if app uses accessibility)
- **Example**: `AppiumBy.ACCESSIBILITY_ID, "Zoek"`

### 2. ID (Android) / Name (iOS)
- **Fast and reliable**
- **Platform-specific**
- **Example**: `AppiumBy.ID, "nl.ah.app:id/search"` (Android)

### 3. XPath (Flexible but Fragile)
- **Most flexible** but can break with UI changes
- **Platform-specific syntax**
- **Example**: `AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Zoek']"`

### 4. Class Name (Less Specific)
- **Finds element type** but not specific element
- **Use when other selectors don't work**
- **Example**: `AppiumBy.CLASS_NAME, "XCUIElementTypeButton"`

## Testing Selectors

### Test in Appium Inspector
1. **Click on element** in Appium Inspector
2. **Copy selector** from element properties
3. **Use "Find Element"** feature to test selector
4. **Verify element is found** correctly

### Test in Code
```python
# Test selector
try:
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Zoek")
    print(f"✅ Found element: {element}")
except Exception as e:
    print(f"❌ Failed to find element: {e}")
```

## Updating Selectors in Code

### Step 1: Open `backend/src/ah_automation.py`

### Step 2: Update Search Button Selectors

**Find this section:**
```python
search_selectors = [
    # iOS selectors
    (AppiumBy.ACCESSIBILITY_ID, "Zoek"),
    (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Zoek']"),
    # Android selectors
    (AppiumBy.ID, "nl.ah.app:id/search"),
]
```

**Replace with your found selectors:**
```python
search_selectors = [
    # iOS selectors - UPDATE THESE
    (AppiumBy.ACCESSIBILITY_ID, "YOUR_FOUND_ACCESSIBILITY_ID"),
    (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='YOUR_FOUND_NAME']"),
    # Android selectors - UPDATE THESE
    (AppiumBy.ID, "YOUR_FOUND_ID"),
    (AppiumBy.XPATH, "//android.widget.Button[@content-desc='YOUR_FOUND_DESC']"),
]
```

### Step 3: Update Search Input Selectors

**Find this section:**
```python
search_selectors = [
    # iOS selectors
    (AppiumBy.ACCESSIBILITY_ID, "search_field"),
    (AppiumBy.XPATH, "//XCUIElementTypeSearchField"),
    # Android selectors
    (AppiumBy.ID, "nl.ah.app:id/search_input"),
]
```

**Replace with your found selectors**

### Step 4: Update Product Selectors

**Find this section:**
```python
product_selectors = [
    # iOS selectors
    (AppiumBy.XPATH, "//XCUIElementTypeCell[1]"),
    # Android selectors
    (AppiumBy.ID, "nl.ah.app:id/product_card"),
]
```

**Replace with your found selectors**

### Step 5: Update "Voeg toe" Button Selectors

**Find this section:**
```python
button_selectors = [
    # iOS selectors
    (AppiumBy.ACCESSIBILITY_ID, "Voeg toe"),
    (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name, 'Voeg toe')]"),
    # Android selectors
    (AppiumBy.ID, "nl.ah.app:id/add_to_basket"),
]
```

**Replace with your found selectors**

### Step 6: Test Updated Selectors

```bash
# Start Appium server
appium

# Start backend
cd backend
python src/main.py

# Test with one product
# Use frontend or test script
```

## Common Issues and Solutions

### Issue 1: Element Not Found
**Solution:**
- Check if element is visible
- Wait for element to load
- Try different selector
- Check if app structure changed

### Issue 2: Multiple Elements Found
**Solution:**
- Use more specific selector
- Use XPath with index `[1]`
- Use parent/child relationship

### Issue 3: Selector Works Sometimes
**Solution:**
- Add wait for element
- Check element visibility
- Add retry logic
- Use multiple selectors with fallback

### Issue 4: App Structure Changed
**Solution:**
- Re-inspect app in Appium Inspector
- Update selectors
- Test again

## Best Practices

### 1. Use Accessibility ID First
- Most stable
- Works across platforms
- App should have accessibility labels

### 2. Use Multiple Selectors
- Provide fallback options
- Try different selector types
- Handle app updates

### 3. Test Selectors
- Test in Appium Inspector first
- Test in code
- Test on different devices

### 4. Document Selectors
- Keep list of working selectors
- Note app version
- Update when app changes

### 5. Handle Errors
- Add try-catch blocks
- Provide fallback selectors
- Log errors for debugging

## Quick Reference

### iOS Selectors
```python
# Accessibility ID (Best)
AppiumBy.ACCESSIBILITY_ID, "Zoek"

# XPath
AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Zoek']"

# Name
AppiumBy.NAME, "Zoek"

# Class Name
AppiumBy.CLASS_NAME, "XCUIElementTypeButton"
```

### Android Selectors
```python
# ID (Best)
AppiumBy.ID, "nl.ah.app:id/search"

# XPath
AppiumBy.XPATH, "//android.widget.Button[@content-desc='Zoek']"

# Accessibility ID
AppiumBy.ACCESSIBILITY_ID, "Zoek"

# Class Name
AppiumBy.CLASS_NAME, "android.widget.Button"
```

## Next Steps

1. **Install Appium Inspector**
2. **Start Appium Server**
3. **Connect Device**
4. **Inspect Albert Heijn App**
5. **Find Selectors** for:
   - Search button
   - Search input
   - Product results
   - "Voeg toe" button
   - + button (quantities)
   - Back button
6. **Update Selectors** in `ah_automation.py`
7. **Test Selectors** in code
8. **Test Automation** with one product
9. **Test with Multiple Products**
10. **Adjust if Needed**

## Resources

- **Appium Inspector**: https://github.com/appium/appium-inspector
- **Appium Documentation**: https://appium.io/docs/en/2.1/
- **XCUIElement Query**: https://developer.apple.com/documentation/xctest/xcuielementquery
- **UiAutomator2**: https://developer.android.com/training/testing/ui-automator

