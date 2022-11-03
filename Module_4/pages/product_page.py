from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def press_add_to_cart_button(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BUTTON)
        login_link.click()

    def should_be_add_to_card_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CARD_BUTTON), "Add to cart button is not presented"

    def check_product_name_matches_the_added_to_cart_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_to_cart_message = self.browser.find_element(*ProductPageLocators.ADDED_TO_CART_MESSAGE).text
        assert product_name.lower() == added_to_cart_message.lower(), "The wrong product was added to the cart"

    def price_matches_price_of_goods_in_cart(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        goods_in_cart = self.browser.find_element(*ProductPageLocators.PRICE_OF_GOODS_IN_CART).text
        assert product_price in goods_in_cart, "The price of the goods in cart doesn't match the price of the product"
