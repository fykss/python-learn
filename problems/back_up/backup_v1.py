import os
import time


path = "/Users/vladyslavlietun/Documents/Projects/Python/Introduction/problems/back_up"
file_path = path + "/test.txt"
target_dir = path

# os.sep - path separator for a specific operating system "/"
# time.strftime - time output format
target = target_dir + os.sep + time.strftime("%Y_%m_%d_%H_%M_%S") + ".zip"

# description zip -qr in book "A byte of Python" p. 324
zip_command = "zip -qr {0} {1}".format(target, ' '.join(file_path))

if os.system(zip_command) == 0:
    print("Backup success created in", target_dir)
else:
    print("Backup didn't create")
