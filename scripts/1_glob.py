import shutil
import os

source = 'relative path to root folder' #only relative path not full path

def recursive_copy(path):

    for f in sorted(os.listdir(os.path.join(os.getcwd(), path))):

        file = os.path.join(path, f)

        if os.path.isfile(file):

            temp = os.path.split(path)
            f_name = '-'.join(temp)
            file_name = f_name + '-' + f
            shutil.copy2(file, file_name)

        else:

            recursive_copy(file)
         
recursive_copy(source)