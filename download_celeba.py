import os
from zipfile import ZipFile

import gdown

os.makedirs('celeb_dataset')

url = "https://drive.google.com/uc?id=1O7m1010EJjLE5QxLZiM9Fpjs7Oj6e684"
output = "celeb_dataset/data.zip"
print('start downloading')
gdown.download(url, output, quiet=False)
print('end downloading')

print('start extraction')
with ZipFile("celeb_dataset/data.zip", "r") as zipobj:
    zipobj.extractall("celeb_dataset")
print('end extraction')
os.remove('celeb_dataset/data.zip')
