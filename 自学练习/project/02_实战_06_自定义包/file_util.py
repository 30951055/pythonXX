'''接收传入文件得路径，打印文件得全部内容'''
def print_file_info(file_name):
    file = None
    try:
        file = open(file_name, 'r', encoding='UTF-8')
        # return file.readlines()
        print(file.readlines())
    except Exception as e:
        # return '该文件不存在'
        print('粗错啦：',e)
    finally:
        if file:
            file.close()


'''接收文件路径以及传入得数据，将数据写入到文件中'''
def append_to_file(file_name,data):
    with open(file_name, 'a', encoding='UTF-8') as file:
        file.write(data)
        # 写入磁盘
        file.flush()
        return '写入文件成功'


# 测试
if __name__ == '__main__':
    append_to_file('D:\\temp\\data\\入静法要.txt','哈哈哈')
    print_file_info('D:\\temp\\data\\入静法要.txt')
