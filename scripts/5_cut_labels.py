import numpy as np
import pandas as pd
import os

csv_path = 'labels_file.csv'
df = pd.read_csv(os.path.join(os.getcwd(), csv_path))

def getnames(path):
    files = os.listdir(path)
    filelist = []
    for file in files:
        filelist.append(file[:-4])
    return filelist

file_list_front = getnames(os.path.join(os.getcwd(), 'cluster_op', 'front'))
file_list_top = getnames(os.path.join(os.getcwd(), 'cluster_op', 'top'))
file_list_left = getnames(os.path.join(os.getcwd(), 'cluster_op', 'left'))
file_list_right = getnames(os.path.join(os.getcwd(), 'cluster_op', 'right'))


def split_data(view):
    splitdata = df.loc[df['file'].isin(view)]
    return splitdata

front_data = split_data(file_list_front)
top_data = split_data(file_list_top)
left_data = split_data(file_list_left)
right_data = split_data(file_list_right)


left_data.to_csv(os.path.join(os.getcwd(), 'raw_labels', 'front_data.csv'))
right_data.to_csv(os.path.join(os.getcwd(), 'raw_labels', 'top_data.csv'))
left_data.to_csv(os.path.join(os.getcwd(), 'raw_labels', 'left_data.csv'))
right_data.to_csv(os.path.join(os.getcwd(), 'raw_labels', 'right_data.csv'))


