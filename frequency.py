import sys
import json

## Load the tweets
def load_tweets(tweet_file):

    tweets = []
    line = tweet_file.readline()
    while line:
        tweet = json.loads(line.strip())
        tweets.append(tweet)
        line = tweet_file.readline()

    return tweets

## Get the tweet text
def tweet_text(tweets):
    
    text = []
    for tweet in tweets:
        if 'text' in tweet:
            text.append(tweet['text'])
        else:
            continue

    return text

# Split tweets by words
def tweet_words(text):
    lst = []
    for tweet in text:
        words = []
        for word in tweet.split():
            words.append(word)

        lst.append(words)

    return lst

def term_dict(tweet_file):

    tweets = load_tweets(tweet_file) 
    text = tweet_text(tweets)
    tweets_words = tweet_words(text)

    # Dictionary for word counts
    word_dict = {}
    # Total word count
    tot = 0

    for tweet in tweets_words:
        for word in tweet:
            tot += 1
            word_dict[word] = word_dict[word] + 1 if word in word_dict.keys() else 1

    # Print the word, word frequency
    for word, count in word_dict.items():
        print "%s %f" % (word, float(count)/float(tot))

def main():

    tweet_file = open(sys.argv[1])
    term_dict(tweet_file)
    tweet_file.close()



if __name__ == '__main__':
    main()









