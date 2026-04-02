from pages.login_page import LoginPage
from utils.driver_setup import get_driver
from config.config import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.dashboard_page import DashboardPage
from utils.screenshot import take_screenshot


def test_login_valid():
    """
    TC-LOG-001
    Expected: User berhasil login dan masuk dashboard
    """
    driver = get_driver()
    wait = WebDriverWait(driver, 10)
    login = LoginPage(driver)

    driver.get(BASE_URL)

    try:
        login.click_sign_in()
        login.input_username(USERNAME_VALID)
        login.input_password(PASSWORD_VALID)
        login.click_login()

        dashboard = DashboardPage(driver)

        wait.until(lambda d: dashboard.is_dashboard_loaded())

        assert dashboard.is_dashboard_loaded(), "Login gagal, dashboard tidak muncul"

        print("✅ TC-LOG-001 PASS")

    except Exception as e:
        take_screenshot(driver, "TC-LOG-001")
        print("❌ TC-LOG-001 FAIL | Actual Result:", str(e))
        raise

    finally:
        driver.quit()


def test_login_invalid():
    """
    TC-LOG-002
    Expected: Muncul error message
    """
    driver = get_driver()
    wait = WebDriverWait(driver, 10)
    login = LoginPage(driver)

    driver.get(BASE_URL)

    try:
        login.click_sign_in()
        login.input_username(USERNAME_INVALID)
        login.input_password(PASSWORD_INVALID)
        login.click_login()

        wait.until(lambda d: ERROR_INDICATOR in d.page_source.lower())

        actual = ERROR_INDICATOR in driver.page_source.lower()

        assert actual, "Actual Result: Error tidak muncul"

        print("✅ TC-LOG-002 PASS")

    except Exception as e:
        take_screenshot(driver, "TC-LOG-002")
        print("❌ TC-LOG-002 FAIL | Actual Result:", str(e))
        raise

    finally:
        driver.quit()