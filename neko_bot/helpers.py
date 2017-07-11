import random
import twitter
import os
import pygsheets

NEKO_CONSUMER_KEY        = os.getenv("NEKO_CONSUMER_KEY")
NEKO_CONSUMER_SECRET     = os.getenv("NEKO_CONSUMER_SECRET")
NEKO_ACCESS_TOKEN_KEY    = os.getenv("NEKO_ACCESS_TOKEN_KEY")
NEKO_ACCESS_TOKEN_SECRET = os.getenv("NEKO_ACCESS_TOKEN_SECRET")

def login_to_twitter():

    """
        Tries to establish a connection to the twitter API.
        Verifies the validity of passed credentials.
        Returns an error message in case of an issue. (and logs it)
        Returns the api object otherwise.
    """

    api = twitter.Api(
                consumer_key=NEKO_CONSUMER_KEY,
                consumer_secret=NEKO_CONSUMER_SECRET,
                access_token_key=NEKO_ACCESS_TOKEN_KEY,
                access_token_secret=NEKO_ACCESS_TOKEN_SECRET
    )

    print("Logging in to twitter ...")

    try:

        api.VerifyCredentials()

    except twitter.error.TwitterError:
        print("Could not authenticate you. Please check your credentials. \
You need your consumer_key, consumer_secret, access_token_key \
and access_token_secret to access the service.")
        # Log the error to a file
        return
        # sys.exit

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
        print("Could not authenticate you to google sheets: {}".format(e))
        # Log the error to a file
        return
        # sys.exit
    else:
        print("All good !")
        print("Opening spreadsheet ...")
        sheet               = gc.open("Tweets").sheet1
        print("Spreadsheet opened !")
        return sheet

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

def publish_tweet(api_connection, tweet):

    """
        Accepts a string as an argument
        Calls twitter.Api.PostUpdate, passing it the tweet
        If an exception is raised, we print the error and add it to the logs
    """

    try:
        print("Posting update to twitter ...")
        api_connection.PostUpdate(tweet)
    except Exception as e:
        print(e)
        # log the issue
    else:
        print("Posted !")

