'''
通过无数次的循环测试来破解密码
前提是要准备一个密码本，可以是自己的，也可以网上下载 彩虹表

'''

# 作为方法使用的代码
import zipfile
import argparse


# 定义一个破解程序
def un_zip(zip_file, target_path, pwd2):
    try:
        zip_file.extractall(path=target_path, pwd=pwd2.encode('utf-8'))
        print(f'zip密码是：{pwd2}')
        return True
    except:
        print('粗错啦！')
        return False

# 使用破解程序
if __name__ == '__main__':
    # 载入被上了密码的文件
    zip_path = '加密文件.zip'
    # 载入密码本
    pwd_path = '密码本.txt'
    target_path = '.'
    zip_file = zipfile.ZipFile(zip_path)
    with open(pwd_path, 'r') as f:
        for pwd1 in f.readlines():
            pwd2 = pwd1.strip()
            if un_zip((zip_file, target_path, pwd2)):
                break


'''
通过接收外部参数来实现解密
    使用方法：
        穷举法_破解密码.py -n 加密文件.zip -p 密码本.txt
'''
# 定义一个破解程序
def un_zip2(zip_file, target_path, pwd4):
    try:
        zip_file.extractall(path=target_path, pwd=pwd4.encode('utf-8'))
        print(f'zip密码是：{pwd2}')
        return True
    except:
        print('粗错啦！')
        return False


# 使用破解程序
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='fuck zip file')
    parser.add_argument('-n',type=str,default='')
    parser.add_argument('-p',type=str,default='')
    args = parser.parse_args()
    # 载入被上了密码的文件
    zip_path = args.n
    # 载入密码本
    pwd_path = args.p
    target_path = '.'
    zip_file = zipfile.ZipFile(zip_path)
    with open(pwd_path, 'r') as f:
        for pwd3 in f.readlines():
            pwd4 = pwd3.strip()
            if un_zip2((zip_file, target_path, pwd4)):
                break