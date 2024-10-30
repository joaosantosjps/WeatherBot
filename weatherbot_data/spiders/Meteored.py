import scrapy
from weatherbot_data.items import WeatherbotDataItem

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
        
        days = block.xpath('//span[@class="subtitle-m"]/text()').extract()
        max_temps = block.xpath('//span[@class="max changeUnitT"]/text()').extract()
        min_temps = block.xpath('//span[@class="min changeUnitT"]/text()').extract()
        wind_speeds = block.xpath('//span[@class="changeUnitW"]/text()').extract()
        temps = block.xpath('//span[@class="prediccion col"]/span/img[@class="simbW"]/@alt').extract()

        precipitation_path = block.xpath('//span[@class="prediccion col"]/span[@class="precip col"]')
        rain_probabilities = precipitation_path.xpath('span[@class="txt-strng probabilidad center"]/text()').extract()
        rain_amounts = precipitation_path.xpath('span[@class="changeUnitR"]/text()').extract()

        processed_data = self.processing(days, max_temps, min_temps, wind_speeds, temps, rain_probabilities, rain_amounts)

        yield WeatherbotDataItem(processed_data)

    def processing(self, days, max_temps, min_temps, wind_speeds, temps, rain_probabilities, rain_amounts):
        processed = {}

        processed["days"] = [string.replace(".", "") for string in days]

        processed["max_temps"] = [int(num.replace("°", "")) for num in max_temps]
        
        processed["min_temps"] = [int(num.replace("°", "")) for num in min_temps]
    
        cleaned_speeds = [int(speed.strip()) for speed in wind_speeds if speed.strip().isdigit()]
        processed["wind_speeds"] = [[cleaned_speeds[i], cleaned_speeds[i+1]] for i in range(0, len(cleaned_speeds) - 1, 2)][:7]
    
        processed["rain_probabilities"] = [int(num.replace("%", "")) for num in rain_probabilities]
    
        processed["rain_amounts"] = [float(num.replace("mm", "")) for num in rain_amounts]     

        processed["temps"] = temps
        return processed
