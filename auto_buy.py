import pyautogui
import pytesseract
import time

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
time.sleep(10)
#pyautogui.position()

#买入5日均线上穿10日均线的股票

from hikyuu.interactive.interactive import *

ENDTIME=Datetime.now()
#ENDTIME=Datetime(201806260000)
###上证交易日期，用于判断停牌
sh = sm['sh000001']
#print(sh)
sh_k = sh.getKData(QueryByDate(s.startDatetime, ENDTIME,recoverType=Query.FORWARD))
sh_day = sh_k[-1].datetime
print("上证指数交易日期",sh_day)

i = 0
#遍历所有股票
for s in blocka:
    i += 1
    ###过滤ST和退市
    if not ('*' in s.name or 'ST' in s.name or '退' in s.name) :
        ktest = s.getKData(QueryByDate(s.startDatetime, ENDTIME,recoverType=Query.FORWARD))
        ###求取有多少跟K线，也就是有多少个交易日
        daytest= len(ktest)
        ###选取至少交易200天且今日不停牌的票
        if daytest >200 and(ktest[-1].datetime.year == sh_day.year and                               ktest[-1].datetime.month == sh_day.month and                               ktest[-1].datetime.day == sh_day.day) :
            k = s.getKData(QueryByDate(ktest[-100].datetime, ENDTIME,recoverType=Query.FORWARD))
            ma5= MA(CLOSE(k),5)
            ma10= MA(CLOSE(k),10)
            if ma5[-2] <ma10[-2] and ma5[-1]>ma10[-1]:
                print("被选中股票：",s)
                stock = s.code
                ###要操作的证券代码可以来自hikyuu\quantaxis\聚宽\米筐等量化
                #stock = '002049'
                ###要操作的股票数量，买入操作首先要保证账户内有足够资金
                amount = '100'
                ##按纽在屏幕上的坐标需要修改成适合自己机器的
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
                region=(755, 605, 70 ,20)
                x,y = pyautogui.center(region)
                pyautogui.click(x,y)
                time.sleep(1)
                ##资金不足，确认
                region=(750, 605, 75,25)
                x,y = pyautogui.center(region)
                pyautogui.click(x,y)
                time.sleep(1)   
                ##查看持仓
                region=(365, 445, 40,25)
                x,y = pyautogui.center(region)
                pyautogui.click(x,y)
                time.sleep(1)

