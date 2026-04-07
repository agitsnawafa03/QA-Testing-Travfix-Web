from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_sign_in(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()

    def input_username(self, username):
        self.driver.find_element(By.XPATH, "//input[contains(@placeholder,'username')]").send_keys(username)

    def input_password(self, password):
        self.driver.find_element(By.XPATH, "//input[contains(@placeholder,'password')]").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, "//button[contains(.,'Sign In')]").click()