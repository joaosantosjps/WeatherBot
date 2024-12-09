from weatherbot_database.Connection_Mongodb import MongodbDatabase


class WeatherbotDataPipeline:
    data_ordered = []
    
    def process_item(self, item, spider):
        rain_amounts = item["rain_amounts"]
        rain_probabilities = item["rain_probabilities"]

        del item["rain_amounts"]
        del item["rain_probabilities"]
         
        self.process_data(item, rain_amounts, rain_probabilities)

        return item
    
    def process_data(self,item, rain_amounts, rain_probabilities):

        for index in range(len(item["days"])):
            self.data_ordered.clear()
            
            for value in item.values():
                self.data_ordered.append(value[index])

            for check in "Chuva", "Trovoada":
                if check in self.data_ordered[4]:
                    rain_prob = rain_probabilities.pop(0)
                    rain_mm = rain_amounts.pop(0)

                    self.data_ordered.append(rain_prob)
                    self.data_ordered.append(rain_mm)
            self.insert_data(self.data_ordered)

        return item

        
    def insert_data(self, item):
        connection = MongodbDatabase()
        collection = connection.collection_create()

        """collection.insert_one(dict(item))

        return item"""