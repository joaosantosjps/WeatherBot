from weatherbot_database.Connection_Mongodb import MongodbDatabase


class WeatherbotDataPipeline:
    data_ordered = []
    
    def process_item(self, item, spider):
        rain_amounts = item["rain_amounts"]
        rain_probabilities = item["rain_probabilities"]

        del item["rain_amounts"]
        del item["rain_probabilities"]
         
        self.process_data(item, rain_amounts, rain_probabilities)
    
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
            
            self.transform_dict(self.data_ordered)

    def transform_dict(self, values):
        record = {
            "date": values[0],
            "temp_max": values[1],
            "temp_min": values[2],
            "temp_range": values[3],
            "condition": values[4]
        }

        if len(values) > 5:
            record["rain_probability"] = values[5]
        if len(values) > 6:
            record["rain_quantity"] = values[6]

        self. insert_data(record)

        
    def insert_data(self, item):
        print(item)
        connection = MongodbDatabase()
        collection = connection.collection_create()

        collection.insert_one(dict(item))

        return item