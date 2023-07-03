import pytest

from utilities.BaseClass import BaseClass
from pagesObj.HomePage import HomePage
from actions.HomePageActions import HomePageActions
from pagesObj.Rules import RulesPage


@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def goHome(self):
        self.driver.get("https://www.seart.pl/")

    def goSales(self):
        self.driver.get("https://www.seart.pl/wyprzedaz-c-462.html")

    def goSaleProd(self):
       self.driver.get("https://www.seart.pl/drewniana-szafka-rtv-country-limited-17.html")

    def test_HomePage_and_rules(self, setup):
        # ODKOMENTOWAĆ DO TESTÓW
        rules_page = RulesPage(self.driver)
        homePage = HomePage(self.driver)
        home_page_actions = HomePageActions(self.driver)
        homePage.homePage_assertions()

        home_page_actions.loginBtnClick()
        home_page_actions.searchTest()
        home_page_actions.menu_homepge()
        home_page_actions.rules_click()
        rules_page.rulesPage_assertions()
        home_page_actions.rules_services_click()

        pass


