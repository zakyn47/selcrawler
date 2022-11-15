import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import AlzaLocators, Locators


class Collector(object):

    email_regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    phone_regex = re.compile(r"(^\+?[\d\s?]{10,15})")

    urls = []
    phones = []
    emails = []

    def log_this(func):
        """Decorator for data logging."""

        def wrapper(self):
            with open("log.txt", "a") as f:
                for element in func(self):
                    f.write(element + "\n")
        return wrapper

    @log_this
    def get_emails(self) -> list:
        """Returns list of all emails on the page."""
        print("collecting emails at page: " + self.driver.current_url)
        try:
            for element in self.all_page_elements():
                email_addresses = self.email_regex.findall(element.text)
                self.emails.extend(email_addresses)
        except Exception as e:
            print(e)
        return email_addresses

    @log_this
    def get_phones(self) -> list:
        """Returns list of all phone numbers on the page."""
        print("collecting phones at page: " + self.driver.current_url)
        try:
            for element in self.all_page_elements():
                phone_numbers = self.phone_regex.findall(element.text)
                self.phones.extend(phone_numbers)
        except Exception as e:
            print(e)
        return phone_numbers

    def all_page_elements(self) -> list:
        """Returns list of all elements on the page."""
        WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_all_elements_located(Locators.BODY))
        return self.driver.find_elements(*Locators.BODY)

    @log_this
    def get_urls(self) -> list:
        """Returns list of all urls on the page."""
        print("collecting urls at page: " + self.driver.current_url)
        urls = []
        url_links = self.driver.find_element(
            *Locators.BODY).find_elements(By.TAG_NAME, "a")
        try:
            for link in url_links:
                if link.get_attribute("href").startswith("http"):
                    self.urls.append(link.get_attribute("href"))
                    urls.append(link.get_attribute("href"))
        except:
            pass
        return urls