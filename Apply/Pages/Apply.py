from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Apply.Locators import *
from time import sleep
import re

from test_utils import wait_until_element_is_enabled


class Apply:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def login_button(self):
        wait_until_element_is_enabled(self.driver, 'xpath', login_button)

    def enter_username(self, username):
        wait_until_element_is_enabled(self.driver, 'name', username_textbox)
        self.driver.find_element('name', username_textbox).send_keys(username)

    def next_step(self):
        wait_until_element_is_enabled(self.driver, 'xpath', next_step)

    def enter_password(self, password):
        wait_until_element_is_enabled(self.driver, 'name', password_textbox)
        self.driver.find_element('name', password_textbox).send_keys(password)

    def submit(self):
        wait_until_element_is_enabled(self.driver, 'xpath', submit)

    def user_profile(self):
        wait_until_element_is_enabled(self.driver, 'xpath', user_profile)

    def mainpage_button_xpath(self):
        wait_until_element_is_enabled(self.driver, 'xpath', mainpage_button_xpath)

    def job_group_filter(self):
        wait_until_element_is_enabled(self.driver, 'xpath', job_group_filter)

    def filter_selection(self):
        wait_until_element_is_enabled(self.driver, 'xpath', filter_selection)

    def search_in_jobs(self):
        wait_until_element_is_enabled(self.driver, 'xpath', search_in_jobs)

    def post_job_selection(self):
        wait_until_element_is_enabled(self.driver, 'xpath', post_job_selection)

    def apply_for_job(self):
        wait_until_element_is_enabled(self.driver, 'xpath', apply_for_job)

    def check_apply_for_job(self):
        wait_until_element_is_enabled(self.driver, 'xpath', check_apply_for_job)

    def check_apply_for_suggested_jobs(self):
        wait_until_element_is_enabled(self.driver, 'xpath', check_apply_for_suggested_jobs)

    def close_check_apply_modal(self):
        wait_until_element_is_enabled(self.driver, 'xpath', close_check_apply_modal)

    def logout(self):
        wait_until_element_is_enabled(self.driver, 'xpath', logout)

    def jobs_page(self):
        wait_until_element_is_enabled(self.driver, 'xpath', jobs_page)

    def search_job(self):
        wait_until_element_is_enabled(self.driver, 'xpath', search_job)
        load_more = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, search_job)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", load_more)
        self.driver.execute_script("window.scrollBy(0,-200);")
        load_more.send_keys("برنامه نویس")

    def search_job_in_job_group_filter(self):
        wait_until_element_is_enabled(self.driver, 'xpath', search_job_in_job_group_filter)
        load_more = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, search_job_in_job_group_filter)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", load_more)
        self.driver.execute_script("window.scrollBy(0,-200);")
        load_more.send_keys("برنامه نویس")

    def select_job_in_job_group_filter(self):
        wait_until_element_is_enabled(self.driver, 'xpath', select_job_in_job_group_filter)

    def number_of_jobs(self):
        wait_until_element_is_enabled(self.driver, 'xpath', number_of_jobs)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, number_of_jobs))
        )
        text = element.text  # Get the text content of the element
        # Extract numbers from the text using regex
        numbers = re.findall(r'\d+', text)
        if numbers:
            numeric_value = int(numbers[0])  # Assuming the first number is the count
            assert numeric_value > 100, f"Expected more than 100 jobs, found: {numeric_value}"
        else:
            assert False, "No numeric value found in the element text"

    def search_in_jobs_page(self):
        wait_until_element_is_enabled(self.driver, 'xpath', search_in_jobs_page)

    def confirm_job_page(self):
        wait_until_element_is_enabled(self.driver, 'xpath', confirm_job_page)

    def recommended_jobs_page(self):
        wait_until_element_is_enabled(self.driver, 'xpath', recommended_jobs_page)

    def check_apply_for_recommended_jobs_page(self):
        wait_until_element_is_enabled(self.driver, 'xpath', check_apply_for_recommended_jobs_page)

