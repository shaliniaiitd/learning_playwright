#Home Task – 02:
#1.Create a new spec file contact.spec.js under tests folder.

#6.Practice with other types of selectors, Actions and Assertions.


import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #2.Write test script to navigate to https://ultimateqa.com.
    page.goto("https://ultimateqa.com/")
    #Hover on About dropdown
    page.get_by_role("link", name="About 3").hover()
    #click on Contact Us
    page.get_by_role("link", name="Contact Us").click()

    #On contact page fill the required fields
    page.locator("#et_pb_contact_first_0").click()
    page.locator("#et_pb_contact_first_0").fill("shalini")


    page.locator("#et_pb_contact_first_0").press("Tab")
    page.get_by_placeholder("Last Name").fill("Agarwal")

    page.get_by_placeholder("Last Name").press("Tab")
    page.locator("#et_pb_contact_email_0").fill("shalinia.iitd@gmail.com")

    page.locator("#et_pb_contact_email_0").press("Tab")
    page.get_by_placeholder("Message").fill("Sent through Playwright")

    page.get_by_placeholder("Message").press("Tab")
    #Close the pop-up
    page.get_by_role("button", name="Close").click()
    #click on Send Message
    page.get_by_role("button", name="5 Send Message 9").click()

    #Verify Thank you for contacting us text displayed
    expect(page.get_by_text("Thanks for contacting us")).to_be_visible()
    time.sleep(3)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)