import configparser
from os.path import dirname, abspath


class EnvSettings:
    def __init__(self, browser: str):
        project_root = dirname(dirname(abspath(__file__)))
        config = configparser.ConfigParser()
        config.read(f"{project_root}/configs/config.ini")
        self.browser_path = config.get("BrowserSetting", f"{browser}Path")
        self.product_path = config.get("ProductSetting", "productPath")
        self.project_root = project_root
