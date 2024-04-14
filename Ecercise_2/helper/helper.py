import os

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from datetime import datetime

from selenium.webdriver.common.by import By


class Helper:
    def __init__(self, driver):
        self.driver = driver

    # Метод сохраняющий скриншот элемента
    def get_screenshot_by_elem(self, element, name_dir):
        try:
            elem = self.driver.find_element(By.XPATH, element)
            now_date = datetime.now().strftime("%Y.%m.%d_%H-%M-%S")
            file_name = f"screenshot_{now_date}.png"
            directory_path = f"Ecercise_2/output/{name_dir}"
            if not os.path.isdir(directory_path):
                os.makedirs(directory_path)
            elem.screenshot(os.path.join(directory_path, file_name))
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    # Скрол страницы до элемента
    def scroll_to_elem(self, elem):
        while True:
            try:
                element = self.driver.find_elements(By.XPATH, elem)
                if element:
                    element[0].click()
                    break
            except NoSuchElementException:
                self.driver.find_element(By.CSS_SELECTOR, "html").send_keys(Keys.ARROW_DOWN)
