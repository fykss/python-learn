import os

# Open, create file and write() or read()

inputfile = "basic/10-files/user_names.txt"
outputfile = "basic/10-files/names_vlad.txt"


myfile1 = open(inputfile, mode='r')
myfile2 = open(outputfile, mode='w')

for line in myfile1:
    if "Vlad" in line:
        myfile2.write(line)

# myfile1.close()
# myfile2.close()


# File Positions

position = myfile1.tell()

print(position)