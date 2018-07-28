import pyautogui
import pytesseract
import time

##按纽在屏幕上的坐标需要修改成适合自己机器的
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
time.sleep(10)
#pyautogui.position()
###最小化程序启动窗口 防止干扰
region=(1295, 10, 10,10)
x,y = pyautogui.center(region)
pyautogui.doubleClick(x,y)
time.sleep(5)
###移动鼠标到最右上角，防止干扰开始菜单
pyautogui.moveTo(screenWidth, 0)
time.sleep(1)
###开始菜单位置
# WINLEFT键
pyautogui.press('winleft')
time.sleep(1)
###游戏位置
# 五次 向上键
freq=0
while freq <5 :
    pyautogui.press('up')
    time.sleep(0.5)
    freq += 1
###PlayOnLinux
# 向右键
pyautogui.press('right')
#启动PlayOnLinux
#  ENTER键
pyautogui.press('enter')
time.sleep(3)
#启动钱龙旗舰版
# TAB 键
pyautogui.press('tab')
time.sleep(0.5)
#向下键 三次
freq=0
while freq <3 :
    pyautogui.press('down')
    time.sleep(0.5)
    freq += 1
#  ENTER键
pyautogui.press('enter')
time.sleep(55)
###登录 已设为自动登录
##按纽在屏幕上的坐标region需要修改成适合自己机器的
#region=(708, 413, 185, 42)
#x,y = pyautogui.center(region)
#pyautogui.click(x,y)
#time.sleep(5)
###数据下载维护
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(355, 70, 80, 25)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(1)
###权息资料 前打勾
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(285, 385, 65, 15)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(1)
### 添加
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(682, 195, 75, 30)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(2)
###沪深市场
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(305, 190, 70, 15)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(2)
### 全选 打勾
region=(670, 170, 50, 20)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(2)
### 确定
region=(550, 420, 85, 30)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(9)
###下载
region=(665, 350, 100, 28)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(29)
test = 'None'
###下载结束的图片需要事先生成
while test == 'None' :
    test = pyautogui.locateCenterOnScreen('image/ql_down_end.png')
    time.sleep(5)
### 关闭 数据维护
region=(750, 75, 12, 12)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(2)
### 关闭 钱龙旗舰
region=(1001, 28, 15, 15)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(2)
### 直接退出
region=(655, 325, 90, 25)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(2)
### 关闭广告
region=(798, 78, 14, 14)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(2)
