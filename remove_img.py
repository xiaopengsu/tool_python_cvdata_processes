#!/usr/bin/Python
# -*- coding: utf-8 -*-
import os
import sys
def remove_image(argv):
    '''
    多桩连续图像抽稀为少量图像,移除部分图像
    :dir=argv[1] 图像存放路径
    :n=int(argv[2]) 图像抽稀倍数
    :return: 
    '''
    dir=argv[1]
    n=int(argv[2])
    # dir = '/home/ubuntu/Camer_Lidar/2020-07-05_09-02-25'
    imgList = os.listdir(dir) 
    num_imgs = len(imgList)  
    print (num_imgs)
    count = 0
    for i in range(0, num_imgs):
        imgPath = os.path.join(dir, imgList[i]) 
        print(imgPath)
        # if(i>=300):
        #     os.remove(imgPath)
        if(0==i%n):
            print(count)
            os.remove(imgPath)

if __name__=="__main__":
    remove_image(sys.argv)
