# Write code here
import pandas as pd
import time
df=pd.read_csv("ecdict.mini.csv")
time_start = time.time()
df.fillna('Nan',inplace=True)
dictation={}
keys = ["phonetic","definition","translation","pos","collins","oxford","tag","bnc","frq","exchange","detail","audio"]
translation = {"phonetic":"单词名称", "definition":"单词释义（英文）", "translation":"单词释义（中文）", "pos":"词语位置", "collins":"柯林斯星级", "oxford":"是否是牛津三千核心词汇", "tag":"字符串标签", "bnc":"英国国家语料库词频顺序", "frq":"当代语料库词频顺序", "exchange":"时态复数等变换", "detail":"json 扩展信息", "audio":"读音音频 url"}
for values in df.values:
    content={}
    for key_i in range (11):
        key = keys[key_i]
        content[key] = values[key_i+1]
    dictation[values[0]] = content
time_end = time.time()
print("Dictionary construction delay: ",time_end-time_start,"s")
print(dictation)


word=str(input())
dic_word=dictation.get(word)
if dic_word == None:
    print('error')
else:
    for key in dic_word.keys():
        if dic_word[key] != 'Nan':
            print(translation[key],dic_word[key])
