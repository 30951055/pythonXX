


f = open('D:\BaiduNetdiskWorkspace\PG_XX\python\教程资料\资料\可视化案例数据\动态柱状图数据\\1960-2019全球GDP数据.csv','r',encoding='EUC')
data_lines = f.readlines()
f.close()
# 删除第一条数据
data_lines.pop(0)
# 将数据转换成字典存储
data_dict = {}
for line in data_lines:
    year = int(lin)