import os
 
filenames = os.listdir(".")
if len(filenames) == 0:
    print("You have no files")
else:
    print("Files on your system:")
    # loop through files and print them out
    for filename in filenames:
        print(filename)
