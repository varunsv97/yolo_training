Yolo Training

Hardware requirements: An NVIDIA GPU and a good amount of RAM.
System Requirements: Python 3 and above with virtualenv installed if not use the command below to install.

        Linux/MacOS: python3 -m pip install --user virtualenv
        Windows: py -m pip install --user virtualenv
        Anaconda: conda install -c anaconda virtualenv


Step 0: Navigate to 'yolo_training' directory and create the virtual environment by running the command below.

        Linux/MacOS:  python3 -m venv yolo-env
        Windows: py -m venv yolo-env
        Anaconda: conda create -n yolo-env pip

        Now 'yolo-env' virtual environment is created, activate it using command below.

        Linux/MacOS: source yolo-env/bin/activate
        Windows cmd: yolo-env\Scripts\activate.bat
        Windows PowerShell: yolo-env\Scripts\Activate.ps1
        Windows PowerShell Core: yolo-env/bin/Activate.ps1
        Anaconda: conda activate yolo-env

Clone the yolo repository from github using the command: 

git clone https://github.com/ultralytics/yolov5 

Now install the requirements in the virtul environment using:

pip install -r yolov5/requirements.txt (or navigate to yolov5 repository and use : pip install -r requirements.txt)

Run 0_clear_all.py to clear delete.txt files in all empty folders

Preprocessing:

PS: Open each script and give the paths as in your local system before running.

Step 1 : If the data is in nested folders, run 1_glob.py on the repository. 
         All the files will be copied to root folder, cut and paste them in all images directory.
         New file names will be folder names and old filename joined by '-'.

Step 2 : Run 2_sepr.py to seperate labelled images from unlabelled. Change the logic of 'if' condition 
         that seperates the labelled from unlabelled appropriately for new data. Labelled images are saved in labelled_images folder.
         unlabelled images are saved in images subfolder of dataset folder.

Step 3 : Run 3_prep.py on the label co-ordinates csv file. If the file is in xls first convert it to csv by saving it csv file.
         The filename column should have the same name as the image file, make sure the logic is changed for new data appropriately.
         The changed csv file should have columns: filename, label, x, y. 

Step 4 : Run 4_nclus.py on all images. This will cluster the images into 4 directories for each orientation (front, left, right, top).
         Output will be saved in cluster_op folder with 4 subfolders, see the images in the folders and rename them as front, top, left, right.

Step 5 : Run 5_cut_labels.py to cut the labels csv file into 4 files, one for each orientation. Will be saved in raw_labels directory.

Step 5 : Annotation for height and width. 
         Go to https://www.makesense.ai/ website. Upload 4 images, one image of each orientation. Now select object detection.
         Upload labels.txt file for labels. Change the file appropriately for new data, order should be same as in labels csv file.
         Now draw the bounding boxes for all labels and export the annotations as a csv file using export option.
         Copy the bounding box height and width of each orientation from the exported file into the labels CSV files for that particular orientation.

Step 6 : The label files are now to be converted to yolo annotations format.
         Run 6_totxt.py, it runs on all csv files in raw_labels. This produces one txt file for one image in dataset/images and saves these in dataset/labels.
         Copy the label_list arry printed during this run into bird-maker.yaml file as class names. Change the number of classes accordingly.


Step 7 : Run 7_split.py to split the data into test and validation sets. Change the set variable to 'val' and run for creating validation set 
         and set it to 'test' and run for creating test set.


step 8 : Copy and paste the dataset folder in yolov5 directory, and paste the bird-marker.yaml file in data subfolder of yolov5 directory.
         Check if the paths are given correctly in bird-marker.yaml file.

Training:

Navigate to yolov5 directory and run this command tostart training :

$ python train.py --img 640 --batch 16 --epochs 50 --data bird-marker.yaml --weights yolov5s.pt

epochs can range 50-100 depending on the type of data. Precision and recall is monitored on each epoch.
batch is the batch size
img is image size
ProTip: Add --cache ram or --cache disk to speed up training (requires significant RAM/disk resources). 

results will be saved in runs/exp#
model will be saved in runs/exp#/weights/best.pt
this model can be used for inference

refer to https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data for more information
contact me regarding any errors during training 

