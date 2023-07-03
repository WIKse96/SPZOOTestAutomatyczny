import time
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By

from pagesObj.HomePage import HomePage

class HomePageActions(HomePage):

    def __init__(self, driver):
        self.searchIcon = None
        self.driver = driver
        #wyszukiwany tekst w funcji searchDeskopt(), key - pierwsze szukanie, value - tekst do szukania
        self.searchTextsDic = {1:'komoda'}

    # button click

    def loginBtnClick(self):
        self.loginBtn.click_button()
        assert "możliwość przechowywania wielu adresów dostawy" in self.driver.page_source


    def searchTest(self):
        pass

    def menu_homepge(self):
        action = AC(self.driver)
        action.move_to_element(self.menu_meble)
        action.perform()
        action.click(self.toaletki_menu)
        action.perform()

        pass
    def searchDesktop(self):
        self.search_bar.click_button()
        self.search_bar.set_text(self.searchTextsDic[1])
        self.search_btn.click_button()
        highlighted_links = self.driver.find_elements(By.XPATH, "//span[@class='searchindex-highlight']")
        for idx, highlighted_link in enumerate(highlighted_links):
            assert self.searchTextsDic[1] == highlighted_link.text.lower()
            break
    def rules_click(self):
        self.rules.click()
    def rules_gifts_click(self):
        self.rules_gifts.click()

    def rules_services_click(self):
        self.rules_services.click()

    def rules_opinion_click(self):
        self.rules_opinion.click()

    def policy_privacy_click(self):
        self.policy_privacy.click()