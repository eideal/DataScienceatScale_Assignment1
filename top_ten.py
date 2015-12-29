import sys
import json
import operator

## Load the tweets
def load_tweets(tweet_file):

    tweets = []
    line = tweet_file.readline()
    while line:
        tweet = json.loads(line.strip())
        tweets.append(tweet)
        line = tweet_file.readline()

    return tweets

## Create dictionary of tweets' hashtags and counts
def get_hashtags(tweet_file):

    tweets = load_tweets(tweet_file)

    hashtags = {}
    for tweet in tweets:
        if 'entities' in tweet and tweet['entities']['hashtags']:
            for dic in range(len(tweet['entities']['hashtags'])):
                tag = tweet['entities']['hashtags'][dic]['text']
                hashtags[tag] = hashtags[tag] + 1 if tag in hashtags.keys() else 1
    return hashtags

## Returns the top ten most frequent hashtags and their counts
def top_ten(tweet_file):

    hashtags = get_hashtags(tweet_file)

    sorted_list = sorted(hashtags.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(10):
        print "%s %i" % (sorted_list[i][0], sorted_list[i][1])


def main():
    tweet_file = open(sys.argv[1])
    
    top_ten(tweet_file)

    tweet_file.close()
        
        

if __name__ == '__main__':
    main()
