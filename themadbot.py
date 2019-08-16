import tweepy
import os
import random
import inspect
import numpy as np
from twitter_actions import TwitterActions
from quotes import Quotes
from websites import Websites
from dotenv import load_dotenv

load_dotenv()

os.system('cls' if os.name == 'nt' else 'clear')

menu = np.array(["Tweet",
                 "Summarize Article",
                 "News",
                 "Like",
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
    username = os.getenv("USERNAME")
    consumer_key = os.getenv("KEY")
    consumer_secret = os.getenv("SECRET")
    access_token = os.getenv("TOKEN")
    access_token_secret = os.getenv("TOKEN_SECRET")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    mad_bot = TwitterActions(api, username)

    while True:
        choice = display_menu(menu)
        if choice == 1:
            get_quote = Quotes()
            mad_bot.tweet(get_quote.good_reads())
        elif choice == 2:
            url = input("Paste url: ")
            mad_bot.tweet_thread(url)
        elif choice == 3:
            scrape = Websites()
            link = [scrape.ny_times(),
                    scrape.nine_news(),
                    scrape.the_star(),
                    scrape.abc(),
                    scrape.bbc(),
                    scrape.towards_data_science(),
                    scrape.nature(),
                    scrape.google_ai(),
                    scrape.tech_crunch(),
                    scrape.malaysia_kini()]
            random.shuffle(link)
            for i in range(len(link)):
                mad_bot.tweet_news(link[i])
        elif choice == 4:
            mad_bot.like_tweets()
        elif choice == 5:
            break
