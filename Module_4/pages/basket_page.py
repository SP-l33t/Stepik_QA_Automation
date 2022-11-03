from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_no_goods_in_the_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), \
            'There are goods in the basket'

    def should_be_empty_cart(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Missing empty basket text"
