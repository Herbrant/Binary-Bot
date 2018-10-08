# -*- coding: utf-8 -*-

# Telegram
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler, CallbackQueryHandler, RegexHandler
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)

# System libraries
import yaml
import re
import heapq

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
    def __str__(self):      #String rappresentation
        return self.number

#Class Operation
class operation:
    def __init__(self, num1, num2, op, priority):
        self.num1 = num1
        self.num2 = num2
        self.op = op
        self.priority = priority
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

    #Overloading operator
    def __eq__(self, other):
        if self.priority == other.priority:
            return True
        return False
    def __gt__(self, other):
        if self.priority > other.priority:
            return True
        return False
    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        return False
    def __ge__(self, other):
        if self > other | self == other:
            return True
        return False
    def __le__(self, other):
        if self < other | self == other:
            return True
        return False




#Start function
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hi! I'm Binary Bot and I can manipulate binary number. If you want to know what you can do, use /help")

#Decimal to binary function
def dec2binary(n):
    if n == 0:
        return '0'
    else:
        return dec2binary(n // 2) + str(n%2)


#Calculate function
def calculate(bot, update, args):
    i = 0
    while(i < len(args)):
        
        
    bot.sendMessage(chat_id=update.message.chat_id, text="Risultato: ")