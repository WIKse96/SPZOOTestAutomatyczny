from seleniumpagefactory.Pagefactory import PageFactory


class RulesPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.seart.pl/"



    # Locators
    locators = {
        'obowiazuje_od': ('xpath', "//center[contains(text(),'(obowiązuje od 01.08.2023 r.)')]"),
        'p1': ('xpath', "//li[contains(text(),'Sklep internetowy pod adresem www.seart.pl prowadz')]"),
        'p2': ('xpath', "//li[contains(text(),'żytkownikowi będącemu konsumentem w rozumieniu art')]"),
        'obowiazuje_od_uslug_elektr': ('xpath', "//center[contains(text(),'(obowiązuje od 01.08.23 r.)')]"),
        'old_rules_uslug_elektr': ('xpath', "//center[contains(text(),'(Regulaminy obwiązujące przed tą datą są dostępne ')]"),

    }


# assertios
    def rulesPage_assertions(self):
        assert self.obowiazuje_od.visibility_of_element_located()
        assert self.p1.visibility_of_element_located()
        assert self.p2.visibility_of_element_located()

    def rulesPage_electr(self):
        assert self.obowiazuje_od_uslug_elektr.visibility_of_element_located()
        assert "Sklep internetowy pod adresem www.seart.pl prowadzi Seart Group sp. z o.o. z siedzibą w Kotlicach 103, 26-020 Chmielnik, NIP: 6572978750, REGON: 52526189500000 zwana dalej Seart.pl." in self.driver.page_source
