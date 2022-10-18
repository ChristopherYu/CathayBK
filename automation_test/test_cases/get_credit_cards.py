from utilies import get_browser_agent, find_element_with_text_and_click, wait_element_by_selector_and_click
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from automation_test.classes import ConfigSettings

# initial
Settings = ConfigSettings.EnvSettings("Chrome")
chrome = get_browser_agent("Chrome", Settings, is_mobile=True)
burger_icon = "a.cubre-a-burger"

# open product home page
chrome.get(Settings.product_path)

# open burger
wait_element_by_selector_and_click(chrome, burger_icon)
WebDriverWait(chrome, 30).until(ec.visibility_of_element_located(
    (By.CSS_SELECTOR, ".cubre-o-nav")))

# get first item of all sub menu items, should be "產品介紹"
find_element_with_text_and_click(chrome.find_elements(By.CSS_SELECTOR, "div.cubre-a-menuSortBtn.-l1"), "產品介紹")

# wait until sub menu expand
WebDriverWait(chrome, 30).until(ec.visibility_of_element_located(
    (By.CSS_SELECTOR,
     "div.cubre-o-menu__item.is-L1open")))

# get all items under 產品介紹
product_intro = chrome.find_element(By.CSS_SELECTOR, "div.cubre-o-menu__item.is-L1open")
find_element_with_text_and_click(product_intro.find_elements(By.CSS_SELECTOR, "div.cubre-a-menuSortBtn"), "信用卡")
# wait until all sub items displayed under 信用卡
WebDriverWait(chrome, 30).until(ec.visibility_of_element_located(
    (By.CSS_SELECTOR, "a[href*='/cathaybk/personal'].cubre-a-menuLink.-channel.is-active")))

main_page = product_intro.find_element(By.CSS_SELECTOR, ".cubre-o-menuLinkList__content")
find_element_with_text_and_click(main_page.find_elements(By.CSS_SELECTOR, "#lnk_Link"), "卡片介紹")
# wait until all content loaded
WebDriverWait(chrome, 30).until(ec.presence_of_all_elements_located(
    (By.CSS_SELECTOR, "head.at-element-marker")))
# find all buttons of slid cards
card_bullets = chrome.find_elements(By.CSS_SELECTOR, "span.swiper-pagination-bullet")
print(f"所有卡片（包含停發卡）數量為：{len(card_bullets)}")
for index, card_bullet in enumerate(card_bullets, 1):
    action = ActionChains(chrome)
    action.move_to_element(card_bullet).click().perform()
    chrome.save_screenshot(f"{Settings.project_root}/screenshot/{index}.png")
chrome.close()
