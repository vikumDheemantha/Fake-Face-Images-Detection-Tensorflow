import os
import shutil

os.mkdir('fake-detection-cooccurrenct/data/train/real')
os.mkdir('fake-detection-cooccurrenct/data/train/gan')

os.mkdir('fake-detection-cooccurrenct/data/validate/real')
os.mkdir('fake-detection-cooccurrenct/data/validate/gan')

os.mkdir('fake-detection-cooccurrenct/data/test/real')
os.mkdir('fake-detection-cooccurrenct/data/test/gan')

real_list = os.listdir('celeb_dataset/celeba')
fake_list = os.listdir('StyleGAN_generated')

for i in range(0,600):
    source_real = f'celeb_dataset/celeba/{real_list[i]}'
    source_fake = f'StyleGAN_generated/{fake_list[i]}'

    dest_real = f'fake-detection-cooccurrenct/data/train/real/image_real_{i}.jpg'
    dest_fake = f'fake-detection-cooccurrenct/data/train/gan/image_gan_{i}.jpg'

    if os.path.isfile(source_real):
        shutil.copy(source_real, dest_real)
        print('copied', source_real)
    
    if os.path.isfile(source_fake):
        shutil.copy(source_fake, dest_fake)
        print('copied', source_fake)



for i in range(600,800):
    source_real = f'celeb_dataset/celeba/{real_list[i]}'
    source_fake = f'StyleGAN_generated/{fake_list[i]}'

    dest_real = f'fake-detection-cooccurrenct/data/validate/real/image_real_{i}.jpg'
    dest_fake = f'fake-detection-cooccurrenct/data/validate/gan/image_gan_{i}.jpg'

    if os.path.isfile(source_real):
        shutil.copy(source_real, dest_real)
        print('copied', source_real)
    
    if os.path.isfile(source_fake):
        shutil.copy(source_fake, dest_fake)
        print('copied', source_fake)


for i in range(800,1000):
    source_real = f'celeb_dataset/celeba/{real_list[i]}'
    source_fake = f'StyleGAN_generated/{fake_list[i]}'

    dest_real = f'fake-detection-cooccurrenct/data/test/real/image_real_{i}.jpg'
    dest_fake = f'fake-detection-cooccurrenct/data/test/gan/image_gan_{i}.jpg'

    if os.path.isfile(source_real):
        shutil.copy(source_real, dest_real)
        print('copied', source_real)
    
    if os.path.isfile(source_fake):
        shutil.copy(source_fake, dest_fake)
        print('copied', source_fake)