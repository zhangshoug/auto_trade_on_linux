# coding: utf-8

# In[10]:


import pyautogui
import pytesseract
import time


# In[11]:


import sys
import codecs


# In[12]:


from hikyuu.interactive.interactive import *
import numpy as np
import talib as tl
import functools


# In[13]:


#realtimeUpdate('tushare')
#realtimeUpdate('sina')
#realtimeUpdate('qq')


# In[26]:


##按纽在屏幕上的坐标需要修改成适合自己机器的
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
time.sleep(10)
#pyautogui.position()


# In[21]:


# 同花顺和通达信等软件中的SMA
def SMA_CN(close, timeperiod) :
    close = np.nan_to_num(close)
    return functools.reduce(lambda x, y: ((timeperiod - 1) * x + y) / timeperiod, close)
    
# 同花顺和通达信等软件中的KDJ
def KDJ_CN(high, low, close, fastk_period, slowk_period, fastd_period) :
    kValue, dValue = tl.STOCHF(high, low, close, fastk_period, fastd_period=1, fastd_matype=0)
    
    kValue = np.array(list(map(lambda x : SMA_CN(kValue[:x], slowk_period), range(1, len(kValue) + 1))))
    dValue = np.array(list(map(lambda x : SMA_CN(kValue[:x], fastd_period), range(1, len(kValue) + 1))))
    
    jValue = 3 * kValue - 2 * dValue
    
    func = lambda arr : np.array([0 if x < 0 else (100 if x > 100 else x) for x in arr])
    
    kValue = func(kValue)
    dValue = func(dValue)
    jValue = func(jValue)
    return kValue, dValue, jValue

# 同花顺和通达信等软件中的RSI
def RSI_CN(close, timeperiod) :
    diff = list(map(lambda x, y : x - y, close[1:], close[:-1]))
    diffGt0 = list(map(lambda x : 0 if x < 0 else x, diff))
    diffABS = list(map(lambda x : abs(x), diff))
    diff = np.array(diff)
    diffGt0 = np.array(diffGt0)
    diffABS = np.array(diffABS)
    diff = np.append(diff[0], diff)
    diffGt0 = np.append(diffGt0[0], diffGt0)
    diffABS = np.append(diffABS[0], diffABS)
    rsi = list(map(lambda x : SMA_CN(diffGt0[:x], timeperiod) / SMA_CN(diffABS[:x], timeperiod) * 100
            , range(1, len(diffGt0) + 1) ))
    
    return np.array(rsi)
    

# 同花顺和通达信等软件中的MACD
def MACD_CN(close, fastperiod, slowperiod, signalperiod) :
    macdDIFF, macdDEA, macd = tl.MACDEXT(close, fastperiod=fastperiod, fastmatype=1, slowperiod=slowperiod, slowmatype=1, signalperiod=signalperiod, signalmatype=1)
    macd = macd * 2
    return macdDIFF, macdDEA, macd 


# In[25]:


ENDTIME=Datetime.now()
N=3
###上证交易日期，用于判断停牌
sh = sm['sh000001']
#print(sh)
sh_k = sh.getKData(QueryByDate(s.startDatetime, ENDTIME,recoverType=Query.FORWARD))
sh_day = sh_k[-1].datetime
print("上证指数交易日期",sh_day)

encoding="gbk"
with codecs.open('/home/zhangshoug/.PlayOnLinux/wineprefix/ztzqallinone/drive_c/new_ztzq_allinone/T0002/export/自选股20180805.txt',"r",encoding) as f :
    line =f.readline()
    while line:
        list=line.split('\t')
        stock=list[0]
        if stock.isdigit() :
            price=float(list[3])
            #print(stock,price)
            """
            请写上一段代码代替print(stock,price),以实现你的想法
            """           
            i = 0
            #遍历所有股票
            for s in blocka:
                i += 1
                if s.code==stock:
                    ktest = s.getKData(QueryByDate(s.startDatetime, ENDTIME,recoverType=Query.FORWARD))
                    daytest= len(ktest)
                    before_N_day = ktest[daytest-N].datetime
                    ###今日未停牌
                    if ktest[-1].datetime.year == sh_day.year and ktest[-1].datetime.month == sh_day.month and                     ktest[-1].datetime.day == sh_day.day :                        
                        k = s.getKData(QueryByDate(ktest[-100].datetime, ENDTIME,recoverType=Query.FORWARD))
                        kMIN = s.getKData(QueryByDate(before_N_day, ENDTIME,kType=Query.MIN,recoverType=Query.FORWARD))
                        ma3= MA(CLOSE(k),3)
                        ma10= MA(CLOSE(k),10)
                        #df = k.to_df()
                        #close = [float(x) for x in df['close']]
                        #highPrice = [float(x) for x in df['high']]
                        #lowPrice = [float(x) for x in df['low']]
                        #计算KDJ指标
                        #df['kValue'],df['dValue'],df['jValue']=KDJ_CN(np.array(highPrice),np.array(lowPrice),np.array(close),fastk_period=9,slowk_period=3,fastd_period=3)
                        #KDJ_k=df['kValue']
                        #KDJ_d=df['dValue']
                        #KDJ_j=df['jValue']  
                        ###计算60分钟级别MACD
                        kMin60 = s.getKData(QueryByDate(ktest[-100].datetime, ENDTIME, kType=Query.MIN60,recoverType=Query.FORWARD))
                        df = kMin60.to_df()
                        close = [float(x) for x in df['close']]
                        highPrice = [float(x) for x in df['high']]
                        lowPrice = [float(x) for x in df['low']]
                        df['macdDIFF'],df['macdDEA'],df['macd'] = MACD_CN(np.array(close),fastperiod=12, slowperiod=26, signalperiod=9)
                        macdDIFF=df['macdDIFF']
                        macdDEA=df['macdDEA']
                        macd=df['macd']
                        
                        ###求区间内最高价及出现在第多少个交易日(起点为零交易日即区间起始日)
                        max_high = 0
                        #max_high_day = 0
                        for v in kMIN :
                            if v.highPrice > max_high :
                                max_high = v.highPrice
                        fall_from_buy=kMIN[-1].closePrice/price
                        fall_from_max_high=kMIN[-1].closePrice/max_high
                        if fall_from_buy<0.95 or fall_from_max_high<0.93 or (ma3[-2]>ma10[-2] and ma3[-1]<ma10[-1]) or                         (macdDIFF[-2]>macdDEA[-2] and macdDIFF[-1]<macdDEA[-1] and macd[-2]> macd[-1] ) :
                            print(s,"危险，该卖出了")
                            ###要操作的证券代码可以来自hikyuu\quantaxis\聚宽\米筐等量化,同时确保目前持仓中有该只股票
                            #stock = '002049'
                            ###要操作的股票数量，卖出操作首先要保证持仓中有足够的仓位
                            amount = '100'
                            ##只是演示，故设置一个不可能卖出的价格
                            price_sell = str(max_high*1.5)
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
                            #pyautogui.click(x,y)
                            pyautogui.doubleClick(x,y)
                            time.sleep(0.5)
                            secs_between_keys = 0.1
                            pyautogui.typewrite(stock, interval=secs_between_keys)
                            time.sleep(4)
                            ##卖出价格
                            region=(330, 535, 50,25)
                            x,y = pyautogui.center(region)
                            pyautogui.click(x,y)
                            time.sleep(0.5)
                            ##六次 退格键
                            freq=0
                            while freq <6 :
                                pyautogui.press('backspace')
                                time.sleep(0.1)
                                freq +=1
                            #pyautogui.doubleClick(x,y)
                            time.sleep(1)
                            secs_between_keys = 0.1
                            pyautogui.typewrite(price_sell, interval=secs_between_keys)
                            time.sleep(2)
                            ##输入卖出数量
                            ##按纽在屏幕上的坐标region需要修改成适合自己机器的
                            region=(275, 595, 100,25)
                            x,y = pyautogui.center(region)
                            pyautogui.click(x,y)
                            time.sleep(1)
                            pyautogui.click(x,y)
                            #pyautogui.doubleClick(x,y)
                            time.sleep(1)
                            secs_between_keys = 0.1
                            pyautogui.typewrite(amount, interval=secs_between_keys)
                            time.sleep(2)
                            ##点击卖出下单
                            ##按纽在屏幕上的坐标region需要修改成适合自己机器的
                            region=(330, 620, 70,25)
                            x,y = pyautogui.center(region)
                            pyautogui.click(x,y)
                            time.sleep(1)
                            ##点击卖出确认
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
        line =f.readline()
f.close()
