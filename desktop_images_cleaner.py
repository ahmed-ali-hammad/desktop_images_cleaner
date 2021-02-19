import os
import shutil
from datetime import date

files = [f for f in os.listdir('C:/Users/lakeland/Desktop')] #this gets a list of all the files on the desktop
new_folder_name = str(date.today()) # getting todays date to use it as a folder name

try: # creating a folder inside the Image folder on the desktop with today's date
    new_distination = os.path.join('C:/Users/lakeland/Desktop/Images',new_folder_name)
    os.mkdir(new_distination)
except FileNotFoundError: # in case there is no folder on the desktop under image
    os.mkdir('C:/Users/lakeland/Desktop/Images')
    new_distination = os.path.join('C:/Users/lakeland/Desktop/Images',new_folder_name)
    os.mkdir(new_distination)
except FileExistsError: # in case there is a folder inside the image folder with today's date
    pass

# moving the images from the desktop
for f in files:
    if f.endswith(".png") or f.endswith('.jpg') or f.endswith(".PNG"):
        shutil.move(os.path.join('C:/Users/lakeland/Desktop', f), new_distination)
