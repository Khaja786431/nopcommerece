import logging
from selenium.webdriver.common.by import By


class Login_Admin_Page:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    btn_login_xpath = "//button[@type='submit']"
    logout_link_txt = "Logout"

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def enter_username(self, username):
        self.logger.info(f"Entering username: '{username}'")
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.logger.info(f"Entering password: '{password}'")
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.logger.info("Clicking on 'Login' button")
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_logout(self):
        self.logger.info("Clicking on 'Logout' button")
        self.driver.find_element(By.LINK_TEXT, self.logout_link_txt).click()
