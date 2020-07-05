from glob import glob 
import cv2,os

def dhash(img_path,hash_size):
    img=cv2.imread(img_path)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    resized=cv2.resize(gray,(hash_size+1,hash_size))
    diff=resized[:,1:]>resized[:,:-1]
    return sum([2**i for i,v in enumerate(diff.flatten()) if v])

def dict_maker(img_list,hash_size):
    img_dict={}
    for img_path in img_list:
        h=dhash(img_path,hash_size)
        try:
            img_dict[h].append(img_path)
        except KeyError:
            img_dict[h]=[]
            img_dict[h].append(img_path)
    return img_dict

def dup_remove(img_dict):
    for key in img_dict:
        hash_key_len=len(img_dict[key])
        if hash_key_len != 1:
            for i in range(hash_key_len-1):
                os.remove(img_dict[key][i])

if __name__=="__main__":
    folder_list=glob("./train/*")
    for folder in folder_list:
        img_list=glob(os.path.join(folder,"*"))
        image_dict=dict_maker(img_list,8)
        dup_remove(image_dict)
        print(image_dict)



