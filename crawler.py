from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from collector import Collector
import random


class Crawler(Collector):

    urls = []
     

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
    crawler = Crawler("https://www.seznam.cz")
    start_time = time.time()


    next_pages = 5
    while next_pages > 0:
        next_pages -= 1
        crawler.get_urls()
        crawler.go_to_next_url()


    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")
    crawler.close()


