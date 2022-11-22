'''
xlrd读取Excel文件数据
    该工具只对xls有效，对xlsx不支持。
    选择工作表 有三种方式
        book_1.sheets()[0]
        book_1.sheet_by_index(0)
        book_1.sheet_by_name('Sheet1')
    选择cell要点：
        sheet.cell(行，列)，如：
            sheet.cell(1,0) 代表A2
            sheet.cell(0,1) 代表B1
'''
import xlrd
import xlutils.copy
import xlwt as xlwt

# 读入已存在的xlsx文件
book_1 = xlrd.open_workbook('people1.xls')
# 选择工作表 的三种方式 推荐第三种sheet_13方式，因为sheet即便改变了顺序，但通过名字还是能精确找到
sheet_11 = book_1.sheets()[0]
sheet_12 = book_1.sheet_by_index(0)
sheet_13 = book_1.sheet_by_name('Sheet1')
# 选择cell sheet_11.cell(row,col) A2cell
# 读入后的结果查看
print('用xlrd读入后的结果是：',xlrd.open_workbook('people1.xls').sheets()[0].cell(1,0))


'''
xlwt将数据写入Excel文件
    缺点：只能写入xls文件，写入xlsx文件的话是无法打开的。
        如果要解决这个问题，需要用到openpyxl 见02_04_02_用openpyxl操作表格.py
'''
# 创建xls文件对象 注意：这是xls，不是xlsx
book_2 = xlwt.Workbook()
# 新建工作表
sheet_21 = book_2.add_sheet('Sheet1')
# 写入数据
sheet_21.write(1,0,'张三')
# 保存为xls文件
book_2.save('temp.xls')
# 写入后的结果查看
print('用xlwt写入后的结果是：',xlrd.open_workbook('temp.xls').sheets()[0].cell(1,0))


'''
xlutils复制Excel文件
    用xlutils变相地实现直接修改工作表中已有的数据
    思路：将xlrd所属对象转为xlwt所属对象，从而实现直接修改工作表中已有数据的目的
'''
wb = xlrd.open_workbook('people1.xls')
nwb = xlutils.copy.copy(wb)
ws1 = nwb.get_sheet(0)
# ws2 = nwb.get_sheet('sheet1')
# ws3 = nwb.add_sheet('sheet2')
ws3 = ws1.write(1,0,'老张')
nwb.save('people1.xls')
# 修改后的结果查看
print('用xlutils复制并修改后的结果是：',xlrd.open_workbook('people1.xls').sheets()[0].cell(1,0))
