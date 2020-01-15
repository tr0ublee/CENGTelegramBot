import telebot

#init bot


#read token
#TODO
# ADD TOKEN TO .gitignore
bot=telebot.TeleBot(input())



#command = /smth
#message = smth

"""
How to add your own function? 

1-start a message_handler for your function

2-while doing so, use the format regexp="\\byour_command\\b" (just like send_sa)

3-to reach all the information about the message, for instance the whole message, 
 you can reach it as message.text 
"""



@bot.message_handler(commands=['start'])
def send_welcome(message):
    global bot
    bot.reply_to(message,"Agalar sa")

@bot.message_handler(commands=['help'])
def send_help(message):
    global bot
    bot.reply_to(message,"su anlik yardim edilecek bir sey yok")

@bot.message_handler(regexp="\\bsa\\b")
def send_sa(message):
    global bot
    bot.reply_to(message,"as")

bot.polling()


