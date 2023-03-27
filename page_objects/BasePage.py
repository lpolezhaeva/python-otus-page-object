from selenium.webdriver import ActionChains

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    TIMEOUT = 5.0
    PAUSE = 0.1

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        ActionChains(self.driver).move_to_element(element).pause(self.PAUSE).click().perform()

    def _input(self, element, value):
        self.click(element)
        element.clear()
        element.send_keys(value)

    def _send_keys(self, locator: tuple, keys):
        element = self.element(locator)
        element.send_keys(keys)

    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        return self.element(parent_locator).find_element(*child_locator)

    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element is not visible {locator}")

    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element is not visible {locator}")
