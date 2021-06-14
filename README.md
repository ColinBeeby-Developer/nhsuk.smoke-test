# nhsuk.smoke-test
Prototype code for smoke testing / UI testing

## Install
Clone this repo into a convenient folder

## Configuration
Before running the nhsuk.smoke-test you may need to set up the required details in the testspec json files. They are configured to run the smoke tests on the localhost on port 8000. You may with to modify the hostname, protocol and port settings to point to a different instance. Also within the cmslogin-spec.json file you'll need to replace \< username \> with a valid username and \< password \> with a valid password.
  
## Installing the webdriver
  In order to run these smoketest you will need to install a webdriver for the browser of your choice. For example you can download the chrome driver from here https://chromedriver.chromium.org/downloads . When you have downloaded the webdriver which you require, copy it to the webdrivers folder.
  
## Run The Smoke Test
Before running the smoke test, enter the virtual environment:
  pipenv shell
To run the smoke test do 
  python smoketest.py --test-spec-folder \<path to testspec folder\> --webdriver \< webdriver \>
