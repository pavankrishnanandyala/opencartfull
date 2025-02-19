import pytest

from pageObjects.Registration import Registration
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Registration:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    def test_registration(self, setup):
        self.logger.info("*************** Starting Registration Test ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.reg = Registration(self.driver)
        self.reg.clickMyAccount()
        self.reg.clickRegister()
        self.reg.setFirstname("vara")
        self.reg.setLastname("prasad")
        self.reg.InputEmail(self.username)
        self.reg.inputPhoneNo("0708888888")
        self.reg.setPassword(self.password)
        self.reg.confirmPassword(self.password)
        self.reg.clickPPcheckbox()
        self.reg.contineRegistration()
        self.reg.confirmRegistation()
        self.reg.logOut()
        self.driver.close()
        self.logger.info("*************** Registration Test Complete ***************")
        self.logger.info("*************** Test_001_Registration Successful ***************")

