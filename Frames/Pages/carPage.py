from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.newCarLaunchesPage import newCarLaunchesPage
import time
from selenium.webdriver.support import expected_conditions



class carPage(BasePage):

    #locators (defined using different ways)
    #new_cars_btn= "//*[contains(text(),'NEW CARS')]"
    new_cars_btn= (By.XPATH,"//*[contains(text(),'NEW CARS')]")
    new_launches_option= (By.XPATH,"//a[@href='/new-car-launches/']")
    search_inputbox= (By.XPATH, "//div[contains(@class,'home-page__home-banner-container o-bfyaNx')]//div[@trendingsearcheslabel='Trending Searches']//input[@type='text']")
    search_dropdown=(By.XPATH,"//div[contains(text(),'Trending Searches')]//parent::li")  
    search_btn = (By.XPATH,"//button[contains(text(),'Search')]")
    dropdown_value= (By.XPATH,"//li[contains(@data-label,'Camry')]")
    car_heading = (By.XPATH,"//h1")

    def __init__(self, driver):
        self.driver=driver
        super().__init__(driver)
        
    def navigate_new_launches(self):
       self.click_on_locator(self.new_cars_btn)
       self.click_on_locator(self.new_launches_option)
       return newCarLaunchesPage(self.driver)
    
    def search_car(self, valueParam):
        self.click_on_locator(self.search_inputbox)
        self.sendKeys(self.search_inputbox, valueParam)
        self.wait.until(expected_conditions.visibility_of_element_located(self.dropdown_value))
        self.click_on_locator(self.dropdown_value)

    def get_heading(self):    
        return self.wait.until(expected_conditions.visibility_of_element_located(self.car_heading)).text