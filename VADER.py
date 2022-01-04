# used guide https://gist.github.com/akashsenta13/bc23444d619c37dc0db62574f189ab7e#file-vader_sentiment_anlysis-ipynb

import nltk
import pandas as pd

#remove comment below to download lexicon - only needed first time
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

#enter path to file below
file = r'CSV_files\other_MDT_colleges\UKCP_Updates_tweets at_2022-01-03.csv'

df = pd.read_csv(file)
df.head()
print(
  'number of tweets downloaded: ' +
  str(df['id'].count())
)

df.dropna(inplace=True)

sid.polarity_scores(df.iloc[0]['text'])

df['scores'] = df['text'].apply(lambda text:sid.polarity_scores(text))
df.head()

#The compound score is computed by summing the valence scores of each word in the lexicon, adjusted according to the rules, and then normalized to be between -1 (most extreme negative) and +1 (most extreme positive). This is the most useful metric if you want a single unidimensional measure of sentiment for a given sentence. Calling it a 'normalized, weighted composite score' is accurate.
df['compound'] = df['scores'].apply(lambda d:d['compound'])
df.head()

#df['score'] = df['compound'].apply(lambda score: 'pos' if score >=0 else 'neg')
#df.head()

print(df.head())
df.to_csv(file, index=False)
print(df['compound'].mean())

#create account name for CSV - may need to be tweaked based on file structure (I know its not good syntax! it just works!)
account = file.replace('_tweets at_2022-01-03.csv','').replace('CSV_files\\','').replace('other_MDT_colleges\\','').replace('Acad_med_colleges\\','')

# write to csv (https://stackoverflow.com/questions/2363731/append-new-row-to-old-csv-file-python)
import csv

fields=[account,df['id'].count(),df['compound'].mean()]

with open(r'CSV_files\Scoring_files\MDTscores.csv', 'a', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(fields)

with open(r'CSV_files\Scoring_files\allscores.csv', 'a', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(fields)  
  
print(fields)
