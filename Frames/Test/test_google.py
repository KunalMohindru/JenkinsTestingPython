from Test.baseTest import BaseTest
from Pages.googlePage import GooglePageClass
from Test.baseTest import BaseTest


class Test2(BaseTest):
   
    def test_facebook_search(self):
        self.driver.get(self.config_obj.FB_URL)
        google_obj = GooglePageClass(self.driver)
        #assert google_obj.isElementDisplayed(google_obj.facebook_icon)==True
        print("cookies are :",self.driver.get_cookies())


    def test_youtube_search(self):
        self.driver.get(self.config_obj.YOUTUBE_URL)
        google_obj = GooglePageClass(self.driver)
        assert google_obj.isElementDisplayed(google_obj.youtbe_icon)==True    