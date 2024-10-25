import scrapy


class MeteoredSpider(scrapy.Spider):
    name = "Meteored"
    domain = "https://www.tempo.pt"
    city = "moimenta-da-beira"

    def start_requests(self):
        yield scrapy.Request(
            self.domain + f"/{self.city}.htm",
            callback=self.get_forecast_by_week
        )

    def get_forecast_by_week(self, response):
        block = response.xpath('//ul[@class="grid-container-7 dias_w"]')
        
        day = block.xpath('//span[@class="subtitle-m"]/text()').extract()
        max_temperature = block.xpath('//span[@class="max changeUnitT"]/text()').extract()
        min_temperature = block.xpath('//span[@class="min changeUnitT"]/text()').extract()
        wind_speed = block.xpath('//span[@class="changeUnitW"]/text()').extract()

        path = block.xpath('//span[@class="prediccion col"]/span[@class="precip col"]')
        porcent_rain = path.xpath('span[@class="txt-strng probabilidad center"]/text()').extract()
        aumat_rain = path.xpath('span[@class="changeUnitR"]/text()').extract_first()
        
        collected = {
            "day": day,
            "max_temperature": self.processing_temp(max_temperature),
            "min_temperature": self.processing_temp(min_temperature),
            "wind_speed": self.processing_wind(wind_speed),
            "porcent_rain": porcent_rain,
            "aumat_rain": aumat_rain
        }

        yield collected

    def processing_temp(self, info, tag):
        for data in info:
            print(data.replace("°", ""))
        
    def processing_wind(self, info):
        for data in info:
            print(data.replace("km/h", ""))
        
        """for data in collected["wind_speed"]:
            print(data)

        for data in collected["porcent_rain"]:
            print(data)

        for data in collected["porcent_rain"]:
            print(data)"""

