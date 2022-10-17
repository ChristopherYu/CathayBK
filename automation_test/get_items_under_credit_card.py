from utilies import get_browser_agent, find_element_with_text_and_click
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from classes import ConfigSettings

# initial
Settings = ConfigSettings.EnvSettings("Chrome")
chrome = get_browser_agent("Chrome", Settings, is_mobile=True)
burger_icon = "a.cubre-a-burger"

# open product home page
chrome.get(Settings.product_path)

# wait burger icon display
WebDriverWait(chrome, 30).until(ec.visibility_of_element_located(
    (By.CSS_SELECTOR, burger_icon)))

# open burger
chrome.find_element(By.CSS_SELECTOR, burger_icon).click()

# wait until side menu display
WebDriverWait(chrome, 30).until(ec.visibility_of_element_located(
    (By.CSS_SELECTOR, ".cubre-o-nav")))
# get item at side menu
main_menu = chrome.find_elements(By.CSS_SELECTOR, "div.cubre-a-menuSortBtn.-l1")
find_element_with_text_and_click(main_menu, "產品介紹")

# wait until sub menu expand
WebDriverWait(chrome, 30).until(ec.visibility_of_element_located(
    (By.CSS_SELECTOR,
     "div[style='display: block;")))
# get first item of all sub menu items, should be "產品介紹"
product_intro = chrome.find_element(By.CSS_SELECTOR, "div.cubre-o-menu__item.is-L1open")

# get sub items of “產品介紹”
sub_menu = product_intro.find_elements(By.CSS_SELECTOR, "div.cubre-a-menuSortBtn")
find_element_with_text_and_click(sub_menu, "信用卡")

# wait until sub items expand
WebDriverWait(chrome, 30).until(ec.visibility_of_element_located(
    (By.CSS_SELECTOR, "div.cubre-o-menuLinkList__item.is-L2open")))
main_page = product_intro.find_element(By.CSS_SELECTOR, ".cubre-o-menuLinkList__content")
items = main_page.find_elements(By.CSS_SELECTOR, "#lnk_Link")
chrome.save_screenshot(f"{Settings.project_root}/screenshot/信用卡子選單.png")
print(f"信用卡的子選單有：{len(items)}")
chrome.close()
