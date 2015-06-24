
# coding: utf-8

# In[2]:

import dataiku
from dataiku import pandasutils as pdu
import pandas as pd


# In[1]:

## Example: load a DSS dataset as a Pandas dataframe
#mydataset = dataiku.Dataset("mydataset")
#mydataset_df = mydataset.get_dataframe()
#mydataset_df.head(10)


# In[3]:

## Example: audit a dataframe
#pdu.audit(mydataset_df)


# In[4]:

tweet='We have some delightful new food in the cafeteria. Awesome!!!'
print tweet


# In[5]:

positive_words=['awesome','good','nice','super','fun']


# In[6]:

positive_words.append('delightful')


# In[7]:

positive_words.append(like)


# In[8]:

print positive_words


# In[9]:

negative_words=['awful','lame','horrible','bad']
print negative_words


# In[10]:

emotional_words=negative_words+positive_words
print emotional_words


# In[11]:

words= tweet.split(' ')
print words


# In[12]:

len(words)


# In[13]:

len(tweet)


# In[14]:

for word in words:
    print word


# In[15]:

for word in words:
    if word in positive_words:
        print word


# In[16]:

for word in words:
    if word in positive_words:
        print word+'  is a positive word'


# In[17]:

tweet.lower()


# In[18]:

for word in words:
   print word.lower()


# In[19]:

for word in words:
   if word.lower() in positive_words:
       print word.lower()+' is a positive word'


# In[20]:

print tweet.replace('!','')


# In[21]:

tweet_noex=tweet.replace('!','')


# In[22]:

print tweet_noex


# In[23]:

tweet_processed=tweet.replace('!','').replace('.','')


# In[24]:

print tweet_processed


# In[25]:

tweet_processed=tweet_processed.lower()
words=tweet_processed.split(' ')
print words


# In[26]:

from string import punctuation
print punctuation


# In[27]:

tweet_processed=tweet.lower()


# In[28]:

for p in list(punctuation):
    tweet_processed=tweet_processed.replace(p,'')


# In[29]:

print tweet_processed


# In[30]:

for word in words:
   if word in positive_words:
       print word + ' is a positive word'


# In[31]:

positive_counter=0
tweet_processed=tweet.lower()
 for p in list(punctuation):
    tweet_processed=tweet_processed.replace(p,'')
print tweet_processed


# In[32]:

positive_counter=0
tweet_processed=tweet.lower()


# In[33]:

for p in list(punctuation):
   tweet_processed=tweet_processed.replace(p,'')


# In[34]:

print tweet_processed


# In[35]:

for word in words:
    if word in positive_words:
        print word+ ' is a positive word'
        positive_counter=positive_counter+1


# In[36]:

print positive_counter


# In[37]:

positive_counter/len(words)


# In[38]:

from __future__ import division


# In[39]:

positive_counter/len(words)


# In[40]:

import urllib


# In[41]:

url='http://www.unc.edu/~ncaren/haphazard/negative.txt'


# In[42]:

file_name='negative.txt'


# In[43]:

urllib.urlretrieve(url,file_name)


# In[44]:

urllib.urlretrieve('http://www.unc.edu/~ncaren/haphazard/negative.txt','negative.txt')


# In[45]:

files=['negative.txt','positive.txt','obama_tweets.txt']


# In[46]:

path='http://www.unc.edu/~ncaren/haphazard/'


# In[47]:

for file_name in files:
    urllib.urlretrieve(path+file_name,file_name)


# In[48]:

tweets = open("obama_tweets.txt").read()


# In[49]:

tweets_list = tweets.split('\n')


# In[50]:

len(tweets_list)


# In[51]:

for tweet in tweets_list[0:10]:
    print tweet


# In[52]:

print tweets_list[1:2]


# In[53]:

pos_sent = open("positive.txt").read()


# In[54]:

positive_words=pos_sent.split('\n')


# In[55]:

print positive_words[:10]


# In[56]:

for tweet in tweets_list:
    positive_counter=0
    tweet_processed=tweet.lower()
    for p in list(punctuation):
        tweet_processed=tweet_processed.replace(p,'')
        words=tweet_processed.split(' ')
    for word in words:
        if word in positive_words:
            print word
            positive_counter=positive_counter+1
    print positive_counter/len(words)


# In[57]:

from __future__ import division


# In[58]:

for tweet in tweets_list:
    positive_counter=0
    tweet_processed=tweet.lower()
    for p in list(punctuation):
        tweet_processed=tweet_processed.replace(p,'')
        words=tweet_processed.split(' ')
    for word in words:
        if word in positive_words:
            print word
            positive_counter=positive_counter+1
    print positive_counter/len(words)


# In[59]:

positive_counts=[]


# In[60]:

positive_counts.append(positive_counter/word_count)


# In[61]:

positive_counts.append(positive_counter/word.count)


# In[62]:

import csv


# In[63]:

writer = csv.writer(open('tweet_sentiment.csv', 'wb'))


# In[64]:

writer.writerows(positive_counts)


# In[65]:

output=zip(tweets_list,positive_counts)


# In[66]:

writer = csv.writer(open('tweet_sentiment.csv', 'wb'))
writer.writerows(output)


# In[ ]:




# In[ ]:



