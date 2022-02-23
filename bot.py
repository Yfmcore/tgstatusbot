# telegram status bot v1.3 by @codingstorm (@yfimsky)
import time  # i dunno why i put it here
import pythonping  # really need to make bot working
import telebot  # "bones" and "meat" of ur bot
from datetime import datetime  # useless shit but i have it l0l

bot = telebot.TeleBot('')  # put ur telegram bot token here

banList = []  # ban list that using in start command

admin = []  # put ur id here

channel = ""  # put ur telegram channel here but before add the bot there and make him admin


@bot.message_handler(commands=['start'])  # start command use it everywhere coz its doesnt matter
def send_message(message):
    if message.from_user.id not in banList:
        if message.from_user.id in admin:
            bot.reply_to(message, 'Started.')  # bot says what hes started important thing
            while True:
                ping = pythonping.ping('').rtt_avg_ms  # ping thing. type any host u want
                now = datetime.now()  # u can delete this if u want
                current_time = now.strftime("%H:%M:%S")  # this too
                bot.send_message(channel,
                                 'Telegram ping is: ' + str(ping) + '\n' + 'Local time is: ' + current_time)
                time.sleep(300)  # bed time!
        else:
            bot.reply_to(message, 'You can not use that bot.\n' + 'Bot was not made chatting.')
            bot.send_message(message.chat.id, str(message.from_user.id) + " was banned.")
            print(str(message.from_user.id) + ' was banned')
            banList.append(int(message.from_user.id))
    else:
        if message.from_user.id in banList:  # lil shit to do not cloning the same user id
            pass
        else:
            banList.append(int(message.from_user.id))
            print(banList)


@bot.message_handler(commands=['stop'])  # stop command useful thing
def stop(message):
    if message.from_user.id in admin:
        bot.reply_to(message, ':(')
        bot.stop_bot()
    else:
        pass


bot.polling(non_stop=True)
