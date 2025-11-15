"""
Albert Heijn Mobile App Automation Backend
Handles automation of the Albert Heijn mobile app via Appium
"""

import asyncio
import logging
from typing import List, Optional
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import os
from dotenv import load_dotenv
from .ah_automation import add_multiple_products

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Albert Heijn Automation API")

# CORS middleware for Expo app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your Expo app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global driver instance
driver: Optional[webdriver.Remote] = None


class Product(BaseModel):
    name: str
    quantity: int = 1


class AutomationRequest(BaseModel):
    products: List[Product]
    device_type: str = "ios"  # "ios" or "android"


class AutomationStatus(BaseModel):
    status: str
    message: str
    progress: float = 0.0


def get_appium_options(device_type: str):
    """Get Appium options based on device type"""
    if device_type.lower() == "ios":
        options = XCUITestOptions()
        options.platform_name = "iOS"
        options.device_name = os.getenv("IOS_DEVICE_NAME", "iPhone")
        options.platform_version = os.getenv("IOS_VERSION", "17.0")
        options.bundle_id = os.getenv("AH_BUNDLE_ID", "nl.ah.ahapp")  # Albert Heijn app bundle ID
        options.udid = os.getenv("IOS_UDID", "")  # Device UDID if needed
        options.automation_name = "XCUITest"
        options.no_reset = True
        options.full_reset = False
    else:  # Android
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = os.getenv("ANDROID_DEVICE_NAME", "Android Device")
        options.app_package = os.getenv("AH_PACKAGE", "nl.ah.app")  # Albert Heijn app package
        options.app_activity = os.getenv("AH_ACTIVITY", "nl.ah.app.MainActivity")
        options.automation_name = "UiAutomator2"
        options.no_reset = True
        options.full_reset = False
    
    return options


async def connect_to_appium():
    """Connect to Appium server"""
    appium_server_url = os.getenv("APPIUM_SERVER_URL", "http://localhost:4723")
    return appium_server_url


async def automate_albert_heijn_app(products: List[Product], device_type: str, websocket: WebSocket = None):
    """
    Automate Albert Heijn mobile app to add products to basket
    
    This function:
    1. Opens Albert Heijn app
    2. Navigates to search/product selection
    3. Adds products to basket
    4. Returns status updates via WebSocket if provided
    """
    global driver
    appium_url = await connect_to_appium()
    options = get_appium_options(device_type)
    
    try:
        # Send status update
        if websocket:
            await websocket.send_json({
                "status": "connecting",
                "message": "Connecting to device...",
                "progress": 10.0
            })
        
        # Initialize driver
        driver = webdriver.Remote(appium_url, options=options)
        logger.info("Connected to Appium server and device")
        
        if websocket:
            await websocket.send_json({
                "status": "connected",
                "message": "Device connected successfully",
                "progress": 20.0
            })
        
        # Wait for app to load
        await asyncio.sleep(3)
        
        # Handle potential login/splash screen
        if websocket:
            await websocket.send_json({
                "status": "navigating",
                "message": "App opened, navigating...",
                "progress": 20.0
            })
        
        # Try to find and handle login/skip if needed
        # This is app-specific and may need adjustment
        try:
            # Example: Skip login or handle splash screen
            # Try multiple selectors for skip/close buttons
            skip_selectors = [
                (AppiumBy.ACCESSIBILITY_ID, "Skip"),
                (AppiumBy.ACCESSIBILITY_ID, "Overslaan"),
                (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Skip' or @name='Overslaan']"),
                (AppiumBy.XPATH, "//android.widget.Button[@text='Skip' or @text='Overslaan']"),
            ]
            for by, selector in skip_selectors:
                try:
                    skip_button = driver.find_element(by, selector)
                    if skip_button.is_displayed():
                        logger.info(f"Found skip button: {selector}")
                        skip_button.click()
                        await asyncio.sleep(1)
                        break
                except:
                    continue
        except Exception as e:
            logger.info(f"No skip button found or already past login: {e}")
        
        if websocket:
            await websocket.send_json({
                "status": "ready",
                "message": "Ready to add products...",
                "progress": 25.0
            })
        
        # Prepare product list with quantities
        products_list = [
            {"name": product.name, "quantity": product.quantity}
            for product in products
        ]
        
        # Use the adapted automation functions
        total_products = len(products)
        success_count, failed_items = await add_multiple_products(
            driver, 
            products_list, 
            device_type, 
            websocket
        )
        
        # Calculate actual products added
        added_count = success_count
        
        if websocket:
            await websocket.send_json({
                "status": "completed",
                "message": f"Successfully added {added_count}/{total_products} products",
                "progress": 100.0
            })
        
        return {
            "status": "success",
            "message": f"Added {added_count}/{total_products} products to basket",
            "products_added": added_count,
            "total_products": total_products,
            "failed_items": failed_items
        }
        
    except Exception as e:
        error_msg = f"Automation error: {str(e)}"
        logger.error(error_msg)
        if websocket:
            await websocket.send_json({
                "status": "error",
                "message": error_msg,
                "progress": 0.0
            })
        raise HTTPException(status_code=500, detail=error_msg)
    
    finally:
        # Don't close driver immediately - keep it open for potential further actions
        pass


@app.get("/")
async def root():
    return {"message": "Albert Heijn Automation API", "status": "running"}


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "driver_connected": driver is not None
    }


@app.post("/automate", response_model=AutomationStatus)
async def start_automation(request: AutomationRequest):
    """Start automation via HTTP POST"""
    try:
        result = await automate_albert_heijn_app(request.products, request.device_type)
        return AutomationStatus(
            status=result["status"],
            message=result["message"],
            progress=100.0
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.websocket("/ws/automate")
async def websocket_automate(websocket: WebSocket):
    """Start automation via WebSocket for real-time updates"""
    await websocket.accept()
    
    try:
        # Receive automation request
        data = await websocket.receive_json()
        request = AutomationRequest(**data)
        
        # Start automation with real-time updates
        result = await automate_albert_heijn_app(
            request.products,
            request.device_type,
            websocket
        )
        
        # Send final result
        await websocket.send_json(result)
        
    except WebSocketDisconnect:
        logger.info("WebSocket disconnected")
    except Exception as e:
        error_msg = f"WebSocket error: {str(e)}"
        logger.error(error_msg)
        await websocket.send_json({
            "status": "error",
            "message": error_msg
        })


@app.post("/disconnect")
async def disconnect_driver():
    """Disconnect from Appium driver"""
    global driver
    if driver:
        driver.quit()
        driver = None
        return {"status": "disconnected", "message": "Driver disconnected successfully"}
    return {"status": "already_disconnected", "message": "No active driver"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

