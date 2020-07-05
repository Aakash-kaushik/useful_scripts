import os
from glob import glob

unwanted_extensions=["gif","svgz"]

folder_list=glob("./train/*")

for folder in folder_list:
    img_list=glob(os.path.join(folder,"*"))
    for img_path in img_list:
        img_extension = img_path.split(".")[-1]
        for unwanted_extension in unwanted_extensions:
            if unwanted_extension in img_extension:
                os.remove(img_path)
    print(folder+" done")
