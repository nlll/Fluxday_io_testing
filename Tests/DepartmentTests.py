import unittest
from time import strftime, gmtime

from selenium.webdriver.common.alert import Alert

from Tests.BaseTest import BaseTest
from Pages.DepartmentsPage import DepartmentsPage
from Util.AjaxHelper import AjaxHelper


class DepartmentTest(BaseTest):
    def testCreateDepartment(self):
        # login with admin
        depart = DepartmentsPage(self.driver)
        depart.login_with_admin()

        # click Departments link
        depart.click_departments_link()

        # create department
        create_depart = DepartmentsPage(self.driver)
        create_depart.click_depart_link()

        # fill department title
        depart_title = DepartmentsPage(self.driver)
        depart_title.fill_create_depart_title('Awesome department')

        # fill department code
        depart_code = DepartmentsPage(self.driver)
        depart_code_generator = 'Awesome_code_' + strftime('%Y%m%d%H%M%S', gmtime())
        depart_code.fill_create_depart_code(depart_code_generator)

        # click save button
        depart.click_save_btn()

        # assert department is created
        depart.refresh()
        self.assertTrue('Awesome department' in self.driver.page_source)

    def testEditDepartmentTitle(self):
        # login with admin
        depart = DepartmentsPage(self.driver)
        depart.login_with_admin()

        # click Departments link
        depart.click_departments_link()

        # click Departments settings icon
        depart.click_settings_icon()

        # click Edit Department
        depart.click_edit_link()

        # fill department title
        edit_depart_title = DepartmentsPage(self.driver)
        edit_depart_title.fill_create_depart_title('Awesome department_new')

        # click save button
        depart.click_save_btn()

        # assert department title is edited
        depart.refresh()
        self.assertTrue('Awesome department_new' in self.driver.page_source)

    def testEditDepartmentDescription(self):
        # login with admin
        depart = DepartmentsPage(self.driver)
        depart.login_with_admin()

        # click Departments link
        depart.click_departments_link()

        # click Departments settings icon
        depart.click_settings_icon()

        # click Edit Department
        depart.click_edit_link()

        # fill department description
        edit_description = DepartmentsPage(self.driver)
        edit_description.fill_depart_description('Awesome description')

        # click save button
        depart.click_save_btn()

        # assert department description is edited
        depart.refresh()
        self.assertTrue('Awesome description' in self.driver.page_source)

    def testEditDepartmentUrl(self):
        # login with admin
        depart = DepartmentsPage(self.driver)
        depart.login_with_admin()

        # click Departments link
        depart.click_departments_link()

        # click Departments settings icon
        depart.click_settings_icon()

        # click Edit Department
        depart.click_edit_link()

        # fill department url
        edit_url = DepartmentsPage(self.driver)
        edit_url.fill_depart_url('Awesome url')

        # click save button
        depart.click_save_btn()

        # assert department url is edited
        depart.refresh()
        self.assertTrue('Awesome url' in self.driver.page_source)

    def testDeleteDepartment(self):
        # login with admin
        depart = DepartmentsPage(self.driver)
        depart.login_with_admin()

        # click Departments link
        depart.click_departments_link()

        # click Departments settings icon
        depart.click_settings_icon()

        # click Delete department
        depart.click_depart_delete()
        AjaxHelper.suspend(2)
        Alert(self.driver).accept()

        # assert department is deleted
        depart.refresh()
        self.assertFalse('Awesome department' in self.driver.page_source)


if __name__ == '__main__':
    unittest.main(verbosity=2)
