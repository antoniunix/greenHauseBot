#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import time
#time.sleep(60)

"""
This is a detailed example using almost every command of the API
"""

import credencialtelegrambotservice
import command
import telebot
from telebot import types
import time
import os

userStep = {} # so they won't reset every time the bot restarts

hideBoard = types.ReplyKeyboardRemove() # if sent as reply_markup, will hide the keyboard


# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text


bot = telebot.TeleBot(credencialtelegrambotservice.TOKEN)
bot.set_update_listener(listener) # register listener

# help page
@bot.message_handler(command.commands.upper()=['AYUDA','HELP'})
def command_help(m):
    cid = m.chat.id
    help_text = "Estos son los comandos disponibles: \n"
    for key in command.commands:
        help_text += "/" + key + ": "
        help_text += command.commands[key] + "\n"
    bot.send_message(cid, help_text)



# filter on a specific message
@bot.message_handler(func=lambda message: message.text == "temperatura")
def command_text_hi(m): bot.send_message(m.chat.id, "Muy buenas")



@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    # this is the standard reply to a normal message
    bot.send_message(m.chat.id, "No te entiendo, prueba con /ayuda")

bot.polling()
