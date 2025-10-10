import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def xpath(self, value):
        return (By.XPATH, value)

    def css(self, value):
        return (By.CSS_SELECTOR, value)

    def id(self, value):
        return (By.ID, value)

    def name(self, value):
        return (By.NAME, value)

    def class_name(self, value):
        return (By.CLASS_NAME, value)

    def is_open(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except:
            return False

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(locator)
        self.highlight_element(locator)
        element.click()

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def highlight_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].style.border='3px solid red'; arguments[0].style.backgroundColor='yellow';", element)

    def select(self, locator, value):
        selectable = self.wait.until(EC.presence_of_element_located(locator))
        select = Select(selectable)
        select.select_by_visible_text(value)

    def wait_f(self, value):
        self.wait.until(EC.visibility_of_element_located(value))

    def get_list_count(self, value):
        return len(self.driver.find_elements(*value))

    def hover_on_element(self, locator):
        element = self.driver.find_element(*locator)
        self.scroll_to_element(locator)
        self.highlight_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def sleep(self, value):
        time.sleep(value)

    def switch_to_next_tab(self):
        handles = self.driver.window_handles
        current_index = handles.index(self.driver.current_window_handle)
        next_index = (current_index + 1) % len(handles)
        self.driver.switch_to.window(handles[next_index])

    def check_address(self, value):
        return value in self.driver.current_url
