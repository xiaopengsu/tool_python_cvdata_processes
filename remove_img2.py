#!/usr/bin/Python
# -*- coding: utf-8 -*-
import os
import sys
def remove_image(argv):
    '''
    将大于阈值的图像移除
    :dir=argv[1] 图像存放路径
    :n=int(argv[2]) 阈值的设置
    :return:
    '''
    dir=argv[1]
    m=int(argv[2])
    imgList = os.listdir(dir)
    num_imgs = len(imgList)
    for i in range(0, num_imgs):
        imgPath = os.path.join(dir, imgList[i])
        if(i>=m):
            print(imgPath)
            os.remove(imgPath)

if __name__=="__main__":
    remove_image(sys.argv)
