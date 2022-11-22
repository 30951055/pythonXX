'''
python批量操作文件
    查找文件
        os.path模块只能一层一层文件夹读取文件，需要写多个循环所以效率不高。
        Pathlib 可以实现任何深度的子文件夹搜索
            list(p.glob('**/*.xlsx'))   搜索所有文件夹中的xlsx文件
            list(p.glob('**/*~$*.xlsx'))    搜索所有文件夹中带有~$的xlsx文件。
            os.path.join(os.path.expanduser("~"), 'Desktop') + '/'  得到'C:\\Users\\当前用户名\\Desktop/'
    删除文件
        os.remove(文件名)
'''
import pandas as pd
import os
import re
import glob
from pathlib import Path

# os模块只能一层一层文件夹读取文件，需要写多个循环所以效率不高。
# dirPath = glob.iglob('D:\WORK\GIT\XX_Study_Base')
# for file in dirPath:
#     files = os.listdir(file)
#     print((files))

# Pathlib 可以实现任何深度的子文件夹搜索
# delPath = input('请输入你要删除~$文件的盘符：')
# p = Path(delPath)
# fileList = list(p.glob('**/*~$*.xlsx')) # 得到所有的xlsx文件
# for file2 in fileList:
#     print('找到了如下文件：\n',file2)
#     print('稍等，正在删除中...')
#     if os.remove(file2):
#         print('删除完毕')
#     else:
#         print('粗错啦。')


# 把搜索到的目标文件里面想要的内容提取出来
# 请将热搜数据文件夹保存至桌面
#如果执行失败说明Path路径手动设置为自己的桌面对应路径
# path = os.path.join(os.path.expanduser("~"), 'Desktop') + '/热搜数据/'
path = 'D:\\WORK\\temp\\临时Temp\\zaoqi-Python-master\\办公自动化系列\\批量处理文件\\热搜数据'
p = Path(path)  # 初始化构造Path对象

FileLists = list(p.glob("**/*.md"))  # 得到所有的markdown文件

filelist = list(filter(lambda x: str(x).find(
    "23点") >= 0, FileLists))  # 去重，每天保留一条数据

for file in filelist:
    with open(file,'r',encoding='UTF-8') as f:
        lines = f.readlines()
        lines = [i.strip() for i in lines]  # 去除空字符
        # list(filter(None, lines))  里面的None代表空列表，空字符或再数字上等于0的对象。list代表将处理的结果以一个列表呈现出来
        data = list(filter(None, lines))
        # 删除数组中第一个数据
        del data[0]
        data = data[0:100]
        # 通过正则表达式re来提取文件名中的“01月01日”（提取从字符’年‘到’2‘之间的内容）
        date = re.findall('年(.+)2', str(file))[0]
        # 从开始到结束，步长为2，相当于是取偶数行
        content = data[::2]  # 奇偶分割
        rank = data[1::2]
        # 提取内容与排名
        for i in range(len(content)):
            # 从content[i]中截取每条记录中’、‘顿号以后的内容
            content[i] = re.findall('、(.+)', content[i])[0]
        for j in range(len(rank)):
            # 从rank[j]中截取每条记录中空格以后的内容
            rank[j] = re.findall(' (.+)', rank[j])[0]

        dict = {'热搜': content,
                '热度': rank}
        dfTemp = pd.DataFrame(dict)
        # 在dfTemp中将date插入到最左边的时间列。(※如果时间列不存在，则自动新建一个时间列)
        dfTemp.insert(0, '时间', date)
        # 定义excel表格头部
        df = pd.DataFrame(columns=['热搜', '热度'])
        df = pd.concat([df,dfTemp])
# 把数据用“时间”来排序 ascending=True升序
df = df.sort_values(by="时间", ascending=True)
# 将自带的index设置为101~150,并替换原来的index
df = df.set_index(pd.Series(['101','102','103','104','105','106','107','108','109','110','111','112','113','114','115','116','117','118','119','120','121','122','123','124','125','126','127','128','129','130','131','132','133','134','135','136','137','138','139','140','141','142','143','144','145','146','147','148','149','150']), inplace=False)
# 将上述手动设置的index去掉并恢复自带的index
df = df.reset_index(drop=True)

df.to_excel('热搜数据.xlsx')
print('文件已生成')
