import scrapy
from datetime import datetime 
from tqdm import tqdm
import bs4 


class InsideWebSpider(scrapy.Spider):
    name = "inside_web"
    allowed_domains = ["www.inside.com.tw"]
    start_urls = ["https://www.inside.com.tw/"]
    page_param = '?page='

    def parse(self, response):
        for i in range(1, 100):  
            yield scrapy.Request(url=response.urljoin(self.page_param + str(i)), callback=self.parse_page_number)

    def parse_page_number(self, response):
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        titles = soup.find_all('h3', {'class': 'post_title'})

        for title in titles:
            print(f"\nURL: {response.url}")
            print(f"Title: {title.text.strip()}")
            yield {'title': title.text.strip()}
        
    