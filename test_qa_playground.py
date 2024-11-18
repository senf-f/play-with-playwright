from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://qaplayground.dev/apps/dynamic-table/")
    elements = page.query_selector_all("#tbody tr")
    result = None
    for element in elements:
        if "Spider-Man" in element.inner_text():
            real_name = element.query_selector("td:nth-child(3)")
            result = real_name.inner_text()

    assert result == "Peter Parker"
