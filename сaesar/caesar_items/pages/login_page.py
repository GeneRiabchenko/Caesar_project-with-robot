from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from caesar_items.pages.base_page import BasePage
from caesar_items.locators.locators import LogInLocators, GroupPageLocators
from caesar_items.pages.groups_page import GroupsPage
import logging


class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_login_field_text(self, user_login=''):
        """ Enter user login in login field."""
        try:
            login_field = self.driver.find_element(*LogInLocators.LOGIN_FIELD)
            login_field.clear()
            login_field.send_keys(user_login)
            logging.warning("Fill login field works!")
        except Exception:
            logging.warning("Fill login field doesn't work!")

    def set_password_field_text(self, user_password=''):
        """ Enter user password in password field."""
        try:
            password_field = self.driver.\
                find_element(*LogInLocators.PASSWORD_FIELD)
            password_field.clear()
            password_field.send_keys(user_password)
            logging.warning("Fill password field works!")
        except Exception:
            logging.warning("Fill password field doesn't work!")

    def get_message_text(self):
        """ Get error message above login field."""
        try:
            error_message = self.driver.find_element(*LogInLocators.
                                                     FIELD_MESSAGE).text
            logging.warning("Error message was found.")
            return error_message
        except Exception:
            logging.warning("Error message wasn't found.")

    def submit_button(self):
        """ Get submit button web element."""
        try:
            submit_button = self.driver.find_element(*LogInLocators.CONFIRM_ACTION)
            logging.warning("Submit button was found!")
            return submit_button
        except Exception:
            logging.warning("Submit button wasn't found!")

    def click_submit_button(self):
        """ Click on submit button and wait for user photo."""
        self.driver.find_element(*LogInLocators.CONFIRM_ACTION).click()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(GroupPageLocators.USER_PHOTO))
            logging.warning("Submit button was clicked!")
            return GroupsPage(self.driver)
        except Exception:
            logging.warning("Submit button wasn't clicked!")
            return self

    def auto_login(self, user):
        """ Custom function to login on site."""
        self.set_login_field_text(user.login)
        self.set_password_field_text(user.password)
        return self.click_submit_button()

    def login_use_tab_n_enter_keys(self, user):
        """ Login on site using Enter and Tab keys."""
        try:
            ActionChains(self.driver).send_keys(user.login).send_keys(Keys.TAB) \
                .send_keys(user.password).send_keys(Keys.ENTER).perform()
            WebDriverWait(self.driver, 5).\
                until(EC.visibility_of_element_located(GroupPageLocators.
                                                       USER_PHOTO))
            logging.warning("Func login_use_tab_n_enter_keys works!")
            return GroupsPage(self.driver)
        except Exception:
            logging.warning("Func login_use_tab_n_enter_keys doesn't work!")



