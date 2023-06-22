import tkinter as tk
from dict import dict1_build,dict1_search

translation = {"phonetic":"音标", "definition":"单词释义（英文）", "translation":"单词释义（中文）", "pos":"词语位置", "collins":"柯林斯星级", "oxford":"是否是牛津三千核心词汇", "tag":"字符串标签", "bnc":"英国国家语料库词频顺序", "frq":"当代语料库词频顺序", "exchange":"时态复数等变换", "detail":"json 扩展信息", "audio":"读音音频 url"}

def mapSearch():
    (delay_build,dictation) = dict1_build()

    building_delay = "Dictionary built in "+str(delay_build)+"s"
    dictionary_build_time_label.config(text=building_delay)

    B.config(command=lambda: searchHandler(dictation))

def hashSearch():
    return 0

def searchHandler(dictionary):
    word = str(entry.get())
    (delay2,value) = dict1_search(dictionary,word)
    search_time = "Word searching in "+str(delay2)+"s"
     
    # configure
    searching_delay_label.config(text = search_time)
    meaning_label.config(text = translation['translation']+ ": "+ value['translation'])
    phonetic_label.config(text = translation['phonetic']+": "+ value['phonetic'])

window = tk.Tk()
window.geometry("500x200")

choice_dictionary = tk.IntVar()
choice_dictionary.set(0) # initialiser
r1 = tk.Radiobutton(window, text="Map", variable=choice_dictionary, value=1,command=mapSearch)
r1.pack(anchor = tk.W)
r2 = tk.Radiobutton(window, text="Hashmap", variable=choice_dictionary, value=2,command=hashSearch)
r2.pack(anchor = tk.W)

dictionary_build_time_label = tk.Label()
dictionary_build_time_label.pack()

entry = tk.Entry(width=50)
entry.pack()

B = tk.Button(window, text ="search")
B.pack()

searching_delay_label = tk.Label()
searching_delay_label.pack()

meaning_label = tk.Label()
meaning_label.pack()

phonetic_label = tk.Label()
phonetic_label.pack()

window.mainloop()