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

def main():
    # unzip
    for root, subdirs, files in os.walk('.'):
        for file in files:
            if ('.ZIP' in file.upper()):
                with zipfile.ZipFile(os.path.join(root, file), 'r') as zip_ref:
                    zip_ref.extractall(root)
                    print('process file: ',zip_ref.filename)
                    # process
                    for root_inner, subdirs, files in os.walk(zip_ref.filename):
                        for file in files:
                            if ('JPG' in file.split('.')[1].upper()):
                                img = cv2.imread(os.path.join(root, file), 0)
                                txt_path = os.path.splitext(os.path.join(root_inner, file))[0] + '.txt'
                                print(txt_path)
                                if (not os.path.isfile(txt_path)):
                                    scan = pytesseract.image_to_string(img)
                                    with open(txt_path, 'w') as f:
                                        f.write(scan)
                                        os.remove(os.path.join(root_inner, file))
                    print('remove file: ', root)
                os.remove(os.path.join(zip_ref.filename))
main()