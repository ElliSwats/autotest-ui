import pytest
import allure
from allure_commons.types import Severity
# from playwright.sync_api import expect, Page
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.routes import AppRoute
from config import settings


@pytest.mark.regression
@pytest.mark.authorization
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @pytest.mark.parametrize('email, password', [
        ('user.name@gmail.com', 'password'),
        ('user.name@gmail.com', '  '),
        ('  ', 'password')])
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title('User login with wrong email or password')
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.go_to_url(AppRoute.LOGIN)
        login_page.login_form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title('User login with correct email and password')
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(
            self, dashboard: DashboardPage, registration: RegistrationPage, login_page: LoginPage):
        registration.go_to_url(AppRoute.REGISTRATION)
        registration.registration_form.fill(
            email=settings.test_user.email, username=settings.test_user.username, password=settings.test_user.password)
        registration.click_registration_button()

        dashboard.dashboard_toolbar_view.check_visible()
        dashboard.navbar.check_visible('username')
        dashboard.sidebar.check_visible()
        dashboard.sidebar.click_logout()

        login_page.login_form.fill(email=settings.test_user.email, password=settings.test_user.password)
        login_page.click_login_button_go_to_dashboard()

        dashboard.dashboard_toolbar_view.check_visible()
        dashboard.navbar.check_visible("username")
        dashboard.sidebar.check_visible()

    @allure.tag(AllureTag.NAVIGATION)
    @allure.title('Navigation from login page to registration page')
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(self, login_page: LoginPage, registration: RegistrationPage):
        login_page.go_to_url(AppRoute.LOGIN)
        login_page.click_registration_link()
        registration.registration_form.check_visible(email="", username="", password="")


# def test_wrong_authorization(chromium_page: Page, email: str, password: str):
#     chromium_page.goto(AppRoute.LOGIN)
#
#     email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
#     email_input.fill(email)
#
#     password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
#     password_input.fill(password)
#
#     login_button = chromium_page.get_by_test_id('login-page-login-button')
#     login_button.click()
#
#     chromium_page.wait_for_timeout(2000)
#
#     wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
#     expect(wrong_email_or_password_alert).to_be_visible()
#     expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
