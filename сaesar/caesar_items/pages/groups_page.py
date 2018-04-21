import random
import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from caesar_items.locators.locators import \
    GroupPageLocators, LeftMenuLocators, RightMenuLocators, TopMenuLocators, \
    CreateGroupWindowLocators, LocationWindowLocators, AboutPageLocators, \
    DevelopmentPanelLocators, QualityAssurancePanelLocators, AdminPageLocators
from caesar_items.pages.base_page import BasePage
from caesar_items.pages.admin_page import AdminPage
from resource.url_site import PathUrl
from resource.constants_creating_group import TIME_TO_WAIT, \
    TEST_TEACHER_INDEX, TEST_FIRST_EXPERT_NAME, TEST_START_DATE


class AboutPage(object):
    def __init__(self, driver):
        self.driver = driver

    def development_research_button(self):
        """ Get Development & Research button from about page."""
        try:
            dev_res_button = \
                self.driver.find_element(*AboutPageLocators.
                                         DEVELOPMENT_RESEARCH_BUTTON)
            logging.warning(" Development_research_button was found.")
            return dev_res_button
        except Exception:
            logging.warning(" Development_research_button wasn't found.")

    def quality_assurance_button(self):
        """ Get Quality Assurance button from about page."""
        try:
            qa_button = self.driver.find_element(*AboutPageLocators.
                                                 QUALITY_ASSURANCE)
            logging.warning(" QA button was found!")
            return qa_button
        except Exception:
            logging.warning(" QA button wasn't found!")

    def management_button(self):
        """ Get Management and Mentoring button from about page."""
        try:
            managment_button = \
                self.driver.find_element(*AboutPageLocators.
                                         MANAGEMENT_MENTORING_BUTTON)
            logging.warning(" Management_button was found!")
            return managment_button
        except Exception:
            logging.warning(" Management_button wasn't found!")

    def additional_thanks_button(self):
        """ Get Additional Thanks button from about page."""
        try:
            button = \
                self.driver.find_element(*AboutPageLocators.
                                         ADDITIONAL_THANKS_BUTTON)
            logging.warning(" additional_thanks_button was found!")
            return button
        except Exception:
            logging.warning(" additional_thanks_button wasn't found!")

    def team_doloto_icon(self):
        """ Get Team Doloto icon from Development & Research."""
        try:
            button = \
                self.driver.find_element(*DevelopmentPanelLocators.
                                         TEAM_DOLOTO_ICON)
            logging.warning(" team_doloto_icon was found!")
            return button
        except Exception:
            logging.warning(" team_doloto_icon wasn't found!")

    def get_department_text(self):
        """ Get current department text. """
        try:
            text = \
                self.driver.find_element(*AboutPageLocators.
                                         DEPARTMENT_NAME).text
            logging.warning(" department_text was found!")
            return text
        except Exception:
            logging.warning(" department_text wasn't found!")

    def floppy_drive_team_icon(self):
        """ Get Floppy Drive 8 team icon from Development & Research."""
        try:
            button = \
                self.driver.find_element(*DevelopmentPanelLocators.
                                         FLOPPY_DRIVE_TEAM_ICON)
            logging.warning(" floppy_drive_team_icon was found!")
            return button
        except Exception:
            logging.warning(" floppy_drive_team_icon wasn't found!")

    def fix_machine_icon(self):
        """ Get Fix Machine team icon from Development & Research."""
        try:
            button = \
                self.driver.find_element(*DevelopmentPanelLocators.
                                         FIX_MACHINE_TEAM_ICON)
            logging.warning(" fix_machine_icon was found!")
            return button
        except Exception:
            logging.warning(" fix_machine_icon wasn't found!")

    def light_side_icon(self):
        """ Get The Light Side team icon from Quality Assurance."""
        try:
            button = \
                self.driver.find_element(*QualityAssurancePanelLocators.
                                         LIGHT_SIDE_ICON)
            logging.warning(" light_side_icon was found!")
            return button
        except Exception:
            logging.warning(" light_side_icon wasn't found!")

    def fluffy_dots_icon(self):
        """ Get Fluffy Dots team icon from Quality Assurance."""
        try:
            button = \
                self.driver.find_element(*QualityAssurancePanelLocators.
                                         FLUFFY_DOTS_ICON)
            logging.warning(" fluffy_dots_icon was found!")
            return button
        except Exception:
            logging.warning(" fluffy_dots_icon wasn't found!")

    def charming_chaos_icon(self):
        """ Get Charming Chaos team icon from Quality Assurance."""
        try:
            button = \
                self.driver.find_element(*QualityAssurancePanelLocators.
                                         CHARMIN_CHAOS_ICON)
            logging.warning(" charming_chaos_icon was found!")
            return button
        except Exception:
            logging.warning(" charming_chaos_icon wasn't found!")

    def get_panel_with_photos(self):
        """ Get panel where placed photo of teammates."""
        try:
            panel = \
                self.driver.find_element(*AboutPageLocators.
                                         DEVELOPMENT_TEAM_PHOTOS_PANEL)
            logging.warning(" panel_with_photos was found!")
            return panel
        except Exception:
            logging.warning(" panel_with_photos wasn't found!")

    def get_all_photos(self):
        """ Get all teammates photos when open team window."""
        try:
            photos = self.driver.find_elements(*AboutPageLocators.PHOTO)
            logging.warning("All photos was found.")
            return photos
        except Exception:
            logging.warning("All photos wasn't found.")

    def get_teammate_name_text(self):
        """ Get teammate name from panel with  photos."""
        return self.driver.find_element(*AboutPageLocators.TEAMMATE_NAME).text


class LocationsWindow(object):
    def __init__(self, driver):
        self.driver = driver

    def select_dnipro_location(self):
        """ Click on location on location window."""
        try:
            self.driver.find_element(
                *LocationWindowLocators.DNIPRO_LOCATION).click()
            logging.warning(" Select Dnipro Location works!")
            return self
        except Exception:
            logging.warning(" Select Dnipro Location doesn't work!")

    def select_chernivtsy_location(self):
        """ Click on location on location window."""
        try:
            self.driver.find_element(
                *LocationWindowLocators.CHERNIVTSY_LOCATION).click()
            logging.warning(" Select Cherenivtsy Location works!")
            return self
        except Exception:
            logging.warning(" Select Cherenivtsy Location doesn't work!")

    def select_ivano_frankivsk_location(self):
        """ Click on location on location window."""
        try:
            self.driver.find_element(
                *LocationWindowLocators.IVANO_FRANKIVSK_LOCATION).click()
            logging.warning(" Select ivano_frankivsk Location works!")
            return self
        except Exception:
            logging.warning(" Select ivano_frankivsk Location doesn't work!")

    def select_kyiv_location(self):
        """ Click on location on location window."""
        try:
            self.driver.find_element(
                *LocationWindowLocators.KYIV_LOCATION).click()
            logging.warning(" Select kyiv Location works!")
            return self
        except Exception:
            logging.warning(" Select kyiv Location doesn't work!")

    def select_lviv_location(self):
        """ Click on location on location window."""
        try:
            self.driver.find_element(
                *LocationWindowLocators.LVIV_LOCATION).click()
            logging.warning(" Select lviv Location works!")
            return self
        except Exception:
            logging.warning(" Select lviv Location doesn't work!")

    def select_rivne_location(self):
        """ Click on location on location window."""
        try:
            self.driver.find_element(
                *LocationWindowLocators.RIVNE_LOCATION).click()
            logging.warning(" Select rivne Location works!")
            return self
        except Exception:
            logging.warning(" Select rivne Location doesn't work!")

    def select_sofia_location(self):
        """ Click on location on location window."""
        try:
            self.driver.find_element(
                *LocationWindowLocators.SOFIA_LOCATION).click()
            logging.warning(" Select rivne Location works!")
            return self
        except Exception:
            logging.warning(" Select rivne Location doesn't work!")

    def save_button(self):
        """ Return save button web element."""
        try:
            save_button = self.driver.find_element(*LocationWindowLocators.SAVE_BUTTON)
            logging.warning("Save button was found.")
            return save_button
        except Exception:
            logging.warning("Didn't found save button.")

    def disabled_save_button(self):
        """ Return disabled save button web element."""
        try:
            disabled_save_button = self.driver.find_element(*LocationWindowLocators.
                                                            DISABLED_SAVE_BUTTON)
            logging.warning("Disabled save button was found.")
            return disabled_save_button
        except Exception:
            logging.warning("Didn't found disabled save button.")

    def cancel_button(self):
        """ Return cancel button web element."""
        try:
            cancel_button = self.driver.find_element(*LocationWindowLocators.
                                                     CANCEL_BUTTON)
            logging.warning("Cancel button was found.")
            return cancel_button
        except Exception:
            logging.warning("Didn't found cancel button.")

    def get_current_url(self):
        """ Get url on current page."""
        return self.driver.current_url


class LeftMenu(object):
    def __init__(self, driver):
        self.driver = driver

    def create_group_button(self):
        """ Get create button web element."""
        return WebDriverWait(self.driver, TIME_TO_WAIT).until(
            EC.visibility_of_element_located(
                LeftMenuLocators.BUTTON_CREATE_GROUP))

    def search_group_button(self):
        """ Get search button web element."""
        return self.driver.find_element(*LeftMenuLocators.BUTTON_SEARCH_GROUP)

    def edit_group_button(self):
        """ Get edit button web element."""
        return self.driver.find_element(*LeftMenuLocators.BUTTON_EDIT_GROUP)

    def delete_group_button(self):
        """ Get delete button web element."""
        return self.driver.find_element(*LeftMenuLocators.BUTTON_DELETE_GROUP)


class RightMenu(object):
    def __init__(self, driver):
        self.driver = driver

    def click_logout_button(self):
        """ Click on logout web element."""
        self.driver.find_element(*RightMenuLocators.BUTTON_LOGOUT).click()

    def get_user_full_name_text(self):
        """ Get user name from left menu."""
        return self.driver.find_element(*RightMenuLocators.USER_NAME).text

    def get_user_role_text(self):
        """ Get user role from left menu."""
        return self.driver.find_element(*RightMenuLocators.USER_ROLE).text

    def click_edit_user_button(self):
        """ Click on edit user button on right menu."""
        self.driver.find_element(*RightMenuLocators.BUTTON_EDIT_PROFILE).click()

    def get_current_url(self):
        """ Get current url of page."""
        return self.driver.current_url


class TopMenu(object):
    def __init__(self, driver):
        self.driver = driver
        self.locations = LocationsWindow(self.driver)
        self.about = AboutPage(self.driver)

    def click_locations_button(self):
        """ Click locations button on top menu and wait when save button appears."""
        self.driver.find_element(*TopMenuLocators.LOCATIONS_BUTTON).click()
        WebDriverWait(self.driver, TIME_TO_WAIT) \
            .until(EC.visibility_of_element_located(LocationWindowLocators.
                                                    SAVE_BUTTON))
        return LocationsWindow(self.driver)

    def click_groups_button(self):
        """ Click groups button on top menu."""
        self.driver.find_element(*TopMenuLocators.GROUPS_BUTTON_).click()
        self.driver.implicitly_wait(2)

    def click_students_button(self):
        """ Click students button on top menu."""
        self.driver.find_element(*TopMenuLocators.STUDENTS_BUTTON).click()
        self.driver.implicitly_wait(2)

    def click_schedule_button(self):
        """ Click schedule button on top menu."""
        self.driver.find_element(*TopMenuLocators.SCHEDULE_BUTTON).click()
        self.driver.implicitly_wait(2)

    def click_add_button(self):
        """ Click add button on top menu."""
        self.driver.find_element(*TopMenuLocators.ADD_BUTTON).click()
        self.driver.implicitly_wait(2)

    def click_about_button(self):
        """ Click about button on top menu."""
        self.driver.find_element(*TopMenuLocators.ABOUT_BUTTON).click()
        self.driver.implicitly_wait(2)
        return AboutPage(self.driver)

    def click_logout_button(self):
        """ Click about button on top menu."""
        self.driver.find_element(*TopMenuLocators.BUTTON_LOGOUT).click()
        self.driver.implicitly_wait(2)


class GroupsPage(BasePage):
    group_page_title = 'Caesar'
    driver = None

    def __init__(self, driver):
        super().__init__(driver)
        GroupsPage.driver = driver
        self.left_menu = LeftMenu(self.driver)
        self.right_menu = RightMenu(self.driver)
        self.top_menu = TopMenu(self.driver)

    def get_group_location_text(self):
        """ Get current locations from middle panel."""
        return self.driver.find_element(*GroupPageLocators.GROUP_LOCATION).text

    def my_group_button(self):
        """ Get my group web element button."""
        return self.driver.find_element(*GroupPageLocators.BUTTON_MY_GROUPS)

    def all_groups_button(self):
        """ Get all groups web element button."""
        return self.driver.find_element(*GroupPageLocators.BUTTON_ALL_GROUPS)

    def ended_groups_button(self):
        """ Get finished groups web element button."""
        return self.driver.find_element(*GroupPageLocators.ENDED_GROUPS)

    def current_groups_button(self):
        """ Get current groups web element button."""
        return self.driver.find_element(*GroupPageLocators.CURRENT_GROUPS)

    def button_boarding_groups(self):
        """ Get boarding groups web element button."""
        return self.driver.find_element(*GroupPageLocators.BOARDING_GROUPS)

    def select_group_by_name(self, group_name):
        """ Find group by name and click on it."""
        groups = self.driver.find_elements(*GroupPageLocators.GROUPS)
        for group in groups:
            if group_name == group.text:
                group.click()
                return 0
        return "group not exist"

    def list_group_current(self):
        """ Get list of groups web element from current stage."""
        groups_list = []
        groups = self.driver.find_elements(*GroupPageLocators.GROUPS)
        for group in groups:
            groups_list = group.text
        return groups_list

    def list_of_groups(self):
        """ Get all groups from all stages."""
        self.ended_groups_button().click()
        list_of_groups = self.list_group_current()
        self.current_groups_button().click()
        list_of_groups += self.list_group_current()
        self.button_boarding_groups().click()
        list_of_groups += self.list_group_current()
        return list_of_groups

    def open_left_menu(self):
        """ Move mouse on left side page."""
        left_menu = self.driver.find_element(*GroupPageLocators.LEFT_MENU)
        ActionChains(self.driver). \
            move_to_element_with_offset(left_menu, 105, 300).perform()
        WebDriverWait(self.driver, TIME_TO_WAIT) \
            .until(EC.visibility_of_element_located(LeftMenuLocators.
                                                    BUTTON_SEARCH_GROUP))
        return self.left_menu

    def open_right_menu(self):
        """ Click on user photo."""
        self.driver.find_element(*GroupPageLocators.USER_PHOTO).click()
        WebDriverWait(self.driver, TIME_TO_WAIT). \
            until(EC.visibility_of_element_located(RightMenuLocators.
                                                   BUTTON_LOGOUT))
        return self.right_menu

    def open_top_menu(self):
        """ Move mouse on top page."""
        top_menu = self.driver.find_element(*GroupPageLocators.TOP_MENU)
        ActionChains(self.driver).move_to_element(top_menu).perform()
        return self.top_menu

    def open_admin_page(self):
        """ Open admin page panel."""
        self.driver.get(PathUrl().ADMIN_PAGE)
        WebDriverWait(self.driver, TIME_TO_WAIT) \
            .until(EC.visibility_of_element_located(AdminPageLocators.
                                                    BUTTON_ESCAPE))
        return AdminPage(self.driver)

    def get_group_stage_text(self):
        """ Get stage text from bottom of middle panel."""
        group_stage = WebDriverWait(self.driver, TIME_TO_WAIT) \
            .until(
            EC.visibility_of_element_located(GroupPageLocators.GROUP_STAGE))
        return group_stage.text

    def confirm_deletion_button(self):
        """ Get confirm deletion web element button."""
        return self.driver. \
            find_element(*GroupPageLocators.BUTTON_CONFIRM_DELETION)

    def cancel_deletion_button(self):
        """ Get cancel deletion web element button."""
        return self.driver. \
            find_element(*GroupPageLocators.BUTTON_CANCEL_DELETION)

    def group_info_button(self):
        """ Get group's info button."""
        return self.driver.find_element(*GroupPageLocators.INFO_GROUP_BUTTON)

    def group_students_button(self):
        """ Get group's students button."""
        return self.driver.find_element(*GroupPageLocators.
                                        STUDENTS_IN_GROUP_BUTTON)

    def group_schedule_button(self):
        """ Get group's schedule button."""
        return self.driver.find_element(*GroupPageLocators.
                                        SCHEDULE_GROUP_BUTTON)

    def group_message_button(self):
        """ Get group's message button."""
        return self.driver.find_element(*GroupPageLocators.
                                        MESSAGE_GROUP_BUTTON)

    def group_edit_button(self):
        """ Get group edit button from info panel."""
        return self.driver.find_element(*GroupPageLocators.
                                        MESSAGE_GROUP_BUTTON)

    class CreateGroupWindow(object):
        def __init__(self):
            self.driver = GroupsPage.driver
            self.group_name_field = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.element_to_be_clickable(CreateGroupWindowLocators.
                                                 GROUP_NAME_FIELD))
            self.group_name_form = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.presence_of_element_located(CreateGroupWindowLocators.
                                                     GROUP_NAME_FORM))
            self.group_direction_form = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.presence_of_element_located(CreateGroupWindowLocators.
                                                     DIRECTION_FORM))
            self.group_location_form = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.presence_of_element_located(CreateGroupWindowLocators.
                                                     LOCATION_FORM))
            self.start_date_form = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.presence_of_element_located(CreateGroupWindowLocators.
                                                     START_DATE_FORM))
            self.experts_form = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.presence_of_element_located(CreateGroupWindowLocators.
                                                     EXPERTS_FORM))
            self.group_direction_list = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.element_to_be_clickable(CreateGroupWindowLocators.
                                                 DIRECTION_DROP_LIST))
            self.group_location_list = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.element_to_be_clickable(CreateGroupWindowLocators.
                                                 LOCATION_DROP_LIST))
            self.teacher_add_button = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.element_to_be_clickable(CreateGroupWindowLocators.
                                                 ONE_MORE_TEACHER_BUTTON))
            self.start_date_field = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.element_to_be_clickable(CreateGroupWindowLocators.
                                                 START_DATE_FIELD))
            self.finish_date_field = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.element_to_be_clickable(CreateGroupWindowLocators.
                                                 FINISH_DATE_FIELD))
            self.save_group_button = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.element_to_be_clickable(CreateGroupWindowLocators.
                                                 SAVE_BUTTON))
            self.cancel_button = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.element_to_be_clickable(CreateGroupWindowLocators.
                                                 CANCEL_BUTTON))
            self.add_expert_button = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.element_to_be_clickable(CreateGroupWindowLocators.
                                                 ADD_EXPERT_BUTTON))

        def get_group_name_field(self) -> object:
            """ Get group name field web element."""
            return self.group_name_field

        def set_group_name(self, new_group_name) -> object:
            """ Set group name using entered value."""
            self.clear_group_name_field()
            self.group_name_field.send_keys(new_group_name)
            return self

        def clear_group_name_field(self) -> object:
            """ Clear group name field."""
            self.group_name_field.clear()
            return self

        def get_group_name_form(self) -> object:
            """ Get group name form web element. """
            return self.group_name_form

        def get_group_direction_form(self) -> object:
            """ Get direction form web element."""
            return self.group_direction_form

        def get_group_location_form(self) -> object:
            """ Get location form web element."""
            return self.group_location_form

        def get_start_date_form(self) -> object:
            """ Get start date form web element."""
            return self.start_date_form

        def get_experts_form(self) -> object:
            """ Get expert form web element."""
            return self.experts_form

        def get_value_group_name_field(self) -> str:
            """ Get value from group name field."""
            return self.group_name_field.get_attribute("value")

        def get_group_direction(self) -> object:
            """ Get  group direction web element."""
            return self.group_direction_list

        def set_group_direction(self, str_direction) -> object:
            """ Set  chosen group direction."""
            select_direction = Select(self.group_direction_list)
            select_direction.select_by_value(str_direction)
            return self

        def get_value_of_direction(self) -> str:
            """ Get value of group from direction field."""
            return self.group_direction_list.get_attribute("value")

        def get_group_location(self) -> object:
            """ Get  group location web element."""
            return self.group_location_list

        def set_group_location(self, location_value) -> object:
            """ Set  chosen group location."""
            self.group_location_list.click()
            select_location = Select(self.group_location_list)
            select_location.select_by_visible_text(location_value)
            return self

        def get_value_of_location(self) -> str:
            """ Get value from group location field."""
            return self.group_location_list.get_attribute("value")

        def get_teacher_add_button(self) -> object:
            """ Get  teacher add button web element."""
            return self.teacher_add_button

        def get_teachers_drop_list(self) -> object:
            """ Get  teachers drop down list web element ."""
            self.teacher_add_button.click()
            try:
                return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                    EC.element_to_be_clickable(CreateGroupWindowLocators.
                                               TEACHERS_DROP_LIST))
            finally:
                return NoSuchElementException

        def select_teacher(self, teacher_name) -> object:
            """ Select teacher from teachers drop down list."""
            self.get_teacher_add_button().click()
            self.get_teachers_drop_list().click()
            select = Select(self.get_teachers_drop_list())
            select.select_by_index(teacher_name)
            self.driver.find_element(CreateGroupWindowLocators.ACCEPT_TEACHER_BUTTON)
            return self

        def add_teacher(self) -> object:
            """ Accept choosing teacher from teachers drop down list."""
            self.get_teacher_add_button().click()
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ACCEPT_TEACHER_BUTTON)).click()
            return self

        def get_values_from_added_teachers_list(self) -> list:
            """ Get values from "added teachers" list."""
            added_teachers_form = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               ADDED_TEACHERS_FORM))
            added_teachers_list = added_teachers_form.find_elements(By.CLASS_NAME, 'list-item')
            list_of_teachers_values = []
            for added_teacher in added_teachers_list:
                list_of_teachers_values.append(added_teacher.text)
            return list_of_teachers_values

        def set_start_date(self, start_date_value) -> object:
            """ Set value to "start date" field."""
            self.start_date_field.send_keys(start_date_value)
            self.finish_date_field.send_keys(Keys.ENTER)
            return self

        def submit_group_creating_button(self) -> object:
            """ End group creating and save all fields."""
            self.save_group_button.click()
            return self

        def get_save_group_button(self) -> object:
            """ Get "Save" button web element."""
            return self.save_group_button

        def get_warning_message_by_form(self, form) -> object:
            """ Get  pop-up warning message web element, attached to this form."""
            warning_message = None
            hints = form.find_elements(By.CLASS_NAME, 'hint')
            for hint in hints:
                hint = hint.find_elements(
                    By.TAG_NAME, 'p')
                for message_text in hint:
                    warning_message = message_text.text
            return warning_message

        def cancel_button_get(self) -> object:
            """ Get "Cancel" button web element."""
            return self.cancel_button

        def add_expert(self, expert_name) -> object:
            """ Add expert - first click the "+one more expert" button, then set
            expert's name and then click  "accept  expert" button."""
            self.add_expert_button.click()
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(
                    CreateGroupWindowLocators.EXPERTS_NAME_FIELD)). \
                send_keys(expert_name)
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(
                    CreateGroupWindowLocators.ACCEPT_EXPERT_BUTTON)).click()
            return self

        def get_added_experts_list(self) -> list:
            """ Get values from "added experts" list."""
            added_experts_form = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               ADDED_EXPERTS_LIST))
            added_experts_list = added_experts_form. \
                find_elements(By.CLASS_NAME, 'list-item')
            list_of_values = []
            for added_expert in added_experts_list:
                list_of_values.append(added_expert.text)
            return list_of_values

        def auto_fill_all_fields(self, new_group_name, group_location,
                                 group_direction) -> None:
            """ Fill  all fields, to create some group,
                            function used to test deleting of groups."""
            self.group_direction_list.click()
            self.set_group_direction(group_direction)
            self.group_location_list.click()
            select_location = Select(self.group_location_list)
            select_location.select_by_value(group_location)
            self.teacher_add_button.click()
            drop_list_teachers = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           TEACHERS_DROP_LIST))
            drop_list_teachers.click()
            select = Select(drop_list_teachers)
            select.select_by_index(TEST_TEACHER_INDEX)
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ACCEPT_TEACHER_BUTTON)).click()
            self.add_expert(TEST_FIRST_EXPERT_NAME)
            self.start_date_field.send_keys(TEST_START_DATE)
            self.finish_date_field.send_keys(Keys.ENTER)
            self.group_name_field.clear()
            self.group_name_field.send_keys(new_group_name)
            self.save_group_button.click()
