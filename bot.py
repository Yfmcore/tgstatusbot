# telegram status bot v1.1 by @codingstorm (@yfimsky)

import time # i dunno why i put it here
import pythonping # really need to make bot working
import telebot # "bones" and "meat" of ur bot
from datetime import datetime # useless shit but i have it l0l

bot = telebot.TeleBot('') # put ur telegram bot token here

ping = pythonping.ping('') # put ur url here
latency = ping.rtt_avg_ms # pinging site here

banList = [] # ban list that using in start command

admin = [] # put ur id here


@bot.message_handler(commands=['start']) # start command use it everywhere coz its doesnt matter
def send_message(message):
    if message.from_user.id not in banList:
        if message.from_user.id in admin:
            bot.reply_to(message, 'Started.')
            while latency < 2000:
                now = datetime.now() # u can delete this if u want
                current_time = now.strftime("%H:%M:%S") # this too
                bot.send_message(-1001517841488,
                                 'Telegram ping is: ' + str(latency) + '\n' + 'Local time is: ' + current_time)
                time.sleep(300)
            else:
                bot.send_message(-1001517841488, 'Telegram or server is down') # lib thinking 2000 ping = dead
        else:
            bot.reply_to(message, 'You can not use that bot.\n' + 'Bot was not made chatting.')
            bot.send_message(message.chat.id, str(message.from_user.id) + " was banned.")
            print(str(message.from_user.id) + ' was banned')
            banList.append(int(message.from_user.id))
    else:
        if message.from_user.id in banList: # lil shit to do not cloning the same user id
            pass
        else:
            banList.append(int(message.from_user.id))
            print(banList)


@bot.message_handler(commands=['stop']) # stop command useful thing
def stop(message):
    if message.from_user.id in admin:
        print(':(')
        bot.stop_bot()
    else:
        pass


bot.polling(non_stop=True)
