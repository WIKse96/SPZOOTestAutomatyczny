from selenium.webdriver.common.by import By
from tests.conftest import store as store_var

class Functions():
    def __init__(self, driver):
        self.driver = driver

    def goHome(self):
        self.driver.get(f"{store_var}")
    def goRules(self):
        self.driver.get(f"{store_var}/regulamin-i-11.html")
    def goPolicy(self):
        self.driver.get(f"{store_var}/polityka-prywatnosci-i-20.html")

    def goRulesElSer(self):
        self.driver.get(f"{store_var}/polityka-prywatnosci-i-20.html")
    def gocontanct(self):
        self.driver.get(f"{store_var}/contacts")

    def goHistory(self):
        self.driver.get(f"{store_var}/historia-firma-seart-97.html")

    def goRulesOpinion(self):
        self.driver.get(f"{store_var}/regulaminy-opinii")
    def goPayMethod(self):
        self.driver.get(f"{store_var}/formy-platnosci.html")
    def goBankTransfers(self):
        self.driver.get(f"{store_var}/konta-bankowe.html")
    def goProductSimple(self):
        self.driver.get(f"{store_var}/lustro-sosnowe-rustyk-pion-poziom.html")