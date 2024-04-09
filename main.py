import os
import os.path as path

from PIL import Image
from glob import glob

# Source directory
sourcedir = path.abspath('fullsize')

# Destination directory
destdir = path.abspath('thumbnails')

def main():
    # Create destination folder if not exist
    if not path.exists(destdir):
        os.mkdir(destdir)

    files = glob(path.join(sourcedir, '*.jpg'))
    
    #print(files)
    for imgfile in files:
        # #print(imgfile)

        # # Create image path
        # imgpath = path.join(sourcedir, imgfile)
        # # print(imgpath)

        # Create image destination patch
        destpath = path.join(destdir, path.basename(imgfile))
        print(destpath)

        # # Open Image
        # image = Image.open(imgpath)

        # Open Image
        image = Image.open(imgfile)

        # Get Image size
        current_size = image.size
        # print(current_size)

        # Get Image width and height
        current_width, current_height = image.size
        # print(current_width, current_height)

        # Get new width by decreasing it by a 1/4
        # using interger division '//'
        new_width = current_width // 4
        # print(new_width)

        # Get new height by decreasing it by a 1/4
        # using interger division '//'
        new_height = current_height // 4
        # print(new_height)

        # Create new image size
        new_size = (new_width, new_height)

        # Make thumbnails of images
        image.thumbnail(new_size)

        # Save new sized image to destpath
        image.save(destpath)

    print(os.listdir(destdir))


if __name__ == '__main__':
    main()