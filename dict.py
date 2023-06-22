# Write code here
import pandas as pd
import time

def dict1_build():
    time_start = time.time()
    df=pd.read_csv("ecdict.mini.csv")
    df.fillna('Nan',inplace=True)
    dictation={}
    keys = ["phonetic","definition","translation","pos","collins","oxford","tag","bnc","frq","exchange","detail","audio"]
    translation = {"phonetic":"音标", "definition":"单词释义（英文）", "translation":"单词释义（中文）", "pos":"词语位置", "collins":"柯林斯星级", "oxford":"是否是牛津三千核心词汇", "tag":"字符串标签", "bnc":"英国国家语料库词频顺序", "frq":"当代语料库词频顺序", "exchange":"时态复数等变换", "detail":"json 扩展信息", "audio":"读音音频 url"}
    for values in df.values:
        content={}
        for key_i in range (11):
            key = keys[key_i]
            content[key] = values[key_i+1]
        dictation[str(values[0])] = content
    time_end = time.time()
    delay = time_end-time_start
    return (delay,dictation)


# return the delay and the dictionary object
def dict1_search(dict,word):
    time_start = time.time()
    res = 'not found'
    for word_search in dict.keys():
        if word_search == word:
            res = dict[word]
    time_end = time.time()
    delay = time_end-time_start
    return (delay,res)


(delay_build,dictation) = dict1_build()
(delay_search,value) = dict1_search(dictation,'why not')
print(value)

#word=str(input())
#time_start = time.time()
#dic_word=dictation.get(word)
#time_end = time.time()
#check_time = time_end - time_start
#print('Word Finding time:',check_time,'s')
#if dic_word == None:
#    print('error')
#else:
#    for key in dic_word.keys():
#        if dic_word[key] != 'Nan':
#            print(translation[key],dic_word[key])
