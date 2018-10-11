# -*- coding: utf-8 -*-

# Telegram
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler, CallbackQueryHandler, RegexHandler

# System libraries
import re

# Token
tokenconf = open('config/token.conf', 'r').read()
tokenconf = tokenconf.replace("\n", "")

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


#Decimal to binary function
def dec_to_binary(n):
    if n == 0:
        return '0'
    else:
        return dec_to_binary(n // 2) + str(n%2)

#Binary to decimal function
def binary_to_dec(n):
    return int(n,2)

#Binary sum
def binary_sum(a, b):
    len_max = max(len(a), len(b))

    a = a.zfill(len_max)
    b = b.zfill(len_max)

    result = ''
    carry = 0

    for i in range(len_max - 1, -1, -1):
        r = carry
        if a[i] == '1':
            r += 1
        if b[i] == '1':
            r += 1
        if(r % 2 == 1):
            result += 1
        if r < 2:
            carry = 0
        else:
            carry = 1
    if carry != 0:
        result = '1' + carry
    return result.rzfill(len_max)



#Bot Command

#Decimal to binary command
def dec_to_binary_cmd(bot, update, args):
    if not(args):
        message = "BANANA"
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
