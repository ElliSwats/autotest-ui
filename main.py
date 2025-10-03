from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_disabled()

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    for character in 'user@gmail.com':
        page.keyboard.press(character, delay=300)

    page.keyboard.press("ControlOrMeta+A")

    page.wait_for_timeout(2000)

    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill("password")

    login_button = page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
