import os
import telebot
from weatherbot_database.Connection_Mongodb import MongodbDatabase


key_api = os.getenv("KEY_API_BOT_TELEGRAM")

bot = telebot.TeleBot(key_api)




@bot.message_handler(commands=["Weather"])
def Weather(message):
    connection = MongodbDatabase()
    db = connection.db.client["Weather_Forecast"]["Weather"]
    for c in db.find({}):
        bot.send_message(message.chat.id, f'{c["date"]} > 
                         {c["condition"]} > 
                         {c.get("rain_probability", "")}% > 
                         {c.get("rain_quantity", "")}m.m')



bot.polling()