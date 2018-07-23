import pyautogui
import pytesseract
import time

##交易密码改成自己的
password = '123456'
##按纽在屏幕上的坐标需要修改成适合自己机器的
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
time.sleep(10)
#pyautogui.position()
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
#启动中投证券合一版
#启动中投证券合一版
# TAB 键
pyautogui.press('tab')
time.sleep(0.5)
#向下键
pyautogui.press('down')
time.sleep(0.5)
#  ENTER键
pyautogui.press('enter')
time.sleep(9)
##取消报错
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(770, 550, 80 ,25)
x,y = pyautogui.center(region)
pyautogui.doubleClick(x,y)
time.sleep(5)
##关闭PlayOnLinux界面
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(1055, 140, 11 ,11)
x,y = pyautogui.center(region)
pyautogui.doubleClick(x,y)
time.sleep(2)
##确定关闭PlayOnLinux界面
##按纽在屏幕上的坐标region需要修改成适合自己机器的
region=(930, 420, 75 ,20)
x,y = pyautogui.center(region)
pyautogui.doubleClick(x,y)
time.sleep(9)
###登录行情加交易
##输入框在屏幕上的坐标需要修改成适合自己机器的
pyautogui.click(560,380)
secs_between_keys = 0.1
pyautogui.typewrite(password, interval=secs_between_keys)
##识别验证码输入验证码
###captcha == ''，登录成功后出验证码的位置出现什么字符，每台机器屏幕不一样，需要根据具体的机器改动,这台机器正好是'',另一台机器不是''
captcha = 'testcaptcha'
while not (captcha == '') :
    ##按纽在屏幕上的坐标region需要修改成适合自己机器的
    im = pyautogui.screenshot(region=(798, 400, 60 ,25))
    im.save('/tmp/temp.png')
    time.sleep(9)
    captcha = pytesseract.image_to_string('/tmp/temp.png')
    time.sleep(3)
    ###captcha == ''，登录成功后出验证码的位置出现什么字符，每台机器屏幕不一样，需要根据具体的机器改动
    if not (captcha == '') :
        ##输入验证码
        ##输入框在屏幕上的坐标需要修改成适合自己机器的
        region=(695, 465, 145,30)
        x,y = pyautogui.center(region)
        pyautogui.click(x,y)
        time.sleep(0.5)
        secs_between_keys = 0.1
        pyautogui.typewrite(captcha, interval=secs_between_keys)
        ##点击登录
        ##按纽在屏幕上的坐标region需要修改成适合自己机器的
        region=(555, 435, 60 ,20)
        x,y = pyautogui.center(region)
        pyautogui.doubleClick(x,y)
        time.sleep(20)
