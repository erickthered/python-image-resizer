#!./venv/bin/python

import os
import sys
from PIL import Image

class Resizer():
    def __init__(self, directory):
        self.directory = directory
        self.files = []

    def getFiles(self):
        self.files = [item for item in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, item))]

    def getNewSize(self, oldsize, width = 0, height = 0):
        if (width > 0):
            height = int(width/oldsize[0] * oldsize[1])
        else:
            width = int(height/oldsize[1] * oldsize[0])
        return (width, height)

    def process(self, maxwidth = 0, maxheight = 0):
        self.getFiles()
        for file in self.files:
            try:
                image = Image.open(os.path.join(self.directory, file))
                if maxwidth > 0 and image.width > maxwidth:
                    newSize = self.getNewSize(image.size, width=maxwidth)
                    image = image.resize(newSize)
                    image.save(os.path.join(self.directory, file))
                elif maxheight > 0 and image.height > maxheight:
                    newSize = self.getNewSize(image.size, height=maxheight)
                    image = image.resize(newSize)
                    image.save(os.path.join(self.directory, file))
            except IOError:
                pass

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(sys.argv[0], "<path_to_process> <width> <height>")
    else:
        msg = "WARNING:\nThis program will overwrite any image files "
        msg += "that exceed the given size in pixels, please make sure "
        msg += "that you have a backup.\n"
        msg += "Do you want to proceed? [yes/no]: "
        yesno = input(msg)
        if yesno.lower() == "yes":
            resizer = Resizer(sys.argv[1])
            resizer.process(maxwidth=int(sys.argv[2]), maxheight=int(sys.argv[3]))
        else:
            print ("Nothing has been modified")