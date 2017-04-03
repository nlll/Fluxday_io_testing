from Pages.BasePage import BasePage, InvalidPageException
from selenium.webdriver.common.keys import Keys
from Util.locators import locators_home_page, locators_login_page


class HomePage(BasePage):
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)


    # @property
    # def get_user_link(self):
    #     return self.driver.find_element_by_xpath(locators_home_page['loc_homepage_user'])

    def logged_user(self, user):
        if self.driver.find_element_by_link_text(user):
            return True
        else:
            return False

    @property
    def get_search_field(self):
        return self.driver.find_element_by_id(locators_home_page['loc_search_field'])

    def click_search_field(self):
        self.get_search_field.clear()
        self.get_search_field.send_keys("Reports")
        self.get_search_field.send_keys(Keys.ENTER)
 
    @property
    def get_oauth_app_btn(self):
        oauth=self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul[2]/li[8]/a')
        return oauth

    def click_oauthapp_btn(self):
        self.get_oauth_app_btn.click()
        
    def _validate_page(self):
        try:
            assert self.driver.find_element_by_css_selector(locators_home_page['home_page_title']).text == 'Entries'
        except AssertionError:
            raise InvalidPageException('Home page not loaded')
