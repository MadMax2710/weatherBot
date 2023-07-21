import telebot
import requests
import json

bot = telebot.TeleBot("6363782544:AAG9xIbmxuCyd1C41oPsjLAvfywNW3DsL4Y")
API_key = 'c3ec06a00f858dee3438238db706b620'
# 041253db4df14d0d895143255232107
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id , "Погода \nвведіть місто для погоди або поділіться своєю геолокацією!")

@bot.message_handler(content_types=['location'])
def handle_location(message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    res = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid={API_key}')
    data = json.loads(res.text)
    main = data["main"]
    clouds = data["clouds"]["all"]
    bot.reply_to(message,f'Температура зараз:{main["temp"]} \nНайвища {main["temp_max"]} \nНайнижча {main["temp_min"]}\nХмарність {clouds}%')
    # bot.send_message(message.chat.id, f"Your location: {latitude}, {longitude}")

@bot.message_handler(content_types=['text'])
def get_data(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric")
    data = json.loads(res.text)
    main = data["main"]
    clouds = data["clouds"]["all"]
    bot.reply_to(message,f'Температура зараз:{main["temp"]} \nНайвища {main["temp_max"]} \nНайнижча {main["temp_min"]}\nХмарність {clouds}%')
    




bot.polling(non_stop=True)