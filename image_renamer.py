import os
import os.path as path

# Source directory
sourcedir = path.absprath('fullsize')

files_to_rename = os.listdir(sourcedir)
# print(files_to_rename)

folder = r"fullsize"

print(sourcedir + '\n' + folder)

count = 0
for file in os.listdir(folder):
    # Create ccounter to append incrementaly to filenames
    count += 1
    if file in files_to_rename:
        # construct current name using file name and path
        old_name = os.path.join(folder, file)
        # print(old_name)

        # Get the file name while dropping the file extension
        only_name = os.path.splitext(file)[0]
        # print(only_name)

        # Add the new name with extension
        new_base = "lingerie_" + str(count) + ".jpg"
        # print(new_base)

        # Construct the full file path
        new_name = os.path.join(folder, new_base)
        ## print(new_name)

        # Rename the image
        os.rename(old_name, new_name)

# Prit the results
res = os.listdir(folder)
print(res)