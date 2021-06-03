from uitestcore.page import BasePage
from uitestcore.page_element import PageElement


class TestActions(BasePage):
    """Class contains methods to interact with web pages"""

    def __init__(self, driver):
        super().__init__(driver)

    def load_page(self, server_details, page_url):
        """Load the specified web page"""
        self.interact.open_url(f"{server_details}{page_url}")
        self.wait.for_page_to_load()

    def close_window(self):
        self.interact.close_current_window()

    def is_element_visible(self, server_details, test_spec):
        """Invoke the is_element_visible method"""
        if not self.interrogate.is_element_visible(
            PageElement(test_spec.locator_type, test_spec.locator_value)
        ):
            print(f"Test {test_spec.operation} - {test_spec.locator_value} failed")

    def is_text_element_visible(self, server_details, test_spec):
        """Invoke the is_element_visible_and_contains_text method"""
        if not self.interrogate.is_element_visible_and_contains_text(
            PageElement(test_spec.locator_type, test_spec.locator_value),
            test_spec.test_value,
        ):
            print(f"Test {test_spec.operation} - {test_spec.locator_value} failed")

    def click(self, server_details, test_spec):
        """Invoke the click_element method"""
        self.interact.click_element(
            PageElement(test_spec.locator_type, test_spec.locator_value)
        )
        if test_spec.wait_for_load:
            self.wait.for_page_to_load()

    def get_current_url(self, server_details, test_spec):
        """Invoke the get_current_url method"""
        if (
            self.interrogate.get_current_url()
            != f"{server_details}{test_spec.test_value}"
        ):
            print(f"Test {test_spec.operation} - {test_spec.locator_value} failed")

    def enter_text(self, server_details, test_spec):
        self.interact.enter_text(
            PageElement(test_spec.locator_type, test_spec.locator_value),
            test_spec.test_value,
            clear_first=True,
        )
