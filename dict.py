# Write code here
import pandas as pd
import time
df=pd.read_csv("ecdict.mini.csv")
time_start = time.time()
dictation={}
keys = ["phonetic","definition","translation","pos","collins","oxford","tag","bnc","frq","exchange","detail","audio"]
for values in df.values:
    content={}
    for key_i in range (11):
        key = keys[key_i]
        content[key] = values[key_i+1]
    dictation[values[0]] = content
time_end = time.time()
print("Dictionary construction delay: ",time_end-time_start,"s")
print(dictation['by pass'])

