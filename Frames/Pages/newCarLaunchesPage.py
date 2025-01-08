from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions


class newCarLaunchesPage(BasePage):

    #locators
    all_car_titles= (By.XPATH,"//h3")    

    def __init__(self, driver):
        self.driver=driver
        super().__init__(driver)
        
    def get_all_car_titles(self):
       all_cars=self.wait.until(expected_conditions.visibility_of_any_elements_located(self.all_car_titles))
       carlist=[]
       for i in all_cars:
           carlist.append(i.text)
       return carlist
