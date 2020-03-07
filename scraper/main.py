""" 
Get your electricity bills from TNEB.

Google Pay or other Payment services also provide such options, whats special about this? It keeps sending you emails every day until you have paid your bill :)

"""

import logging
import os
import platform

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


log = logging.getLogger(__name__)
TNEB_LOGIN_URL = "https://www.tnebnet.org/awp/login"


class Tneb:
    def __init__(self, *args, **kwargs):
        self.driver = self.get_driver()

    def get_driver(self):
        try:
            platform_ = platform.system().lower()
            options = Options()

            #  Code to disable notifications pop up of Chrome Browser
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-infobars")
            options.add_argument("--mute-audio")

            chrome_driver = os.path.join(os.getcwd(), f"chromedriver_{platform_}")
            return webdriver.Chrome(
                executable_path=chrome_driver, options=options
            )
        except Exception:
            log.exception(
                "Kindly replace the Chrome Web Driver with the latest one from "
                "http://chromedriver.chromium.org/downloads "
                "and also make sure you have the latest Chrome Browser version."
                "\nYour OS: {platform_}"
            )
            exit(1)

    def login(self):
        """ Log into tneb"""
        driver = self.driver
        driver.get(TNEB_LOGIN_URL)
        driver.maximize_window()

        # Find & Send username and password
        dr
        

    def get_account_data(self):
        """ Get data from Account summary page """
        pass
