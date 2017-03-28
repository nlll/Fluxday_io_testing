from abc import abstractmethod

from Util.AjaxHelper import AjaxHelper
from Util.locators import locators_home_page


class BasePage:
    """This is the super class of all pages, all pages inherit from it"""

    def __init__(self, driver):
        self.driver = driver
        self._validate_page()

    @property
    def get_dep_link(self):
        return self.driver.find_element_by_link_text(locators_home_page['loc_departments'])

    def go_to_depart(self):
        self.get_dep_link.click()
        AjaxHelper.suspend(2)
        from Pages.DepartmentsPage import DepartmentsPage
        return DepartmentsPage(self.driver)

    @property
    def get_team_link(self):
        return self.driver.find_element_by_link_text(locators_home_page['loc_team'])

    def go_to_team(self):
        self.get_team_link.click()
        AjaxHelper.suspend(2)
        from Pages.TeamPage import TeamPage
        return TeamPage(self.driver)

    @property
    def get_users_link(self):
        return self.driver.find_element_by_link_text(locators_home_page['loc_users'])

    def go_to_users(self):
        self.get_users_link.click()
        AjaxHelper.suspend(2)
        from Pages.UsersPage import UsersPage
        return UsersPage(self.driver)


    @property
    def get_reports_link(self):
        return self.driver.find_element_by_link_text(locators_home_page['loc_reports'])

    def go_to_reports(self):
        self.get_reports_link.click()
        AjaxHelper.suspend(2)
        from Pages.ReportsPage import ReportsPage
        return ReportsPage(self.driver)

    @property
    def get_oauth_link(self):
        return self.driver.find_element_by_link_text(locators_home_page['loc_oauth'])

    def go_to_oauth(self):
        self.get_oauth_link.click()
        AjaxHelper.suspend(2)
        from Pages.OAuthPage import OAuthPage
        return OAuthPage(self.driver)

    @abstractmethod
    def _validate_page(self):
        pass


class InvalidPageException(Exception):
    """Throw this exception when you don't find the correct page"""
