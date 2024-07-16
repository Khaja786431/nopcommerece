import pytest
# from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def test_title_verification(self, setup, logger):
        self.logger.info("**************Test_01_Admin_Login*************** ")
        self.logger.info("***********Verification of admin login page title*************** ")
        self.logger.info("***********Title verification has started*************** ")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "Your store. Login"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./screenshots/test_title_verification.png")
            self.logger.info("**************Title not matches as expected*************** ")
            self.driver.close()
            assert False

    def test_valid_admin_login(self, setup, logger):
        self.logger.info("***********Test valid admin login has  started*************** ")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_dashboard_txt = self.driver.find_element(By.XPATH, "//div[@class='content-header']/h1").text
        exp_dashboard_txt = "Dashboard"
        if act_dashboard_txt == exp_dashboard_txt:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./screenshots/test_valid_admin_login.png")
            self.logger.info("**************Title not matches as expected*************** ")
            self.driver.close()
            assert False

    def test_invalid_admin_login(self, setup, logger):
        self.logger.info("***********Test invalid admin login has started*************** ")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_message = self.driver.find_element(By.XPATH, "//li").text
        if error_message == "No customer account found":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./screenshots/test_invalid_admin_login.png")
            self.logger.info("**************Title not matches as expected*************** ")
            self.driver.close()
            assert False


