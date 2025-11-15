"""
Albert Heijn Mobile App Automation Functions
Adapted from web automation to work with Appium mobile app automation
"""

import asyncio
import time
import logging
from typing import Optional
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

logger = logging.getLogger(__name__)


def type_text(element, text, delay=0.05):
    """
    Type text with human-like delays
    
    Args:
        element: Appium WebElement
        text: Text to type
        delay: Delay between each character (default: 0.05 seconds)
    """
    for char in text:
        element.send_keys(char)
        time.sleep(delay)


async def scroll_into_view(driver, element):
    """
    Scroll element into view (mobile app equivalent)
    
    Args:
        driver: Appium WebDriver
        element: WebElement to scroll into view
    """
    try:
        # For iOS
        driver.execute_script("mobile: scroll", {"direction": "down", "element": element})
    except:
        try:
            # For Android
            driver.execute_script("mobile: scroll", {"direction": "down", "element": element})
        except:
            # Fallback: try to scroll using touch actions
            try:
                location = element.location
                size = element.size
                x = location['x'] + size['width'] / 2
                y = location['y'] + size['height'] / 2
                driver.execute_script("mobile: scroll", {"direction": "down", "x": x, "y": y})
            except:
                pass


async def search_item(driver, item_name, device_type="ios", websocket=None):
    """
    Search for an item in Albert Heijn mobile app with human-like behavior
    
    Args:
        driver: Appium WebDriver
        item_name: Name of the item to search
        device_type: "ios" or "android"
        websocket: Optional WebSocket for real-time updates
    
    Returns:
        bool: True if search was successful, False otherwise
    """
    try:
        if websocket:
            await websocket.send_json({
                "status": "searching",
                "message": f"Searching for: {item_name}",
                "current_product": item_name
            })
        
        logger.info(f"🔍 Searching for: {item_name}")
        
        # Navigate to home/search screen (app should already be open)
        # Try to find search button/tab first
        try:
            # Look for search icon/button to open search
            search_selectors = [
                # iOS selectors
                (AppiumBy.ACCESSIBILITY_ID, "Zoek"),
                (AppiumBy.ACCESSIBILITY_ID, "Search"),
                (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Zoek' or @name='Search']"),
                (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@label, 'Zoek')]"),
                # Android selectors
                (AppiumBy.ID, "nl.ah.app:id/search"),
                (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Zoek' or @content-desc='Search']"),
                (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Zoek']"),
            ]
            
            search_button_found = False
            for by, selector in search_selectors:
                try:
                    search_button = driver.find_element(by, selector)
                    if search_button.is_displayed():
                        logger.info(f"   Found search button: {selector}")
                        await scroll_into_view(driver, search_button)
                        time.sleep(0.5)
                        search_button.click()
                        search_button_found = True
                        await asyncio.sleep(1)
                        break
                except:
                    continue
            
            if not search_button_found:
                logger.info("   Search button not found, trying to find search box directly")
        except Exception as e:
            logger.info(f"   Could not find search button: {e}")
        
        # Find search box
        search_selectors = [
            # iOS selectors
            (AppiumBy.ACCESSIBILITY_ID, "search_field"),
            (AppiumBy.ACCESSIBILITY_ID, "Zoek"),
            (AppiumBy.XPATH, "//XCUIElementTypeSearchField"),
            (AppiumBy.XPATH, "//XCUIElementTypeTextField[@placeholder='Zoek' or @placeholder='Search']"),
            (AppiumBy.XPATH, "//XCUIElementTypeTextField[contains(@name, 'Zoek')]"),
            # Android selectors
            (AppiumBy.ID, "nl.ah.app:id/search_input"),
            (AppiumBy.ID, "nl.ah.app:id/search_box"),
            (AppiumBy.XPATH, "//android.widget.EditText[@hint='Zoek' or @hint='Search']"),
            (AppiumBy.XPATH, "//android.widget.EditText[contains(@content-desc, 'Zoek')]"),
            (AppiumBy.CLASS_NAME, "android.widget.EditText"),
        ]
        
        search_box = None
        for by, selector in search_selectors:
            try:
                search_box = driver.find_element(by, selector)
                if search_box.is_displayed():
                    logger.info(f"   Found search box: {selector}")
                    break
            except:
                continue
        
        if not search_box:
            logger.error("❌ Could not find search box")
            return False
        
        # Scroll search box into view
        await scroll_into_view(driver, search_box)
        await asyncio.sleep(0.5)
        
        # Click search box
        try:
            search_box.click()
        except:
            # Try using JavaScript click
            driver.execute_script("mobile: tap", {"x": search_box.location['x'], "y": search_box.location['y']})
        
        await asyncio.sleep(0.5)
        
        # Clear search box thoroughly
        try:
            # Select all and delete
            if device_type.lower() == "ios":
                search_box.send_keys("\ue003" * 50)  # Delete key multiple times
            else:
                search_box.send_keys("\uE017" * 50)  # Clear key for Android
            
            # Clear using clear() method
            search_box.clear()
            
            # Additional clearing by sending backspace
            for _ in range(20):
                if device_type.lower() == "ios":
                    search_box.send_keys("\ue003")  # Delete
                else:
                    search_box.send_keys("\ue017")  # Backspace
                time.sleep(0.01)
        except Exception as e:
            logger.info(f"   Error clearing search box: {e}")
        
        # Type with human-like delays
        logger.info(f"   Typing: {item_name}")
        type_text(search_box, item_name, delay=0.05)
        
        await asyncio.sleep(0.5)
        
        # Submit search (press enter or search button)
        try:
            # Try pressing enter
            if device_type.lower() == "ios":
                search_box.send_keys("\ue007")  # Enter
            else:
                search_box.send_keys("\ue006")  # Enter for Android
        except:
            # Try finding and clicking search button
            try:
                search_button_selectors = [
                    (AppiumBy.ACCESSIBILITY_ID, "Zoeken"),
                    (AppiumBy.ACCESSIBILITY_ID, "Search"),
                    (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Zoeken' or @name='Search']"),
                    (AppiumBy.ID, "nl.ah.app:id/search_button"),
                ]
                for by, selector in search_button_selectors:
                    try:
                        search_btn = driver.find_element(by, selector)
                        search_btn.click()
                        break
                    except:
                        continue
            except:
                pass
        
        await asyncio.sleep(2)  # Wait for search results
        
        logger.info("   ✅ Search submitted")
        return True
        
    except Exception as e:
        logger.error(f"❌ Error searching: {e}")
        return False


async def click_first_product(driver, device_type="ios", websocket=None):
    """
    Click on the first product to go to its detail page
    
    Args:
        driver: Appium WebDriver
        device_type: "ios" or "android"
        websocket: Optional WebSocket for real-time updates
    
    Returns:
        bool: True if product was clicked, False otherwise
    """
    try:
        if websocket:
            await websocket.send_json({
                "status": "selecting_product",
                "message": "Clicking first product...",
            })
        
        logger.info("   🖱️  Clicking first product...")
        
        # Try multiple selectors for product links
        product_selectors = [
            # iOS selectors
            (AppiumBy.XPATH, "//XCUIElementTypeCell[1]"),
            (AppiumBy.XPATH, "//XCUIElementTypeCell[@visible='true'][1]"),
            (AppiumBy.ACCESSIBILITY_ID, "product_card"),
            (AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, 'product')]/ancestor::XCUIElementTypeCell[1]"),
            # Android selectors
            (AppiumBy.ID, "nl.ah.app:id/product_card"),
            (AppiumBy.XPATH, "//android.widget.RecyclerView/android.view.ViewGroup[1]"),
            (AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'product')][1]"),
            (AppiumBy.CLASS_NAME, "android.widget.FrameLayout"),
        ]
        
        first_product = None
        for by, selector in product_selectors:
            try:
                if by == AppiumBy.XPATH and "[1]" in selector:
                    # For XPath with [1], try to get first element
                    products = driver.find_elements(by, selector.replace("[1]", ""))
                    if products and len(products) > 0:
                        first_product = products[0]
                        if first_product.is_displayed():
                            logger.info(f"   Found product using selector: {selector}")
                            break
                else:
                    first_product = driver.find_element(by, selector)
                    if first_product.is_displayed():
                        logger.info(f"   Found product using selector: {selector}")
                        break
            except:
                continue
        
        if not first_product:
            logger.error("   ❌ Could not find product link")
            return False
        
        # Scroll to product
        await scroll_into_view(driver, first_product)
        await asyncio.sleep(0.5)
        
        # Click product
        try:
            first_product.click()
        except:
            # Try using JavaScript click
            try:
                location = first_product.location
                size = first_product.size
                x = location['x'] + size['width'] / 2
                y = location['y'] + size['height'] / 2
                driver.execute_script("mobile: tap", {"x": x, "y": y})
            except:
                # Try using touch action
                from appium.webdriver.common.touch_action import TouchAction
                action = TouchAction(driver)
                action.tap(first_product).perform()
        
        logger.info("   ✅ Clicked product")
        await asyncio.sleep(2)  # Wait for product page to load
        
        return True
        
    except Exception as e:
        logger.error(f"   ❌ Error clicking product: {e}")
        return False


async def click_voeg_toe_button(driver, device_type="ios", quantity=1, websocket=None):
    """
    Click the 'Voeg toe' (+) button on product detail page
    
    Args:
        driver: Appium WebDriver
        device_type: "ios" or "android"
        quantity: Number of times to click the button (default: 1)
        websocket: Optional WebSocket for real-time updates
    
    Returns:
        bool: True if button was clicked, False otherwise
    """
    try:
        if websocket:
            await websocket.send_json({
                "status": "adding_to_basket",
                "message": "Looking for 'Voeg toe' button...",
            })
        
        logger.info("   🔍 Looking for 'Voeg toe' button...")
        await asyncio.sleep(2)  # Wait for page to load
        
        # Find all buttons and filter carefully
        logger.info("   🔍 Searching through all buttons...")
        
        # Try multiple strategies to find the add button
        button_selectors = [
            # iOS selectors - try specific button first
            (AppiumBy.ACCESSIBILITY_ID, "Voeg toe"),
            (AppiumBy.ACCESSIBILITY_ID, "Voeg toe:"),
            (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name, 'Voeg toe')]"),
            (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@label, 'Voeg toe')]"),
            (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name, 'toevoegen')]"),
            # Android selectors
            (AppiumBy.ID, "nl.ah.app:id/add_to_basket"),
            (AppiumBy.ID, "nl.ah.app:id/add_button"),
            (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Voeg toe')]"),
            (AppiumBy.XPATH, "//android.widget.Button[contains(@content-desc, 'Voeg toe')]"),
        ]
        
        add_button = None
        for by, selector in button_selectors:
            try:
                add_button = driver.find_element(by, selector)
                if add_button.is_displayed():
                    logger.info(f"   ✅ Found add-to-cart button: {selector}")
                    break
            except:
                continue
        
        # If not found by specific selector, try filtering all buttons
        if not add_button:
            logger.info("   🔍 Searching through all buttons...")
            try:
                all_buttons = driver.find_elements(AppiumBy.TAG_NAME, "button")
                logger.info(f"   Found {len(all_buttons)} total buttons")
                
                for idx, button in enumerate(all_buttons):
                    try:
                        if device_type.lower() == "ios":
                            button_text = (button.get_attribute('name') or '').lower()
                            aria_label = (button.get_attribute('label') or '').lower()
                            button_info = f"{button_text} {aria_label}"
                        else:
                            button_text = (button.text or '').lower()
                            aria_label = (button.get_attribute('content-desc') or '').lower()
                            button_info = f"{button_text} {aria_label}"
                        
                        # EXCLUDE favorite buttons explicitly
                        exclude_keywords = ['favoriet', 'favorite', 'bewaar', 'save', 'hart', 'heart']
                        if any(keyword in button_info for keyword in exclude_keywords):
                            continue
                        
                        # Look for add-to-cart keywords
                        add_keywords = ['voeg toe', 'toevoegen aan', 'in mandje', 'bestellen', 'add']
                        
                        # Check if it's an add-to-cart button
                        if any(keyword in button_info for keyword in add_keywords):
                            # Extra verification: should contain "voeg toe" pattern
                            if 'voeg toe' in button_info:
                                logger.info(f"   ✅ Found add-to-cart button #{idx}: '{button_info}'")
                                add_button = button
                                break
                    except:
                        continue
            except Exception as e:
                logger.error(f"   Error searching buttons: {e}")
        
        if not add_button:
            logger.error("   ❌ Could not find 'Voeg toe' button")
            return False
        
        # Scroll button into view
        await scroll_into_view(driver, add_button)
        await asyncio.sleep(0.5)
        
        # Click button
        try:
            add_button.click()
        except:
            # Try using JavaScript click
            try:
                location = add_button.location
                size = add_button.size
                x = location['x'] + size['width'] / 2
                y = location['y'] + size['height'] / 2
                driver.execute_script("mobile: tap", {"x": x, "y": y})
            except:
                # Try using touch action
                from appium.webdriver.common.touch_action import TouchAction
                action = TouchAction(driver)
                action.tap(add_button).perform()
        
        logger.info("   ✅ Button clicked!")
        
        # If quantity > 1, click the button multiple times
        if quantity > 1:
            await asyncio.sleep(1)  # Wait before clicking again
            for i in range(quantity - 1):
                try:
                    quantity_num = i + 2
                    if websocket:
                        await websocket.send_json({
                            "status": "adding_to_basket",
                            "message": f"Adding quantity {quantity_num}/{quantity}...",
                        })
                    logger.info(f"   Adding quantity {quantity_num}/{quantity}...")
                    
                    # Try clicking the same button again (might be a + button now)
                    try:
                        # First try to find if button has changed to a + button
                        plus_selectors = [
                            (AppiumBy.ACCESSIBILITY_ID, "+"),
                            (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='+' or @label='+']"),
                            (AppiumBy.XPATH, "//android.widget.Button[@content-desc='+' or @text='+']"),
                            (AppiumBy.ID, "nl.ah.app:id/increment"),
                        ]
                        plus_button = None
                        for by, selector in plus_selectors:
                            try:
                                plus_button = driver.find_element(by, selector)
                                if plus_button.is_displayed():
                                    plus_button.click()
                                    logger.info(f"   Clicked + button for quantity {quantity_num}")
                                    break
                            except:
                                continue
                        
                        if not plus_button:
                            # Fallback: try clicking the same location (button might still be there)
                            try:
                                add_button.click()
                                logger.info(f"   Clicked add button again for quantity {quantity_num}")
                            except:
                                # Last resort: tap the same location
                                try:
                                    location = add_button.location
                                    size = add_button.size
                                    x = location['x'] + size['width'] / 2
                                    y = location['y'] + size['height'] / 2
                                    driver.execute_script("mobile: tap", {"x": x, "y": y})
                                    logger.info(f"   Tapped button location for quantity {quantity_num}")
                                except Exception as tap_error:
                                    logger.error(f"   Could not click button for quantity {quantity_num}: {tap_error}")
                                    break
                    
                    await asyncio.sleep(1)  # Wait between clicks
                except Exception as e:
                    quantity_num = i + 2 if 'i' in locals() else quantity
                    logger.error(f"   Error adding quantity {quantity_num}: {e}")
                    break
        
        await asyncio.sleep(2.5)  # Wait for item to be added
        
        return True
        
    except Exception as e:
        logger.error(f"   ❌ Error clicking button: {e}")
        return False


async def add_first_product_to_cart(driver, device_type="ios", quantity=1, websocket=None):
    """
    Navigate to first product and add it to cart
    
    Args:
        driver: Appium WebDriver
        device_type: "ios" or "android"
        quantity: Number of items to add (default: 1)
        websocket: Optional WebSocket for real-time updates
    
    Returns:
        bool: True if product was added, False otherwise
    """
    try:
        # Step 1: Click first product to open detail page
        if not await click_first_product(driver, device_type, websocket):
            return False
        
        # Step 2: Click 'Voeg toe' button on detail page (with quantity)
        if not await click_voeg_toe_button(driver, device_type, quantity, websocket):
            return False
        
        # Step 3: Go back to search results for next item
        logger.info("   ⬅️  Going back to search results...")
        try:
            driver.back()
        except:
            # Try pressing back button using key code
            if device_type.lower() == "android":
                driver.press_keycode(4)  # Android back button
            else:
                # iOS doesn't have back button, try finding back button
                try:
                    back_selectors = [
                        (AppiumBy.ACCESSIBILITY_ID, "Back"),
                        (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Back']"),
                        (AppiumBy.XPATH, "//XCUIElementTypeNavigationBar//XCUIElementTypeButton[1]"),
                    ]
                    for by, selector in back_selectors:
                        try:
                            back_button = driver.find_element(by, selector)
                            back_button.click()
                            break
                        except:
                            continue
                except:
                    pass
        
        await asyncio.sleep(1)
        
        return True
        
    except Exception as e:
        logger.error(f"   ❌ Error adding product: {e}")
        return False


async def add_item(driver, item_name, device_type="ios", quantity=1, websocket=None):
    """
    Search and add an item to cart
    
    Args:
        driver: Appium WebDriver
        item_name: Name of the item to add
        device_type: "ios" or "android"
        quantity: Number of items to add (default: 1)
        websocket: Optional WebSocket for real-time updates
    
    Returns:
        bool: True if item was added, False otherwise
    """
    logger.info(f"\n{'='*60}")
    if await search_item(driver, item_name, device_type, websocket):
        result = await add_first_product_to_cart(driver, device_type, quantity, websocket)
        logger.info(f"{'='*60}\n")
        return result
    logger.info(f"{'='*60}\n")
    return False


async def add_multiple_products(driver, products_list, device_type="ios", websocket=None):
    """
    Add multiple products with quantities
    
    Args:
        driver: Appium WebDriver
        products_list: List of dicts with 'name' and 'quantity' keys
        device_type: "ios" or "android"
        websocket: Optional WebSocket for real-time updates
    
    Returns:
        tuple: (success_count, failed_items)
    """
    success_count = 0
    failed_items = []
    
    total_products = len(products_list)
    
    for idx, product in enumerate(products_list):
        product_name = product.get('name', product) if isinstance(product, dict) else product
        quantity = product.get('quantity', 1) if isinstance(product, dict) else 1
        
        if websocket:
            progress = 25 + (idx / total_products) * 70
            await websocket.send_json({
                "status": "adding_product",
                "message": f"Adding {product_name} (x{quantity})... ({idx + 1}/{total_products})",
                "progress": progress,
                "current_product": product_name
            })
        
        if await add_item(driver, product_name, device_type, quantity, websocket):
            success_count += 1
            # Human-like delay between items
            await asyncio.sleep(1)
        else:
            failed_items.append(product_name)
            await asyncio.sleep(0.5)
    
    logger.info(f"\n{'='*60}")
    logger.info(f"📊 SUMMARY:")
    logger.info(f"{'='*60}")
    logger.info(f"✅ Successfully added: {success_count}/{total_products} products")
    if failed_items:
        logger.info(f"❌ Failed items: {', '.join(failed_items)}")
    logger.info(f"{'='*60}\n")
    
    return success_count, failed_items

