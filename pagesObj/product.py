import time

from selenium.webdriver.common.by import By
from tests.conftest import store as store_var

class Product():
    def __init__(self, driver):
        self.driver = driver
    def goProductSimple(self):
        self.driver.get(f"{store_var}/lustro-sosnowe-rustyk-pion-poziom.html")
    def addToCart(self):
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 150)")
        self.driver.find_element(By.XPATH, "//button[@title='Do koszyka']/span").click()
        time.sleep(2)
        self.driver.get(f'{store_var}/checkout/cart/')
        self.driver.find_element(By.XPATH, "//div[@class='totals']//ul[@class='checkout-types']//li//button[@title='Przejdź do kasy']//span//span[contains(text(),'Przejdź do kasy')]").click()

    def fillOut(self):
        self.driver.find_element(By.XPATH, "//input[@id='billing:firstname']").send_keys("Test")
        self.driver.find_element(By.XPATH, "//input[@id='billing:lastname']").send_keys("Test")
        self.driver.find_element(By.XPATH, "//input[@id='billingemail']").send_keys("test@seart.pl")
        self.driver.find_element(By.XPATH, "//input[@id='billing:telephone']").send_keys("555999666")
        self.driver.find_element(By.XPATH, "//input[@id='billing:street1']").send_keys("testowa")
        self.driver.find_element(By.XPATH, "//input[@id='billing:street2']").send_keys("6a")
        self.driver.find_element(By.XPATH, "//input[@id='billingfloor']").send_keys("3")
        self.driver.find_element(By.XPATH, "//input[@id='billing:postcode']").send_keys("20-026")
        self.driver.find_element(By.XPATH, "//input[@id='billing:city']").send_keys("Chmielnik")

        time.sleep(1)
        # self.driver.find_element(By.XPATH, "//label[@for='s_method_freeshipping_freeshipping']").click()
        self.driver.find_element(By.XPATH, "//label[@for='p_method_banktransfer']").click()
        # self.driver.find_element(By.XPATH, "//label[@for='agreement-1']").click()
        # self.driver.find_element(By.XPATH, "//label[@for='agreement-3']").click()

        self.checkuoutAssertions()

    def checkuoutAssertions(self):
        assert "55 1140 2004 0000 3002 8367 4515" and "41 1140 2004 0000 3312 1919 6940" and "08 1140 2004 0000 3512 1919 6951" in self.driver.find_element(By.XPATH, "//div[@class='banktransfer-instructions-content agreement-content']").text
        print(self.driver.find_element(By.XPATH, "//div[@class='banktransfer-instructions-content agreement-content']").text)