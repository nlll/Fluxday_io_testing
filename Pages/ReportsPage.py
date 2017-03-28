
from selenium.webdriver.common.keys import Keys

from Pages.BasePage import BasePage, InvalidPageException
from Util.locators import locators_reports_page,locators_home_page


class ReportsPage(BasePage):
    def __init__(self, driver):
        super(ReportsPage, self).__init__(driver)

    @property
    def get_worklogs(self):
        return self.driver.find_element_by_xpath(locators_reports_page['loc_worklogs'])

    def click_worklogs(self):
        self.get_worklogs.click()

    @property
    def get_worklogs_drop(self):
        return self.driver.find_element_by_xpath(locators_reports_page['loc_worklogs_drop'])

    def click_worklogs_drop(self):
        return self.get_worklogs_drop.click()

    @property
    def get_reports_month(self):
        return self.driver.find_element_by_css_selector(locators_reports_page['loc_month'])

    def click_reports_month(self):
        return self.get_reports_month.click()

    @property
    def get_reports_year(self):
        return self.driver.find_element_by_css_selector(locators_reports_page['loc_year'])

    def click_reports_year(self):
        return self.get_reports_year.click()

    @property
    def get_type_month(self):
        return self.driver.find_element_by_css_selector(locators_reports_page['loc_type_month'])

    def type_month(self):
        return self.get_type_month.click()

    def rep_month(self):
        self.get_type_month.send_keys(Keys.ENTER)

    def rep_year(self):
        self.get_reports_month.clear()
        self.get_reports_month.send_keys("2016")

    @property
    def get_reports_button(self):
        return self.driver.find_element_by_xpath(locators_reports_page['loc_report_butt'])

    def click_reports_button(self):
        return self.get_reports_button.click()

    @property
    def get_reports_calendar(self):
        return self.driver.find_element_by_id(locators_reports_page['loc_calendar'])

    def click_calendar(self):
        return self.get_reports_calendar.click()

    @property
    def get_reports_calendar_next(self):
        return self.driver.find_element_by_css_selector(locators_reports_page['loc_calendar_next'])

    def click_calendar_next(self):
        return self.get_reports_calendar_next.click()

    @property
    def get_reports_type(self):
        return self.driver.find_element_by_css_selector(locators_reports_page['loc_group_by_name'])

    def click_type(self):
        return self.get_reports_type.click()

    @property
    def get_reports_chosen_type(self):
        return self.driver.find_element_by_css_selector(locators_reports_page['loc_report_chosen_type'])

    def choose_reports_type(self):
        return self.get_reports_chosen_type.click()

    @property
    def get_reports_name(self):
        return self.driver.find_element_by_css_selector(locators_reports_page['loc_group_by_name'])

    def click_reports_name(self):
        return self.get_reports_name.click()

    # Validate the Reports Page
    def _validate_page(self):
        try:
            self.driver.find_element_by_css_selector(locators_reports_page['loc_reports'])
        except:
            raise InvalidPageException("Reports page is not loading")


'''
    @property
    def get_detailed_report(self):
        return self.driver.find_element_by_xpath(locators_reports_page['loc_detailed_report'])

    def click_detailed_report(self):
        return self.get_detailed_report.click()

    @property
    def get_reports_pdf(self):
        return self.driver.find_element_by_xpath(locators_reports_page['loc_report_pdf'])

    def click_reports_pdf(self):
        return self.get_reports_pdf.click()
'''
