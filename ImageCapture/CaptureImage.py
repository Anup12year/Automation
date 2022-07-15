import dropbox
import time
import cv2
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(number) + '.png'
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    
    return img_name
    print('snapshottaker')
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = 'sl.BK0cMDwHo36dl_w1MsMBz7D7P9W_1uedMfiDTIOcC1LMVJ5sTcDOYaAw8lkNZJZmMHGbM3e9HVOy4oc8Q1NKiYjvr9kRUGseFE6Oqbsv9XW8RXPggCw4E7jXfhtCeqEuJxV5v80'
    file = img_name
    file_from = file
    file_to = '/testfolder/' + (img_name) 
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print('file uploaded')

def main():
    while(True):
        if((time.time()- start_time)>=300):
            name = take_snapshot()
            upload_file(name)
            
main()

     

 
