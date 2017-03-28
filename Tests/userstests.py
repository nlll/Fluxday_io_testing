import unittest
from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest


class UsersTests(BaseTest):
    def test_add_user(self):
        # Test add user as admin
        log_user = LoginPage(self.driver)
        home_page = log_user.log_in_with_user('admin@fluxday.io', 'password')  # login as admin
        self.assertTrue(home_page.logged_user('Admin User'))  # assert login user is admin user
        add_user = home_page.go_to_users()
        add_user.add_new_user('Peter', 'Pete', 'pet@dssf.vf', 'dtd33', '123456789')  # create new user
        self.assertTrue(add_user.find_user('Peter'))  # verify new user exists

    def test_change_user_empl_code(self):
        # Test admin user can change user employee code
        log_user = LoginPage(self.driver)
        home_page = log_user.log_in_with_user('admin@fluxday.io', 'password')  # login as admin
        self.assertTrue(home_page.logged_user('Admin User'))  # assert login user is admin user
        change_emplcode = home_page.go_to_users()
        change_emplcode.change_user_empl_code('Peter', 'PT33')  # change user Peter empl code
        self.assertIn('successfully updated', change_emplcode.message_box.text)  # assert success

    def test_delete_user(self):
        # Test admin user can delete user
        log_user = LoginPage(self.driver)
        home_page = log_user.log_in_with_user('admin@fluxday.io', 'password')  # login as admin
        self.assertTrue(home_page.logged_user('Admin User'))  # assert login user is admin user
        del_user = home_page.go_to_users()
        del_user.del_user('Peter')  # delete user Peter
        self.assertFalse(del_user.find_user('Peter'))  # assert no user Peter

    def test_empl_cant_change(self):
        # Test employee user can`t change other users
        log_user = LoginPage(self.driver)
        home_page = log_user.log_in_with_user('emp2@fluxday.io', 'password')  # login as Employee 2
        self.assertTrue(home_page.logged_user('Employee 2'))  # assert login user is Employee 2
        empl_sett = home_page.go_to_users()
        empl_sett.click_user('Admin User')  # click on Admin user
        self.assertTrue(len(empl_sett.sett_buttons) == 0)  # assert settings button disabled
        empl_sett.click_user('Team Lead')  # click on Team lead user
        self.assertTrue(len(empl_sett.sett_buttons) == 0)  # assert settings button disabled
        empl_sett.click_user('Employee 1')  # click on Employee 1 user
        self.assertTrue(len(empl_sett.sett_buttons) == 0)  # assert settings button disabled

    def test_empl_change_nickname(self):
        # Test change employee can change own nickname
        log_user = LoginPage(self.driver)
        home_page = log_user.log_in_with_user('emp2@fluxday.io', 'password')  # login as Employee 2
        self.assertTrue(home_page.logged_user('Employee 2'))  # assert login user is Employee 2
        empl_nick = home_page.go_to_users()
        empl_nick.change_user_nickname('Employee 2', 'em2')  # change employee nickname
        self.assertIn('successfully updated', empl_nick.message_box.text)  # assert success


if __name__ == "__main__":
    unittest.main(verbosity=2)
