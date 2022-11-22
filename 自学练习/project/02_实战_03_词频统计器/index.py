import jieba
from collections import Counter

import lambada as lambada


# 定义一个读取文件的方法
def read_file(path):
    with open(path,'r',encoding='UTF-8') as file:
        res = file.read()
    return res

txt = read_file('云南村民挖到5斤重的蘑菇.txt')

words = jieba.cut(txt)

# 列出要排除的垃圾字符
spam_list = ['，','。','的','了','就','\n','在',' ']


words_list = [word for word in words if word and word not in spam_list]
'''
words_list = [word for word in words if word and word not in spam_list]
相当于下面的代码：
words_list = []
for word in words:
    if word and word not in spam_list:
        words_list.append(word)
'''

# 统计个数
res = Counter(words_list)
print(res.items())
# sorted：排序 revese：从大到小排列（反转倒叙）
res = sorted(res.items(),key=lambda x:x[1],reverse=True)
'''
匿名函数lambda x:y[1]
相当于下面的代码：
    def temp(x):
        return y[1]
'''

# 取前五位
top_5 = res[:5]

print(top_5)
for word in top_5:
    print(f'{word[0]}的词频为：{word[1]/len(words_list)}')
