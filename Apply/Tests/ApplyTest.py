from Apply.Pages.Apply import Apply
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
from pathlib import Path
import os
from selenium.webdriver.common.action_chains import ActionChains


class ApplyTests(unittest.TestCase):

    def setUp(self) -> None:
        self.options = Options()
        self.options.add_argument("--window-size=1366,768")
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.service = Service(
            executable_path='/var/lib/jenkins/.wdm/drivers/chromedriver/linux64/112.0.5615/chromedriver')
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        root_path = Path(__file__).parent.parent.parent
        config_file_path = os.path.join(root_path, 'Config.json')
        with open(config_file_path, 'r') as config_file:
            self.config = json.load(config_file)

    def test_group_filter_home_page(self):
        self.driver.get(self.config["Links"]["base_url"])
        apply = Apply(driver=self.driver)
        apply.login_button()
        apply.enter_username(self.config["User"]["username"])
        apply.next_step()
        apply.enter_password(self.config["User"]["password"])
        apply.submit()
        sleep(3)
        apply.user_profile()
        apply.mainpage_button_xpath()
        apply.job_group_filter()
        apply.filter_selection()
        apply.search_in_jobs()
        apply.post_job_selection()
        apply.apply_for_job()
        apply.check_apply_for_job()
        apply.close_check_apply_modal()

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
