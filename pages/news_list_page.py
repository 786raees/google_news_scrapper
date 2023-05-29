from automated_selenium import BasePage
from resources.resources import NewsListResources

class NewsListPage(BasePage):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.driver.get(NewsListResources.url)
    
    def search_keyword(self, search_keyword: str):
        pass