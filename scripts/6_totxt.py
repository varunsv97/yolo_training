from __future__ import annotations
import pandas as pd
import numpy as np
import os

img_width = 1280
img_height = 960


def totext(data):

    label_list = data['label'].unique().tolist()
    print(label_list) #paste this in bird-marker.yaml file
    file_list = data['file'].unique().tolist()

    for _files in file_list:
        
        file_path = os.path.join(annotations_path, str(_files) + '.txt')

        subset = data.loc[data['file'] == _files]
        subset = subset.dropna()
        subset['x'] = subset['x'].div(img_width)
        subset['Width'] = subset['Width'].div(img_width)
        subset['y'] = subset['y'].div(img_height)
        subset['Height'] = subset['Height'].div(img_height)

        count = 0
        for index, row in subset.iterrows():
            count += 1 
            label_id = str(label_list.index(row['label']))
            obj_row = label_id + " " + str(row['x'])[:6] + " " + str(row['y'])[:6] + " " + str(row['Width'])[:6] + " " + str(row['Height'])[:6]
            with open(file_path, 'a') as f:
                f.write(obj_row)
                if count <= len(subset.index) - 1:
                    f.write("\n")


annotations_path = os.path.join(os.getcwd(), 'dataset', 'labels', 'train')

path = os.path.join(os.getcwd(), 'raw_labels')

for f_ in os.listdir(path):

    data_ = pd.read_csv(os.path.join(path, f_))
    totext(data_)
    print(f_)
