

class WeatherbotDataPipeline:
    data_ordered = []
    
    def process_item(self, item, spider):
        rain_amounts = item["rain_amounts"]
        rain_probabilities = item["rain_probabilities"]

        del item["rain_amounts"]
        del item["rain_probabilities"]

        for index in range(0,7):
            self.data_ordered.clear()
            for key, value in item.items():
                self.data_ordered.append(value[index])

            for check in "Chuva", "Trovoada":
                if check in self.data_ordered[4]:
                    for index in range(0, len(rain_probabilities)):
                        self.data_ordered.append(rain_probabilities[index])
                        del rain_probabilities[index]
        
                    print(self.data_ordered)
        #return item
