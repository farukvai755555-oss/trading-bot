import os
import telebot

TOKEN = "9208785820:AAG5c1769f8769s88DZIs61EJHeX1ukgpSs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "হ্যালো! আপনার ট্রেডিং বট সফলভাবে চালু হয়েছে।")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "আপনার মেসেজ পাওয়া গেছে। ট্রেডিং বট কাজ করছে!")

print("Bot is running...")
bot.infinity_polling()
