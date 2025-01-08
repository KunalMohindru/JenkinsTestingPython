from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions

class GooglePageClass(BasePage):

    facebook_icon= (By.XPATH, "//img[contains(@class,'fb_logo')]")
    youtbe_icon= (By.XPATH,"//yt-icon[@id='logo-icon']")

    def __init__(self, driver):
        self.driver=driver
        super().__init__(driver)


    def isElementDisplayed(self,locatorParam):
        log=self.getLogger()
        log.info("This is logger testing and element is displayed")
        webelement= self.wait.until(expected_conditions.visibility_of_element_located(locatorParam))
        return webelement.is_displayed()
