#!/usr/bin/python3
import telebot
from yaml import safe_load


def get_config(path):
    with open(path, 'r') as stream:
        config = safe_load(stream)
    return config

try:
    bot = telebot.TeleBot(get_config('conf')['BOT_TOKEN'])
except Exception as E:
        print ("ERROR:", E)        
        sys.exit(-1)

@bot.message_handler(commands=['report'])
def get_text_messages(message):
    file_name = 'report/report.xlsx';
    with open(file_name, 'rb') as f:
        bot.send_document(message.chat.id, f)
            
@bot.message_handler(commands=['info'])
def message_info(message):
        out_message = "ETL bot by Antipin O.O."
        bot.send_message(message.chat.id, out_message)

#@bot.message_handler(content_types='text')
@bot.message_handler(func=lambda message: True)
def message_reply(message):
        out_message = "What is a '" + message.text + "' ??? 😗"
        bot.send_message(message.chat.id, out_message)


if __name__ == '__main__':
    bot.infinity_polling()