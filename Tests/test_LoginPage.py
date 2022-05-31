#from Pages.LoginPage import LoginPage
from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from Config.TestData import TestData


class Test_LoginPage(BaseTest):

    def test_verify_userid_locator(self):
        self.loginpage=LoginPage(self.driver)
        self.loginpage.Goto_Url_Link(TestData.BaseUrl)
        flag=self.loginpage.verify_UserId_locator()
        assert flag
#testgit addgit status
    def test_veify_password_locator(self):
        self.loginpage=LoginPage(self.driver)
        self.loginpage.Goto_Url_Link(TestData.BaseUrl)
        flag1 = self.loginpage.verify_Password_locator()
        assert flag1

    def test_loginpage_title(self):
        self.loginpage=LoginPage(self.driver)
        self.loginpage.Goto_Url_Link(TestData.BaseUrl)
        actual_title=self.loginpage.verify_title()
        assert actual_title== TestData.LOGINPAGE_TITLE

    def test_Login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.Goto_Url_Link(TestData.BaseUrl)
        self.loginpage.Input_UserID(TestData.UserName)
        self.loginpage.Input_Password(TestData.PassWord)
        self.loginpage.click_login_button()
        Homepage_title=self.loginpage.verify_title()
        assert Homepage_title==TestData.HOMEPAGE_TITLE


    def test_Reset(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.Goto_Url_Link(TestData.BaseUrl)
        self.loginpage.Input_UserID(TestData.UserName)
        self.loginpage.Input_Password(TestData.PassWord)
        self.loginpage.click_reset_button()

