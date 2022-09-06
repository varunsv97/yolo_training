import shutil
import os

source = os.path.join(os.getcwd(), 'all_imges')
destination1 = os.path.join(os.getcwd(), 'labelled_images')
destination2 = os.path.join(os.getcwd(), 'dataset', 'images', 'train')

for filename in os.listdir(source):
    f = filename.split('.')

    if f[0][-1] == 'd': #condition to seperate labelled from unlabelled
        shutil.copy2(os.path.join(source, filename), destination1)
    else:
        shutil.copy2(os.path.join(source, filename), destination2)
        continue