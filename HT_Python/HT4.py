#Home Task – 04:
#Demo site: https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login

from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

# Add mode Parallel to the suite and Enable Video recording.
# Scenario 1: Perform withdraw with zero Balance.
# 1.Navigate to the above demo Banking site and click on Customer Login.
# 2.From Your Name dropdown select any user (eg: Hermoine) and Click Login.
# 3.Click on Transaction and click reset button if any existing transaction is available.
# 4.Navigate to the Withdraw page and enter amount to be Withdrawn and click Withdraw button.
# 5.Verify Message display “Transaction Failed. You cannot withdraw amount more than the balance”.
# 6.Enable Video Recording and take screenshot for the failed withdraw message.

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir="videos/",
    record_video_size={"width": 640, "height": 480})

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    page.get_by_role("button", name="Customer Login").click()
    page.locator("#userSelect").select_option("1")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Transactions").click()
    page.get_by_role("button", name="Reset").click()
    page.get_by_role("button", name="Back").click()
    page.get_by_role("button", name="Withdrawl").click()
    page.get_by_placeholder("amount").click()
    page.get_by_placeholder("amount").click()
    page.get_by_placeholder("amount").fill("100")
    page.get_by_role("button", name="Withdraw", exact=True).click()


    try:
        msg_element = page.get_by_text("Transaction Failed. You can not withdraw amount more than the balance.")
        expect(msg_element).to_be_visible()
        page.screenshot(path='screenshot_fail.png')
    except :

        print("An error occurred ")

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="traced.zip")
    # ---------------------
    page.close()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)




# Scenario 2: Add deposit to the account.
# 1.Navigate to the above demo Banking site and click on Customer Login.
# 2.From Your Name dropdown select any user (eg: Harry) and Click Login.
# Note: select another user as it should not depend on above scenario.
# 3.Click on Deposit and Enter Amount to be Deposited and click Deposit.
# 4.Verify Amount added in the Balance section.