# 数据类型
    # print(666)
    # print(12.13)
    # print('我来啦')

    # 测试：
        # 余额 = 50
        # 冰激凌 = 10
        # 可乐 = 5
        # print('当前钱包余额：',余额)
        # print('购买了冰激淋，花费：',冰激凌)
        # print('购买了可乐，花费：',可乐*2)
        # print('最终，钱包剩余：',余额-冰激凌-可乐*2)

        # 数据类型 = type('hello')
        # print(数据类型)

# 数据类型转换
        # print(int(123.23))
        # print(float('123'))
        # print(str(456.1234))

"""
标识符（变量）命名规则：
    内容限定
        只允许出现 英文，中文，数字(不能用于开头)，下划线 这四类
    区分大小写
    不可使用关键字（共有下面等35个）
        例外：如果大小写跟关键字不一致的话不算违规。
        True	布尔类型，表示真
        False	布尔类型，表示否
        def		函数定义
        if		逻辑中的如果
        elif	逻辑中的或者如果
        else	逻辑中的否则
        try		异常语句的开启
        is		判断变量是否是某个类的实例
        not		逻辑运算，非的操作
        or		逻辑运算，或的操作
        pass	无意义，站位字符
        raise	主动抛出异常
        in		判断变量是否在序列中
        while	While循环语句
        with	简化python语句
        yield	从循环或函数依次返回数据
        import	导入语句，可与from共用
"""
import time

"""
运算符
    算术运算符
    +	加 - 两个对象相加	                10 + 20 输出结果 30
    -	减 - 得到负数或是一个数减去另一个数	30 - 40 输出结果 -10
    *	乘 - 两个数相乘或是返回一个被重复若干次的字符串	100 * 2 输出结果 200
    /	除 - x除以y	                    4 / 2 输出结果 2.0
    %	取模 - 返回除法的余数	            9 % 2 输出结果 1
    **	幂 - 返回x的y次幂	                2**2 为2的2次方， 输出结果 4
    //	取整除 - 返回商的整数部分（向下取整）	
                                        >>> 9//2
                                        4
                                        >>> -9//2
                                        -5
                                        >>> 11//2
                                        5
    赋值运算符：=
    复合赋值运算符：
        以下假设变量a为10，变量b为20：
            =	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
            +=	加法赋值运算符	c += a 等效于 c = c + a
            -=	减法赋值运算符	c -= a 等效于 c = c - a
            *=	乘法赋值运算符	c *= a 等效于 c = c * a
            /=	除法赋值运算符	c /= a 等效于 c = c / a
            %=	取模赋值运算符	c %= a 等效于 c = c % a
            **=	幂赋值运算符	    c **= a 等效于 c = c ** a
            //=	取整除赋值运算符	c //= a 等效于 c = c // a
"""

# 关于print的换行
    # print('我会自动换行\n，对吧。')
    # print('我们会在一行内显示',end='')
    # print('不信你就看',end='')

# 字符串格式化，实现字符拼接之 1
    # 好处：要注意区别类型，要做精度控制
        # a = 1
        # b = 2
        # beijingGongzi = 20000
        # shanghaiGongzi = 19000
        # print('我'+'是'+'中国人')
       # print('我'+'是'+a+'中国人')
        # print('我'+'是 %s' % a+'中国人')
        # print('python大数据学科，北京平均工资%s元，上海平均工资%s元。' % (beijingGongzi,shanghaiGongzi))
        # name = '传智播客'
        # year = 2006
        # stock_price = 19.99
        # print('%s,成立于：%d,今天的股价是:%f' % (name,year,stock_price))
        # 精度控制   m.n的形式控制
        # num1 = 1234567
        # num2 = 123.456789
        # print('数字12345宽度限制为5，结果是：%5d' % num1)
        # print('数字12345宽度限制为2，结果是：%2d' % num1)
        # 如果m小于整数的位数不生效，反之则以空格补齐。
        # print('数字123.456789宽度限制为10，小数精度3，结果是：%10.3f' % num2)
        # print('数字123.456789宽度限制为2，小数精度3，结果是：%2.3f' % num2)
        # print('数字123.456789宽度不限制，小数精度2，结果是：%.2f' % num2)
# 字符串格式化，实现字符串拼接之 2（优雅写法）
    # 好处：不理会类型，不做精度控制
        # name = '传智播客'
        # year = 2006
        # stock_price = 39.10
        # print(f'我是{name},成立于{year}年，今天的股价是：{stock_price}')
# 表达式的格式化
    # print('2*2的结果是：%d' % (2*2))
    # print(f'3*2的结果是：{3*2}')
    # print('字符串在python中的类型名是：%s' % type('呃呃'))
# 关于格式化的练习题
    # name = '传播止咳'
    # stock_price = 19.99 #股票价格
    # stock_code = '003032' #股票号码
    # stock_price_daily_growth_factor = 1.2 #增长系数
    # growth_days = 7 #增长天数
    # print(f'公司：{name},股票代码：{stock_code},当前股价：{stock_price}')
    # print('每日增长系数是：%s,经过%d天的增长后,股价达到了：%.2f'
    #       %(stock_price_daily_growth_factor,growth_days,stock_price*stock_price_daily_growth_factor**growth_days))

# input语句
    # print('请告诉我你是谁？')
    # name = input()
    # print(f'我知道了，你是{name}')
    # sex = input('告诉我你的性别：')
    # print(f'噢噢，你的性别是{sex}')
    # mima = input('请输入你的银行卡密码：')
    # print(f'晓得了，你的密码是：{int(mima)}')

    # user_name = input('请输入你的姓名：')
    # user_type = input('你是用户类型是：')
    # print(f'你好：{user_name},你是尊贵的{user_type}用户，欢迎你的光临')

# if语句
    # age = input('欢迎来到黑马儿童游乐场，儿童免费，成人收费。\n请输入你的年龄：')
    # if (int(age) >= 30):
    #     print('您已成年，游玩需要补票10元')
    # print('祝您游玩愉快')

# if else 语句
    # shengao = int(input('欢迎来到黑马动物园。\n请输入你的身高：'))
    # if shengao >= 120:
    #     print('你的身高超出120cm，游玩需要购票10元')
    # else:
    #     print('你的身高未超出120cm，可以免费游玩。')
    # print('祝您游玩愉快。')

# 练习题 猜数字 初级版
    # num = 10
    # if int(input('请输入一个数字，看看是不是我想的数字：')) == num:
    #     print('恭喜你一次就答对了。')
    # elif int(input('不对，请再猜一次：')) == num:
    #     print('恭喜你答对啦。我猜想的数字正是 10.')
    # elif int(input('不对，再猜最后一次：')) == num:
    #     print(f'最后一次机会答对啦。我猜想的数字正是 {num}.')
    # else:
    #     print(f'sorry,全部猜错啦，我想的数字是：{num}')

# 练习题 猜数字 中级版
    # 取随机数
    # import random
    # num = random.randint(1,10)
    # guess_num = int(input('输入你要猜的数字：'))
    # if guess_num == num:
    #     print('恭喜你第一次就猜对了')
    # else:
    #     if guess_num < num:
    #         print('小了')
    #     else:
    #         print('大了')
    #     guess_num = int(input('再次输入你要猜的数字：'))
    #     if guess_num == num:
    #         print('恭喜你第二次就猜对了')
    #     if guess_num > num:
    #         print('大了')
    #     else:
    #         print('小了')
    #     guess_num = int(input('最后一次输入你要猜的数字：'))
    #     if guess_num == num:
    #         print('恭喜你第三次就猜对了')
    #     if guess_num > num:
    #         print('大了')
    #     else:
    #         print('小了')
    #     print('三次机会已经用完啦。')

# while循环
    # 循环某一个东西10次
    # i = 0
    # while i < 10:
    #     print(f'第{i+1}次说，小妹我喜欢你。')
    #     i += 1

    # 求1-100的和
    # sum = 0
    # j = 1
    # while j <= 100:
    #     sum += j
    #     j = j+1
    # print('从1加到100的总和是：',sum)

    # 求1-366的和
    # sum = 0
    # j = 1
    # while j <= 366:
    #     sum += j
    #     j = j+1
    # print('从1加到366的总和是：',sum)

# 猜数字 高级版
    # count = 0
    # import random
    # num = random.randint(1,100)
    # flag = True
    # while flag:
    #     guess_num = int(input('请输入要猜的数字：'))
    #     count += 1
    #     if guess_num == num:
    #         print(f'恭喜你答对了。\n你总共猜了{count}次')
    #         flag = False
    #     else:
    #         if guess_num < num:
    #             print('小了')
    #         else:
    #             print('大了')

# 循环嵌套
    # i = 1
    # while i <= 100:
    #     print(f'今天是第{i}天，准备表白...')
    #     j = 1
    #     while j <= 3:
    #         print(f'送给小美第{j}朵玫瑰花')
    #         j += 1
    #     print('小美，我喜欢你')
    #     i += 1
    # print(f'坚持到了第{i}天，表白成功。')

"""
循环嵌套之 九九乘法表
i是竖着的1-9，j是横着的1-9
"""
    # i = 1
    # while i <= 9:
    #     j = 1
    #     while j <= i:
    #         print(f'{j}*{i}={j*i}\t',end='')
    #         j += 1
    #     i += 1
    #     print() #换行

# for循环 遍历
    # count = 0
    # for xunhuan in 'itheima is a brand of itcast':
    #     if xunhuan == 'a':
    #         count += 1
    # print(f'"itheima is a brand of itcast"文字段中有{count}个“a”')

"""
 range语句
    range(5)    #数字序列   包头不包尾
        表示从0-4
    range(5,10)   #数字序列   包头不包尾
        表示从5-9
    range(5,10,2)   #等差数列   起始，结束，步长
        表示从5到10间隔2位取数字：5,7,9
"""
    # for x in range(-5,5):
    #     print(x)

    # 求1-100中共有多少个偶数（不包括100本身）
    # count = 0
    # for y in range(1,100):
    #     if y %2 == 0:
    #         count += 1
    # print(f'从1到100之中共有{count}个偶数')

# for循环 九九乘法表
    # for i in range(1,10):
    #     for j in range(1,i+1):
    #         print(f'{j}×{i}={i*j} \t',end='')
    #     print()

# 上述基础学习之后的综合案例练习
    # import random
    # monney = 10000
    # for x in range(1,21):
    #     y = random.randint(1,10)
    #     if (y < 5):
    #         print(f'第{x}位员工的绩效分是{y},不合格，没有工资，下一位')
    #         continue
    #     elif (y >= 5):
    #         monney -= 1000
    #         print(f'第{x}位员工的绩效分是{y},合格，领取工资1000元。公司账户余额还剩：{monney}')
    #         if (monney == 0):
    #             print('工资发完了，下月再来吧。')
    #             break

# 函数
    # def jiankangma (param):
    #     print('欢迎。\n请测量体温！')
    #     if param <= 37.2:
    #         print(f'你的体温是{param}度，体温正常，请进')
    #     else:
    #         print(f'你的体温是{param}度，需要隔离！')
    #
    # 调用jiankangma函数
    # import random
    # jiankangma(random.randint(35.0,43.0))
    # jiankangma(round(random.uniform(35,43),1))


# 全局变量 global
    # num= 5
    # global num  # 在需要使用num的地方设置num为全局变量

# 综合案例 模拟银行ATM v0.1
     # moneyTotal = 500000
     # def infomation():
     #      info = ''
     #      info += '\n -------黑马ATM-------\n'
     #      info += ' 查询余额\t【1】\n'
     #      info += ' 存款\t\t【2】\n'
     #      info += ' 取款\t\t【3】\n'
     #      info += ' 退出\t\t【4】\n'
     #      return info
     #
     # def cunQian():
     #      print('存钱业务')
     #      inputMoney = input('请输入你要存入的金额：')
     #      global moneyTotal
     #      moneyTotal += int(inputMoney)
     #      print(f'你的账户当前余额为{moneyTotal}元。欢迎下次光临！')
     # def quQian():
     #      print('取钱业务')
     #      inputMoney = input('请输入你要取出的金额：')
     #      global moneyTotal
     #      moneyTotal -= int(inputMoney)
     #      print(f'你的账户当前余额为{moneyTotal}元。欢迎下次光临！')
     # def chaYuE():
     #      print('查询余额业务')
     #      return f'你的账户余额为{moneyTotal}元。欢迎下次光临！'
     #
     # def main():
     #      xingming = input('请输入你的姓名：')
     #      info = infomation()
     #      print(f'欢迎{xingming}的到来。{info}')
     #      inputShuzi = input('请输入你要操作业务的数字：')
     #      return  inputShuzi
     # while True:
     #      num = main()
     #      if num == '1':
     #           print(chaYuE())
     #      elif num == '2':
     #           cunQian()
     #      elif num == '3':
     #           quQian()
     #      else:
     #           break


# 综合案例 模拟银行ATM v0.2
     # moneyTotal = 500000
     # name = None
     # name = input('请输入你的姓名：')
     # def infomation():
     #      info = ''
     #      info += '\n -------黑马ATM-------\n'
     #      info += ' 查询余额\t【1】\n'
     #      info += ' 存款\t\t【2】\n'
     #      info += ' 取款\t\t【3】\n'
     #      info += ' 退出\t\t【4】\n'
     #      return info
     # def cunQian():
     #      print('存钱业务')
     #      inputMoney = input('请输入你要存入的金额：')
     #      global moneyTotal
     #      moneyTotal += int(inputMoney)
     #      chaYuE(False)
     # def quQian():
     #      print('取钱业务')
     #      inputMoney = input('请输入你要取出的金额：')
     #      global moneyTotal
     #      moneyTotal -= int(inputMoney)
     #      chaYuE(False)
     #      print(f'你的账户当前余额为{moneyTotal}元。')
     # def chaYuE(showHeader):
     #      if showHeader:
     #           print('------查询余额------')
     #      print( f'你的账户当前余额为{moneyTotal}元。')
     # def main():
     #      info = infomation()
     #      global name
     #      print(f'欢迎{name}的到来。{info}')
     #      inputShuzi = input('请输入你要操作业务的数字：')
     #      return  inputShuzi
     # while True:
     #      num = main()
     #      if num == '1':
     #           chaYuE(True)
     #           continue
     #      elif num == '2':
     #           cunQian()
     #           continue
     #      elif num == '3':
     #           quQian()
     #           continue
     #      else:
     #           print('欢迎下次光临。')
     #           break


"""
数据容器 共5类
     列表list（类似数组）
          以 [] 作为标识，每一个元素之间用逗号隔开
               # 查找
                    myList = ['张三', '李四', '王五']
                    # 查找元素的位置      1
                    myList.index('李四')
               # 追加元素
                    myList = ['张三','李四','王五']
                    # 修改指定下标的元素内容    ['老王','李四','王五']
                    myList[0] = '老王'
                    # 插入新元素到指定位置    ['老王','赵六','李四','王五']
                    myList.insert(1,'赵六')
                    # 在数组末尾新追加单个元素    ['老王','赵六','李四','王五','田七']
                    myList.append('田七')
                    # 在数组末尾新追加批量元素    ['老王','赵六','李四','王五','田七','小美','小娟','小丽']
                    myList.extend(['小美','小娟','小丽'])
               # 删除元素
                    myList = ['张三', '李四', '王五']
                    # 删除指定下标的元素    ['张三', '李四']
                    del myList[2]
                    # 从数组里面取出指定下标元素     ['张三', '王五']
                    element = myList.pop(1)
                    # 从数组里面直接删除元素  ['李四', '王五']
                    myList.remove('张三')
                    # 清空整个列表  []
                    myList.clear()
               # 统计
                    myList = ['张三', '李四', '王五','张三']
                    # 统计数组里面的元素个数  2
                    count = myList.count('张三')
                    # 统计该数组的元素总数量  4
                    count = len(myList)
                    
     元组
          用 () 标识,单个或者多个元素都要用逗号分割，且不可被修改
          注意1：即便是单个元素，也必须要在末尾加上逗号，不然不会被判定为元组。如：
               temp1 = ('hello')   #非元组
               temp2 = ('hello',)  #元组
          注意2：虽然元组里面的元素不可修改，但元组里面嵌套的list是可以修改的。
    字符串
    集合
    字典
          
"""
# 基础练习
     # myList = [21,25,21,23,22,20]
     # myList.append(31)
     # print('myList.append(31)后的结果是：',myList)
     # myList.extend([29,33,30])
     # print('myList.extend([29,33,30])后的结果是：',myList)
     # handle = myList.pop(0)
     # print('handle = myList.pop(0)后的结果是：',handle)
     # handle2 = myList.pop(-1)
     # print('handle2 = myList.pop(-1)后的结果是：',handle2)
     # index = myList.index(31)
     # print('myList.index("31")后的结果是：',index)

# while循环取出列表内的偶数
     # myList1 = [1,2,3,4,5,6,7,8,9,10]
     # resultList1 = []
     # i = 1
     # while i <= len(myList1):
     #      result = myList1[i-1]
     #      if result % 2 == 0:
     #           resultList1.extend([result])
     #      i += 1
     # print('用while循环执行的结果是：',resultList1)


     # for循环取出列表内的偶数
     # myList2 = [1,2,3,4,5,6,7,8,9,10]
     # resultList2 = []
     # for j in myList2:
     #      if j % 2 == 0:
     #           resultList2.extend([j])
     # print('用for循环执行的结果是：',resultList2)

# 元组
     # temp1 = ('hello')
     # temp2 = ('hello',)
     # print('没有逗号的不是元组，而是：',type(temp1))
     # print('有逗号的是：',type(temp2))
     # 元组嵌套
     # yuanzu = ((1,2,3),(4,5,6))
     # print(f'去除元素6的结果是：{yuanzu[1][2]}')
# 操作元组
     # 用index()查找该元素所在的位置
     # personTuple1 = ('张三','李四','王五','赵六','田七','李四')
     # indexNo = personTuple1.index('王五')
     # print(indexNo)
     # 用count统计元组
     # count = personTuple1.count('李四')
     # print(f'在personTouple这个元组中，共有{count}个“李四”')
     # length = len(personTuple1)
     # print(f'personTouple这个元组里面的总元素是{length}个')
     # 元组内嵌套list数组
     # personTuple2 = (1,2,['老王','小张'])
     # personTuple2[2][0] = '小丽'
     # print('修改后的元组personTouple内容是：',personTuple2)

# 元组的练习题
     # yuanzu = ('周杰伦',11,['football','music'])
     # print(f'年龄是：{yuanzu[1]}')
     # print(f'姓名是：{yuanzu[0]}')
     # del (yuanzu[2][0])
     # print(f'删除学生爱好后的元组是：{yuanzu}')
     # yuanzu[2].append('coding')
     # print(f'增加coding在爱好中之后的元组是：{yuanzu}')

"""
字符串
     字符串跟元组一样，不能进行修改，但支持replace替换，split分割，strip去首尾的空格以及换行符（同java的strim()）
"""
     # str = '      56隔壁有老王 老李 老赵  5'
     # stripResult1 = str.strip().strip('56').strip()
     # print('strip(“56”)去掉首尾5或者6后的结果是：',stripResult1)
     # stripResult2 = str.strip()
     # print('执行strip之后的结果是：',stripResult2)
     # countResult = stripResult1.count('老')
     # print(f'str字符串中有：{countResult}个“老”字')
     # replaceResult = stripResult1.replace(' ','|')
     # print("执行str.replace(' ','|')后的结果是：",replaceResult)
     # splitResult = replaceResult.split('|')
     # print("执行replaceResult.split('|',' ')后的结果是：",splitResult)

# 数据容器的切片 类似java的substr()
    # temp[index:index-1:步长(正数)]
    # temp[index:index+1:步长(负数)]

    # list1 = ['a','b','c','d','e','f','g']
    # list2 = ('h','i','j','k','l','m','n')
    # list3 = 'opqrstuvwxyz'
    # 正向 从左到右取 # temp[index:index-1:步长(正数)]
    # print(f'list从index1开始，到第四位结束，步长1（步长默认为1，可以省略不写）：{list1[1:4]}')
    # print(f'元组从头开始，到最后结束，步长1（步长默认为1，可以省略不写）：{list2[:]}')
    # print(f'str从头开始，到最后结束，步长2：{list3[::2]}')
    # 反向 从右到左取 # temp[index:index+1:步长(负数)]
    # print(f'str从头开始，到最后结束，步长1（步长默认为1，可以省略不写）等同于将序列反转了：{list3[::-1]}')
    # print(f'list从index3开始，到第1位(反向时为index)结束，步长-1（步长默认为1，可以省略不写）：{list1[3:1:-1]}')
    # print(f'tuple从开头开始，到最后结束，步长-2：{list1[::-2]}')

    # 练习
        # 从字符串：'。万过薪月，员序程马黑来，nohtyp学'得到“黑马程序员”
        # 第一种方法
        # list1 = '。万过薪月，员序程马黑来，nohtyp学'
        # daoxu = list1[::-1][9:14]
        # print(daoxu)
        #
        # 第二种方法
        # fenge = list1.split('，')[1].replace('来','')[::-1]
        # print(fenge)

"""
集合（set）
    集合特点：
        里面元素不允许重复，如果有重复的话，会自动去重
        顺序没有办法保证的，所以不支持下标索引访问。
    定义集合：
        定义一个有元素的集合的方式：
            {},里面用逗号分割
        定义空集合的方式
            set()

"""
# 操作集合
    # my_set = {'张三','李四','王五','赵六','田七','钱八'}
    # 添加新元素
        # my_set.add('小丽')
        # print(my_set)
    # 移除元素
        # my_set.remove('赵六')
        # print(my_set)
        # 随机移除一个元素
        # popResult = my_set.pop()
        # print('被取出来的元素是：',popResult)
    # 清空集合
        # my_set.clear()
    # 集合的比较（取差集） 取出差集后，原有的集合的元素不会有变动
        # set1 = {1,2,3}
        # set2 = {1,5,6}
        # result = set1.difference(set2)
    # 集合的比较（取差集） 取出差集后，删除俩集合相同的元素
        # 删除set1中与set2相同的元素
        # set1.difference_update(set2)
        #     # print(set1)
        #     # print(set2)
    # 合并集合. 因为集合有自动去重功能，所以会被去重。
        # set3 = set1.union(set2)
        # print(set3)
    # 统计集合中的元素
        # print(len(set3))
    # 集合的遍历 因为集合没有顺序，不支持下标索引，所以不能用while循环，只能用for循环。
        # for i in set3:
        #     print(i)

    # 课后练习
        # 把如下列表添加到一个集合中
        # myList = ['张三','李四','王五','赵六','田七','钱八','张三','李四','王五','赵六','田七','钱八','张三','李四','王五','赵六','田七','钱八']
        # mySet = set()
        # for i in myList:
        #     mySet.add(i)
        # print(mySet)

"""
字典
    特征：
        以键值对的形式存在，键不允许重复，值可以。
        内容以逗号分割
    定义一个空字典：
        {}
        dict()
    定义一个有内容的字典：
        {'张三':20,'李四':18,'王五':29,}
"""
    # 取值
        # myDict = {'张三':20,'李四':18,'王五':29,}
        # print('张三的年龄是：',myDict['张三'])
    # 新增元素 如果存在就更新，如果不曾在就新增
        # myDict['赵六'] = 25
        # myDict['李四'] = 26
        # print(myDict)
    # 移出(删除)元素 使用pop的话可以将移出的键的值表示出来。
        # popResult = myDict.pop('张三')
        # print(f'移出后的显示结果是：{myDict}\n被移出的张三的年龄是：',popResult)
    # 获取字典里的所有键
        # allKey = myDict.keys()
        # print('获取所有的key：',allKey)
    # 遍历字典 获取所有的值 不能用while循环。
        # for key in allKey:
        #     print('字典的key是：',key)
        #     print('字典的value是：',myDict[key])
    # 统计字典里面的元素数量
        # print('字典里面的元素数量是：',len(myDict))
    # 清除所有元素
        # myDict.clear()

"""
课后练习
    将该表格里面所有级别为1级的员工，级别升1级，薪水增加1000元。
        姓名	    部门	    工资	    级别
        张三	    科技部	3000	1
        李四	    市场部	5000	2
        王五	    市场部	7000	3
        赵六	    科技部	4000	1
        田七	    市场部	6000	2
"""
    # myDict = {
    #     '张三':{
    #         '部门':'科技部',
    #         '工资':3000,
    #         '级别':1
    #     },
    #     '李四':{
    #         '部门':'市场部',
    #         '工资':5000,
    #         '级别':2
    #     },
    #     '王五': {
    #         '部门':'市场部',
    #         '工资':7000,
    #         '级别':3
    #     },
    #     '赵六':{
    #         '部门':'科技部',
    #         '工资':4000,
    #         '级别':1
    #     },
    #     '田七':{
    #         '部门':'市场部',
    #         '工资':6000,
    #         '级别':2
    #     }
    # }
    # for key in myDict.keys():
    #     print(key)
    #     if myDict[key]['级别'] == 1:
    #         myDict[key]['工资'] += 1000
    #         myDict[key]['级别'] += 1
    # print(myDict)

# 5类数据容器的通用操作
   # 求长度
        # len()
   # 求最大值
        # max()
   # 求最小值
        # min()
   # 各种容器之间相互转换
        # list()  # 转列表
        # str()  # 转字符串
        # tuple()  # 转元组
        # set()  # 转集合
   # 排序  排序结果是都被转换成了list数组,默认为顺序，如果加上reverse=True则为倒序
         # sorted(容器,reverse=True)

        # # 利用带名函数将数组中的元素的值进行排序
        #     my_list = [['a',33],['b',55],['c',11]]
        #     def choose_sort_key(element):
        #         return element[1]
        #     my_list.sort(key=choose_sort_key,reverse=True)
        #     print(my_list)

        # # 利用匿名函数将数组中的元素的值进行排序
        # my_list = [['a',33],['b',55],['c',11]]
        # my_list.sort(key=lambda element:element[1],reverse=True)
        # print(my_list)


    # 字符的大小比较 字符的比较主要基于ASCII码来进行比较的
    # print('a'>'A')

#
'''
函数的多种传参方式：
    位置传参
    关键字传参
    
'''

'''
文件的操作
    模式：
        r 只读模式
        w 写入模式 如果文件存在将会被覆盖，如果不存在则新建一个文件
        a 追加模式 如果文件存在则追加，如果不存在则新建一个文件然后执行追加功能
'''
    # 指定要打开的文件目录
    # file = open('D:/BaiduNetdiskWorkspace/PG_XX/python/自学练习/project/test.txt','r',encoding='UTF-8')
'''
read读取文件 将文件内容原原本本地读取并显示出来。
    小细节：第二次读取开始的位置将会是第一次读取的结束位置
'''
    # print('读取5个字节的结果是：',file.read(5))
    # print('读取该文件的所有内容：',file.read())

'''
readlines读取文件所有行
 将文本作为列表的方式读取出来，并将格式作为编码读取出来
'''
    # file2 = file.readlines()
    # print(file2)

'''
readline读取文件单行
 将文本作为列表的方式读取出来，并将格式作为编码读取出来
'''
    # print('第一行的读取内容是：',file.readline())
    # print('第二行的读取内容是：',file.readline())
    # print('第三行的读取内容是：',file.readline())

    # 用for循环读取每一行的内容
    # count = 0
    # for i in file:
    #     count += 1
    #     print(f'每{count}行的内容是：',i)

'''
文件占用 sleep
    该行为可以让文件一直处于被占用状态。
'''
    # time.sleep(5000)

    # 手动关闭文件 close
    # file.close()

    # 自动关闭文件    读取完毕之后自动关闭 避免关闭遗忘
    # with open('D:/BaiduNetdiskWorkspace/PG_XX/python/自学练习/project/test.txt','r',encoding='UTF-8') as file:
    #     count = 0
    #     for i in file:
    #         count += 1
    #         print(f'每{count}行的内容是：', i)

    # 课后练习
        # 第一种方式
            # with open('D:/BaiduNetdiskWorkspace/PG_XX/python/自学练习/project/word.txt','r',encoding='UTF-8') as file2:
            #     count = 0
            #     for i in file2:
            #         line = i.strip()
            #         words = line.split(' ')
            #         for word in words:
            #             if word == 'itheima':
            #                 count += 1
            # print(f'itheima一共出现了{count}次')

        # 第二种方式
            # with open('D:/BaiduNetdiskWorkspace/PG_XX/python/自学练习/project/word.txt','r',encoding='UTF-8') as file3:
            #     readResult = file3.read()
            #     countResult = readResult.count('itheima')
            #     print(countResult)

'''
文件写入操作
    w 写入模式
        如果指定的该文件不存在，则自动新建一个文件后执行写入操作;如果存在，则覆盖原来的内容。
    a 追加写入模式
        如果指定的该文件不存在，则自动新建一个文件后执行写入操作;如果存在，则在原有内容后面追加内容。
    write() 写入内存，并非写入磁盘
    flush() 写入磁盘
        close()也有写入磁盘得功能在里面。
'''
    # with open('D:/BaiduNetdiskWorkspace/PG_XX/python/自学练习/project/write.txt','w',encoding='UTF-8') as file4:
    #     file4.write('hello python！！！！')
    #     file4.flush()

# 综合练习
    # file5 = open('D:/BaiduNetdiskWorkspace/PG_XX/python/自学练习/project/bill.txt','r',encoding='UTF-8')
    # file6 = open('D:/BaiduNetdiskWorkspace/PG_XX/python/自学练习/project/bill.xlsx', 'w', encoding='UTF-8')
    # file7 = open('D:/BaiduNetdiskWorkspace/PG_XX/python/自学练习/project/bill.txt.bak', 'r', encoding='UTF-8')
    # for line in file5:
    #     line = line.strip()
    #     if line.split(',')[4] == '测试':
    #         continue
    #     file6.write(line)
    #     file6.write('\n')
    #     file6.flush()
    # file5.close()
    # file6.close()
    # print(file7.read())
    # file7.close()

# 模块的导入
    # import time
    # print('A：你好')
    # time.sleep(3)
    # print('B：你也好')

# 在自定义模块中做测试用的代码
    # if __name__ == '__main__':
    #     print()
    #     # 这里面的代码只有在该模块作为主程序的时候才会被执行
    #     # 多用于模块的测试。


'''第三方包
    比较有名的包如下：
        rumpy 可续结算中长用
        pandas 数据分析常用
        pyspark,apache-flink 大数据计算常用
        matplotlib,pyecharts 图形可视化常用
        tensorflow 人工智能常用
        
        在国内安装包的话，速度会非常慢，因为是pip是国外的。
        解决方案：
            pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名
'''



'''pyecharts的基本使用'''
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 创建一个折线图对象
line = Line()
# 给折线图对象添加x轴得数据
line.add_xaxis(['中国','美国','英国'])
# 给折线图对象添加y轴得数据
line.add_yaxis('GDP',[30,20,10])
# 通过render方法，将代码生成图像 这部操作将会生成一个带有图表得html文件，可独立运行。
line.render()

'''pyecharts的全局配置项 用global_opts来设置'''
# 创建一个折线图对象
line2 = Line()
# 给折线图对象添加x轴得数据
line2.add_xaxis(['中国','美国','英国'])
# 给折线图对象添加y轴得数据
line2.add_yaxis('GDP',[30,20,10])
# 折线图得全局配置
line2.set_global_opts(
    # 控制标题 pos_left:position_left，左侧距的意思。
    title_opts=TitleOpts(title='GDP展示',pos_left='center',pos_bottom='1%'),
    # 控制图例 默认显示
    legend_opts=LegendOpts(is_show=True),
    # 工具箱控制 可编辑折线图
    toolbox_opts=ToolboxOpts(is_show=True),
    # 视觉映射
    visualmap_opts=VisualMapOpts(is_show=True)
    # 其他功能见 https://pyecharts.org/#/

)






# 通过render方法，将代码生成图像 这部操作将会生成一个带有图表得html文件，可独立运行。
line2.render()


