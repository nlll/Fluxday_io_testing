from Pages.BasePage import BasePage, InvalidPageException
from Pages.HomePage import HomePage
from Util.locators import locators_login_page


class LoginPage(BasePage):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    @property
    def get_login_username_field(self):
        return self.driver.find_element_by_css_selector(locators_login_page['loc_login_user'])

    @property
    def get_login_password_field(self):
        return self.driver.find_element_by_css_selector(locators_login_page['loc_login_pass'])

    @property
    def get_login_button(self):
        return self.driver.find_element_by_css_selector(locators_login_page['loc_login_butt'])

    def log_in_with_user(self, username, password):
        self.get_login_username_field.send_keys(username)
        self.get_login_password_field.send_keys(password)
        self.get_login_button.click()
        return HomePage(self.driver)

    def _validate_page(self):
        try:
            self.driver.find_element_by_css_selector(locators_login_page['loc_login_title'])
        except:
            raise InvalidPageException("Login page is not loading")
