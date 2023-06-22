# Write code here
import pandas as pd
import time

test_dict = "ecdict.mini.csv"

def dict1_build():
    time_start = time.time()
    df=pd.read_csv(test_dict)
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
    res = {}
    for word_search in dict.keys():
        if word_search == word:
            res = dict[word]
            break
    time_end = time.time()
    delay = time_end-time_start
    return (delay,res)

def dict2_build():
    df=pd.read_csv(test_dict)
    df.fillna('Nan',inplace=True)
    nb = len(df.axes[0])
    hash_key = {}
    keys = ["phonetic","definition","translation","pos","collins","oxford","tag","bnc","frq","exchange","detail","audio"]
    translation = {"phonetic":"音标", "definition":"单词释义（英文）", "translation":"单词释义（中文）", "pos":"词语位置", "collins":"柯林斯星级", "oxford":"是否是牛津三千核心词汇", "tag":"字符串标签", "bnc":"英国国家语料库词频顺序", "frq":"当代语料库词频顺序", "exchange":"时态复数等变换", "detail":"json 扩展信息", "audio":"读音音频 url"}
    time_start = time.time()
    for i in range(nb):
        word = df['word'][i]
        hash_value = calculate_hash(word)
        if hash_value in hash_key.keys():
            hash_key[hash_value].append((word,i))
        else:
            hash_key[hash_value]=[(word,i)]
    
    hash_key = dict(sorted(hash_key.items(), key=lambda x: x[0]))
    time_end = time.time()
    return (time_end-time_start,hash_key)

def dict2_search(hash_key,word):
    df=pd.read_csv(test_dict)
    df.fillna('Nan',inplace=True)
    content={}
    keys = ["phonetic","definition","translation","pos","collins","oxford","tag","bnc","frq","exchange","detail","audio"]
    target = -1
    time_start = time.time()
    hash = calculate_hash(word)
    for key in hash_key.keys():
        if key == hash:
            buffer_list = hash_key[key]
            for w,index in buffer_list:
                if w==word:
                    target = index
                    break
    time_end = time.time()
    if target != -1:
        for key in range(11):
            content[keys[key]]=df[keys[key]][target]
    return (time_end-time_start,content)

def calculate_hash(word):
    res = 0
    for i in word:
        if i.isalpha():
            res+=ord(i)
            res*=ord(i)
    return res%1024

(delay_build,dictation) = dict1_build()
(delay_search,value) = dict1_search(dictation,'why not')
print(value)
(time_delay,hash_key) = dict2_build()
print(dict2_search(hash_key,"why not"))

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
