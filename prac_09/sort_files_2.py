"""sorts based on user input and extension"""
import os


category = {}
os.chdir("FilesToSort")
for filename in os.listdir('.'):
    # Ignore directories, just process files
    if os.path.isdir(filename):
        continue

    extension = filename.split('.')[-1]
    if extension not in category:
        new_category = input("What category are {} files? ".format(extension))
        category[extension] = new_category
        try:
            # We don't expect to get an exception due to the if statement
            # But we'll play it safe anyway in case the user chooses an existing folder
            os.mkdir(new_category)
        except FileExistsError:
            pass

    os.rename(filename, "{}/{}".format(category[extension], filename))
