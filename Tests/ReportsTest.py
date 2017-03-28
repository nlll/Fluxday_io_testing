from Tests.BaseTest import BaseTest

class ReportsTest(BaseTest):
    def test_worklogs(self):
    # Verifing the worklogs dropdown menu

        from Pages.LoginPage import LoginPage
        login_user = LoginPage(self.driver)
        # Navigate to Login Page

        LoginPage.log_in_with_user(login_user, username='admin@fluxday.io', password='password')
        # Login with valid credentials

        from Pages.BasePage import BasePage
        go = BasePage(self.driver)
        go.go_to_reports()
        # Navigate to Reports Page

        from Pages.ReportsPage import ReportsPage
        rep = ReportsPage(self.driver)
        rep._validate_page()
        # Verify the right page: Reports Page

        rep.click_worklogs()
        # Click the worklog dropdown menu
        rep.click_worklogs_drop()
        # Choose one worklog type from the dropdown menu

        # Verify the right result: a table is presented
        self.assertTrue("tr" in self.driver.page_source)

    def test_group_reports(self):
        from Pages.LoginPage import LoginPage
        login_user = LoginPage(self.driver)
        # Navigate to Login Page

        LoginPage.log_in_with_user(login_user, username='admin@fluxday.io', password='password')
        # Login with valid credentials

        from Pages.BasePage import BasePage
        go = BasePage(self.driver)
        go.go_to_reports()
        # Navigate to Reports Page

        from Pages.ReportsPage import ReportsPage
        rep = ReportsPage(self.driver)
        rep._validate_page()
        # Verifing the right page: Reports Page

        rep.click_reports_month()
        # Chose reports month
        rep.click_reports_year()
        # Chose reports year
        rep.click_reports_button()
        # Click submit button

        self.assertTrue("March" in self.driver.page_source)
        # Verify the right result


    def test_reports_calendar(self):
    # Verifing the reports calendar

        from Pages.LoginPage import LoginPage
        login_user = LoginPage(self.driver)
        # Navigate to Login Page

        LoginPage.log_in_with_user(login_user, username='admin@fluxday.io', password='password')
        # Login with valid credentials

        from Pages.BasePage import BasePage
        go = BasePage(self.driver)
        go.go_to_reports()
        # Navigate to Reports Page

        from Pages.ReportsPage import ReportsPage
        rep = ReportsPage(self.driver)
        rep._validate_page()
        # Verifing the right page: Reports Page

        # Chose the worklog
        rep.click_worklogs()
        # Pick one worklog from the dropdown menu
        rep.click_worklogs_drop()
        # Click the calendar to open it
        rep.click_calendar()
        # Change the month by clicking next month
        rep.click_calendar_next()

        # Verify the right result
        self.assertTrue("April" in self.driver.page_source)


    def test_group_reports_by_name(self):
    # Verify the grouping by name option from the NameField in the reports table


        from Pages.LoginPage import LoginPage
        login_user = LoginPage(self.driver)
        LoginPage.log_in_with_user(login_user, username='admin@fluxday.io', password='password')
        # Navigate to Login Page

        from Pages.BasePage import BasePage
        go = BasePage(self.driver)
        go.go_to_reports()
        # Navigate to Reports Page

        from Pages.ReportsPage import ReportsPage
        rep = ReportsPage(self.driver)
        rep._validate_page()
        # Validate Reports Page

        #Click to arrange ascending
        rep.click_type()
        #Click to arrange descending
        rep.click_type()
        #Click to arrange ascending
        rep.click_type()
        # Click to arrage ascending
        rep.click_type()
        # Assert the right type of arranging
        self.assertTrue("headerSortUp" in self.driver.page_source)


    def test_reports_type(self):
    # Verify groupig reports by type from the type dropdown menu
        from Pages.LoginPage import LoginPage
        login_user = LoginPage(self.driver)
        LoginPage.log_in_with_user(login_user, username='admin@fluxday.io', password='password')
        # Navigate to Login Page

        from Pages.BasePage import BasePage
        go = BasePage(self.driver)
        go.go_to_reports()
        # Nav to Reports Page

        from Pages.ReportsPage import ReportsPage
        rep = ReportsPage(self.driver)
        rep._validate_page()
        # Validate the right page
        rep.click_type()
        # Click to chose reports type
        rep.choose_reports_type()
        #Chose type
        self.assertTrue("report_type_select" in self.driver.page_source)
        # Verify the right result

