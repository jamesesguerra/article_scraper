import scrapy
import json


class ABSSpider(scrapy.Spider):
    name = 'gma'
    start_urls = ['https://data2.gmanews.tv/gno/widgets/grid_reverse_listing/story_btbbalita/1']


    def __init__(self, pages='', **kwargs):
        self.pages = pages
        self.count = 1
        super().__init__(**kwargs)


    def parse(self, response):
        base_url = 'https://www.gmanetwork.com/news/'
        articles = json.loads(response.body)['data']
        for article in articles:
            yield response.follow(f"{base_url}{article['article_url']}", callback=self.parse_articles)
        
        self.count += 1

        if self.count <= int(self.pages):
            next_page = f"https://data2.gmanews.tv/gno/widgets/grid_reverse_listing/story_btbbalita/{self.pages}"
            yield response.follow(next_page, callback=self.parse)


    def parse_articles(self, response):
        # init_summary = ''.join(response.css('div.article-body > p:first-child *::text').getall())
        # summary = init_summary if init_summary != ' ' else ' '.join(response.css('div.article-body > p:nth-of-type(2) *::text').getall()).strip()

        yield {
            'title': response.css('h1::text').get(),
            'article_text': ' '.join(response.css('div.article-body p::text').getall()).strip(),
            'article_date': response.css('div.article-date::text').get().strip(),
            'source': response.request.url
        }