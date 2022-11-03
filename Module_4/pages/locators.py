from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, ".alertinner>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    PRICE_OF_GOODS_IN_CART = (By.CSS_SELECTOR, ".basket-mini")
