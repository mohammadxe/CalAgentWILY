# Migration from Web Automation to Mobile App Automation

## Overview

This document explains how the Albert Heijn web automation code was adapted for mobile app automation using Appium.

## Key Changes

### 1. Selenium → Appium

**Before (Web):**
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(options=chrome_options)
```

**After (Mobile):**
```python
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
driver = webdriver.Remote(appium_url, options=options)
```

### 2. CSS Selectors → Appium Selectors

**Before (Web):**
```python
search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
```

**After (Mobile):**
```python
# iOS
search_box = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "search_field")
# Or Android
search_box = driver.find_element(AppiumBy.ID, "nl.ah.app:id/search_input")
```

### 3. Browser Navigation → App Navigation

**Before (Web):**
```python
driver.get("https://www.ah.nl")
```

**After (Mobile):**
```python
# App is already open, navigate within app
# Find and click search button/tab
search_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Zoek")
search_button.click()
```

### 4. Scrolling

**Before (Web):**
```python
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
```

**After (Mobile):**
```python
# iOS/Android mobile scrolling
driver.execute_script("mobile: scroll", {"direction": "down", "element": element})
# Or use touch actions
```

### 5. Typing Behavior

**Before (Web):**
```python
for char in text:
    element.send_keys(char)
    time.sleep(0.05)
```

**After (Mobile):**
```python
# Same human-like typing, but with mobile-specific key codes
for char in text:
    element.send_keys(char)
    time.sleep(0.05)
# Clear using mobile key codes
element.send_keys("\ue003" * 50)  # Delete key (iOS)
```

### 6. Button Clicking

**Before (Web):**
```python
button.click()
# Or JavaScript click
driver.execute_script("arguments[0].click();", button)
```

**After (Mobile):**
```python
button.click()
# Or mobile tap
driver.execute_script("mobile: tap", {"x": x, "y": y})
# Or touch action
from appium.webdriver.common.touch_action import TouchAction
action = TouchAction(driver)
action.tap(button).perform()
```

### 7. Going Back

**Before (Web):**
```python
driver.back()
```

**After (Mobile):**
```python
driver.back()
# Or Android back button
driver.press_keycode(4)  # Android back button
# Or find back button
back_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Back")
back_button.click()
```

## Function Adaptations

### `search_item()`

**Changes:**
- Removed `driver.get()` - app is already open
- Added search button click to open search
- Changed CSS selectors to Appium selectors (iOS/Android)
- Added mobile-specific scrolling
- Changed clear method to use mobile key codes

### `click_first_product()`

**Changes:**
- Changed CSS selectors to Appium selectors
- Added mobile scrolling
- Added multiple click fallbacks (tap, touch action)
- Added iOS/Android specific selectors

### `click_voeg_toe_button()`

**Changes:**
- Changed button filtering to work with mobile app structure
- Added quantity handling (click multiple times)
- Added + button detection for incrementing quantity
- Changed to Appium selectors
- Added mobile-specific click methods

### `add_first_product_to_cart()`

**Changes:**
- Added quantity parameter
- Changed back navigation to mobile methods
- Added Android back button support

### `add_item()`

**Changes:**
- Added quantity parameter
- Updated to use mobile automation functions

### `add_multiple_items()`

**Changes:**
- Renamed to `add_multiple_products()`
- Changed to handle product dicts with name and quantity
- Updated progress calculation for WebSocket

## Selector Strategy

### Multiple Selector Fallback

The code uses multiple selectors with fallback to handle different app versions and platforms:

```python
search_selectors = [
    # iOS selectors
    (AppiumBy.ACCESSIBILITY_ID, "Zoek"),
    (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Zoek']"),
    # Android selectors
    (AppiumBy.ID, "nl.ah.app:id/search"),
    (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Zoek']"),
]

for by, selector in search_selectors:
    try:
        element = driver.find_element(by, selector)
        if element.is_displayed():
            break
    except:
        continue
```

### Selector Types

1. **Accessibility ID** (Preferred)
   - Most stable across updates
   - Works for both iOS and Android
   - Example: `AppiumBy.ACCESSIBILITY_ID, "Zoek"`

2. **XPath** (Fallback)
   - Flexible but fragile
   - Platform-specific
   - Example: `AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Zoek']"`

3. **ID** (Android)
   - Android-specific
   - Fast and reliable
   - Example: `AppiumBy.ID, "nl.ah.app:id/search"`

## Human-like Behavior

All human-like behavior from the web version is preserved:

1. **Typing delays**: 0.05 seconds between characters
2. **Wait times**: 1-2.5 seconds between actions
3. **Scrolling**: Scroll elements into view before clicking
4. **Error handling**: Multiple fallbacks for each action
5. **Logging**: Detailed logging for debugging

## Platform Support

### iOS
- Uses XCUITest automation
- XPath with `XCUIElementType*` elements
- Accessibility IDs
- Touch actions

### Android
- Uses UiAutomator2 automation
- Android resource IDs
- XPath with `android.widget.*` elements
- Key codes for back button

## Testing

### Before Testing

1. **Install Appium Inspector**: To find correct selectors
2. **Connect Device**: Via USB
3. **Configure .env**: Set device type, UDID, package/bundle ID
4. **Find Selectors**: Use Appium Inspector to find actual selectors

### Testing Strategy

1. **Test Individual Functions**: Test each function separately
2. **Test with One Product**: Start with a single product
3. **Test Multiple Products**: Test with multiple products
4. **Test Quantities**: Test with different quantities
5. **Test Error Handling**: Test with invalid selectors

## Important Notes

1. **Selectors Must Be Customized**: The current selectors are placeholders and must be found using Appium Inspector
2. **Platform Differences**: iOS and Android have different selector strategies
3. **App Versions**: Selectors may change with app updates
4. **Error Handling**: Multiple fallbacks are provided, but may need adjustment
5. **Timing**: Wait times may need adjustment based on device performance

## Next Steps

1. **Find Actual Selectors**: Use Appium Inspector to find correct selectors
2. **Update Selectors**: Update selectors in `ah_automation.py`
3. **Test on Device**: Test on actual device with Albert Heijn app
4. **Adjust Timing**: Adjust wait times if needed
5. **Handle Edge Cases**: Add handling for edge cases (login, popups, etc.)

## Resources

- [Appium Documentation](https://appium.io/docs/en/2.1/)
- [XCUIElement Query Guide](https://developer.apple.com/documentation/xctest/xcuielementquery)
- [UiAutomator2 Selectors](https://developer.android.com/training/testing/ui-automator)
- [Appium Inspector](https://github.com/appium/appium-inspector)

