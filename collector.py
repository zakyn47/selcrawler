from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from locators import Locators, AlzaLocators

class Collector(object):

    email_regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    phone_regex = re.compile(r"(^\+?[\d\s?]{10,15})")


    def __init__(self) -> None:
        self.urls = []
        

    def get_emails(self):
        print("collecting emails at page: " + self.driver.current_url)
        for element in self.all_page_elements():
            emails = self.email_regex.findall(element.text)
            if emails:
                print(emails)


    def get_phones(self):
        print("collecting phones at page: " + self.driver.current_url)
        for element in self.all_page_elements():
            phones = self.phone_regex.findall(element.text)
            if phones:
                print(phones)


    def all_page_elements(self) -> list:
        """Returns list of all elements on the page."""
        WebDriverWait(self.driver, 10) \
        .until(EC.presence_of_all_elements_located(Locators.BODY))
        return self.driver.find_elements(*Locators.BODY)


    def get_urls(self):
        print("collecting urls at page: " + self.driver.current_url)
        url_links = self.driver.find_element(*Locators.BODY).find_elements(By.TAG_NAME, "a")
        try:
            for link in url_links:
                if link.get_attribute("href").startswith("http"):
                    self.urls.append(link.get_attribute("href"))
                    print(link.get_attribute("href"))
                    with open("links.txt", "a") as f:
                        f.write(link.get_attribute("href"))
                        f.write("\n")
        except:
            pass


    # alza
    def alza_items(self):
        print("collecting items at page: " + self.driver.current_url)
        items = self.driver.find_element(*AlzaLocators.ITEMS).find_elements(By.TAG_NAME, "a")
        print(len(items))
        for item in items:
            print(item.text)
