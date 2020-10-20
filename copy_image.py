# !/usr/bin/Python
# -*- coding: utf-8 -*-

import os
import shutil
import sys
# def read_copy_image(file_path,tm_st,tm_end):
def read_copy_image(argv):
    '''
    :param argv:
    file_path=argv[1] 文件路径
    tm_st=argv[2] 起始时间 图片名 去'.jpg'
    tm_end=argv[3] 终止时间 图片名 去'.jpg'
    flag=argv[4] 是否新建文件夹
    return:
    #run :  python XX.py ./2020-07-05_09-02-25 1592816375.0721023  1592816380.3491347 1
    '''

    file_path=argv[1]
    tm_st=argv[2]
    tm_end=argv[3]
    flag=argv[4]
    for root,dirs,files in os.walk(file_path):
        if('1'==flag):
            os.mkdir(root+'_rslt')

        for file in files:
            # 获取文件路径
            # print(os.path.join(root, file))
            if ('txt'==file.split('.')[1]):
                continue
            # print(float(file[0:13]))
            time_stamp=float(file[0:13])
            sourceFile=os.path.join(root, file)
            targetFile=sourceFile[0:15]+'_rslt/'+file
            time_st=float(tm_st)
            time_end= float(tm_end)
            # print (time_stamp ,time_st,time_end)
            if(time_st<time_stamp and time_end>time_stamp):
                print ('________________')
                print (sourceFile, targetFile)
                open(targetFile, "wb").write(open(sourceFile, "rb").read())


if __name__=="__main__":
    read_copy_image(sys.argv)





# # -*- coding: UTF-8 -*-
# import os
# import numpy as np
# import decimal
# import random
#
# #for i in range(14289,34836):
# x=range(14290,34835)
# random.shuffle(x)
# path_dir="yizhuangkc/data_image"
# for i in x:
#     list = [path_dir+' '+str(i)+' '+'l', '\n']
#     print(list)
