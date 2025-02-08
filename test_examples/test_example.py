import re
from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://www.baidu.com")
    yield
    
    print("after the test runs")
def test_has_title(page: Page):
    page.goto("https://www.baidu.com")

    # Expect a title "to contain" a substring.
    expect(page).to_have_url("https://www.baidu.com/")

def test_get_started_link(page: Page):
    page.goto("https://cn.bing.com/")

    # Click the get started link.
    page.get_by_label("输入搜索词").click(timeout=6000)
    page.locator("input[name='q']").fill("playwright")
    page.get_by_label("搜索").nth(0).click(timeout=6000)

    # Expects page to have a heading with the name of Installation.
    # expect(page.get_by_role("input", name="wd"))