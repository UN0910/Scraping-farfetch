import scrapy

class FFSpider(scrapy.Spider):
    name = 'farfetch'
    start_urls = ['https://www.farfetch.com/fr/shopping/women/gucci/items.aspx']

    def parse(self, response):
        urlstarting = 'https://www.farfetch.com'
        for products in response.css('div.css-pgof6c-ProductCardFlex'):
            yield {
                'name': products.css('.css-4y8w0i-Body::text').get(),
                'brand': products.css('.css-14ahplz-Body-BodyBold-ProductCardBrandName::text').get(),
                'collection': products.css('.css-1b1o78-Body-LabelPrimary::text').get(),
                'price': products.xpath('/html/body/div[2]/main/section[1]/div/div[3]/div[2]/div[2]/div/div[1]/ul/div[1]/a/div[2]/div[2]/p').get(),
                'link': urlstarting + products.css('a::attr(href)').get()
            }