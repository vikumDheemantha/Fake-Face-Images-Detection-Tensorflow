import os
from PIL import Image
from tqdm import tqdm

img_dir1 = 'data/train/gan/'
img_dir2 = 'data/train/real/'
img_dir3 = 'data/validate/gan/'
img_dir4 = 'data/validate/real/'
img_dir5 = 'data/test/gan/'
img_dir6 = 'data/test/real/'

imgs = os.listdir(img_dir1)
for img in tqdm(imgs):
    try:
        im = Image.open(img_dir1 + img)
        im.load()
    except:
        os.remove(img_dir1+img)


imgs = os.listdir(img_dir2)
for img in tqdm(imgs):
    try:
        im = Image.open(img_dir2 + img)
        im.load()
    except:
        os.remove(img_dir2+img)


imgs = os.listdir(img_dir3)
for img in tqdm(imgs):
    try:
        im = Image.open(img_dir3 + img)
        im.load()
    except:
        os.remove(img_dir3+img)

imgs = os.listdir(img_dir4)
for img in tqdm(imgs):
    try:
        im = Image.open(img_dir4 + img)
        im.load()
    except:
        os.remove(img_dir4+img)

imgs = os.listdir(img_dir5)
for img in tqdm(imgs):
    try:
        im = Image.open(img_dir5 + img)
        im.load()
    except:
        os.remove(img_dir5+img)


imgs = os.listdir(img_dir6)
for img in tqdm(imgs):
    try:
        im = Image.open(img_dir6 + img)
        im.load()
    except:
        os.remove(img_dir6+img)

print(len(os.listdir(img_dir1)))
print(len(os.listdir(img_dir2)))
print(len(os.listdir(img_dir3)))
print(len(os.listdir(img_dir4)))
print(len(os.listdir(img_dir5)))
print(len(os.listdir(img_dir6)))