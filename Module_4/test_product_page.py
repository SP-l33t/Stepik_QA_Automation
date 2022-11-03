from .pages.product_page import ProductPage
from time import sleep

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_card_button()
    page.press_add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.check_product_name_matches_the_added_to_cart_product()
    page.price_matches_price_of_goods_in_cart()
