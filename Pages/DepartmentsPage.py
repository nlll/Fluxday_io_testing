from Pages.BasePage import BasePage, InvalidPageException
from Pages.LoginPage import LoginPage
from Util.AjaxHelper import AjaxHelper
from Util.locators import locators_home_page, locators_depart_page


class DepartmentsPage(BasePage):
    def __init__(self, driver):
        super(DepartmentsPage, self).__init__(driver)

    @property
    def get_create_depart_link(self):
        return self.driver.find_element_by_link_text(locators_depart_page['loc_create_depart'])

    def click_depart_link(self):
        self.get_create_depart_link.click()

    @property
    def get_create_depart_title(self):
        return self.driver.find_element_by_css_selector(locators_depart_page['loc_create_depart_title'])

    def fill_create_depart_title(self, department_title):
        self.get_create_depart_title.clear()
        self.get_create_depart_title.send_keys(department_title)

    @property
    def get_create_depart_code(self):
        return self.driver.find_element_by_css_selector(locators_depart_page['loc_create_depart_code'])

    def fill_create_depart_code(self, department_code):
        self.get_create_depart_code.clear()
        self.get_create_depart_code.send_keys(department_code)

    @property
    def get_depart_title(self):
        return self.driver.find_element_by_css_selector(locators_depart_page['loc_depart_title'])

    def depart_title(self):
        self.get_depart_title.text()

    @property
    def get_create_depart_save_btn(self):
        return self.driver.find_element_by_css_selector(locators_depart_page['loc_create_depart_save_btn'])

    def click_create_depart_save_btn(self):
        self.get_create_depart_save_btn.click()

    @property
    def get_icon_settings(self):
        return self.driver.find_element_by_css_selector(locators_depart_page['loc_depart_icon_settings'])

    def click_icon_settings(self):
        self.get_icon_settings.click()

    @property
    def get_depart_edit(self):
        return self.driver.find_element_by_link_text(locators_depart_page['loc_depart_icon_settings_edit'])

    def click_depart_edit(self):
        self.get_depart_edit.click()

    @property
    def get_depart_edit_description(self):
        return self.driver.find_element_by_css_selector(locators_depart_page['loc_depart_edit_description'])

    def fill_depart_description(self, department_description):
        self.get_depart_edit_description.clear()
        self.get_depart_edit_description.send_keys(department_description)

    @property
    def get_depart_edit_url(self):
        return self.driver.find_element_by_css_selector(locators_depart_page['loc_depart_edit_url'])

    def fill_depart_url(self, url):
        self.get_depart_edit_url.clear()
        self.get_depart_edit_url.send_keys(url)

    @property
    def get_depart_delete(self):
        return self.driver.find_element_by_link_text(locators_depart_page['loc_depart_icon_settings_delete'])

    def click_depart_delete(self):
        self.get_depart_delete.click()

    def _validate_page(self):
        try:
            self.driver.find_element_by_css_selector(locators_home_page['loc_homepage_logo'])
        except:
            raise InvalidPageException('Departments page not loaded')

    # Departments page methods
    def login_with_admin(self):
        login_with_admin = LoginPage(self.driver)
        login_with_admin.log_in_with_user('admin@fluxday.io', 'password')

    def click_departments_link(self):
        depart_link = BasePage(self.driver)
        depart_link.go_to_depart()

    def click_save_btn(self):
        save_depart = DepartmentsPage(self.driver)
        AjaxHelper.suspend(2)
        save_depart.click_create_depart_save_btn()

    def click_settings_icon(self):
        settings_icon = DepartmentsPage(self.driver)
        AjaxHelper.suspend(2)
        settings_icon.click_icon_settings()

    def click_edit_link(self):
        edit_link = DepartmentsPage(self.driver)
        edit_link.click_depart_edit()

    def refresh(self):
        self.driver.refresh()
        AjaxHelper.suspend(2)
