# while True:
#     str = input('用户::')
#     print('机器人::'+str.strip('吗？')+'!')

# 定义一个读取文件的方法
def read_file(path):
    with open(path,'r',encoding='UTF-8') as file:
        res = file.read()
    return res
txt = read_file('酱油妹词库.txt')
# print(txt)
# replaceResult = txt.replace('\n\n\n','\n\n').replace('\n\n','\'","').replace('\n','":"\'')\
#     .replace('":"":"','","').replace('{','{"').replace('，',' ').replace('？','  ').replace('""','","').replace('！',' ')\
#     .replace('。',' ')
pinchuan = '{'+ txt + '}'
# print(pinchuan)
pinchuanResult = eval(pinchuan)
# splitResult = txt.split(':')
# dictResult = dict(txt)
# print(type(pinchuan))

my_set = {'你说啥？','你说什么我不懂啊','真心不懂','不明白啊','请换个词好吗？','能说一下其他的话题吗？'}

while True:
    str = input('用户::')
    # 完全匹配
    if str not in pinchuanResult:
        popResult = my_set.pop()
        print(popResult)
        my_set.add(popResult)
    else:
        print('酱油妹::'+pinchuanResult[str])

