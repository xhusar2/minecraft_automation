from PIL import Image
import os

folder_path = './images/player_recognition/training_set'
for subdir, dirs, files in os.walk(folder_path):
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if ('JPG' not in file_extension.split('.')[1].upper()):
            im1 = Image.open(os.file)
            im1.save(filename + '.jpg')