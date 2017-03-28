import unittest
from selenium.webdriver.common.keys import Keys
from Tests.BaseTest import BaseTest


class SeacrhFieldTest(BaseTest):
    def test_worklogs(self):
        #Verify Search Field

        from Pages.LoginPage import LoginPage
        login_user = LoginPage(self.driver)
        home_page = login_user.log_in_with_user('admin@fluxday.io', 'password')
        #home_page._validate_page()

        from Pages.HomePage import HomePage
        #home = HomePage(self.driver)
        #home._validate_page()

        search = HomePage(self.driver)
        #Click search field and write keyword
        search.click_search_field()
        #Verify the results for the searched keyword are shown
        self.assertTrue("Reports" in self.driver.page_source)

if __name__ == "__main__":
    unittest.main(verbosity=2)