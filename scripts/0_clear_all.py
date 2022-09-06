import os


def clear_dir(dir_path):
    for file in os.listdir(dir_path):
        os.remove(os.path.join(os.getcwd(), dir_path, file))


clear_dir('all_images')
clear_dir('cluster_op')
clear_dir('all_images')
clear_dir('labelled_images')
clear_dir('raw_labels')

clear_dir(os.path.join('dataset', 'images', 'train'))
clear_dir(os.path.join('dataset', 'images', 'test'))
clear_dir(os.path.join('dataset', 'images', 'val'))
clear_dir(os.path.join('dataset', 'labels', 'train'))
clear_dir(os.path.join('dataset', 'labels', 'test'))
clear_dir(os.path.join('dataset', 'labels', 'val'))
