# -*- coding:utf8 -*-

import os

class BatchRename():
    '''
    批量重命名文件夹中的图片文件
    os.rename(current_file_name, new_file_name) todo
    '''
    def __init__(self):
        self.path = './data_image_guoguo2/'  #表示需要命名处理的文件夹

    def rename(self):
        filelist = os.listdir(self.path) #获取文件路径
        filelist = sorted(filelist)
        total_num = len(filelist) #获取文件长度（个数）
        i = 0  #表示文件的命名是从1开始的
        for item in filelist:
            if item.endswith('.jpg'):  #初始的图片的格式为jpg格式的（或者源文件是png格式及其他格式，后面的转换格式就可以调整为自己需要的格式即可）
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), ''+str(i).zfill(10) + '.jpg')#处理后的格式也为jpg格式的，当然这里可以改成png格式
                #dst = os.path.join(os.path.abspath(self.path), '0000' + format(str(i), '0>3s') + '.jpg')    这种情况下的命名格式为0000000.jpg形式，可以自主定义想要的格式
                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print ('total %d to rename & converted %d jpgs' % (total_num, i))

if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()



# import os
# path_name = r'G:/data_annimal/data/'  # 批量修改的文件夹路径
# i = 1   # 起始数字
# f = open('G:/data_annimal/1.txt', mode='w')  # 生成一个txt文件用于记录原始名和新名
# for item in os.listdir(path_name):
#     original_name = os.path.join(path_name, item)
#     new_name = os.path.join(path_name, (str(i).zfill(6)+'.jpg'))
#     f.write(str(i).zfill(6) + ': ' + item + '\n')    # 将原始名和新名写入txt文件用于记录
#     os.rename(original_name, new_name)  # 重命名 os.rename(current_file_name, new_file_name)
#     i += 1
