"""program to sort files based on file extension"""
import os


os.chdir("FilesToSort")
for filename in os.listdir('.'):
    # Ignore directories, just process files
    if os.path.isdir(filename):
        continue

    extension = filename.split('.')[-1]
    try:
        os.mkdir(extension)
    except FileExistsError:
        pass
    print("{}/{}".format(extension, filename))
    os.rename(filename, "{}/{}".format(extension, filename))

