from .helpers import (
    fetch_random_tweet_from_google_sheet,
    login_to_google_sheets,
    login_to_twitter,
    publish_tweet
)


def main():
    api     = login_to_twitter()
    sheet   = login_to_google_sheets()
    tweet   = fetch_random_tweet_from_google_sheet(sheet)
    publish_tweet(api, tweet)

if __name__ == "__main__":
    main()


