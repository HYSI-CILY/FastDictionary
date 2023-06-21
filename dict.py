# Write code here
import pandas as pd
df=pd.read_csv("ecdict.mini.csv")
dictation={}
for values in df.values:
    dictation[values[0]]=values[1:]
print(dictation)
word=str(input())
dic_word=dictation.get(word)
if dic_word.any == None:
    print('error')
else:
    for i in range(len(dic_word)):
        if dic_word[i] != 'nan':
            print('%s:%s'%(df.keys()[i+1],dic_word[i]))


