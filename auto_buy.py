import pyautogui
import pytesseract
import time

###要操作的证券代码可以来自hikyuu\quantaxis\聚宽\米筐等量化
stock = '002049'
###要操作的股票数量，买入操作首先要保证账户内有足够资金
amount = '100'
##按纽在屏幕上的坐标需要修改成适合自己机器的
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
time.sleep(10)
#pyautogui.position()
###买入操作
#点击买入操作按纽
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(215, 445, 32 ,20)
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
##买入价格，默认市价，故未写代码
##输入买入数量
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(280, 615, 50 ,20)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(0.5)
secs_between_keys = 0.1
pyautogui.typewrite(amount, interval=secs_between_keys)
time.sleep(0.5)
##点击买入下单
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
