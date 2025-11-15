# Adaptation Summary: Web Automation → Mobile App Automation

## What Was Done

I've successfully adapted your Albert Heijn **web automation code** (that used Selenium + Chrome) to work with **mobile app automation** using Appium.

## Key Files Created/Modified

### 1. `backend/src/ah_automation.py` (NEW)
- **Complete mobile app automation module**
- Adapted all functions from web automation:
  - `search_item()` - Search for products in mobile app
  - `click_first_product()` - Click first product in search results
  - `click_voeg_toe_button()` - Click "Voeg toe" button with quantity support
  - `add_first_product_to_cart()` - Add product to cart
  - `add_item()` - Search and add item
  - `add_multiple_products()` - Add multiple products with quantities

### 2. `backend/src/main.py` (MODIFIED)
- **Updated to use new automation functions**
- Integrates `ah_automation.py` module
- Handles quantities properly
- Maintains WebSocket support for real-time updates

### 3. `backend/MIGRATION.md` (NEW)
- **Detailed migration guide**
- Explains all changes from web to mobile
- Selector strategy documentation
- Platform-specific differences

## Key Adaptations

### 1. Selenium → Appium
- ✅ Replaced Selenium WebDriver with Appium WebDriver
- ✅ Changed from Chrome browser to mobile device
- ✅ Updated all driver initialization

### 2. CSS Selectors → Appium Selectors
- ✅ Replaced CSS selectors with Appium selectors
- ✅ Added iOS-specific selectors (XCUIElementType*)
- ✅ Added Android-specific selectors (android.widget.*)
- ✅ Multiple selector fallback strategy (same as web version)

### 3. Browser Navigation → App Navigation
- ✅ Removed `driver.get()` - app is already open
- ✅ Added search button click to open search
- ✅ Updated back navigation for mobile

### 4. Human-like Behavior Preserved
- ✅ Typing delays (0.05 seconds between characters)
- ✅ Wait times between actions
- ✅ Scrolling elements into view
- ✅ Multiple fallback strategies
- ✅ Detailed logging

### 5. Quantity Handling
- ✅ Added quantity support (click button multiple times)
- ✅ Detects + button for incrementing quantity
- ✅ Handles quantity changes properly

### 6. Error Handling
- ✅ Multiple selector fallbacks
- ✅ Multiple click methods (click, tap, touch action)
- ✅ Comprehensive error logging
- ✅ Graceful failure handling

## Features Maintained

### ✅ All Original Features
1. **Search Products** - Search with human-like typing
2. **Click First Product** - Click first search result
3. **Add to Basket** - Click "Voeg toe" button
4. **Handle Quantities** - Support for multiple quantities
5. **Multiple Products** - Add multiple products
6. **Error Handling** - Comprehensive error handling
7. **Logging** - Detailed logging for debugging
8. **Summary** - Summary of added/failed items

### ✅ New Features
1. **Platform Support** - iOS and Android
2. **Multiple Selectors** - Fallback selector strategy
3. **Mobile-Specific** - Mobile scrolling, tapping, etc.
4. **WebSocket Support** - Real-time updates (maintained)
5. **Quantity Support** - Proper quantity handling

## Selector Strategy

### Multiple Selector Fallback
Same strategy as web version - tries multiple selectors until one works:

```python
search_selectors = [
    # iOS selectors
    (AppiumBy.ACCESSIBILITY_ID, "Zoek"),
    (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Zoek']"),
    # Android selectors
    (AppiumBy.ID, "nl.ah.app:id/search"),
    (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Zoek']"),
]
```

### Selector Types Used
1. **Accessibility ID** (Preferred) - Most stable
2. **XPath** (Fallback) - Flexible but fragile
3. **ID** (Android) - Fast and reliable
4. **Class Name** (Fallback) - Less specific

## What Needs to Be Done

### ⚠️ CRITICAL: Find Actual Selectors

The current selectors are **placeholders** and must be customized:

1. **Install Appium Inspector**
   ```bash
   npm install -g appium-inspector
   ```

2. **Connect to Device**
   - Start Appium server
   - Connect device via USB
   - Open Appium Inspector

3. **Find Selectors**
   - Search input field
   - Product results
   - "Voeg toe" button
   - Navigation buttons
   - + button (for quantities)

4. **Update Selectors**
   - Update selectors in `backend/src/ah_automation.py`
   - Test each selector individually
   - Update if app structure changes

### 📋 Configuration

1. **Create .env file**
   ```bash
   cd backend
   python find_ip.py  # Find MacBook IP
   # Create .env with device configuration
   ```

2. **Update Frontend**
   - Update `API_BASE_URL` in `frontend/App.tsx`
   - Use MacBook IP address

3. **Configure Device**
   - Connect device via USB
   - Trust computer on device
   - Configure in .env file

## Testing

### Test Individual Functions
```python
# Test search
await search_item(driver, "melk", "ios")

# Test click product
await click_first_product(driver, "ios")

# Test add to basket
await click_voeg_toe_button(driver, "ios", quantity=2)

# Test full flow
await add_item(driver, "melk", "ios", quantity=1)
```

### Test Multiple Products
```python
products = [
    {"name": "melk", "quantity": 1},
    {"name": "brood", "quantity": 2},
    {"name": "kaas", "quantity": 1},
]
await add_multiple_products(driver, products, "ios")
```

## Differences from Web Version

### 1. Navigation
- **Web**: `driver.get("https://www.ah.nl")`
- **Mobile**: App is already open, navigate within app

### 2. Selectors
- **Web**: CSS selectors (`input[type='search']`)
- **Mobile**: Appium selectors (Accessibility ID, XPath, ID)

### 3. Scrolling
- **Web**: JavaScript scroll
- **Mobile**: Mobile scroll commands or touch actions

### 4. Clicking
- **Web**: Standard click or JavaScript click
- **Mobile**: Click, tap, or touch action

### 5. Going Back
- **Web**: `driver.back()`
- **Mobile**: `driver.back()` or Android back button (`press_keycode(4)`)

### 6. Typing
- **Web**: Standard typing
- **Mobile**: Same typing, but different clear methods (key codes)

## Next Steps

1. **✅ Code Adaptation** - COMPLETE
   - All functions adapted
   - Mobile-specific features added
   - Error handling improved

2. **⚠️ Find Selectors** - TODO
   - Use Appium Inspector
   - Find actual selectors
   - Update selectors in code

3. **⚠️ Test on Device** - TODO
   - Connect device
   - Test with one product
   - Test with multiple products
   - Test with quantities

4. **⚠️ Adjust Timing** - TODO
   - Adjust wait times if needed
   - Test on different devices
   - Optimize for performance

## Summary

✅ **Successfully adapted web automation to mobile app automation**
✅ **All original features preserved**
✅ **Added mobile-specific features**
✅ **Improved error handling**
✅ **Maintained human-like behavior**
✅ **Added quantity support**
✅ **Platform support (iOS/Android)**

⚠️ **Next: Find actual selectors using Appium Inspector**

## Resources

- **Migration Guide**: `backend/MIGRATION.md`
- **Customization Guide**: `CUSTOMIZATION.md`
- **Setup Guide**: `SETUP.md`
- **Appium Inspector**: https://github.com/appium/appium-inspector

## Notes

- All selectors are placeholders and must be customized
- Test on actual device with Albert Heijn app
- Adjust timing if needed based on device performance
- Update selectors if app structure changes
- Handle edge cases (login, popups, etc.)

