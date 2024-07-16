import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.Add_Customer_Page import Add_Customer_Page


class Test_03_Add_New_Customer:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    def test_add_new_customer(self, setup, logger):
        self.logger.info("**************☞➰ ☄︎ Test_03_Add_New_Customer has started ☄︎ ➰☜************")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("~~~~~~~~~~~~~~~☞ Login Completed ☜~~~~~~~~~~~~~~~~")
        self.logger.info("~~~~~~~~~~~~~~~☞ Starting add customer test ☜~~~~~~~~~~~~~~~~")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customer()
        self.add_customer.click_customers_from_menu_options()
        self.add_customer.click_add_new()
        self.logger.info("~~~~~~~~~~~~~~~☞ Providing customer info started ☜~~~~~~~~~~~~~~~~")
        email = generate_random_email()
        print(email)
        self.add_customer.enter_email(email)
        self.add_customer.enter_password("Test@123")
        self.add_customer.enter_firstname("Jack")
        self.add_customer.enter_lastname("Jones")
        self.add_customer.select_gender("Male")
        self.add_customer.enter_dob("10/10/1992")
        self.add_customer.enter_companyname("MyCompany")
        self.add_customer.select_tax_exempt()
        self.logger.info("~~~~~~~~~~~~~☝︎Scroll-UP the page☝︎~~~~~~~~~~~~~~~~")
        self.driver.execute_script("window.scrollTo(0, 200);")
        self.add_customer.select_newsletter("Test store 2")
        self.logger.info("~~~~~~~~~~~~~~~☞ Test store 2 selected ☜~~~~~~~~~~~~~~~~")
        self.add_customer.select_customer_role("Vendors")
        self.add_customer.select_manager_of_vendor("Vendor 1")
        self.add_customer.enter_admin_comments("Test admin comment")
        self.add_customer.click_save()
        # Test case validation  success message in the body
        customer_add_success_txt = "The new customer has been added successfully"
        success_txt = self.driver.find_element(By.XPATH, "//div[@class='content-wrapper']/div[1]").text
        if customer_add_success_txt in success_txt:
            assert True
            self.logger.info("~~~~~~~~~~~~~~~❧ Test_03_Add_New_Customer test passed 😀❧~~~~~~~~~~~~~~~~")
            self.driver.close()
        else:
            self.logger.info("~~~~~~~~~~~~~~~Test_03_Add_New_Customer test failed 👎~~~~~~~~~~~~~~~~")
            self.driver.save_screenshot("./screenshots/test_add_new_user.png")
            self.driver.close()
            assert False


def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'example.com'])
    return f'{username}@{domain}'
