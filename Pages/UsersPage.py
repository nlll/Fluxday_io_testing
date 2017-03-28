from Pages.BasePage import BasePage, InvalidPageException
from selenium.common.exceptions import NoSuchElementException
from Util.AjaxHelper import AjaxHelper
from Util.locators import locators_users_page, locators_home_page


class UsersPage(BasePage):
    def __init__(self, driver):
        super(UsersPage, self).__init__(driver)

    # returns add user button
    @property
    def get_add_users_button(self):
        return self.driver.find_element_by_css_selector(locators_users_page['add_user_button'])

    # returns name field
    @property
    def get_add_users_name_field(self):
        return self.driver.find_element_by_css_selector(locators_users_page['name_add_user'])

    # returns nickname field
    @property
    def get_add_users_nickname_field(self):
        return self.driver.find_element_by_css_selector(locators_users_page['nickname_add_user'])

    # returns email field
    @property
    def get_add_users_email_field(self):
        return self.driver.find_element_by_css_selector(locators_users_page['email_add_user'])

    # returns employee code field
    @property
    def get_add_users_empl_code_field(self):
        return self.driver.find_element_by_css_selector(locators_users_page['empl_code_add_user'])

    # returns password field
    @property
    def get_add_users_pass_field(self):
        return self.driver.find_element_by_css_selector(locators_users_page['pass_add_user'])

    # returns password conformation field
    @property
    def get_add_users_pass_conf_field(self):
        return self.driver.find_element_by_css_selector(locators_users_page['pass_confirm_add_user'])

    # returns save button
    @property
    def get_new_user_save(self):
        # return self.driver.find_element_by_xpath('//*[@id="new_user"]/div[3]/div[2]/input')
        return self.driver.find_element_by_css_selector(locators_users_page['save_button'])

    # adds new user
    def add_new_user(self, name, nickname, email, empl_code, password, ):
        self.get_add_users_button.click()
        self.get_add_users_name_field.send_keys(name)
        self.get_add_users_nickname_field.send_keys(nickname)
        self.get_add_users_email_field.send_keys(email)
        self.get_add_users_empl_code_field.send_keys(empl_code)
        self.get_add_users_pass_field.send_keys(password)
        self.get_add_users_pass_conf_field.send_keys(password)
        self.driver.find_element_by_css_selector(locators_users_page['save_button']).click()

    # returns settings button of a user
    @property
    def get_sett_button(self):
        return self.driver.find_element_by_css_selector(locators_users_page['sett_user_button'])

    # returns settings button of a user as list
    @property
    def sett_buttons(self):
        return self.driver.find_elements_by_css_selector(locators_users_page['sett_user_button'])

    # returns delete button of a user
    @property
    def get_delete_user_button(self):
        return self.driver.find_element_by_link_text(locators_users_page['del_user_butt'])

    # returns edit button of a user
    @property
    def get_edit_user_button(self):
        return self.driver.find_element_by_link_text(locators_users_page['edit_user_butt'])

    # return message box right corner of screen
    @property
    def message_box(self):
        return self.driver.find_element_by_css_selector(locators_users_page['message'])

    def change_user_empl_code(self, user, empl_code):
        # change user employee code
        self.driver.find_element_by_link_text(user).click()
        self.get_sett_button.click()
        self.get_edit_user_button.click()
        self.get_add_users_empl_code_field.clear()
        self.get_add_users_empl_code_field.send_keys(empl_code)
        self.get_new_user_save.click()
        AjaxHelper.suspend(2)

    def change_user_nickname(self, user, nickname):
        # changes user nickname
        self.driver.find_element_by_link_text(user).click()
        self.get_sett_button.click()
        self.get_edit_user_button.click()
        self.get_add_users_nickname_field.clear()
        self.get_add_users_nickname_field.send_keys(nickname)
        self.get_new_user_save.click()
        AjaxHelper.suspend(2)

    def click_user(self, user):
        # clicks on user and opens it
        self.driver.find_element_by_link_text(user).click()

    def del_user(self, user):
        # deletes user
        self.driver.find_element_by_link_text(user).click()
        self.get_sett_button.click()
        self.get_delete_user_button.click()
        AjaxHelper.suspend(1)
        self.driver.switch_to_alert().accept()

    # returns true if user found, if no such user returns false
    def find_user(self, user):
        try:
            self.driver.find_element_by_link_text(user)
        except NoSuchElementException:
            return False
        return True

    def _validate_page(self):
        # validate loaded page is users page
        try:
            assert self.driver.find_element_by_css_selector(locators_home_page['home_page_title']).text == 'Users'
        except AssertionError:
            raise InvalidPageException('Users page not loaded')
