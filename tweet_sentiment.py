import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

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

# Create (term, score) dictionary for word sentiment
def sent_dict(sent_file):
    #afinnfile = open(sent_file)
    scores = {}
    #for line in afinnfile:
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    return scores

# Split tweets by words
def tweet_words(text):
    lst = []
    for tweet in text:
        words = []
        for word in tweet.split():
            words.append(word)

        lst.append(words)

    return lst

# Sum the sentiment scores
def sent_scores(tweet_file, sent_file):
    tweets = load_tweets(tweet_file)
    text = tweet_text(tweets)
    tweets_words = tweet_words(text)
    sent_words = sent_dict(sent_file)

    #scores = []

    for tweet in tweets_words:
        sum = 0
        for word in tweet:
            if word in sent_words:
                sum += sent_words[word]
        #scores.append(sum)
        print sum


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    
    sent_scores(tweet_file, sent_file)


    sent_file.close()
    tweet_file.close()
        
        

if __name__ == '__main__':
    main()
