'''
pandas比openpy更高级，但需要依赖于xlrd和xlwt，所以要先安装这两个东西。
Series和DataFrame之间的关系
    Series+Series=DataFrame
'''
import pandas as pd
# 初步认识pandas 创建三条记录：张三，李四，王五。相当于三道挂面的感觉。为其添加indexNo，然后命名该列为A列
s1 = pd.Series(['张三','李四','王五'],index=[1,2,3],name='A')
print(s1)
print(s1.index)
print(s1.name)
print(s1[1])

# list和字典的两种不同的效果
s2 = pd.Series(['张三',20,'唱歌','广东'],index=[1,2,3,4],name='A')
s3 = pd.Series(['李四',25,'跳舞','上海'],index=[1,2,3,4],name='B')
s4 = pd.Series(['王五',29,'游泳','北京'],index=[1,2,3,4],name='C')
# 如果想让其一行行地插入，就可以用list的方式。
df1 = pd.DataFrame([s2,s3,s4])
print(df1)
# 如果想要以列的方式插入，就可以用字典的方式。把name作为key，它本身作为value，就可以形成Excel的样式
df2 = pd.DataFrame({
    s2.name:s2,
    s3.name:s3,
    s4.name:s4
})
print(df2)


# 除了上述两种定义的方式，还有更简单的，直接用字典的方式即可。
df3 = pd.DataFrame({
    'id':[1,2,3],
    'name':['张三','李四','王五'],
    'age':[30,29,27],
})
print(df3)
print('----------------')
# 自定义df3.id为id，这样可以去掉pandas自带的index
df3 = df3.set_index('id')
print(df3)
# 写出到xlsx文件中。
# df3.to_excel('temp.xlsx')
print('写出到excel完成了。')


'''
 花样读取现存excel表格
'''
# 全部读取,且自带index（0,1,2,...）
rdAll = pd.read_excel('temp.xlsx')
print(rdAll)
print('-------------')
'''
# 自定义读取1 全般读取
    header=2    从第3行开始读取
    sheet_name='sheet1' 指定读取sheet1
'''
rd1 = pd.read_excel('temp.xlsx',header=2,sheet_name='Sheet1')
print(rd1)
'''
# 自定义读取2 自定义标题读取
    header=None    把标题行空出来（无标题）
    sheet_name='sheet1' 指定读取sheet1
'''
rd2 = pd.read_excel('temp.xlsx',header=None,sheet_name='Sheet1')
# 自定义标题
rd2.columns = ['ID','名字','年龄']
print(rd2)
print('指定的表列名是：',rd2.columns)
'''
# 自定义读取3 指定id列为索引（去掉默认索引）
    header=None    把标题行空出来（无标题）
    index_col='id' 指定id为索引index
'''
rd3 = pd.read_excel('temp.xlsx',index_col='id')
# 自定义标题
print(rd3)
# print('指定的表头是：',rd3.head())
print(rd3.head())
'''
# 自定义读取4 多项设置读取
    skiprows=2    跳过2行，从第3行开始读取
    usecols=[0,1] 只读取A~B列
    dtype={}    为各个字段的内容设置数据类型
'''
rd4 = pd.read_excel('temp.xlsx',skiprows=2,usecols=[0,1],
                    dtype={
                        'ID':str,
                        'gender':str,
                        'birthday':str,
                    })
print(rd4)
