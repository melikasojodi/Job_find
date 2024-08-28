from Apply.Pages.Apply import Apply
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
from pathlib import Path
import os
from test_utils import wait_until_element_is_enabled


class ApplyTests(unittest.TestCase):

    def setUp(self) -> None:
        self.options = Options()
        self.options.add_argument("--window-size=1366,768")
        # self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.service = Service(
            executable_path='c:\chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        root_path = Path(__file__).parent.parent.parent
        config_file_path = os.path.join(root_path, 'Config.json')
        with open(config_file_path, 'r') as config_file:
            self.config = json.load(config_file)

    def test_apply(self):
        self.driver.get(self.config["Links"]["base_url"])
        apply = Apply(driver=self.driver)
        apply.login_button()
        apply.enter_username(self.config["User"]["username"])
        apply.next_step()
        apply.enter_password(self.config["User"]["password"])
        apply.submit()
        sleep(3)
        apply.search_job()
        apply.search_btn()
        sleep(3)
        apply.group_job_filter()
        apply.group_job_option()
        apply.sanat_filter()
        apply.sanat_option()
        apply.show_result()
        apply.city_filter()
        apply.city_option()
        apply.option_tree()
        apply.level_filter()
        apply.level_option()
        apply.new_jobs()
        for i in range(2, 29):
            try:
                wait_until_element_is_enabled(self.driver, 'xpath', f"(//div[contains(@class,'mr-3 d-flex')])[{i}]")
                sleep(2)
                apply.send_resume()
                apply.close_check_apply_modal()
                sleep(2)
            except:
                pass

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
