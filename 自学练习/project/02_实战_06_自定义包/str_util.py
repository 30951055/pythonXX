"""
字符串相关得工具模块
"""


'''接受传入字符串，将字符串反转并返回'''
def str_reverse(str):
    return str[::-1]

'''按照下标x和y，对字符串进行切片'''
def substr(str,x,y):
    return str[x:y]


# 测试
if __name__ == '__main__':
    print(str_reverse('python你好'))
    print(substr('python你好',2,5))