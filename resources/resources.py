from selenium.webdriver.common.by import By
from automated_selenium import Selector

class NewsListResources:
    url = "https://news.google.com"
    world_category = Selector(By.XPATH, "//a[@aria-label='World']")