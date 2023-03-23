from selenium import webdriver


class Login:
    emailField_id = "Email"
    passField_id = "Password"
    checkbox_id = "RememberMe"
    button_submit_xpath = "//button[contains(text(),'Log in')]"
    link_logout_linkText = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserMail(self, userMail):
        self.driver.find_element_by_id(self.emailField_id).sendKeys(userMail)
        self.driver.find_element_by_id(self.emailField_id).sendKeys(userMail)

    def setPassword(self, userPass):
        self.driver.find_element_by_id(self.passField_id).sendKeys(userPass)


