import scrapy


class ImdbSpyderSpider(scrapy.Spider):
    name = 'imdb_spyder'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        filmes = response.css('.titleColumn')
        for filme in filmes:
            yield{
                'titulo' : filme.css('.titleColumn a::text').get(),
                'anos' : filme.css('.secondaryInfo::text').get()[1:-1],
                'nota' : response.css('strong::text').get(),
            }

