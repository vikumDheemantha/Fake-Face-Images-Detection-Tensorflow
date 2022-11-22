import os
from zipfile import ZipFile

import gdown

os.makedirs('graphic', exist_ok=True)

url = "https://drive.google.com/drive/folders/1iChdwdW7mZFUyivKtDwL8ehCNhYKQz6D?usp=share_link"
output = "graphic/"
print('start downloading')
gdown.download(url, output, quiet=False)
print('end downloading')

