"""
Home Task – 02:
1.Create a new spec file contact.spec.js under tests folder​.
2.Write test script to navigate to https://ultimateqa.com/ ​.
3.Hover on About dropdown and click on Contact Us​.
4.On contact page fill the required fields and click on Send Message.​
5.Verify Thank you for contacting us text displayed​.
6.Practice with other types of selectors, Actions and Assertions.

"""
from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.goto("https://ultimateqa.com/")
    page.get_by_role("link", name="About 3").click()
    page.locator("#menu-home-page-menu").get_by_role("link", name="Contact Us").click()
    page.locator("#et_pb_contact_first_0").click()
    page.locator("#et_pb_contact_first_0").fill("Shalini ")
    page.locator("#et_pb_contact_first_0").press("Tab")
    page.get_by_placeholder("Last Name").fill("Agarwal")
    page.get_by_placeholder("Last Name").press("Tab")
    page.locator("#et_pb_contact_email_0").click()
    page.locator("#et_pb_contact_email_0").fill("c@d.com")
    page.locator("#et_pb_contact_email_0").press("Tab")
    page.get_by_placeholder("Message").click()
    page.get_by_placeholder("Message").fill("Sending through Playwright")
    page.get_by_role("button", name="5 Send Message 9").click()

    expect(page.get_by_text("Thanks for contacting us")).to_be_visible()

    # page.locator("#et_pb_contact_email_0").click(button="right")
    # page.get_by_text("The Importance of Creating Good Assertions for Testing The Importance of Creatin").click(button="right")
    # page.get_by_role("link", name="The Importance of Creating Good Assertions for Testing").first.click(button="right")
    # page2 = context.new_page()
    # page2.goto("https://ultimateqa.com/good-assertions-for-testing/")
    # locator = page2.locator(".entry-title")
    # expect(locator).to_be_visible()
    #expect(page2.get_by_role('heading', name='The Importance of Creating Good Assertions for Testing')).to_be_visible()

    # ---------------------
    context.close()
    browser.close()
    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")

with sync_playwright() as playwright:
    run(playwright)