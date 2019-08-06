import tweepy
import os
import numpy as np
from twitter_actions import TwitterActions
from dotenv import load_dotenv

load_dotenv()

os.system('cls' if os.name == 'nt' else 'clear')

menu = np.array(["Update Status",
                 "What's New",
                 "Fav/Like",
                 "RT",
                 "Mention/Reply",
                 "Personalised greetings/DM",
                 "Exit"])


def input_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print(" ")
            pass
    return num


def display_menu(options):
    print(" ")
    print("------------ THE MAD BOT ----------------")
    for i in range(len(options)):
        print("{:d}. {:s}".format(i + 1, options[i]))

    option = 0
    while not (np.any(option == np.arange(len(options)) + 1)):
        option = input_number("Please choose your option: ")
        print(" ")
    return option


if __name__ == "__main__":
    consumer_key = os.getenv("KEY")
    consumer_secret = os.getenv("SECRET")
    access_token = os.getenv("TOKEN")
    access_token_secret = os.getenv("TOKEN_SECRET")
    username = os.getenv("USERNAME")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    mad_bot = TwitterActions(api, username)
    like_who_you_follow = []
    what_you_like = ['#ml',
                     '#AI',
                     '#nlp',
                     '#nerdjokes',
                     '#melbourne',
                     '#coding',
                     '#womenintech',
                     '#deakin',
                     'uniten',
                     'engineering',
                     '#github'
                     '#orchestra'
                     'software']

    news_feed = ['https://towardsdatascience.com/',
                 'https://www.nature.com/',
                 'https://www.bbc.com/news',
                 'https://www.abc.net.au/news/',
                 'https://www.malaysiakini.com/']

    while True:
        choice = display_menu(menu)
        if choice == 1:
            tweet = input("Enter your tweet: ")
            mad_bot.tweet(tweet)
        elif choice == 2:
            for website in news_feed:
                mad_bot.scrape_and_tweet(website)
        elif choice == 3:
            # do something
            break
        elif choice == 4:
            #topics = list(input("Enter a hashtag or multiple hashtags: ").split())
            for topic in what_you_like:
                mad_bot.retweet(topic)
        elif choice == 5:
            # do something
            break
        elif choice == 6:
            # do something
            break
        elif choice == 7:  # Exit app
            break
