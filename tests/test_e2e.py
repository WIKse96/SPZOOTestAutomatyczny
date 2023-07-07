import pytest
from actions.assertions import Assertions

from utilities.BaseClass import BaseClass
from pagesObj.functions import Functions
from pagesObj.product import Product


@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_one(self):
        func = Functions(self.driver)
        ass = Assertions(self.driver)
        # func.goHome()
        # ass.test_homePage()
        # func.goRules()
        # ass.test_rules()
        # func.gocontanct()
        # ass.test_contact()
        # func.goPolicy()
        # ass.test_policy()
        # func.goHistory()
        # ass.test_history()
        # func.goBankTransfers()
        # ass.test_BankTransfers()
        # func.goPayMethod()
        # ass.test_paymentMethod()
        # func.goRulesElSer()
        # ass.test_rulesElSer()
        # func.goRulesOpinion()
        # ass.test_rulesOpinion()

    def test_product(self):
        self.driver.delete_all_cookies()
        prod = Product(self.driver)
        prod.goProductSimple()
        prod.addToCart()
        prod.fillOut()






