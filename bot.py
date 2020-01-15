import telebot

#init bot


#read token
bot=telebot.TeleBot(input())



#command = /smth
#message = smth


@bot.message_handler(commands=['start'])
def send_welcome(message):
    global bot
    bot.reply_to(message,"Agalar sa")

@bot.message_handler(commands=['help'])
def send_help(message):
    global bot
    bot.reply_to(message,"su anlik yardim edilecek bir sey yok")

@bot.message_handler(regexp="sa")
def send_sa(message):
    global bot
    bot.reply_to(message,"as")

bot.polling()


