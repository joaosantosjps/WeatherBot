import scrapy


class MeteoredSpider(scrapy.Spider):
    name = "Meteored"
    domain = "https://www.tempo.pt"
    city = "viseu"

    def start_requests(self):
        yield scrapy.Request(
            self.domain + f"/{self.city}.htm",
            callback=self.parse
        )

    def parse(self, response):
        block = response.xpath('//ul[@class="grid-container-7 dias_w"]')
        
        day = block.xpath('//span[@class="subtitle-m"]/text()').extract()
        max_temperature = block.xpath('//span[@class="max changeUnitT"]/text()').extract()
        min_temperature = block.xpath('//span[@class="min changeUnitT"]/text()').extract()
        wind_speed = block.xpath('//span[@class="changeUnitW"]/text()').extract()
        

        print(day)
        print(max_temperature)
        print(min_temperature)
        print(wind_speed)
        
