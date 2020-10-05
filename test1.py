import telebot
import pyowm
from pyowm.utils.config import get_config_from

config_dict = get_config_from('config.json')

owm = pyowm.OWM('a983265a9317de3fcbbb32ae551dc1ea', config_dict)
bot = telebot.TeleBot("1288082498:AAE-VaeDaJDLH1GYCG7IObQ-5jZimyRVGyI")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)  # the observation object is a box containing a weather object
    weather = observation.weather
    print("weather", weather)
    temp = weather.temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + weather.detailed_status + "\n"
    answer += "температура сейчас в районе " + str(temp) + "\n"

    if temp < 10:
        answer += "щас холодно"
    elif temp < 20:
        answer += "не холодно но и не тепло"
    else:
        answer += "щас норм"
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)


