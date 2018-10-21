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


#Bot Command
#Decimal to binary command
def dec_to_binary_cmd(bot, update, args):
    if(re.match('^[-|+]?[0-9]+$', args[0])):        #Regex that check input.
        message = dec_to_two(args[0])
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
        bot.editMessageText(text = "Type /calculate with expression that you want to calculate (e.g /calculate 1011+010).", chat_id = chat_id, message_id = message_id)
    elif data == "bin":
        bot.editMessageText(text = "Type /bin with the decimal number that you want to convert to two's complement binary number (e.g /bin 2).", chat_id = chat_id, message_id = message_id)
    elif data == "dec":
        bot.editMessageText("Type /dec with the two's complement number that you want to convert to decimal number (e.g. /dec 010)", chat_id = chat_id, message_id = message_id)

#Calculate command
def calculate_cmd(bot, update, args):
    if re.match("^([0-1]+[+\-*\/][0-1]+)+$", args[0]):          #Regular expression that check input string
        val = evaluate(str(args[0]))
        message = str(val) + " (" + str(binary_to_dec(val)) + ")"
    else:
        message = "Sintax error. Type /help to more information."

    bot.sendMessage(chat_id = update.message.chat_id, text = message)
