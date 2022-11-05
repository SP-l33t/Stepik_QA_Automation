from .base_page import BasePage
from .locators import LoginPageLocators
from time import sleep


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_on_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.SIGNUP_INPUT_EMAIL), "Email input field is missing"
        assert self.is_element_present(*LoginPageLocators.SIGNUP_INPUT_PASSWORD), "Password input field is missing"
        assert self.is_element_present(*LoginPageLocators.SIGNUP_REPEAT_PASSWORD), "Repeat password input field is missing"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON), "Register button is missing"
        self.input_text(*LoginPageLocators.SIGNUP_INPUT_EMAIL, email)
        self.input_text(*LoginPageLocators.SIGNUP_INPUT_PASSWORD, password)
        self.input_text(*LoginPageLocators.SIGNUP_REPEAT_PASSWORD, password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON).click()
