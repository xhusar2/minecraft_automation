import os
import zipfile
import cv2


import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
'''
for root, subdirs, files in os.walk('.'):
    for file in files:
        if('.ZIP' in file.upper()):
            with zipfile.ZipFile(os.path.join(root, file), 'r') as zip_ref:
                zip_ref.extractall(root)


for root, subdirs, files in os.walk('.'):
    for file in files:
        if('JPG' in file.split('.')[1].upper()):
            img = cv2.imread(os.path.join(root, file), 0)
            txt_path = os.path.splitext(os.path.join(root, file))[0] + '.txt'
            print(txt_path)
            if(not os.path.isfile(txt_path)):
                scan = pytesseract.image_to_string(img)
                with open(txt_path, 'w') as f:
                    f.write(scan)
                    os.remove(os.path.join(root, file))'''



def test(dir_path):

    rootdir = os.getcwd()
    print(rootdir)
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            # print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".jpg"):
                print(filepath)



def process_dir():
    rootdir = os.getcwd()
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filename, file_extension = os.path.splitext(file)
            print('file:', file)
            if file[0] != '.':
                if ('JPG' in file_extension.split('.')[1].upper()):
                    img = cv2.imread(os.path.join(subdir, file), 0)
                    txt_path = os.path.splitext(os.path.join(subdir, file))[0] + '.txt'
                    print(subdir + os.sep + file)
                    if (not os.path.isfile(txt_path)):
                        scan = pytesseract.image_to_string(img)
                        with open(txt_path, 'w', encoding='UTF-8') as f:
                            f.write(scan)
                            os.remove(os.path.join(subdir, file))

def main():
    process_dir()

main()
