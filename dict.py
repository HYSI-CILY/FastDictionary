# Write code here
import pandas as pd
df=pd.read_csv("ecdict.mini.csv")
dictation={}
for values in df.values:
    dictation[values[0]]=values[1:]
print(dictation['by pass'])

