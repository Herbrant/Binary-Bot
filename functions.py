# -*- coding: utf-8 -*-

# Telegram
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler, CallbackQueryHandler, RegexHandler
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)

# System libraries
import yaml
import re

# Token
tokenconf = open('config/token.conf', 'r').read()
tokenconf = tokenconf.replace("\n", "")
with open('config/settings.yaml', 'r') as yaml_config:
    config_map = yaml.load(yaml_config)

# Token of your telegram bot that you created from @BotFather, write it on token.conf
TOKEN = tokenconf

#Class Binary number
class binary:
    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        return binary(self.number + other.number)   #Use relative function
    def __sub__(self, other):
        return binary(self.number - other.number)   #Use relative function
    def __mul__(self, other):
        return binary(self.number * other.number)   #Use relative function
    def __truediv__(self, other):
        return binary(self.number / other.number)   #Use relative function

#Class Operation
class operation:
    def __init__(self, num1, num2, op):
        self.num1 = num1
        self.num2 = num2
        self.op = op
    def result(self):
        if self.op== '+':
            return self.num1 + self.num2
        elif self.op == '-':
            return self.num1 - self.num2
        elif self.op == '*':
            return self.num1 * self.num2
        elif self.op == '/':
            return self.num1 / self.num2
        else:
            return "-1"


#Start function
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hi! I'm Binary Bot and I can manipulate binary number. If you want to know what you can do, use /help")

#Calculate function
def calculate(bot, update, args):
    bot.sendMessage(chat_id=update.message.chat_id, text="Risultato: ")