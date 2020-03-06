import twitter_extractor

hash_tags = ['coronavirus', 'covid19']
tweet_file = 'tweets.json'


def main():
    twitter_streamer = twitter_extractor.TwitterStreamer()
    twitter_streamer.stream_tweets(tweet_file=tweet_file, hash_tag_list=hash_tags)


if __name__ == '__main__':
    main()
