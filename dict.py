# Write code here
import pandas as pd
import time
df=pd.read_csv("ecdict.mini.csv")
time_start = time.time()
dictation={}
keys = ["phonetic","definition","translation","pos","collins","oxford","tag","bnc","frq","exchange","detail","audio"]
for values in df.values:
    dictation[values[0]]=values[1:]

    content={}
    for key_i in range (11):
        key = keys[key_i]
        content[key] = values[key_i+1]
    dictation[values[0]] = content
time_end = time.time()
print("Dictionary construction delay: ",time_end-time_start,"s")
print(dictation['by pass'])
print(dictation)
word=str(input())
dic_word=dictation.get(word)
if dic_word.any == None:
    print('error')
else:
    for i in range(len(dic_word)):
        if dic_word[i] != 'nan':
            print('%s:%s'%(df.keys()[i+1],dic_word[i]))

