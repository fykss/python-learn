import os
import time


path = "/Users/vladyslavlietun/Documents/Projects/Python/Introduction/problems/back_up/"
file_path = path + "/test.txt"
target_dir = path

today = target_dir + os.sep + time.strftime("%Y_%m_%d")
now = time.strftime("%H:%M:%S")

if not os.path.exists(today):
    os.mkdir(today)
    print("Success created folder:", today)

target_name_file = today + os.sep + now + ".zip"

zip_command = "zip -qr {0} {1}".format(target_name_file, ''.join(file_path))

if os.system(zip_command) == 0:
    print("Backup success created in", target_name_file)
else:
    print("Backup didn't create")
