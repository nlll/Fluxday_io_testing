from abc import abstractmethod

from Pages.BasePage import BasePage
from Pages.DepartmentsPage import DepartmentsPage
from Pages.LoginPage import LoginPage


class DepartmentsPageMethods(BasePage):
    def __init__(self, driver):
        super(DepartmentsPageMethods, self).__init__(driver)

    def login_with_admin(self):
        login_with_admin = LoginPage(self.driver)
        login_with_admin.log_in_with_user('admin@fluxday.io', 'password')

    def click_departments_link(self):
        depart_link = BasePage(self.driver)
        depart_link.go_to_depart()

    def click_save_btn(self):
        save_depart = DepartmentsPage(self.driver)
        save_depart.click_create_depart_save_btn()

    def click_settings_icon(self):
        settings_icon = DepartmentsPage(self.driver)
        settings_icon.click_icon_settings()

    def click_edit_link(self):
        edit_link = DepartmentsPage(self.driver)
        edit_link.click_depart_edit()

    @abstractmethod
    def _validate_page(self):
        pass
