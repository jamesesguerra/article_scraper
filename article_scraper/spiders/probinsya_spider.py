from ..utils.placeRemover import clean
import scrapy


class PSNSpider(scrapy.Spider):
    name = 'probinsya'
    start_urls = ['https://www.philstar.com/micro_page.php?qcount=1&micro=102&page=1&cell=2&lastid=2205435']


    def __init__(self, pages='', **kwargs):
        self.pages = pages
        self.count = 0
        super().__init__(**kwargs) 


    def parse(self, response):
        articles = response.css('div.microsite_article')
        for article in articles:
            yield response.follow(article.css('a').attrib['href'], callback=self.parse_articles)
        
        self.count += 1
        next_page = response.css('div.next a').attrib['href']

        if self.count < int(self.pages) and next_page is not None:
            yield response.follow(next_page, callback=self.parse) 


    def parse_articles(self, response):
        yield {
            'title': response.css('.article__title h1::text').get(),
            'article_text': clean(' '.join(response.css('.article__writeup p::text').getall())).strip(),
            'summary': clean(response.css('.article__writeup p:first-of-type::text').get()).strip(),
            'article_date': response.css('.article__date-published::text').get().replace('|', ''),
            'source': response.request.url
        }