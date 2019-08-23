# THE MAD BOT PROJECT
This project is divided into 3 stages:

**Stage 1:**
Twitter API requests, web-scraping, text summarization

**Stage 2:**
Django app

**Stage 3:**
Text generator/question-answering/interactive tweets using SOTA language models


## Getting Started
* This app runs on [Python 3](https://www.python.org/downloads/).
* Clone this repository: `git clone https:://github.com/farahsamat/sentweetment.git`
* Install dependencies: `pip install -r requirements.txt`
* API authentication credentials for Twitter API access: Rename `.env.example` to `.env` and populate it with the required login credentials.
> If you haven't downloaded the trained GPT-2 models:
> * Clone this repository: `git clone https://github.com/openai/gpt-2.git`
> * Run the following scripts to download the desired models:

>     `python gpt-2/download_model.py 124M` or 
    
>     `python gpt-2/download_model.py 355M` or 
    
>   `python gpt-2/download_model.py 774M`

## Using the The Mad Bot app
Run the following script on terminal.

`python themadbot.py`

## Acknowledgments

[Twitter API Doc](https://developer.twitter.com/en/docs/api-reference-index)

[Intent classification](https://towardsdatascience.com/a-brief-introduction-to-intent-classification-96fda6b1f557)