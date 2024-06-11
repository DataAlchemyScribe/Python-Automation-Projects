import os
import shutil
import datetime
import time
import schedule

# source directory variable - write the path of source directory from where all files will get backed-up
src_dir = "C:/Devanshu 7-7-20/Education LDRP/4th Year - B.E. IT/Learning Python"
# destination directory variable - write the path of destination directory where all back-up files resides
dst_dir = "C:/Users/Devanshu/Desktop/TempBackUp"

# Function to perform back-up
def perform_backUp(source, destination):
    today = datetime.date.today()
    # naming folders with date - easy to understand on which date what was backed-up
    dir_destination = os.path.join(destination, str(today))

    try:
        shutil.copytree(source, dir_destination)
        print(f"BackUp Perform Successfully!\nBackUp Folder location : {dir_destination}")
    except FileExistsError:
        print(f"BackUp Folder Already Exist!\nLocation: {dir_destination}")

#calling function to perform back-up operation at specific time 07:00 pm (19:00) everyday
schedule.every().day.at("19:00:00").do(lambda: perform_backUp(src_dir, dst_dir))

# infinite loop, until the time (19:00 hr) to perform back-up arrives
while True:
    schedule.run_pending()
    time.sleep(60)