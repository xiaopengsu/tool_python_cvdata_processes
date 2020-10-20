#!/usr/bin/Python
# -*- coding: utf-8 -*-
# import os
# import shutil
# https://blog.csdn.net/sinat_29957455/article/details/82778306
# https://www.cnblogs.com/wt7018/p/11610286.html
# Python os.path和shutil模块实现文件复制、删除
# https://developer.aliyun.com/article/401418

# # 1、获取test目录下的所有文件
# for root, dirs, files in os.walk(r"/home/ubuntu/Camer_Lidar/20200622"):
#     print(root)
#     os.mkdir(root+'/result2')
#     for file in files:
#         # 获取文件所属目录
#         print(root)
#         # 获取文件路径
#         print(os.path.join(root, file))



# # 2、获取test目录下的所有目录
# for root,dirs,files in os.walk(r"/home/ubuntu/Camer_Lidar/20200622"):
#     for dir in dirs:
#         #获取目录的名称
#         print(dir)
#         #获取目录的路径
#         print(os.path.join(root,dir))
#


# # 二、利用os.listdir递归获取所有的目录路径和文件路径
#
# def get_file_path(root_path, file_list, dir_list):
#     # 获取该目录下所有的文件名称和目录名称
#     dir_or_files = os.listdir(root_path)
#     for dir_file in dir_or_files:
#         # 获取目录或者文件的路径
#         dir_file_path = os.path.join(root_path, dir_file)
#         # 判断该路径为文件还是路径
#         if os.path.isdir(dir_file_path):
#             dir_list.append(dir_file_path)
#             # 递归获取所有文件和目录的路径
#             get_file_path(dir_file_path, file_list, dir_list)
#         else:
#             file_list.append(dir_file_path)
#
#
# if __name__ == "__main__":
#     # 根目录路径
#     root_path =r"/home/ubuntu/Camer_Lidar/20200622"
#     # 用来存放所有的文件路径
#     file_list = []
#     # 用来存放所有的目录路径
#     dir_list = []
#     get_file_path(root_path, file_list, dir_list)
#     print(file_list)
#     print(dir_list)

#
# # coding=utf-8
# import os
# import shutil
#
#
# # 递归复制文件夹内的文件
# def copyFiles(sourceDir, targetDir):
#     # 忽略某些特定的子文件夹
#     if sourceDir.find("exceptionfolder") > 0:
#         return
#
#         # 列出源目录文件和文件夹
#     for file in os.listdir(sourceDir):
#         # 拼接完整路径
#         sourceFile = os.path.join(sourceDir, file)
#         targetFile = os.path.join(targetDir, file)
#
#         # 如果是文件则处理
#         if os.path.isfile(sourceFile):
#             # 如果目的路径不存在该文件就创建空文件,并保持目录层级结构
#             if not os.path.exists(targetDir):
#                 os.makedirs(targetDir)
#                 # 如果目的路径里面不存在某个文件或者存在那个同名文件但是文件有残缺，则复制，否则跳过
#             if not os.path.exists(targetFile) or (
#                     os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
#                 open(targetFile, "wb").write(open(sourceFile, "rb").read())
#                 print targetFile + " copy succeeded"
#
#         # 如果是文件夹则递归
#         if os.path.isdir(sourceFile):
#             copyFiles(sourceFile, targetFile)
#
#
# # 遍历某个目录及其子目录下所有文件拷贝到某个目录中
# def copyFiles2(srcPath, dstPath):
#     if not os.path.exists(srcPath):
#         print "src path not exist!"
#     if not os.path.exists(dstPath):
#         os.makedirs(dstPath)
#         # 递归遍历文件夹下的文件，用os.walk函数返回一个三元组
#     for root, dirs, files in os.walk(srcPath):
#         for eachfile in files:
#             shutil.copy(os.path.join(root, eachfile), dstPath)
#             print eachfile + " copy succeeded"
#
#
# # 删除某目录下特定文件
# def removeFileInDir(sourceDir):
#     for file in os.listdir(sourceDir):
#         file = os.path.join(sourceDir, file)  # 必须拼接完整文件名
#         if os.path.isfile(file) and file.find(".jpg") > 0:
#             os.remove(file)
#             print file + " remove succeeded"
#
#
# if __name__ == "__main__":
    # copyFiles("./dir1", "./dir2")
    # removeFileInDir("./dir2")
    # copyFiles2("./dir1","./dir2")








#
# import os
# import shutil
#
# for root,dirs,files in os.walk(r"/home/ubuntu/Camer_Lidar/20200622"):
#     for dir in dirs:
#         # 获取文件所属目录
#         print(root)
#         #获取目录的名称
#         path_rs=dir+'_rslt'
#         #获取目录的路径
#         print(os.path.join(root,path_rs))
#         # os.mkdir(os.path.join(root,path_rs))
#
#     for file in files:
#         # 获取文件路径
#         print(os.path.join(root, file))
#         print(float(file[0:16]))
#         time_stamp=float(file[0:16])
#         sourceFile=os.path.join(root, file)
#         targetFile=sourceFile[0:57]+'_rslt/'+file
#         print (sourceFile ,targetFile)
#         if(1592816374.7339928<time_stamp and 1592816375.6421475>time_stamp):
#             open(targetFile, "wb").write(open(sourceFile, "rb").read())
#


#!/usr/bin/Python
# -*- coding: utf-8 -*-

import os
import shutil
import sys
# def read_copy_image(file_path,tm_st,tm_end):
def read_copy_image(argv):
    #file_path='./2020-07-05_09-02-25'
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
            targetFile=sourceFile[0:23]+'_rslt/'+file
            time_st=float(tm_st)
            time_end= float(tm_end)
            # print (time_stamp ,time_st,time_end)
            if(time_st<=time_stamp and time_end>=time_stamp):
                print ('________________')
                print (sourceFile, targetFile)
                open(targetFile, "wb").write(open(sourceFile, "rb").read())


if __name__=="__main__":
    read_copy_image(sys.argv)


#
#
# # !/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# import os
# import os.path
# import shutil
# import time, datetime
#
# #主要运用os.path和shutil模块来在实现文件复制、删除，可以根据自己的需求修改相关代码即可。
# def copyFiles(sourceDir, targetDir):  # 把某一目录下的所有文件复制到指定目录中
#     if sourceDir.find(".svn") > 0:
#         return
#     for file in os.listdir(sourceDir):
#         sourceFile = os.path.join(sourceDir, file)
#         targetFile = os.path.join(targetDir, file)
#         if os.path.isfile(sourceFile):
#             if not os.path.exists(targetDir):
#                 os.makedirs(targetDir)
#             if not os.path.exists(targetFile) or (
#                     os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
#                 open(targetFile, "wb").write(open(sourceFile, "rb").read())
#         if os.path.isdir(sourceFile):
#             First_Directory = False
#             copyFiles(sourceFile, targetFile)
#
#
# def removeFileInFirstDir(targetDir):  # 删除一级目录下的所有文件
#     for file in os.listdir(targetDir):
#         targetFile = os.path.join(targetDir, file)
#         if os.path.isfile(targetFile):
#             os.remove(targetFile)
#
#
# def coverFiles(sourceDir, targetDir):  # 复制一级目录下的所有文件到指定目录
#     for file in os.listdir(sourceDir):
#         sourceFile = os.path.join(sourceDir, file)
#         targetFile = os.path.join(targetDir, file)
#         # cover the files
#         if os.path.isfile(sourceFile):
#             open(targetFile, "wb").write(open(sourceFile, "rb").read())
#
#
# def moveFileto(sourceDir, targetDir):  # 复制指定文件到目录
#     shutil.copy(sourceDir, targetDir)
#
#
# def writeVersionInfo(targetDir):  # 往指定目录写文本文件
#     open(targetDir, "wb").write("Revison:")
#
#
# def getCurTime():  # 返回当前的日期，以便在创建指定目录的时候用
#     nowTime = time.localtime()
#     year = str(nowTime.tm_year)
#     month = str(nowTime.tm_mon)
#     if len(month) < 2:
#         month = '0' + month
#     day = str(nowTime.tm_yday)
#     if len(day) < 2:
#         day = '0' + day
#     return (year + '-' + month + '-' + day)
#
#
# if __name__ == "__main__":  # 主函数
#     print ( "Start(S) or Quilt(Q) \n")
#     flag = True
#     while (flag):
#         answer = raw_input()
#         if answer == 'Q':
#             flag = False
#         elif answer == 'S':
#             formatTime = getCurTime()
#             targetFoldername = "Build " + formatTime + "-01"
#             Target_File_Path += targetFoldername
#             copyFiles(Debug_File_Path, Target_File_Path)
#             removeFileInFirstDir(Target_File_Path)
#             coverFiles(Release_File_Path, Target_File_Path)
#             moveFileto(Firebird_File_Path, Target_File_Path)
#             moveFileto(AssistantGui_File_Path, Target_File_Path)
#             writeVersionInfo(Target_File_Path + "\test.txt")
#             print ("all sucess")
#         else:
#             print("not the correct command")
#
