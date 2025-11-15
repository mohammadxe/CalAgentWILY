#!/usr/bin/env python3
"""
Helper script to test selectors in Albert Heijn app
Use this to verify selectors found in Appium Inspector
"""

import time
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
from dotenv import load_dotenv

load_dotenv()


def get_appium_options(device_type: str):
    """Get Appium options based on device type"""
    if device_type.lower() == "ios":
        options = XCUITestOptions()
        options.platform_name = "iOS"
        options.device_name = os.getenv("IOS_DEVICE_NAME", "iPhone")
        options.platform_version = os.getenv("IOS_VERSION", "17.0")
        options.bundle_id = os.getenv("AH_BUNDLE_ID", "nl.ah.ahapp")
        options.udid = os.getenv("IOS_UDID", "")
        options.automation_name = "XCUITest"
        options.no_reset = True
        options.full_reset = False
    else:  # Android
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = os.getenv("ANDROID_DEVICE_NAME", "Android Device")
        options.app_package = os.getenv("AH_PACKAGE", "nl.ah.app")
        options.app_activity = os.getenv("AH_ACTIVITY", "nl.ah.app.MainActivity")
        options.automation_name = "UiAutomator2"
        options.no_reset = True
        options.full_reset = False
    
    return options


def test_selector(driver, by, selector, description, device_type="ios", wait_time=5):
    """
    Test a selector and print results
    
    Args:
        driver: Appium WebDriver
        by: AppiumBy selector type
        selector: Selector string
        description: Description of what we're looking for
        device_type: "ios" or "android" (default: "ios")
        wait_time: Time to wait for element (default: 5 seconds)
    """
    print(f"\n{'='*60}")
    print(f"Testing: {description}")
    print(f"{'='*60}")
    print(f"Selector Type: {by}")
    print(f"Selector: {selector}")
    print(f"{'-'*60}")
    
    try:
        # Wait for element
        wait = WebDriverWait(driver, wait_time)
        element = wait.until(EC.presence_of_element_located((by, selector)))
        
        # Check if element is displayed
        if element.is_displayed():
            print(f"✅ SUCCESS: Found element!")
            print(f"   Element Type: {element.tag_name}")
            try:
                print(f"   Element Text: {element.text}")
            except:
                pass
            print(f"   Element Location: {element.location}")
            print(f"   Element Size: {element.size}")
            
            # Try to get additional properties
            try:
                if device_type.lower() == "ios":
                    name = element.get_attribute('name')
                    label = element.get_attribute('label')
                    accessibility_id = element.get_attribute('accessibility-id')
                    print(f"   Name: {name}")
                    print(f"   Label: {label}")
                    print(f"   Accessibility ID: {accessibility_id}")
                else:
                    text = element.text
                    content_desc = element.get_attribute('content-desc')
                    resource_id = element.get_attribute('resource-id')
                    print(f"   Text: {text}")
                    print(f"   Content Description: {content_desc}")
                    print(f"   Resource ID: {resource_id}")
            except Exception as e:
                print(f"   Could not get additional properties: {e}")
            
            return element
        else:
            print(f"⚠️  WARNING: Element found but not displayed")
            return None
            
    except TimeoutException:
        print(f"❌ FAILED: Element not found within {wait_time} seconds")
        return None
    except NoSuchElementException:
        print(f"❌ FAILED: Element not found")
        return None
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return None


def test_multiple_selectors(driver, selectors_list, description, device_type="ios"):
    """
    Test multiple selectors and return the first one that works
    
    Args:
        driver: Appium WebDriver
        selectors_list: List of (by, selector) tuples
        description: Description of what we're looking for
        device_type: "ios" or "android" (default: "ios")
    
    Returns:
        Element if found, None otherwise
    """
    print(f"\n{'='*60}")
    print(f"Testing Multiple Selectors: {description}")
    print(f"{'='*60}")
    
    for idx, (by, selector) in enumerate(selectors_list, 1):
        print(f"\n[{idx}/{len(selectors_list)}] Testing selector:")
        print(f"   Type: {by}")
        print(f"   Selector: {selector}")
        
        element = test_selector(driver, by, selector, f"{description} (Selector {idx})", device_type, wait_time=3)
        
        if element:
            print(f"\n✅ FOUND WORKING SELECTOR!")
            print(f"   Use this in your code:")
            print(f"   (AppiumBy.{by.name}, \"{selector}\")")
            return element
        
        print(f"   ❌ This selector didn't work, trying next...")
    
    print(f"\n❌ None of the selectors worked!")
    return None


def main():
    """Main function to test selectors"""
    print("="*70)
    print("ALBERT HEIJN APP - SELECTOR TESTING")
    print("="*70)
    print("\nThis script helps you test selectors found in Appium Inspector")
    print("Make sure:")
    print("1. Appium server is running (appium)")
    print("2. Device is connected via USB")
    print("3. Albert Heijn app is installed")
    print("4. .env file is configured")
    print("="*70)
    
    # Get device type
    device_type = input("\nDevice type (ios/android): ").strip().lower() or "ios"
    
    # Get Appium options
    options = get_appium_options(device_type)
    appium_url = os.getenv("APPIUM_SERVER_URL", "http://localhost:4723")
    
    try:
        # Connect to device
        print(f"\nConnecting to device via Appium...")
        print(f"Appium URL: {appium_url}")
        driver = webdriver.Remote(appium_url, options=options)
        print("✅ Connected to device!")
        
        # Wait for app to load
        time.sleep(3)
        
        # Test search button selectors
        print("\n" + "="*70)
        print("TESTING SEARCH BUTTON SELECTORS")
        print("="*70)
        
        search_button_selectors = [
            # iOS selectors - UPDATE THESE with your found selectors
            (AppiumBy.ACCESSIBILITY_ID, "Zoek"),
            (AppiumBy.ACCESSIBILITY_ID, "Search"),
            (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Zoek' or @name='Search']"),
            (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@label, 'Zoek')]"),
            # Android selectors - UPDATE THESE with your found selectors
            (AppiumBy.ID, "nl.ah.app:id/search"),
            (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Zoek' or @content-desc='Search']"),
            (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Zoek']"),
        ]
        
        search_button = test_multiple_selectors(driver, search_button_selectors, "Search Button", device_type)
        
        if search_button:
            print("\n✅ Search button found! Clicking it...")
            try:
                search_button.click()
                time.sleep(2)
            except Exception as e:
                print(f"   Could not click search button: {e}")
        else:
            print("\n⚠️  Search button not found. Continuing to test search input...")
        
        # Test search input selectors
        print("\n" + "="*70)
        print("TESTING SEARCH INPUT SELECTORS")
        print("="*70)
        
        search_input_selectors = [
            # iOS selectors - UPDATE THESE with your found selectors
            (AppiumBy.ACCESSIBILITY_ID, "search_field"),
            (AppiumBy.ACCESSIBILITY_ID, "Zoek"),
            (AppiumBy.XPATH, "//XCUIElementTypeSearchField"),
            (AppiumBy.XPATH, "//XCUIElementTypeTextField[@placeholder='Zoek' or @placeholder='Search']"),
            (AppiumBy.XPATH, "//XCUIElementTypeTextField[contains(@name, 'Zoek')]"),
            # Android selectors - UPDATE THESE with your found selectors
            (AppiumBy.ID, "nl.ah.app:id/search_input"),
            (AppiumBy.ID, "nl.ah.app:id/search_box"),
            (AppiumBy.XPATH, "//android.widget.EditText[@hint='Zoek' or @hint='Search']"),
            (AppiumBy.XPATH, "//android.widget.EditText[contains(@content-desc, 'Zoek')]"),
            (AppiumBy.CLASS_NAME, "android.widget.EditText"),
        ]
        
        search_input = test_multiple_selectors(driver, search_input_selectors, "Search Input", device_type)
        
        if search_input:
            print("\n✅ Search input found! Testing typing...")
            try:
                search_input.clear()
                search_input.send_keys("melk")
                time.sleep(2)
                
                # Try to submit search
                try:
                    if device_type.lower() == "ios":
                        search_input.send_keys("\ue007")  # Enter key (iOS)
                    else:
                        search_input.send_keys("\ue006")  # Enter key (Android)
                    time.sleep(3)
                except:
                    pass
            except Exception as e:
                print(f"   Could not type in search input: {e}")
        else:
            print("\n⚠️  Search input not found. Cannot test further.")
            input("\nPress ENTER to continue testing other selectors...")
            driver.quit()
            return
        
        # Test product selectors
        print("\n" + "="*70)
        print("TESTING PRODUCT SELECTORS")
        print("="*70)
        
        product_selectors = [
            # iOS selectors - UPDATE THESE with your found selectors
            (AppiumBy.XPATH, "//XCUIElementTypeCell[1]"),
            (AppiumBy.XPATH, "//XCUIElementTypeCell[@visible='true'][1]"),
            (AppiumBy.ACCESSIBILITY_ID, "product_card"),
            (AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, 'product')]/ancestor::XCUIElementTypeCell[1]"),
            # Android selectors - UPDATE THESE with your found selectors
            (AppiumBy.ID, "nl.ah.app:id/product_card"),
            (AppiumBy.XPATH, "//android.widget.RecyclerView/android.view.ViewGroup[1]"),
            (AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'product')][1]"),
            (AppiumBy.CLASS_NAME, "android.widget.FrameLayout"),
        ]
        
        product = test_multiple_selectors(driver, product_selectors, "First Product", device_type)
        
        if product:
            print("\n✅ Product found! Clicking it...")
            try:
                product.click()
                time.sleep(3)
            except Exception as e:
                print(f"   Could not click product: {e}")
        else:
            print("\n⚠️  Product not found. Cannot test 'Voeg toe' button.")
            input("\nPress ENTER to close...")
            driver.quit()
            return
        
        # Test "Voeg toe" button selectors
        print("\n" + "="*70)
        print("TESTING 'VOEG TOE' BUTTON SELECTORS")
        print("="*70)
        
        voeg_toe_selectors = [
            # iOS selectors - UPDATE THESE with your found selectors
            (AppiumBy.ACCESSIBILITY_ID, "Voeg toe"),
            (AppiumBy.ACCESSIBILITY_ID, "Voeg toe:"),
            (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name, 'Voeg toe')]"),
            (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@label, 'Voeg toe')]"),
            (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name, 'toevoegen')]"),
            # Android selectors - UPDATE THESE with your found selectors
            (AppiumBy.ID, "nl.ah.app:id/add_to_basket"),
            (AppiumBy.ID, "nl.ah.app:id/add_button"),
            (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Voeg toe')]"),
            (AppiumBy.XPATH, "//android.widget.Button[contains(@content-desc, 'Voeg toe')]"),
        ]
        
        voeg_toe_button = test_multiple_selectors(driver, voeg_toe_selectors, "Voeg toe Button", device_type)
        
        if voeg_toe_button:
            print("\n✅ 'Voeg toe' button found!")
        else:
            print("\n⚠️  'Voeg toe' button not found.")
        
        # Summary
        print("\n" + "="*70)
        print("TESTING COMPLETE")
        print("="*70)
        print("\nNext steps:")
        print("1. Note which selectors worked")
        print("2. Update selectors in backend/src/ah_automation.py")
        print("3. Test automation with one product")
        print("4. Test with multiple products")
        print("="*70)
        
        input("\nPress ENTER to close the driver...")
        driver.quit()
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nMake sure:")
        print("1. Appium server is running")
        print("2. Device is connected")
        print("3. .env file is configured correctly")
        print("4. Albert Heijn app is installed")


if __name__ == "__main__":
    main()

