import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    valid_tweet=tweets.loc[tweets['content'].str.len()>15, ["tweet_id"]]
    return valid_tweet