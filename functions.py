# -*- coding: utf-8 -*-
from evaluate import *

# Telegram
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, CommandHandler, CallbackQueryHandler


# Token
tokenconf = open('config/token.conf', 'r').read()
tokenconf = tokenconf.replace("\n", "")

# Token of your telegram bot that you created from @BotFather, write it on token.conf
TOKEN = tokenconf

#Decimal to binary function
def dec_to_binary(n):
    if n == 0:
        return '0'
    else:
        return dec_to_binary(n // 2) + str(n%2)

#Binary to decimal function
def binary_to_dec(n):
    return int(n,2)


#Bot Command

#Decimal to binary command
def dec_to_binary_cmd(bot, update, args):
    if(re.match('^[0-9]+$', args[0])):        #Regex that check input.
        message = dec_to_binary(int(args[0]))
    else:
        message = "Sintax error. Type /help to more information."
    bot.sendMessage(chat_id=update.message.chat_id, text = message)

#Binary to decimal command
def binary_to_dec_cmd(bot, update, args):
    if(re.match('^[0-1]+$', args[0])):       #Regex that check input.
        message = binary_to_dec(str(args[0]))
    else:
        message = "Sintax error. Type /help to more information."
    bot.sendMessage(chat_id=update.message.chat_id, text = message)

#Start command
def start_cmd(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hi! I'm Binary Bot and I can manipulate binary number. If you want to know what you can do, use /help")


#Help command
def help_cmd(bot, update):
    keyboard = [[InlineKeyboardButton("Calculate", callback_data="calculate")],
                [InlineKeyboardButton("Decimal to Binary", callback_data="bin"),InlineKeyboardButton("Binary to Decimal", callback_data="dec")]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('@Binary_Bot commands:', reply_markup = reply_markup)

def button(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    data = query.data
    
    if data == "calculate":
        bot.editMessageText(text = "Scrivi /calculate inserendo come parametro un'espressione da calcolare.", chat_id = chat_id, message_id = message_id)
    elif data == "bin":
        bot.editMessageText(text = "Scrivi /bin inserendo come parametro un numero decimale da convertire in binario.", chat_id = chat_id, message_id = message_id)
    elif data == "dec":
        bot.editMessageText("Scrivi /dec inserendo come parametro un numero binario da convertire in decimale.", chat_id = chat_id, message_id = message_id)

#Calculate command
def calculate_cmd(bot, update, args):
    message = evaluate(str(args[0]))

    bot.sendMessage(chat_id = update.message.chat_id, text = message)