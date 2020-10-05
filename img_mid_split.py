import cv2
import os
from glob import glob

img_dir = r""
new_folder_dir = r""

if new_folder_dir not in os.listdir():
  os.mkdir(new_folder_dir)

img_path_list = glob(os.path.join(img_dir, "*.*"))

for img_path in img_list:
  img_extension = img_path.split(".")[-1]
  img_name = img_path.split(".")[-2].split("/")[-1]
  img = cv2.imread(img_path)
  mid_width = int(img.shape[1]/2)
  cv2.imwrite(os.path.join(new_folder_dir, (img_name + "_left" + "."+ img_extension)), img[:, 0:mid_width, :])
  cv2.imwrite(os.path.join(new_folder_dir, (img_name + "_right" + "."+ img_extension)), img[:, mid_width:-1, :])






