from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE = (By.CSS_SELECTOR, '.btn-group>a.btn')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    SIGNUP_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    SIGNUP_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    SIGNUP_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, ".alertinner>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    PRICE_OF_GOODS_IN_CART = (By.CSS_SELECTOR, ".basket-mini")


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, ".basket_summary")
