import telebot

BOT_TOKEN = "BOT_TOKEN = "7850690150:AAHDZHkquSUlmvztzTc6CkqPl2M3_j0BFe4"
AD_LINK = "https://omg10.com/4/10607176"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome 🔓\nUnlock here:\n" + AD_LINK)

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(message, "Link lene ke liye pehle unlock kare:\n" + AD_LINK)

bot.infinity_polling()
