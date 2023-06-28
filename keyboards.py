from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

keyboard1 = ReplyKeyboardMarkup(resize_keyboard= True)
button1 = KeyboardButton(text="Motivation of the day")
keyboard1.add(button1)

keyboard2 = InlineKeyboardMarkup()
button2 = InlineKeyboardButton(text = "Change Motivation", callback_data='Cheng_Mot')
keyboard2.add(button2)