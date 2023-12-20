import scrapy
from ptt_education.items import PttEducationItem

class PttEducationSpider(scrapy.Spider):
    name = 'ptt_education'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Education/index.html']

    def parse(self, response):
        # 提取文章列表中的標題和連結
        for article in response.css('.r-ent'):
            title = article.css('.title a::text').get()
            link = response.urljoin(article.css('.title a::attr(href)').get())
            yield {
                'title': title,
                'link': link,
            }

        # 獲取下一頁的鏈接
        next_page = response.css('.btn-group-paging a.btn.wide::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
