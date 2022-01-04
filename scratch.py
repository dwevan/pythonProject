file = r'CSV_files\other_MDT_colleges\UKCP_Updates_tweets at_2022-01-03.csv'

account = file.replace('_tweets at_2022-01-03.csv','').replace('CSV_files\\','').replace('other_MDT_colleges\\','').replace('Acad_med_colleges\\','')
  
print(account +' test')