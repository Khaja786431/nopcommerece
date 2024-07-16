import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Add_Customer_Page:
    link_customer_menu_xpath = "//a[@href='#']//p[contains(text(), 'Customers')]"
    link_customer_menu_option_xpath = "//li[@class='nav-item']//p[normalize-space(text())='Customers']"
    txt_add_new_xpath = "//div[@class='float-right']/a"
    # txt_add_new_xpath = "//i[@class='fas fa-plus-square']"
    txt_email_id = "Email"
    txt_password_id = "Password"
    txt_first_name_id = "FirstName"
    txt_last_name_id = "LastName"
    radio_male_id = "Gender_Male"
    radio_female_id = "Gender_Female"
    txt_dob_id = "DateOfBirth"
    txt_company_name_id = "Company"
    check_box_tax_exempt_id = "IsTaxExempt"
    newsletter_custrole_xpath = "//input[@class='select2-search__field']"  # it gives two elements
    custrole_remove_registered_xpath = "//span[@class='select2-selection__choice__remove']"
    custrole_guest_xpath = "//li[text()='Guests']"
    custrole_administrators_xpath = "//li[text()='Administrators']"
    custrole_forummoderators_xpath = "//li[text()='Forum Moderators']"
    custrole_registered_xpath = "//li[text()='Registered']"
    custrole_vendors_xpath = "//li[text()='Vendors']"
    drpdwn_manager_of_vendor_id = "VendorId"
    drpdwn_manager_of_vendor_xpath = "//div[@class='col-md-9']/select[@class='form-control']']"
    text_admin_comment_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def click_customer(self):
        self.logger.info("Clicking on 'Customers' menu link")
        self.driver.find_element(By.XPATH, self.link_customer_menu_xpath).click()

    def click_customers_from_menu_options(self):
        self.logger.info("Clicking on 'Customers' from menu options")
        self.driver.find_element(By.XPATH, self.link_customer_menu_option_xpath).click()

    def click_add_new(self):
        self.logger.info("Clicking on 'Customers' from menu options")
        self.driver.find_element(By.XPATH, self.txt_add_new_xpath).click()

    def enter_email(self, email):
        self.logger.info(f"Entering email: '{email}'")
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)
        # e.send_keys(email)

    def enter_password(self, password):
        self.logger.info(f"Entering password: '{password}")
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def enter_firstname(self, firstname):
        self.logger.info(f"Entering first name: '{firstname}'")
        self.driver.find_element(By.ID, self.txt_first_name_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.logger.info(f"Entering last name: '{lastname}'")
        self.driver.find_element(By.ID, self.txt_last_name_id).send_keys(lastname)

    def select_gender(self, gender):
        self.logger.info(f"Selecting gender: '{gender}'")
        if gender == "Male":
            self.driver.find_element(By.ID, self.radio_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.radio_female_id).click()
        else:
            self.driver.find_element(By.ID, self.radio_female_id).click()

    def enter_dob(self, dob):
        self.logger.info(f"Entering dob: '{dob}'")
        self.driver.find_element(By.ID, self.txt_dob_id).send_keys(dob)

    def enter_companyname(self, companyname):
        self.logger.info(f"Entering company name: '{companyname}'")
        self.driver.find_element(By.ID, self.txt_company_name_id).send_keys(companyname)

    def select_tax_exempt(self):
        self.logger.info("Selecting tax exempt checkbox '☑️'")
        self.driver.find_element(By.ID, self.check_box_tax_exempt_id).click()

    def select_newsletter(self, value):
        self.logger.info(f"Selecting newsletter: '{value}'")
        elements = self.driver.find_elements(By.XPATH, self.newsletter_custrole_xpath)
        elements = elements[0]
        elements.click()
        time.sleep(3)
        if value == "Your store name":
            self.driver.find_element(By.XPATH, "//li[text()='Your store name']").click()
        elif value == "Test store 2":
            self.driver.find_element(By.XPATH, "//li[text()='Test store 2']").click()
        else:
            self.driver.find_element(By.XPATH, "//li[text()='Your store name']").click()

    def select_customer_role(self, role):
        self.logger.info(f"Selecting customer role: '{role}'")
        elements = self.driver.find_elements(By.XPATH, self.newsletter_custrole_xpath)
        custrole_field = elements[1]
        custrole_field.click()
        time.sleep(3)
        if role == "Guests":
            self.driver.find_element(By.XPATH, self.custrole_registered_xpath).click()
            custrole_field.click()
            self.driver.find_element(By.XPATH, self.custrole_guest_xpath).click()
            print("registered...")
            custrole_field.click()
        elif role == "Administrators":
            self.driver.find_element(By.XPATH, self.custrole_administrators_xpath).click()
            custrole_field.click()
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.custrole_forummoderators_xpath).click()
            custrole_field.click()
        elif role == "Registered":
            pass
        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.custrole_vendors_xpath).click()
            custrole_field.click()
        else:
            self.driver.find_element(By.XPATH, self.custrole_administrators_xpath).click()
            custrole_field.click()

    def select_manager_of_vendor(self, value):
        self.logger.info(f"Selecting manager of vendor: '{value}'")
        drp_dwn = Select(self.driver.find_element(By.ID, self.drpdwn_manager_of_vendor_id))
        drp_dwn.select_by_visible_text(value)

    def enter_admin_comments(self, admincomments):
        self.logger.info(f"Entering admin comments: '{admincomments}'")
        self.driver.find_element(By.ID, self.text_admin_comment_id).send_keys(admincomments)

    def click_save(self):
        self.logger.info("Clicking on 'Save' button")
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
