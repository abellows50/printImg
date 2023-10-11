img = "/home/runner/image-printer/img.jpg"

from PIL import Image, ImageOps
import numpy as np
import sys
import os

img = f"{os.getcwd()}/{sys.argv[1]}" 
# creating a image object
im = Image.open(rf"{img}")
try:
  resolution = float(sys.argv[2])
except:
  if im.size[0] >= 140:
    resolution = 140/im.size[1]
  else:
    resolution = 1
  

printIm = im.resize((round(im.size[0]*resolution), round(im.size[1]*resolution*2.3/5)))
printIm = ImageOps.grayscale(printIm)

px = printIm.load()
w,h = printIm.size

output = """"""
for y in range(h):
  for x in range(w):
    if px[x,y] >= 256*4/5:
      output += "X"
    elif px[x,y] >= 256*3/5:
      output += "x"
    elif px[x,y] >= 256*2/5:
      output += ":"
    elif px[x,y] >= 256/5:
      output += "."
    else:
      output += " "
  output += "\n"



try:
  if sys.argv[3] == "file":
    x = open("imageOut.txt", "w")
    x.write(output)
    x.close()
  else:
    print(output)
except:
  print(output)
