import random
import time
import sys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from collector import Collector


class Crawler(Collector):
    

    def __init__(self, url: str):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(3)
        self.driver.get(url)

    def go_to_next_url(self):
        if len(self.urls) > 1:
            self.driver.get(random.choice(self.urls))

    def close(self):
        self.driver.close()


if __name__ == "__main__":

    start_url = sys.argv[1]
    next_pages = int(sys.argv[2])

    crawler = Crawler(f"https://{start_url}")
    start_time = time.time()

    while next_pages > 0:
        print("next pages: " + str(next_pages))
        next_pages -= 1
        crawler.get_urls()
        crawler.get_emails()
        crawler.get_phones()
        crawler.go_to_next_url()

    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")
    crawler.close()
