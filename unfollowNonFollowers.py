from instabot import Bot
from time import sleep
from random import randint
import backopyConfig

bot = Bot()
bot.login(username = backopyConfig.USERNAME, password = backopyConfig.PASSWORD)
non_followers = set(bot.following) - set(bot.followers)
for nonFollower in non_followers:
    try:
        bot.unfollow(nonFollower)
        sleep(randint(6, 15))
    except Exception as e:
        print(e)
        sleep(randint(30, 300))


