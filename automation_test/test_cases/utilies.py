from os.path import dirname, abspath
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from automation_test.classes import ConfigSettings


def get_browser_agent(browser_name: str, config: ConfigSettings.EnvSettings, is_mobile: bool) -> webdriver:
    # set default resolution
    height, weight = 1024, 768
    if not is_mobile:
        height, weight = config.web_size.split("*")[0], config.web_size.split("*")[1]
    else:
        height, weight = config.mobile_size.split("*")[0], config.mobile_size.split("*")[1]
    if browser_name.lower() == "chrome":
        options = Options()
        options.add_argument("--disable-notifications")
        options.binary_location = config.browser_path
        browser_agent = webdriver.Chrome(
            executable_path=f'{config.project_root}/drivers/chromedriver', chrome_options=options, keep_alive=True)
        browser_agent.set_window_size(height, weight)
        return browser_agent
    elif browser_name.lower() == "firefox":
        # to do : implement firefox  setting and return firefox browser agent
        pass
    else:
        print(f"cannot found the {browser_name}")


def find_element_with_text_and_click(elements, text: str):
    for element in elements:
        if element.text == text:
            element.click()
            break


def wait_element_by_selector_and_click(driver: webdriver, element_selector: str):
    try:
        WebDriverWait(driver, 30).until(ec.element_to_be_clickable(
            (By.CSS_SELECTOR, element_selector)))
        ele = driver.find_element(By.CSS_SELECTOR, element_selector)
        ele.click()
    except Exception as e:
        print(f"Exception : {e}")
