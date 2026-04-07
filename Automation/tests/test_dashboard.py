from utils.driver_setup import get_driver
from config.config import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import take_screenshot


def test_navbar_visible_after_login():
    """
    TC-DASH-001
    Expected: Navbar terlihat setelah login
    """
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    driver.get(BASE_URL)

    try:
        # login
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign In')]"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//input"))).send_keys(USERNAME_VALID)
        driver.find_element(By.XPATH, "//input[@placeholder='Enter password']").send_keys(PASSWORD_VALID)
        driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()

        # cek navbar
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "nav")))
        navbar = driver.find_element(By.TAG_NAME, "nav")

        actual = navbar.is_displayed()

        assert actual, "Actual Result: Navbar tidak terlihat"

        print("✅ TC-DASH-001 PASS")

    except Exception as e:
        take_screenshot(driver, "TC-DASH-001")
        print("❌ TC-DASH-001 FAIL | Actual Result:", str(e))
        raise

    finally:
        driver.quit()