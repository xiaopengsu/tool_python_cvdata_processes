#!/usr/bin/Python
# -*- coding: utf-8 -*-

# import os
# import shutil
# import sys
# # def read_copy_image(file_path,tm_st,tm_end):
# # def read_copy_image(argv):
# def read_copy_image():
#     #file_path='./2020-07-05_09-02-25'
#     # file_path=argv[1]
#     # tm_st=argv[2]
#     # tm_end=argv[3]
#     # flag=argv[4]
#     file_path='Green1'
#     for root,dirs,files in os.walk(file_path):
#         if('1'==flag):
#             os.mkdir(root+'_rslt')
#
#         for file in files:
#             # 获取文件路径
#             # print(os.path.join(root, file))
#             if ('txt'==file.split('.')[1]):
#                 continue
#             # print(float(file[0:13]))
#             time_stamp=float(file[0:13])
#             sourceFile=os.path.join(root, file)
#             targetFile=sourceFile[0:23]+'_rslt/'+file
#             time_st=float(tm_st)
#             time_end= float(tm_end)
#             # print (time_stamp ,time_st,time_end)
#             if(time_st<=time_stamp and time_end>=time_stamp):
#                 print ('________________')
#                 print (sourceFile, targetFile)
#                 open(targetFile, "wb").write(open(sourceFile, "rb").read())
#
#
# if __name__=="__main__":
#     # read_copy_image(sys.argv)
#     read_copy_image()


import os
import shutil
import sys
import matplotlib.image as mpimg
def read_szie_image(argv):
    path_img = argv[1]
    W=argv[2]
    H=argv[3]
    flag=argv[4]
    if('1'==flag):
        os.mkdir(path_img+'_sm')
    # W=15
    # H=20
    ls = os.listdir(path_img)
    print(len(ls))
    for i in ls:
        print (i)
        img = mpimg.imread(path_img+'/'+i)
        if (img.shape[0]< H and img.shape[1]<30) or (img.shape[0]<30 and img.shape[1]< W):
            shutil.move(path_img+'/'+i,path_img+'_sm'+'/'+i)

if __name__=="__main__":
    read_szie_image(sys.argv)