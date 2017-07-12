from .helpers import (
    fetch_random_tweet_from_google_sheet,
    login_to_google_sheets,
    login_to_twitter,
    open_sheet,
    publish_tweet
)


def main():
    twitter_api     = login_to_twitter()
    sheets_api      = login_to_google_sheets()
    worksheet       = open_sheet(sheets_api)
    tweet           = fetch_random_tweet_from_google_sheet(worksheet)
    publish_tweet(tweet)

if __name__ == "__main__":
    main()


