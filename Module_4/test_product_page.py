from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from time import sleep
import pytest
import random
import string


PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def random_email(string_length=10):
    letters = string.ascii_lowercase+string.digits
    return (''.join(random.choice(letters) for i in range(string_length))) + "@fakemail.com"


def random_pass(string_length=10):
    letters = string.ascii_letters + string.digits + '!@#$%()'
    return ''.join(random.choice(letters) for i in range(string_length))


@pytest.mark.authorized
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.passwd = random_pass(random.randint(9, 15))
        self.email = random_email(random.randint(6, 15))
        self.page = LoginPage(browser, PRODUCT_LINK)
        self.page.open()
        self.page.go_to_login_page()
        self.page.register_new_user(self.email, self.passwd)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        page.should_be_no_success_message_is_no_element_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_card_button()
        page.press_add_to_cart_button()
        page.solve_quiz_and_get_code()
        page.check_product_name_matches_the_added_to_cart_product()
        page.price_matches_price_of_goods_in_cart()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                               "/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_card_button()
    page.press_add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.check_product_name_matches_the_added_to_cart_product()
    page.price_matches_price_of_goods_in_cart()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.press_add_to_cart_button()
    page.should_be_no_success_message_is_no_element_present()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.should_be_no_success_message_is_no_element_present()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.press_add_to_cart_button()
    page.should_be_no_success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_on_login_url()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_cart_button()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_be_empty_cart()
    page.should_be_no_goods_in_the_cart()
