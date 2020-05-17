import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.google.com")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnK").click()
    WebDriverWait(driver, 10).until(ec.title_is("webdriver - Google Search"))
