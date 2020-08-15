from glob import glob
import os, shutil

val_dir="./val"
train_dir="./train"

val_folders=glob(os.path.join(val_dir,"*"))
train_folders=glob(os.path.join(train_dir,"*"))

for val_folder,train_folder in zip(val_folders,train_folders):
    imgs=glob(os.path.join(val_folder,"*"))
    for img in imgs:
        try:
            shutil.move(img,train_folder)
        except shutl.Error:
            continue