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

    scores = {}

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

# Derive sentiment scores for non-sentiment-carrying words
# Reference: http://www.cs.cmu.edu/~nasmith/papers/oconnor+balasubramanyan+routledge+smith.icwsm10.pdf
def nonsent_scores(tweet_file, sent_file):
    tweets = load_tweets(tweet_file)
    text = tweet_text(tweets)
    tweets_words = tweet_words(text)
    sent_words = sent_dict(sent_file)

	# Dictionary for nonsent words + sent score, e.g. {word: 153.5}
    nonsent_dict = {}

    for tweet in tweets_words:

        pos = 0
        neg = 0
        nonsent_words = []
        for word in tweet:
            if word in sent_words:
                if sent_words[word] > 0: pos += 1
                if sent_words[word] < 0: neg += 1
            else:
                nonsent_words.append(word)

        if neg != 0:
            pos_neg = float(pos)/float(neg)
        else: 
            pos_neg = pos


        for word in nonsent_words:
            nonsent_dict[word] = nonsent_dict[word] + pos_neg if word in nonsent_dict.keys() else pos_neg

    #print "="*80
    for word, score in nonsent_dict.items():
        print "%s %s" % (word, score)


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    nonsent_scores(tweet_file, sent_file)

    sent_file.close()
    tweet_file.close()
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
