import time

from selenium.webdriver.common.by import By
from tests.conftest import store as store_var

class Assertions():
        def __init__(self, driver):
                self.driver = driver
        def test_homePage(self):
                assert self.driver.find_element(By.XPATH, "//div[@class='col-sm-3 text-left']")
                assert self.driver.find_element(By.XPATH, "//div[@class='infolinia visible-sm visible-md visible-lg a-right']//a[contains(text(),'601 316 615')]")
                assert self.driver.find_element(By.XPATH, "//img[@alt='Drewniane meble sosnowe, bukowe i dębowe - Seart.pl - producent mebli drewnianych']")
        def test_rules(self):
                assert "(obowiązuje od 01.08.2023 r.)" in self.driver.page_source
                assert "Seart Group sp. z o.o. z siedzibą w Kotlicach 103, 26-020 Chmielnik, NIP: 6572978750, REGON: 52526189500000 zwana dalej:" in self.driver.page_source
        def test_contact(self):
                assert "SEART GROUP Sp. z o.o. z siedzibą w Kotlicach 103, 26-020 Chmielnik, NIP: 6572978750, REGON: 52526189500000." in self.driver.page_source

        def test_policy(self):
                assert "(obowiązująca od 01.08.23 r.)" in self.driver.page_source
                assert '<div class="std"><h2 style="text-align: center;">POLITYKA PRYWATNOŚCI</h2>' in self.driver.page_source
                assert '<a href="https://www.seart.pl/polityka-prywatnosci-do-dn-31-07-23">tutaj</a></center>' in self.driver.page_source
                assert ">Podmiotem odpowiedzialnym za przetwarzanie Twoich danych osobowych jest Seart Group sp. z o.o. w Kotlicach NIP: 6572978750" in self.driver.page_source
                assert "Politykę prywatności obowiązującą do dnia 31.07.23 r. zmieniamy w związku z zawarciem przez Seart Group sp. z o.o. w Kotlicach z Anną Sekuła PHUP" in self.driver.page_source
        def test_history(self):
                assert 'Obecnie funkcjonujemy pod nazwą Seart Group sp. z o.o. ' in self.driver.page_source
                assert 'Na terenie naszej firmy powstało studio fotograficzne o pow. 300 m2,' in self.driver.page_source
                assert 'Klientom wyjątkowość oferowanych mebli, charakterystykę drewna, jego usłojenie czy strukturę powierzchni.' in self.driver.page_source

        def test_BankTransfers(self):
                assert '55 1140 2004 0000 3002 8367 4515' in self.driver.page_source
                assert '41 1140 2004 0000 3312 1919 6940' in self.driver.page_source
                assert 'Nr. konta - MBANK- ' in self.driver.page_source
                assert 'Nr. konta dla płatności w euro' in self.driver.page_source
                assert 'Seart Group Spółka z Ograniczoną Odpowiedzialnością' in self.driver.page_source

        def test_paymentMethod(self):
                assert '55 1140 2004 0000 3002 8367 4515' in self.driver.page_source
                assert 'SEART GROUP SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ' in self.driver.page_source
                assert 'przelewy elektroniczne – obsługa – Pay U.' in self.driver.page_source
                assert ' NIP: 779-23-08-495, REGON 300523444.' in self.driver.page_source

        def test_rulesElSer(self):
                assert '01.08.23' in self.driver.page_source
                assert 'Seart Group' in self.driver.page_source
                assert 'NIP: 6572978750' in self.driver.page_source
                assert 'tutaj' in self.driver.page_source
                assert self.driver.find_element(By.XPATH, "//li[contains(text(),'Osoba trzecia, która uzyskała wiadomość o naruszen')]")


