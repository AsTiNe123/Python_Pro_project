import telebot
from keyboards import keyboard1, keyboard2
import requests
from env import TOKEN

bot = telebot.TeleBot(TOKEN)

def send_mot():
    url_of_cat = "https://cataas.com/cat"
    cat = requests.get(url_of_cat).content
    url_of_motivation = "https://favqs.com/api/qotd"
    result= requests.get(url_of_motivation).json()
    return cat, result
print("5555")
@bot.message_handler(commands= ["help", "start"])
def send_message(message):
    bot.send_message(message.chat.id, "th", reply_markup=keyboard1)


@bot.message_handler(func = lambda s: s.text == "Motivation of the day")
def send_motivation(message):
    cat, result = send_mot()
    bot.send_photo(message.chat.id, cat, caption = result["quote"]["body"], reply_markup = keyboard2)

@bot.callback_query_handler(func = lambda s : True)
def callback(call):
    cat, result = send_mot()
    bot.send_photo(call.message.chat.id, cat, caption = result["quote"]["body"], reply_markup = keyboard2)

bot.infinity_polling()
