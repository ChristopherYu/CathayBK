from datetime import datetime
from utilies import get_browser_agent
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from automation_test.classes import ConfigSettings

# get config setting
Settings = ConfigSettings.EnvSettings("Chrome")
# set screenshot file name
today = datetime.now()

# open product home page
chrome = get_browser_agent("Chrome", Settings, is_mobile=True)
chrome.get(Settings.product_path)

# wait any main function appears
WebDriverWait(chrome, 30).until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                  '.cubre-o-quickLink > div.cubre-o-quickLink__item > a')))

# wait until all functions appeared
while len(links := chrome.find_elements(By.CSS_SELECTOR, ".cubre-o-quickLink > div.cubre-o-quickLink__item > a")) < 6:
    chrome.implicitly_wait(1)

# gen screenshot
chrome.save_screenshot(f"{Settings.project_root}/screenshot/{today.strftime('%Y-%m-%d_%H:%M:%S')}.png")
chrome.close()
