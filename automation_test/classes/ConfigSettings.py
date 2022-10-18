import configparser
from os.path import dirname, abspath


class EnvSettings:
    def __init__(self, browser: str):
        project_root = dirname(dirname(abspath(__file__)))
        config = configparser.ConfigParser()
        if not project_root:
            return
        try:
            config.read(f"{project_root}/configs/config.ini")
        except ValueError:
            print(f"ValueError : cannot found {project_root}/configs/config.ini")
        try:
            self.browser_path = config.get("BrowserSetting", f"{browser.lower()}Path")
            self.web_size = config.get("BrowserSetting", "webSize")
            self.mobile_size = config.get("BrowserSetting", "mobileSize")
            self.product_path = config.get("ProductSetting", "productPath")
            self.project_root = project_root
        except Exception as e:
            print(f"Read config file error :", e)
