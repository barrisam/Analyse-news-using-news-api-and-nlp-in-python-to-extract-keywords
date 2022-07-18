pip install newsapi-python
pip install nltk

from newsapi import NewsApiClient
import pandas as pd
import nltk
nltk.download()
from nltk.tokenize import word_tokenize
#importing freqdist
from nltk.probability import FreqDist
from nltk.corpus import stopwords

# Init
newsapi = NewsApiClient(api_key='0ad145af97a64bf4ac3dbbc92334ecb7')

# /v2/everything
all_articles = newsapi.get_everything(q='tech',language='en', page_size=6)

#the data type for all_articles is a dict. We can find the keys using dict methods
print(all_articles.keys())
#dict_keys(['status', 'totalResults', 'articles'])

#this extracts the first five articles
article_text = all_articles['articles'][:6]
print(article_text)

# let's view this better with pandas
df = pd.DataFrame(article_text)
print(df)
# prints news in a tabular format

df.head(5)

#The column we need is the title. we will highlight it.
col = df['title']
text = col.to_string(index = False) #index = false removes the row number
print(text)


#we already have our text in the text variable. We just proceed to tokenize it
word_token = word_tokenize(text)
print(word_token)

#using freqdist to get the frequency of each word
new_text = FreqDist(word_token)

for countt in new_text:
    print(f"'{countt}' appears {new_text[countt]} times")
    
#to get the frequency of single word
print(new_text['Tech'])

# using .most_common() method to get the top 10 reoccurring words
wordcount_10 = new_text.most_common(10)
print(wordcount_10)

# to print the number of stop words
print(len(stopwords.words('english')))
#179

# removing stopwords
# specify the language
stop_words = (stopwords.words('English'))
filtered_text = []

for sw in word_token:
    if sw not in stop_words:
        filtered_text.append(sw)
        
print(filtered_text)

#using freqdist on the filtered text

text_content = FreqDist(filtered_text)
top_10 = text_content.most_common(10)
print(top_10)




