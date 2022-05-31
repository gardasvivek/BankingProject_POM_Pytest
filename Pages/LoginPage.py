from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    USERID=(By.XPATH,"//input[@name='uid']")
    PASSWORD=(By.XPATH,"//input[@name='password']")
    LOGIN=(By.XPATH,"//input[@name='btnLogin']")
    RESET=(By.XPATH,"//input[@name='btnReset']")

    def __init__(self,driver):
        super().__init__(driver)

    def verify_UserId_locator(self):
        return self.is_visible(self.USERID)

    def verify_Password_locator(self):
        return self.is_visible(self.PASSWORD)

    def verify_title(self):
        return self.get_title()

    def Input_UserID(self,userid):
        self.do_sendKeys(self.USERID,userid)

    def Input_Password(self,password):
        self.do_sendKeys(self.PASSWORD,password)

    def click_login_button(self):
        self.do_click(self.LOGIN)

    def click_reset_button(self):
        self.do_click(self.RESET)

    def Goto_Url_Link(self,URL):
        self.goto_url(URL)

