import os

# show all methods
print(dir(os))

# current working directory
print(os.getcwd())

# change directory
os.chdir("/Users/vladyslavlietun/Documents/Projects/Python/")
print(os.getcwd())
os.chdir("/Users/vladyslavlietun/Documents/Projects/Python/Introduction/modules/os")

# show all files in current directory
print(os.listdir())

# create folder
os.mkdir("test_folder1")

# create deep structure folder
os.makedirs("test_folder2/sub_folder")

# remove folder
os.rmdir("test_folder1")
os.removedirs("test_folder2/sub_folder")

# rename file
os.rename("test.txt", "test1.txt")
os.rename("test1.txt", "test.txt")

# walk method search all folder and files
for dirpath, dirnames, filenames in os.walk("/Users/vladyslavlietun/Documents/Projects/Python/Introduction/oop"):
    print("Current path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)
    print()

# instance terminal + command
os.system("open " + os.getcwd())