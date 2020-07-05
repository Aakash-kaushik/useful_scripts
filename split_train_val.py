from glob import glob 
import os, random, shutil

classes_list=glob("train/*")
for classes_path in classes_list:
    img_move_path=os.path.join("val",classes_path.split("/")[-1])
    if not os.path.isdir(img_move_path):
        os.mkdir(img_move_path)
    img_list=glob(os.path.join(classes_path,"*"))
    percent=20
    img_to_move=int((percent/100)*len(img_list))
    for _ in range(img_to_move):
        move_img=random.choice(img_list)
        shutil.move(move_img,img_move_path)
        img_idx=img_list.index(move_img)
        del img_list[img_idx]