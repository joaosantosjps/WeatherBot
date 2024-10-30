import scrapy


class WeatherbotDataItem(scrapy.Item):
    days = scrapy.Field()
    max_temps = scrapy.Field()
    min_temps = scrapy.Field()
    wind_speeds = scrapy.Field()
    temps = scrapy.Field()
    rain_probabilities = scrapy.Field()
    rain_amounts = scrapy.Field()