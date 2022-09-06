import os
import shutil
import random

set = '' #'val' for validation set and 'test' for test set

source = '/Users/varunsudharshnam/Desktop/yolo_training/dataset'

img_path = os.path.join(source, 'images', 'train')
labl_path = os.path.join(source, 'labels', 'train')

img_dest = os.path.join(source, 'images', set) 
labl_dest = os.path.join(source, 'labels', set)


def getRandomFile(path):

    files = os.listdir(path)
    index = random.randrange(0, len(files))
    return files[index]

n = 20

for i in range(n):

    img_file = getRandomFile(img_path)
    file_name = img_file.split('.')[0]
    label_file = file_name + '.txt'
    shutil.move(os.path.join(img_path, img_file), img_dest)
    shutil.move(os.path.join(labl_path, label_file), labl_dest)
