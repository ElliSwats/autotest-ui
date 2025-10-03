from playwright.sync_api import sync_playwright, Request, Response


def log_request(request: Request):
    print(f"Request: {request.url}")


def log_response(response: Response):
    print(f"Response: {response.url}, {response.text}, {response.status}")


with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()

    page.on("request", log_request)
    page.on("response", log_response)

    page.goto(" https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    registration_link = page.get_by_test_id('login-page-registration-link')
    page.wait_for_timeout(2000)
    registration_link.hover()

    page.wait_for_timeout(4000)
