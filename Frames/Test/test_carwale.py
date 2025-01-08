from Pages.carPage import carPage
from Test.baseTest import BaseTest
from Utility.Generic_Methods import Generic_Methods


class Test1(BaseTest):
    def test_loginpage(self):
        carPageObj= carPage(self.driver)
        self.driver.get("https://www.carwale.com/")
        newCarLaunchObj=carPageObj.navigate_new_launches()
        car_list=newCarLaunchObj.get_all_car_titles()
        assert Generic_Methods.list_contains_value(['Honda Amaze'],car_list)==True, "Verify that car is present on the list displayed"

    def test_searchcar(self):
        carPageObj= carPage(self.driver)
        self.driver.get("https://www.carwale.com/")
        carPageObj.search_car("camry")
        heading= carPageObj.get_heading()
        assert heading.__contains__("Camry")

'''
    def test_google(self):
        self.driver.get("https://www.google.co.in/")
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//textarea[@title='Search']").send_keys("facebook")
        time.sleep(10)
        while True:
            pass
'''            