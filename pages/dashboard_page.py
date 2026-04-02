from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def is_dashboard_loaded(self):
        # indikator sederhana (ubah kalau perlu)
        return "booking" in self.driver.page_source.lower() or \
               "logout" in self.driver.page_source.lower()

    def is_navbar_visible(self):
        try:
            navbar = self.driver.find_element(By.TAG_NAME, "nav")
            return navbar.is_displayed()
        except:
            return False