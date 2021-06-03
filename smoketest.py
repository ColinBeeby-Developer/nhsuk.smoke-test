import argparse
import json
import re
import sys
from os import getcwd, listdir

from selenium import webdriver
from selenium.webdriver.common.by import By

from testactions import TestActions
from testspec import TestSpec

LOCATOR_TYPES = {"css_selector": By.CSS_SELECTOR}


class SmokeTest(object):
    """Smoke test the nhs.uk site"""

    def __init__(self, args):
        self._collect_arguments(args)
        self.spec_re = re.compile("^.*-spec.json$")
        driver = webdriver.Chrome(f"webdrivers/{self.webdriver}")
        self.actions = TestActions(driver)

    def _collect_arguments(self, args):
        """Collect the command line arguments"""
        parser = argparse.ArgumentParser(description="Arguments for nhsuk smoke test.")
        parser.add_argument(
            "--test-spec-folder",
            dest="in_dir",
            help="Path and name of the test specification file",
        )
        parser.add_argument(
            "--webdriver", dest="webdriver", help="The webdriver to use"
        )
        arguments = parser.parse_args()
        self.spec_dir = arguments.in_dir
        self.webdriver = arguments.webdriver

    def perform_smoke_test(self):
        """Read in the test specification JSON and process each of the tests"""
        tests_path = f"{getcwd()}/{self.spec_dir}/"
        spec_files = [f for f in listdir(tests_path) if self.spec_re.match(f)]
        for spec_file in spec_files:
            self._process_spec_file(f"{tests_path}/{spec_file}")

        self.actions.close_window()

    def _process_spec_file(self, spec_file):
        """Process a single test specification file"""
        with open(spec_file, "r") as infile:
            test_spec = json.load(infile)
            server_details = self._get_server_details(test_spec)
            print(f"Starting testing server {server_details}")
            for page in test_spec["pages"]:
                self._process_page(server_details, page)
            print(f"Completed testing server {server_details}")

    def _get_server_details(self, test_spec):
        """form the web host root from the protocol, hostname and port"""
        return f"{test_spec['protocol']}://{test_spec['hostname']}:{test_spec['port']}"

    def _process_page(self, server_details, page):
        """Execute the tests for a given page"""
        page_url = page["url"]
        print(f"Started testing page {page_url}")
        self.actions.load_page(server_details, page_url)
        for test in sorted(page["tests"], key=lambda k: int(k["sequence_number"])):
            self._perform_test(server_details, test)
        print(f"Completed testing page {page_url}")

    def _perform_test(self, server_details, test_details):
        """Perform an individual test according to the test specification"""
        test_spec = TestSpec(test_details)
        print(f"Performing test sequence_number {test_spec.sequence_number}")
        try:
            getattr(self.actions, test_spec.operation)(server_details, test_spec)
        except AttributeError:
            print(f"Operation {test_spec.operation} is not recognised")


if __name__ == "__main__":
    smoke_test = SmokeTest(sys.argv)
    smoke_test.perform_smoke_test()
