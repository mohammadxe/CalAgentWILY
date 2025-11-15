# Customization Guide

## Important: App Selectors

The most critical part of this automation is finding the correct selectors for the Albert Heijn mobile app. The current selectors in `backend/src/main.py` are **placeholder values** and need to be customized.

## Using Appium Inspector

### 1. Install Appium Inspector

```bash
# Install Appium Inspector (GUI tool)
npm install -g appium-inspector

# Or download from: https://github.com/appium/appium-inspector/releases
```

### 2. Connect to Device

1. Start Appium server: `appium`
2. Open Appium Inspector
3. Configure connection:
   - **Platform**: iOS or Android
   - **Device Name**: Your device name
   - **Platform Version**: Your iOS/Android version
   - **App Package/Bundle ID**: `nl.ah.ahapp` (iOS) or `nl.ah.app` (Android)
   - **Automation Name**: `XCUITest` (iOS) or `UiAutomator2` (Android)

### 3. Find Selectors

Navigate through the Albert Heijn app and find selectors for:

#### Required Selectors:

1. **Search Input Field**
   - ID: `search_input`
   - XPath: `//XCUIElementTypeTextField[@name='Search']`
   - Accessibility ID: `search_field`

2. **Product Results**
   - ID: `product_item_0`
   - XPath: `//XCUIElementTypeCell[1]`
   - Accessibility ID: `product_result_0`

3. **Add to Basket Button**
   - ID: `add_to_basket`
   - XPath: `//XCUIElementTypeButton[@name='Add to Basket']`
   - Accessibility ID: `add_button`

4. **Navigation Buttons**
   - Back button
   - Close button
   - Skip button (if login screen appears)

### 4. Update Selectors in Code

Edit `backend/src/main.py` and update the selectors:

```python
# Example: Search input field
search_box = driver.find_element(AppiumBy.ID, "search_input")  # Replace with actual selector
# Or:
search_box = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='Search']")
# Or:
search_box = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "search_field")
```

## Selector Strategies

### 1. By ID (Recommended)
- Most reliable
- Fastest
- Requires app to have unique IDs

```python
element = driver.find_element(AppiumBy.ID, "search_input")
```

### 2. By XPath
- Flexible
- Can be fragile if UI changes
- Useful for complex queries

```python
element = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='Search']")
```

### 3. By Accessibility ID
- Good for accessibility
- Stable across updates
- Requires app to have accessibility labels

```python
element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "search_field")
```

### 4. By Class Name
- Useful for finding element types
- Less specific

```python
element = driver.find_element(AppiumBy.CLASS_NAME, "XCUIElementTypeTextField")
```

## Common Selectors for Albert Heijn App

### iOS Selectors:

```python
# Search field
search_box = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSearchField")

# Product list
products = driver.find_elements(AppiumBy.XPATH, "//XCUIElementTypeCell")

# Add to basket button
add_button = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Add']")

# Back button
back_button = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Back']")
```

### Android Selectors:

```python
# Search field
search_box = driver.find_element(AppiumBy.ID, "com.android.app:id/search_input")

# Product list
products = driver.find_elements(AppiumBy.ID, "com.android.app:id/product_item")

# Add to basket button
add_button = driver.find_element(AppiumBy.ID, "com.android.app:id/add_button")

# Back button
back_button = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
```

## Handling Dynamic Content

### Wait for Elements

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for element to appear
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((AppiumBy.ID, "search_input")))
```

### Handle Multiple Results

```python
# Find all product results
products = driver.find_elements(AppiumBy.XPATH, "//XCUIElementTypeCell")
if products:
    first_product = products[0]
    first_product.click()
```

### Handle Errors

```python
try:
    search_box = driver.find_element(AppiumBy.ID, "search_input")
    search_box.send_keys(product.name)
except Exception as e:
    logger.error(f"Failed to find search box: {e}")
    # Try alternative selector
    search_box = driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSearchField")
```

## Testing Selectors

### Test Individual Selectors

```python
# Test if selector works
try:
    element = driver.find_element(AppiumBy.ID, "search_input")
    print(f"✓ Found element: {element}")
except Exception as e:
    print(f"✗ Failed to find element: {e}")
```

### Test Full Flow

1. Start automation with one product
2. Watch Appium Inspector in real-time
3. Verify each step works correctly
4. Adjust selectors as needed

## Best Practices

1. **Use Stable Selectors**: Prefer IDs and Accessibility IDs over XPath
2. **Wait for Elements**: Always wait for elements to appear before interacting
3. **Handle Errors**: Add try-catch blocks for fragile selectors
4. **Test Regularly**: Test selectors after app updates
5. **Document Selectors**: Keep a list of working selectors
6. **Use Multiple Strategies**: Have fallback selectors if primary fails

## Troubleshooting

### Selector Not Found

1. Check if element exists in Appium Inspector
2. Verify selector syntax
3. Check if element is visible/enabled
4. Wait for element to load
5. Try alternative selector

### Selector Works Sometimes

1. Add explicit waits
2. Check for timing issues
3. Verify element state (visible, enabled)
4. Handle dynamic content

### App Updated

1. Re-inspect app with Appium Inspector
2. Update selectors if UI changed
3. Test all selectors
4. Update documentation

## Next Steps

1. **Install Appium Inspector**: Get familiar with the tool
2. **Inspect Albert Heijn App**: Find all required selectors
3. **Update Code**: Replace placeholder selectors in `main.py`
4. **Test**: Run automation with one product
5. **Iterate**: Refine selectors based on results

## Resources

- [Appium Inspector Guide](https://github.com/appium/appium-inspector)
- [Appium Selectors Documentation](https://appium.io/docs/en/2.1/guides/selectors/)
- [XCUIElement Query Guide](https://developer.apple.com/documentation/xctest/xcuielementquery)
- [UiAutomator2 Selectors](https://developer.android.com/training/testing/ui-automator)

