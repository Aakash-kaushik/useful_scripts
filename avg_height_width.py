from glob import glob
from PIL import Image
from statistics import mean
import os


dir="./train"

folders=glob(os.path.join(dir,"*"))

height,width=[],[]

for folder in folders:
    images=glob(os.path.join(folder,"*"))
    for image in images:
        img=Image.open(image)
        width.append(img.size[0])
        height.append(img.size[1])

    print(folder.split("/")[-1]+" done")

print("average height is : "+str(mean(height)))
print("average width is : "+str(mean(width)))