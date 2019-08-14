import tweepy
import os
import textwrap
import random
import numpy as np
from twitter_actions import TwitterActions
from quotes import Quotes
from websites import Websites
from dotenv import load_dotenv

load_dotenv()

os.system('cls' if os.name == 'nt' else 'clear')

menu = np.array(["Tweet",
                 "Post Article Summary",
                 "Post News",
                 "Fav/Like",
                 "Retweet",
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

    mad_bot = TwitterActions(api)

    while True:
        choice = display_menu(menu)
        if choice == 1:
            get_quote = Quotes()
            mad_bot.tweet(get_quote.good_reads())
        elif choice == 2:
            url = input("Paste url: ")
            if len(mad_bot.tweet_thread(url)) <= 140:
                api.update_status('1/1\n', url + '\n', mad_bot.tweet_thread(url))
            else:
                text_chunks = textwrap.wrap(mad_bot.tweet_thread(url), 140)
                api.update_status('2/{}\n'.format(len(text_chunks)) + url + '\n' + text_chunks[0])
                tweet = api.user_timeline(screen_name=username, count=1)[0]
                for i in range(len(text_chunks) - 1):
                    api.update_status('{}/{}\n'.format(i + 2, len(text_chunks)) + text_chunks[i + 1], tweet.id)
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
            # TODO
            break
        elif choice == 5:
            # TODO
            break
        elif choice == 6:
            # TODO
            break
        elif choice == 7:
            # TODO
            break
        elif choice == 8:  # Exit app
            break
