from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from time import sleep


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_cart_button()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_be_empty_cart()
    page.should_be_no_goods_in_the_cart()

