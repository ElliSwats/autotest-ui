from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_login = page.get_by_test_id('registration-form-email-input').locator('input')
    email_login.fill('user.name@gmail.com')

    username_login = page.get_by_test_id('registration-form-username-input').locator('input')
    username_login.fill('username')

    password_login = page.get_by_test_id('registration-form-password-input').locator('input')
    password_login.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses', timeout=2000)

    curses_button = page.get_by_test_id('courses-drawer-list-item-title-text')
    curses_button.click(timeout=4000)

    curses_header = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(curses_header).not_to_be_disabled()
    expect(curses_header).to_have_text('Courses', timeout=2000)

    empty_folder = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_folder).not_to_be_disabled()
    expect(empty_folder).to_be_visible()

    no_results = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results).not_to_be_disabled()
    expect(no_results).to_have_text('There is no results', timeout=2000)

    description_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_text).not_to_be_disabled()
    expect(description_text).to_have_text('Results from the load test pipeline will be displayed here', timeout=2000)

