import pyautogui
import pytesseract
import time

#下载盘后数据，交易日15:45之后运行
##按纽在屏幕上的坐标需要修改成适合自己机器的
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
time.sleep(10)
#pyautogui.position()
###盘后数据下载
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(120, 24, 35 ,25)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(5)
#十二次 向下键
freq=0
while freq <12 :
    pyautogui.press('down')
    time.sleep(0.5)
    freq +=1
#  ENTER键
pyautogui.press('enter')
time.sleep(3)
#下载日线数据
##日线和实时行情数据 前 打勾
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(420, 275, 13 ,13)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(0.5)
##点击 开始下载
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(808, 545, 66 ,24)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
###等待足够长时间以便完成数据下载,我这里不超过20分钟
time.sleep(1200)
#下载分钟线数据
## 选择沪深分钟线
region=(480, 215, 65 ,20)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(0.5)
##1分钟线数据 前 打勾
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(420, 250, 13 ,13)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(0.5)
##5分钟线数据 前 打勾
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(420, 275, 13 ,13)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(0.5)
##点击 开始下载
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(808, 545, 66 ,24)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
###等待足够长时间以便完成数据下载，我这里不超过40分钟
time.sleep(2400)
##导出自选股
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(120, 24, 35 ,25)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(5)
#十二次 向下键
freq=0
while freq <3 :
    pyautogui.press('down')
    time.sleep(0.5)
    freq +=1
#  ENTER键
pyautogui.press('enter')
time.sleep(3)
#报表中所有数据
region=(615, 380, 100,20)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(0.5)
#导出
region=(745, 475, 60,25)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(5)
#导出成功
region=(765, 320, 15,15)
x,y = pyautogui.center(region)
pyautogui.click(x,y)
time.sleep(5)

