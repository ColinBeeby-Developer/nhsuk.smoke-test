from selenium.webdriver.common.by import By

LOCATOR_TYPES = {"css_selector": By.CSS_SELECTOR}


class TestSpec(object):
    """Class to hold the individual test details"""

    def __init__(self, test_details):
        """Set up the elements from the json spec"""
        self.__locator_type = LOCATOR_TYPES.get(test_details.get("locator_type"))
        self.__locator_value = test_details.get("locator_value")
        self.__operation = test_details["operation"]
        self.__sequence_number = test_details["sequence_number"]
        self.__test_value = test_details.get("value")
        self.__wait_for_load = test_details.get("wait_for_load", "False")

    @property
    def locator_type(self):
        return self.__locator_type

    @property
    def locator_value(self):
        return self.__locator_value

    @property
    def operation(self):
        return self.__operation

    @property
    def sequence_number(self):
        return self.__sequence_number

    @property
    def test_value(self):
        return self.__test_value

    @property
    def wait_for_load(self):
        if self.__wait_for_load == "True":
            return True
        return False
