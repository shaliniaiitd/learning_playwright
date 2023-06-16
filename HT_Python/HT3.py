
"""Home Task – 03:
1.Create a new spec file emulation.spec.js under tests folder​.
2 and Android. And perform below scenario in device view.


7.Copy the generated code by codegen and run from the test file."""


from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=False)
    #.Use Playwright Codegen to emulate Devices iPhone 13
    context = browser.new_context(**playwright.devices["Pixel 5"],color_scheme= 'dark')
    #context = browser.new_context(**playwright.devices["iPhone 13"])

    #print(playwright.devices["iPhone 13"])
    page = context.new_page()
    # 3.Navigate to SwagLabs(saucedemo.com) and login with valid credentials.

    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    #zoom out the window
    page.set_viewport_size({"width": 1600, "height": 1200})
    #4.On home page add 3 items to the cart.
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)\"]").click()

    #click on cart
    page.locator("a").filter(has_text="3").click()

    #5.Proceed to Checkout and finish.
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("form").click()

    #fill form
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("Shalini")
    page.locator("[data-test=\"firstName\"]").press("Tab")
    page.locator("[data-test=\"lastName\"]").fill("Agarwal")
    page.locator("[data-test=\"lastName\"]").press("Tab")
    page.locator("[data-test=\"postalCode\"]").fill("534002")
    page.locator("[data-test=\"continue\"]").click()


    page.locator("[data-test=\"finish\"]").click()

    #6.Verify the successful message and Logout of the application.
    try:
        msg_element = page.get_by_role("heading", name="Thank you for your order!")
        expect(msg_element).to_be_visible()
    except :
        print("An error occurred ")


    """ page.locator("[data-test=\"back-to-products\"]").click()
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()"""

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
