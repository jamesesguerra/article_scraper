from ..utils.placeRemover import clean
import scrapy
from urllib import parse


class ABSSpider(scrapy.Spider):
    name = 'abs-cbn'
    start_urls = ['https://news.abs-cbn.com/patrol/tag/tagalog-news']


    def __init__(self):
        self.count = 1


    def parse(self, response):
        base_url = 'https://news.abs-cbn.com/patrol/tag/tagalog-news'
        articles = response.css('.articles article')
        last_page_url = response.css('.last').attrib['href']
        max_pages = parse.parse_qs(parse.urlparse(last_page_url).query)['page'][0]
        for article in articles:
            yield response.follow(article.css('a').attrib['href'], callback=self.parse_articles)
        
        self.count += 1

        if self.count <= int(max_pages):
            next_page = f"{base_url}?page={self.count}"
            yield response.follow(next_page, callback=self.parse)


    def parse_articles(self, response):
        yield {
            'title': response.css('h1.news-title::text').get(),
            'article_text': ' '.join(response.css('div.article-content p::text').getall()),
            'summary': clean(response.css(".article-content > p::text").get()).strip(),
            'article_date': response.css('span.date-posted::text').get(),
            'source': response.request.url
        }