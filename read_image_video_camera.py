from __future__ import absolute_import
from __future__ import print_function

import os
import cv2

image_ext = ['jpg', 'jpeg', 'png', 'webp']
video_ext = ['mp4', 'mov', 'avi', 'mkv']
time_stats = ['tot', 'load', 'pre', 'net', 'dec', 'post', 'merge']


def demo(files):
    """
    :param files: camera or path+video or path (of images)
    :return:
    exampe:
    files = 'webcam'
    files = "/home/ubuntu/PycharmProjects/CenterNet-master/data/test_data/mo_ni_kaoshi/images/1.mp4"
    files = "/home/ubuntu/PycharmProjects/CenterNet-master/data/test_data/mo_ni_kaoshi/images"
    """

    if files == 'webcam' or \
            files[files.rfind('.') + 1:].lower() in video_ext:
        cam = cv2.VideoCapture(0 if files == 'webcam' else files)
        while True:
            _, img = cam.read()
            # todo img
            cv2.imshow('input', img)
            if cv2.waitKey(1) == 27:
                return  # esc to quit
    else:
        if os.path.isdir(files):
            image_names = []
            ls = os.listdir(files)
            for file_name in sorted(ls):
                ext = file_name[file_name.rfind('.') + 1:].lower()
                if ext in image_ext:
                    image_names.append(os.path.join(files, file_name))
        else:
            image_names = [files]

        for (image_name) in image_names:
            img = cv2.imread(image_name)
            # todo img
            # ret = detector.run(image_name)
            cv2.imshow('image', img)
            cv2.waitKey(0)


if __name__ == '__main__':
    # files = 'webcam'
    # files = "/home/ubuntu/PycharmProjects/CenterNet-master/data/test_data/mo_ni_kaoshi/images/1.mp4"
    files = "/home/ubuntu/PycharmProjects/CenterNet-master/data/test_data/mo_ni_kaoshi/images"
    demo(files)
