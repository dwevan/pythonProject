# used guide https://gist.github.com/akashsenta13/bc23444d619c37dc0db62574f189ab7e#file-vader_sentiment_anlysis-ipynb

import nltk
import pandas as pd


nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()


df = pd.read_csv('CSV_files\Acad_med_colleges\RCPI_news_tweets at_2022-01-03.csv')
df.head()
print(df.head())

print(
  'number of tweets downloaded: ' +
  df['id'].count()
)

df.dropna(inplace=True)

sid.polarity_scores(df.iloc[0]['text'])

df['scores'] = df['text'].apply(lambda text:sid.polarity_scores(text))
df.head()
print(df.head())

df['compound'] = df['scores'].apply(lambda d:d['compound'])
df.head()
print(df.head())

df['score'] = df['compound'].apply(lambda score: 'pos' if score >=0 else 'neg')
df.head()
print(df.head())
