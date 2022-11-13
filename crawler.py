from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from collector import Collector

class Crawler(Collector):

    urls = []
     

    def __init__(self, url: str):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(3)
        self.driver.get(url)
    

    def go_to_next_url(self):
        if len(self.urls) > 1:
            self.driver.get(self.urls[0])
            self.urls.pop(0)
    

    def close(self):
        self.driver.close()
        

if __name__ == "__main__":
    UrlGrabber = Crawler("https://www.alza.cz/graficke-karty/18842862.htm")
    start_time = time.time()


    next_pages = 5
    while next_pages > 0:
        next_pages -= 1
        UrlGrabber.alza_items()
        UrlGrabber.get_emails()
        UrlGrabber.get_phones()
        UrlGrabber.go_to_next_url()


    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")
    UrlGrabber.close()