import telebot
import random
from telebot import types
import requests


bot = telebot.TeleBot("823068632:AAHW4I8OzfGGDyUzQVuGU4MxNZciTiNCBVU")
file_id = 'CAADAgAD4gYAAkb7rASS-sWU9H6MThYE'
chat_id = '833816011'
file_info = bot.get_file(file_id)
user = bot.get_me()



photo = open('lol.jpg', 'rb')
music = open('animals.mp3', 'rb')
SOME_FANCY_EMOJI = ['😁','😄','☺','❤','😆']

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Yo, how u doing?")

#find_location=tb.send_location(chat_id, lat, lon)
send_photo = bot.send_photo(chat_id, photo)
@bot.message_handler(commands=['photo'])
def send_photo(message):
	bot.send_chat_action(chat_id, send_photo)
	

@bot.message_handler(content_types='sticker')
def send_message(message):
	bot.send_message(chat_id, message, reply_markup=markup)

@bot.message_handler(commands=['music'])
def send_music(message):
	bot.send_audio(message.chat.id, music)


def handle_messages(messages):
	for message in messages:
		# Do something with the message
		bot.reply_to(message, '😁😄')

bot.set_update_listener(handle_messages)

markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('Saweetie')
itembtnv = types.KeyboardButton('Camila Cabello')
itembtnc = types.KeyboardButton('Maroon5')
itembtnd = types.KeyboardButton('Bhad Bhabie')
itembtne = types.KeyboardButton('Shawn Mendes')
markup.row(itembtna, itembtnv)
markup.row(itembtnc, itembtnd, itembtne)
@bot.message_handler(commands=['hello'])
def send_message(message):
	bot.send_message(message.chat.id, "Choose one singer:", reply_markup=markup)
#markup = types.ReplyKeyboardRemove(selective=False)
#bot.send_message(chat_id, message, reply_markup=markup)

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#	bot.reply_to(message, message.text)

bot.polling()