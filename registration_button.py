from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    login_button = page.get_by_test_id('registration-page-registration-button')
    expect(login_button).to_be_disabled()

    email_login = page.get_by_test_id('registration-form-email-input').locator('input')
    email_login.fill('user.name@gmail.com')

    username_login = page.get_by_test_id('registration-form-username-input').locator('input')
    username_login.fill('username')

    password_login = page.get_by_test_id('registration-form-password-input').locator('input')
    password_login.fill('password')

    page.wait_for_timeout(4000)

    expect(login_button).to_be_enabled()
