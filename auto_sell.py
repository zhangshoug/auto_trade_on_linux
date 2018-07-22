import pyautogui
import pytesseract
import time

###要操作的证券代码可以来自hikyuu\quantaxis\聚宽\米筐等量化,同时确保目前持仓中有该只股票
stock = '002049'
###要操作的股票数量，卖出操作首先要保证持仓中有足够的仓位
amount = '100'
##按纽在屏幕上的坐标需要修改成适合自己机器的
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
time.sleep(10)
#pyautogui.position()
###卖出操作
#点击卖出操作按纽
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(255, 445, 30 ,20)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(1)
##输入证券代码
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(280, 500, 50 ,20)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(0.5)
secs_between_keys = 0.1
pyautogui.typewrite(stock, interval=secs_between_keys)
time.sleep(1)
##卖出价格，默认市价，故未写代码
##输入卖出数量
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(280, 615, 50 ,20)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(0.5)
secs_between_keys = 0.1
pyautogui.typewrite(amount, interval=secs_between_keys)
time.sleep(0.5)
##点击卖出下单
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(330, 640, 65 ,20)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(1)
##点击买入确认
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(710, 655, 65 ,20)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(1)
##非交易日下单，确认隔日委托
##按纽在屏幕上的坐标region需要修改成适合自己机器的
#region=(755, 605, 70 ,20)
#x,y = pyautogui.center(region)
#pyautogui.click(x,y)
#time.sleep(1)
