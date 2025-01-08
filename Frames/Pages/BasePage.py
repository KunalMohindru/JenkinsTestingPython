from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import inspect
import logging

class BasePage:

    def __init__(self, driverParam):
        self.driver=driverParam
        self.wait= WebDriverWait(self.driver,20)
        

    def click_on_locator(self, locatorParam):
        self.wait.until(expected_conditions.visibility_of_element_located(locatorParam)).click()
    

    def sendKeys(self, locatorParam, value):
        self.wait.until(expected_conditions.visibility_of_element_located(locatorParam)).send_keys(value)


    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger
