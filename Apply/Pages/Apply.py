from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Apply.Locators import *
from time import sleep
from selenium.webdriver.support.ui import Select


from test_utils import wait_until_element_is_enabled


class Apply:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def login_button(self):
        wait_until_element_is_enabled(self.driver, 'xpath', login_button)

    def enter_username(self, username):
        element = wait_until_element_is_enabled(self.driver, 'name', username_textbox)
        element.send_keys(username)

    def next_step(self):
        wait_until_element_is_enabled(self.driver, 'xpath', next_step)

    def enter_password(self, password):
        element = wait_until_element_is_enabled(self.driver, 'name', password_textbox)
        element.send_keys(password)

    def submit(self):
        wait_until_element_is_enabled(self.driver, 'xpath', submit)

    def search_job(self):
        element = wait_until_element_is_enabled(self.driver, 'xpath', search_job)
        element.send_keys("front end vue")

    def search_btn(self):
        wait_until_element_is_enabled(self.driver, 'xpath', search_btn)

    def city_filter(self):
        wait_until_element_is_enabled(self.driver, 'xpath', city_filter)

    def city_option(self):
        wait_until_element_is_enabled(self.driver, 'xpath', city_option)

    def option_tree(self):
        wait_until_element_is_enabled(self.driver, 'xpath', option_tree)

    def level_filter(self):
        wait_until_element_is_enabled(self.driver, 'xpath', level_filter)

    def level_option(self):
        wait_until_element_is_enabled(self.driver, 'xpath', level_option)

    def send_resume(self):
        try:
            wait_until_element_is_enabled(self.driver, 'xpath', send_resume)
        except:
            pass

    def close_check_apply_modal(self):
        try:
            wait_until_element_is_enabled(self.driver, 'xpath', close_check_apply_modal)
        except:
            pass

    def group_job_filter(self):
        wait_until_element_is_enabled(self.driver, 'xpath', group_job_filter)

    def group_job_option(self):
        wait_until_element_is_enabled(self.driver, 'xpath', group_job_option)

    def sanat_filter(self):
        wait_until_element_is_enabled(self.driver, 'xpath', sanat_filter)

    def sanat_option(self):
        wait_until_element_is_enabled(self.driver, 'xpath', sanat_option)

    def show_result(self):
        wait_until_element_is_enabled(self.driver, 'xpath', show_result)

    def new_jobs(self):
        new_jobs_element = wait_until_element_is_enabled(self.driver, 'tag name', new_jobs);
        select_element = Select(new_jobs_element)
        select_element.select_by_visible_text("جدیدترین‌ها")
