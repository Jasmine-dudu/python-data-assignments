import csv
import codecs

source = open('filelist.txt','r')   #读文件列表

all_articles = []
for text in source.readlines():
    f = codecs.open(text.split('\n',1)[0], 'r','utf-8')
    file = f.read()
    f.close()
    all_articles.append(file)
all_words = []
for i in range(5):
    words = all_articles[i].split()
    for all_word in words:
        all_words.append(all_word)

fileset = set(all_words)
se = {'a', 'the', 'and', 'in', 'of'}    #去停用词
fileset = fileset - se
filedict = {}  # 创建一个空字典，用于存储
for word in fileset:
    filedict[word] = all_words.count(word)
wordlist = list(filedict.items())
wordlist.sort(key=lambda x: x[1], reverse=True)

for i in range(15):
    print(wordlist[i])

with open('count_words.csv','w')as f:
    mywriter =csv.writer(f)
    header = ['word','frequency']
    mywriter.writerow(header)
    mywriter.writerows(wordlist)