import os
import telebot

TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "হ্যালো! আপনার ট্রেডিং বট সফলভাবে রেলওয়েতে রান করছে!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "আপনার মেসেজ পাওয়া গেছে। ট্রেডিং বট প্রস্তুত!")

print("Bot is running...")
bot.infinity_polling()
