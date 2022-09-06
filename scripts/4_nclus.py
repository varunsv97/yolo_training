import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import cv2
import os, glob, shutil

k = 4 #number of clusters

input_path = 'all_images' #relative path only
output_path = 'cluster_op' #relative path only

input_dir = os.path.join(os.getcwd(), input_path) #input directory
output_dir = os.path.join(os.getcwd(),output_path) #outout directory
glob_dir = input_dir + '/*.png'
images = [cv2.resize(cv2.imread(file), (224, 224)) for file in glob.glob(glob_dir)]
paths = [file for file in glob.glob(glob_dir)]
images = np.array(np.float32(images).reshape(len(images), -1)/255)

model = tf.keras.applications.MobileNetV2(include_top=False,
                                        weights='imagenet', 
                                        input_shape=(224, 224, 3))
predictions = model.predict(images.reshape(-1, 224, 224, 3))
pred_images = predictions.reshape(images.shape[0], -1)


kmodel = KMeans(n_clusters = k, random_state=728)
kmodel.fit(pred_images)
kpredictions = kmodel.predict(pred_images)
shutil.rmtree(output_dir)
for i in range(k):
    os.makedirs(os.path.join(os.getcwd(), output_dir, 'cluster'+ str(i))) 
for i in range(len(paths)):
    shutil.copy2(paths[i], (os.path.join(os.getcwd(), output_dir,'cluster'+str(kpredictions[i]))))
