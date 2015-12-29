import sys
import json
import operator

## State tuples
state_dict = {
    'alabama'                       :'al',
    'alaska'                        :'ak',
    'arizona'                       :'az',
    'arkansas'                      :'ar',
    'california'                    :'ca',
    'colorado'                      :'co',
    'connecticut'                   :'ct',
    'delaware'                      :'de',
    'florida'                       :'fl',
    'georgia'                       :'ga',
    'hawaii'                        :'hi',
    'idaho'                         :'id',
    'illinois'                      :'il',
    'indiana'                       :'in',
    'iowa'                          :'ia',
    'kansas'                        :'ks',
    'kentucky'                      :'ky',
    'lousiana'                      :'la',
    'maine'                         :'me',
    'maryland'                      :'md',
    'massachusetts'                 :'ma',
    'michigan'                      :'mi',
    'minnesota'                     :'mn',
    'mississippi'                   :'ms',
    'missouri'                      :'mo',
    'montana'                       :'mt',
    'nebraska'                      :'ne',
    'nevada'                        :'nv',
    'new hampshire'                 :'nh',
    'new jersey'                    :'nj',
    'new mexico'                    :'nm',
    'new york'                      :'ny',
    'north carolina'                :'nc',
    'north dakota'                  :'nd',
    'ohio'                          :'oh',
    'oklahoma'                      :'ok',
    'oregon'                        :'or',
    'pennsylvania'                  :'pa',
    'rhode island'                  :'ri',
    'south carolina'                :'sc',
    'south dakota'                  :'sd',
    'tennessee'                     :'tn',
    'texas'                         :'tx',
    'utah'                          :'ut',
    'vermont'                       :'vt',
    'virginia'                      :'va',
    'washington'                    :'wa',
    'west virginia'                 :'wv',
    'wisconsin'                     :'wi',
    'wyoming'                       :'wy',
    'american samoa'                :'as',
    'district of columbia'          :'dc',
    'federated states of micronesia':'fm',
    'guam'                          :'gu',
    'marshall islands'              :'mh',
    'northern mariana islands'      :'mp',
    'palau'                         :'pw',
    'puerto rico'                   :'pr',
    'virgin islands'                :'vi',
    'al':'al',
    'ak':'ak',
    'az':'az',
    'ar':'ar',
    'ca':'ca',
    'co':'co',
    'ct':'ct',
    'de':'de',
    'fl':'fl',
    'ga':'ga',
    'hi':'hi',
    'id':'id',
    'il':'il',
    'in':'in',
    'ia':'ia',
    'ks':'ks',
    'ky':'ky',
    'la':'la',
    'me':'me',
    'md':'md',
    'ma':'ma',
    'mi':'mi',
    'mn':'mn',
    'ms':'ms',
    'mo':'mo',
    'mt':'mt',
    'ne':'ne',
    'nv':'nv',
    'nh':'nh',
    'nj':'nj',
    'nm':'nm',
    'ny':'ny',
    'nc':'nc',
    'nd':'nd',
    'oh':'oh',
    'ok':'ok',
    'or':'or',
    'pa':'pa',
    'ri':'ri',
    'sc':'sc',
    'sd':'sd',
    'tn':'tn',
    'tx':'tx',
    'ut':'ut',
    'vt':'vt',
    'va':'va',
    'wa':'wa',
    'wv':'wv',
    'wi':'wi',
    'wy':'wy',
    'as':'as',
    'dc':'dc',
    'fm':'fm',
    'gu':'gu',
    'mh':'mh',
    'mp':'mp',
    'pw':'pw',
    'pr':'pr',
    'vi':'vi',
}

score_dict = {
    'al':[],
    'ak':[],
    'az':[],
    'ar':[],
    'ca':[],
    'co':[],
    'ct':[],
    'de':[],
    'fl':[],
    'ga':[],
    'hi':[],
    'id':[],
    'il':[],
    'in':[],
    'ia':[],
    'ks':[],
    'ky':[],
    'la':[],
    'me':[],
    'md':[],
    'ma':[],
    'mi':[],
    'mn':[],
    'ms':[],
    'mo':[],
    'mt':[],
    'ne':[],
    'nv':[],
    'nh':[],
    'nj':[],
    'nm':[],
    'ny':[],
    'nc':[],
    'nd':[],
    'oh':[],
    'ok':[],
    'or':[],
    'pa':[],
    'ri':[],
    'sc':[],
    'sd':[],
    'tn':[],
    'tx':[],
    'ut':[],
    'vt':[],
    'va':[],
    'wa':[],
    'wv':[],
    'wi':[],
    'wy':[],
    'as':[],
    'dc':[],
    'fm':[],
    'gu':[],
    'mh':[],
    'mp':[],
    'pw':[],
    'pr':[],
    'vi':[],
}
avg_score_dict = {
    'al':[],
    'ak':[],
    'az':[],
    'ar':[],
    'ca':[],
    'co':[],
    'ct':[],
    'de':[],
    'fl':[],
    'ga':[],
    'hi':[],
    'id':[],
    'il':[],
    'in':[],
    'ia':[],
    'ks':[],
    'ky':[],
    'la':[],
    'me':[],
    'md':[],
    'ma':[],
    'mi':[],
    'mn':[],
    'ms':[],
    'mo':[],
    'mt':[],
    'ne':[],
    'nv':[],
    'nh':[],
    'nj':[],
    'nm':[],
    'ny':[],
    'nc':[],
    'nd':[],
    'oh':[],
    'ok':[],
    'or':[],
    'pa':[],
    'ri':[],
    'sc':[],
    'sd':[],
    'tn':[],
    'tx':[],
    'ut':[],
    'vt':[],
    'va':[],
    'wa':[],
    'wv':[],
    'wi':[],
    'wy':[],
    'as':[],
    'dc':[],
    'fm':[],
    'gu':[],
    'mh':[],
    'mp':[],
    'pw':[],
    'pr':[],
    'vi':[],
}


## Load the tweets
def load_tweets(tweet_file):

    tweets = []
    line = tweet_file.readline()
    while line:
        tweet = json.loads(line.strip())
        tweets.append(tweet)
        line = tweet_file.readline()

    return tweets

## Get the tweet text + location for English tweets
def tweet_data(tweets):
    
    text_loc = []
    for tweet in tweets:
        if 'text' in tweet and 'user' in tweet and tweet['user']['lang'] == 'en':
                text_loc.append((tweet['text'], tweet['user']['location']))
        else: continue

    return text_loc

# Create (term, score) dictionary for word sentiment
def sent_dict(sent_file):

    scores = {}

    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    return scores

# Compute sentiment score for tweets and append score to score_dict
# for the appropriate state
def add_score(tweet_file, sent_file):

    tweets = load_tweets(tweet_file)
    text_loc = tweet_data(tweets)
    sent_words = sent_dict(sent_file)

    for text, loc in text_loc:

        # Parse only the tweets with state locations
        state_abb = None
        if loc is None: continue
        # Get rid of some background like "Find me" does not give the state 'ME'
        if not ',' in loc: continue
        for word in loc.lower().split():
            if word in state_dict.keys():
                state_abb = state_dict[word]
                break
        if state_abb is None: continue
        #print loc
        score = 0
        for word in text.split():
            if word in sent_words:
                score += sent_words[word]
        score_dict[state_abb].append(score)


def avg_scores(score_dict):
    for k,v in score_dict.iteritems():
        avg = sum(v)/float(len(v)) if v else 0
        avg_score_dict[k] = avg


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    add_score(tweet_file, sent_file)
    avg_scores(score_dict)
    happiest_state = max(avg_score_dict.iteritems(), key=operator.itemgetter(1))[0]
    #print score_dict
    #print avg_score_dict
    print happiest_state.upper()

    sent_file.close()
    tweet_file.close()
        
        

if __name__ == '__main__':
    main()