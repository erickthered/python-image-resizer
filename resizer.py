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

    def process(self, maxwidth = -1, maxheight = -1):
        self.getFiles()
        for file in self.files:
            try:
                image = Image.open(os.path.join(self.directory, file))
                if maxwidth > 0 and image.width > maxwidth:
                    outfile = os.path.splitext(file)[0] + ".widthresized" + ".".join(os.path.splitext(file)[1:])
                    height = int(maxwidth/image.width * image.height)
                    image = image.resize( (maxwidth, height) )
                    image.save(os.path.join(self.directory, outfile))
                elif maxheight > 0 and image.height > maxheight:
                    outfile = os.path.splitext(file)[0] + ".heightresized" + ".".join(os.path.splitext(file)[1:])
                    width = int(maxheight/image.height * image.width)
                    image = image.resize( (width, maxheight) )
                    image.save(os.path.join(self.directory, outfile))                    
            except IOError:
                pass

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(sys.argv[0], "<path_to_process> <width> <height>")
    else:
        resizer = Resizer(sys.argv[1])
        resizer.process(maxwidth=int(sys.argv[2]), maxheight=int(sys.argv[3]))