import twitter_extractor
import tweet_clean

hash_tags = ['coronavirus', 'covid19']
tweet_file = 'tweets.json'


def main():
    # twitter_streamer = twitter_extractor.TwitterStreamer()
    # twitter_streamer.stream_tweets(tweet_file=tweet_file, hash_tag_list=hash_tags)

    for line in open('tweets.json'):
        if line != "\n" and line.__contains__('text'):
            text = tweet_clean.clean_data(line)
            print(text)


if __name__ == '__main__':
    main()
