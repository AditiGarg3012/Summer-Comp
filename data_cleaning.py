import pandas as pd
import numpy as np
# Change this path before running
file = '/Users/chenwang/Documents/GitHub/Summer-Comp/morganstanley.csv'
df=pd.read_csv(file,index_col=0)
# use TweetTokenizer to tokenise a Tweet Text
from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()

def tokenizer_tweets(df):
    
    text = ''
    for t in df['text']:
        text += str(t)
    tokens = [i.lower() for i in tknzr.tokenize(text)]
    
    return tokens

tokens = tokenizer_tweets(df)
print(len(tokens))
print(tokens[:20])
#import nltk
#nltk.download('stopwords')
# remove stop words and other noise(links and special characters) to get clear tokens
from nltk.corpus import stopwords
import string
punctiuation = list(string.punctuation)
stop = stopwords.words('english') + punctiuation
def clear_tokens(tokens):
    
    tokens_cl = [t for t in tokens if (len(t) >= 3) 
                 and (not t.startswith(('#', '@')))
                 and (not t.startswith('http'))
                 and (t not in stop)
                 and (t[0].isalpha())]
    
    return tokens_cl
tokens_cl = clear_tokens(tokens)
print(len(tokens_cl))
print(tokens_cl[:20])

# top 10 mentions
from nltk import FreqDist
mentions = [t for t in tokens if t.startswith('@')]
mentions_fd = FreqDist(mentions).most_common(10)
print(mentions_fd)
# top 10 hashtags
hashtags = [t for t in tokens if (t.startswith('#') and len(t) != 1)]
hashtags_fd = FreqDist(hashtags).most_common(10)
print(hashtags_fd)

# extract the mean of lenghts:
import numpy as np
mean = np.mean([len(str(i)) for i in df.text])
# The lenght's average in tweets. This needs to be fixed
print("The lenght's average in tweets: %.2f%%" % mean)

# extract the tweet with more FAVs and more RTs:
fav_max = np.max(df['favorites'])
rt_max  = np.max(df['retweets'])

fav = df[df.favorites == fav_max].index[0]
rt  = df[df.retweets == rt_max].index[0]
# Max FAVs:
print("The tweet with more likes is: \n{}".format(df['text'][fav]))
print("Number of likes: {}".format(fav_max))
print()
# Max RTs:
print("The tweet with more retweets is: \n{}".format(df['text'][rt]))
print("Number of retweets: {}".format(rt_max))

#wordcloud
listnew1 = []
for i in tokens_cl:
    listnew1.extend(i.lower().split(" "))
wordcloud = WordCloud(
        background_color="white", #set the background to white
        width=2500,              #set the width
        height=1500,              #set the height
        margin=10               #set the margin
        ).generate('\n'.join(listnew1))
# show the graph
plt.imshow(wordcloud)
plt.axis("off")
# show the picture
plt.show()
# save the picture
wordcloud.to_file('./wordcloud.png')  


