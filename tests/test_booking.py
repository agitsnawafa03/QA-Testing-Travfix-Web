from utils.driver_setup import get_driver
from config.config import *
from selenium.webdriver.common.by import By
from utils.screenshot import take_screenshot


def test_booking_page_load():
    """
    TC-BK-001
    Expected: Halaman booking berhasil dibuka
    """
    driver = get_driver()
    driver.get(BASE_URL)

    try:
        actual = BASE_URL in driver.current_url

        assert actual, "Actual Result: Halaman tidak terbuka"

        print("✅ TC-BK-001 PASS")

    except Exception as e:
        take_screenshot(driver, "TC-BK-001")
        print("❌ TC-BK-001 FAIL | Actual Result:", str(e))
        raise

    finally:
        driver.quit()


def test_book_now_button_visible():
    """
    TC-BK-002
    Expected: Tombol 'Book Now' terlihat
    """
    driver = get_driver()
    driver.get(BASE_URL)

    try:
        button = driver.find_element(By.XPATH, "//button[contains(text(),'Book')]")
        actual = button.is_displayed()

        assert actual, "Actual Result: Button tidak terlihat"

        print("✅ TC-BK-002 PASS")

    except Exception as e:
        take_screenshot(driver, "TC-BK-002")
        print("❌ TC-BK-002 FAIL | Actual Result:", str(e))
        raise

    finally:
        driver.quit()