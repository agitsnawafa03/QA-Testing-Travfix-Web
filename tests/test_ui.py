from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import take_screenshot
import time


def test_ui_zoom():
    """
    TC-UI-001
    Expected: UI tetap normal saat zoom
    """
    driver = get_driver()
    driver.get("http://154.19.37.243:3006/")
    time.sleep(3)

    try:
        driver.execute_script("document.body.style.zoom='80%'")

        navbar = driver.find_element(By.TAG_NAME, "nav")
        assert navbar.is_displayed(), "UI rusak saat zoom"

        print("✅ TC-UI-001 PASS")

    except Exception as e:
        take_screenshot(driver, "TC-UI-001")
        print("❌ TC-UI-001 FAIL | Actual Result:", str(e))
        raise

    finally:
        driver.quit()


def test_responsive_navbar():
    """
    TC-UI-002
    Expected:
    - Hamburger menu muncul di mobile
    - Menu muncul setelah klik hamburger
    """
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    driver.set_window_size(375, 812)
    driver.get("http://154.19.37.243:3006/")
    time.sleep(3)

    try:
        # cari hamburger (sementara generic dulu)
        buttons = driver.find_elements(By.TAG_NAME, "button")

        hamburger = None
        for b in buttons:
            if b.is_displayed():
                text = b.get_attribute("outerHTML").lower()
                if "menu" in text or "toggle" in text or "nav" in text:
                    hamburger = b
                    break

        assert hamburger is not None, "Hamburger tidak ditemukan"

        hamburger.click()
        time.sleep(2)

        navbar = driver.find_element(By.TAG_NAME, "nav")
        assert navbar.is_displayed(), "Menu tidak muncul setelah klik"

        print("✅ TC-UI-002 PASS")

    except Exception as e:
        take_screenshot(driver, "TC-UI-002")
        print("❌ TC-UI-002 FAIL | Actual Result:", str(e))
        raise

    finally:
        driver.quit()