'''
模拟鼠标/键盘精灵
    duration 速度
    moveRel 相对移动relative
'''
import pyautogui
# pyautogui.size()
# 如果屏幕分辨率为1920*1080，那么左上角的坐标为（0，0），右下角的坐标是（1919，1079）
pyautogui.Size(width=1920, height=1080)
width,height = pyautogui.size()

'''
移动篇
'''
# 将鼠标移动到屏幕指定位置  参数分别是：x轴坐标，y轴坐标以及移动速度（可忽略）
pyautogui.moveTo(width/2,height/2,duration=0.5)
# 相对于当前光标位置移动光标
pyautogui.moveRel(200,0,duration=0.5)
# pyautogui.moveRel(200,200,duration=0.5)

'''
鼠标事件篇
'''
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.click()
# 将鼠标移动在duration指定时间2秒内，移动到某个位置（x,y）,然后点击2次
pyautogui.click(x=100,y=100,duration=2,clicks=2)
pyautogui.doubleClick()
pyautogui.rightClick()
# 鼠标中键
pyautogui.middleClick()
# 鼠标左键按住拖动
pyautogui.dragTo(0,100,duration=1)
# 鼠标右键按住拖动
pyautogui.dragTo(30,0,duration=2,button='right')
# 按住左键并拖动到相对于当前鼠标的位置
pyautogui.dragRel(-100,0,duration=1)
# 鼠标滚动事件
pyautogui.scroll(-500)


'''
键盘事件
'''
import time
time.sleep(2)
pyautogui.PAUSE = 0.5
# 键盘输入
pyautogui.typewrite('nihao，laowang')
# 执行全选+拷贝
pyautogui.keyDown('ctrl')
pyautogui.press('a')
pyautogui.press('c')
pyautogui.keyUp('ctrl')
# 模拟按下回车键
pyautogui.typewrite('\n')
# 执行粘贴
pyautogui.keyDown('ctrl')
pyautogui.press('v')
pyautogui.keyUp('ctrl')
# 在指定位置单击
pyautogui.click(600,600)
