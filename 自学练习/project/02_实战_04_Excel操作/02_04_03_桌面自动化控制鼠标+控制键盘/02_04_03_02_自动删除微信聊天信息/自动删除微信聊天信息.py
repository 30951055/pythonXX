'''
pyautugui可以通过图片来获取大体的坐标
    1.先安装pip install Pillow，然后import PIL
    2.然后保存几张要操作的部位图
        如果有变化的图标等等要保存2张以上。
    3.机器会找跟部位图相应的图片，如果找到，返回坐标(left,top,width,height)，
        如果没找到，返回None
'''
import time
# import PIL
import pyautogui

# 判断目标所在位置
# pyautogui.screenshot()
# time.sleep(5)
# pointLeft = pyautogui.locateOnScreen('weixin.png')
# print('当前weixin.png所在的位置是：',pointLeft)


time.sleep(3)
# 两个操作之间暂停0.5秒
pyautogui.PAUSE = 0.5
# 执行操作三次，意味着只删除前三条
for i in range(3):
    pyautogui.screenshot()
    pointLeft = pyautogui.locateOnScreen('信息列表.png')
    print(pointLeft)
    if pointLeft is None:
        print('锁定“信息列表”失败，第二次锁定中：')
        pointLeft = pyautogui.locateOnScreen('信息列表2.png')
        if pointLeft is None:
            print('锁定“信息列表”失败，第三次锁定中：')
            pointLeft = pyautogui.locateOnScreen('信息列表3.png')
            if pointLeft is None:
                print('三次都失败了，算了。')
                break
    # 光标右移100像素。因为pointLeft[0]和pointLeft[1]均为0
    pyautogui.rightClick(pointLeft[0]+100 , pointLeft[1]+200)
    pyautogui.screenshot()
    # 读取删除按钮
    pointDelete = pyautogui.locateOnScreen('delete1.png')
    print(pointDelete)
    if pointDelete is None:
        pointDelete = pyautogui.locateOnScreen('delete2.png')
        if pointDelete is None:
            print('删除操作结束了')
            break
    # 执行点击事件
    pyautogui.click(pointDelete[0]+10, pointDelete[1]+10)