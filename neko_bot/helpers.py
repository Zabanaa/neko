import sys
import random
import twitter
import os
import pygsheets
from .log import logger

NEKO_CONSUMER_KEY        = os.getenv("NEKO_CONSUMER_KEY")
NEKO_CONSUMER_SECRET     = os.getenv("NEKO_CONSUMER_SECRET")
NEKO_ACCESS_TOKEN_KEY    = os.getenv("NEKO_ACCESS_TOKEN_KEY")
NEKO_ACCESS_TOKEN_SECRET = os.getenv("NEKO_ACCESS_TOKEN_SECRET")
NEKO_SPREADSHEET_NAME    = os.getenv("NEKO_SPREADSHEET_NAME")

api = twitter.Api(
    consumer_key=NEKO_CONSUMER_KEY,
    consumer_secret=NEKO_CONSUMER_SECRET,
    access_token_key=NEKO_ACCESS_TOKEN_KEY,
    access_token_secret=NEKO_ACCESS_TOKEN_SECRET
)

def login_to_twitter():

    """
        Tries to establish a connection to the twitter API.
        Verifies the validity of passed credentials.
        Returns an error message in case of an issue. (and logs it)
        Returns the api object otherwise.
    """

    print("Logging in to twitter ...")

    try:

        api.VerifyCredentials()

    except twitter.error.TwitterError as e:
        print("An error occured while authenticating you. \
Please check the logs for more information")
        logger.error("Error: - {}".format(e))
        return sys.exit()

    else:
        print("Logged in!")
        return api

# ========================================================================= #

def login_to_google_sheets():

    """
        Tries to establish a connection to the google spreadsheet service.
        Opens the worksheet named "Tweets"
        Returns the sheet
        Returns an error message in case of an error. (and logs it)
    """

    print("Accessing Google Spreadsheets ...")

    try:
        gc = pygsheets.authorize()

    except Exception as e:
        print("Could not authenticate you to google sheets. \
Please check the logs for more information")
        logger.error("Error: - {}".format(e))
        return sys.exit()

    print("All good ! \n Opening spreadsheet ...")
    return gc

# ========================================================================= #

def open_sheet(connection):

    """
        Tries to open NEKO_SPREADSHEET_NAME
        In case of error, we log it to the file
        Else we return the worksheet
    """

    try:
        worksheet = connection.open(NEKO_SPREADSHEET_NAME).sheet1
    except pygsheets.exceptions.SpreadsheetNotFound as e:
        print("Error - Spreadsheet '{}' does not exist".format(NEKO_SPREADSHEET_NAME))
        return sys.exit()
    else:
        print("Spreadsheet opened !")
        return worksheet

# ========================================================================= #

def fetch_random_tweet_from_google_sheet(sheet):

    """
        Accepts a sheet object as an argument
        Transforms the object into a list
        Extracts a random item from the list and returns it
    """

    list_of_tweets      = list(sheet)
    random_tweet = " ".join(random.choice(list_of_tweets)).strip()
    return random_tweet

# ========================================================================= #

def publish_tweet(tweet):

    """
        Accepts a string as an argument
        Calls twitter.Api.PostUpdate, passing it the tweet
        If an exception is raised, we print the error and add it to the logs
    """

    try:
        print("Posting update to twitter ...")
        api.PostUpdate(tweet)
    except Exception as e:
        print("Could not publish tweet. Please check the logs for more info")
        logger.error(e)
    else:
        print("Posted !")

