# import libraries
from Adafruit_IO import Client, Feed, Data
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import requests
import os

#creation the feed(this should be done only once).....if you want to create the feed automatically from code then run this part of code seperatly or else you can create 
#feed = Feed(name='bot')
#result = aio.create_feed(feed)

#adafruit_io user name and active key
ADAFRUIT_IO_USERNAME = os.getenv('ADAFRUIT_IO_USERNAME')
ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY')
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
Telegram_token = os.getenv('Telegram_token')

# Function to reply when you start the bot
def hi(bot, update):
    bot.send_message(chat_id = update.effective_chat.id, text="Welcome!")
    bot.send_message(chat_id = update.effective_chat.id, text="Wanna turn on the light, then type 'Turn on light' or if you wanna turn off the light, then type 'Turn off light'")

# Function to reply when we give irrespective input
def wrong_message(bot, update):
    bot.send_message(chat_id=update.effective_chat.id, text="Oops :/, Please give another try!")

# Function to send data to adafruit_io feed mentioned
def send_data_adafruit(value1):
  value = Data(value=value1)
  value_send = aio.create_data('bot',value)  

# Function to turn on the light 
def turn_on_light(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Turning on the light")
  bot.send_photo(chat_id, photo='http://scienceblog.cancerresearchuk.org/wp-content/uploads/2015/08/Lightbulb_hero2.jpg')
  send_data_adafruit(1)

# Function to turn off the light
def turn_off_light(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Turning off the light")
  bot.send_photo(chat_id=update.effective_chat.id,photo='https://pngimg.com/uploads/bulb/bulb_PNG1241.png')
  send_data_adafruit(0)

def text_given(bot, update):
  text = update.message.text
  if text == 'hi':
    hi(bot,update)
  elif text == 'Turn on light':
    turn_on_light(bot,update)
  elif text == 'Turn off light':
    turn_off_light(bot,update)
  else:
    wrong_message(bot,update)

    # Final code to call all the functions

u = Updater('1177868055:AAEgWEdeu1LgQ1hSlRSAsaU36zQlSgtUroY')
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text, text_given))
u.start_polling()
u.idle()
