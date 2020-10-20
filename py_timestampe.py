#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time;  # 引入time模块

# 参考:
# 1 https://www.cnblogs.com/jfl-xx/p/8024596.html
# 2 https://www.runoob.com/python3/python-timstamp-str.html

# 3 https://www.runoob.com/python/python-date-time.html  https://tool.lu/timestamp/

ticks = time.time()
print ("当前时间戳为:", ticks)
print(type(ticks))

print("%.6f" % ticks) #  print("%.6f", % ticks)
imgname=("%.6f" % ticks)
img_nam=str(imgname)
print(type(img_nam),img_nam)


years=ticks/(365*24*60*60)+1970  # TODO
print(years)


result=time.localtime(ticks)
print(result)

result2=time.ctime(ticks)
result3=time.asctime(result)
print(result2,' = ',result3)

print('*'*30)

#---------------------------------------------


#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 引入模块
import time, datetime

result=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(result)


# 字符类型的时间
time1='20200420'
time2='115402'
tss1 =time1[0:4]+'-'+time1[4:6]+'-'+time1[6:8]+' '+time2[0:2]+':'+time2[2:4]+':'+time2[4:6]
print (tss1)
# tss1 = '2013-10-10 23:40:00'
# 转为时间数组
timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
print (timeArray)
# timeArray可以调用tm_year等

# 转为时间戳
timeStamp = int(time.mktime(timeArray))
print (timeStamp)  # 1381419600

# 转为时间戳
timeStamp = time.mktime(timeArray)
print (timeStamp)  # 1381419600



# # python格式化输出保留6位小数
#
# #方法1：
# print("%.6f" % 0.13333)
#
# #方法2
# print("{:.6f}".format(0.13333))
#
# #方法3
# round(0.13333, 6)




# 行车记录仪的时间转换
#
#
# #   apply #--------v3 main的函数,参数外置,合并为1个参数-----------
# import cv2
# import time
#
# def video_to_image(file_path):
#     time.time()
#     cameraCapture = cv2.VideoCapture(file_path)
#     time_s=file_path.split('_')
#     time_date =time_s[1]
#     time_time =time_s[2].split('.')[0]
#     time_tran = time_date[0:4] + '-' + time_date[4:6] + '-' + time_date[6:8] + ' ' + time_time[0:2] + ':' + time_time[2:4] + ':' + time_time[4:6]
#     # 转为时间数组
#     timeArray = time.strptime(time_tran, "%Y-%m-%d %H:%M:%S")
#     # 转为时间戳
#     timeStamp = int(time.mktime(timeArray))
#     print (time_date,time_time)
#     success, frame = cameraCapture.read()
#     while success:
#         if cv2.waitKey(1) == 27:
#             break
#         cv2.imshow('Test camera', frame)
#         success, frame = cameraCapture.read()
#         milliseconds = cameraCapture.get(cv2.CAP_PROP_POS_MSEC)
#         start_time_int=timeStamp*1000
#         if frame is None:
#             continue #print("图像为空")
#         cv2.imwrite('./image_list/' + str(long(milliseconds+start_time_int)) + '.jpg', frame)
#         milliseconds=milliseconds//1000+timeStamp
#         timeArray = time.localtime(milliseconds)
#         otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
#         print(otherStyleTime)
#         cv2.waitKey(50)
#     cv2.destroyAllWindows()
#     cameraCapture.release()
#
# if __name__ == '__main__':
#     video_to_image('./Recfront_20200420_115402.mp4')



#  # 获取CPU执行时间  time.clock()
# start = time.clock()
# for i in range(0,10000):
#     print(i)
#
# end = time.clock()
# print(end-start)
#
#
#
# # 程序休眠 time.sleep(1)
#
#
# while True:
#     result=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
#     print(result)
#     time.sleep(1)
#


# 某月的日历

import calendar
print(calendar.month(2020,9))

# 引入模块
import datetime
t=datetime.datetime.now()
print(datetime.datetime.today())
res=t+datetime.timedelta(days=7)
print(t,' ',res)


# 时间差求取 delta.total_seconds()

first=datetime.datetime(1991,11,1,00,00,00)
print(first ,type(first))
second=datetime.datetime(2020,11,1,1,11,12)
delta=second-first
print(delta ,type(delta))
print(delta.total_seconds())

