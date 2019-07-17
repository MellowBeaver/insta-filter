#Import image from PIL
from PIL import Image

#Load images into obj
base_img = Image.open("433random.jpg")
img_filter = Image.open("filter1.jpeg")

#Set op img size
size=(760,760)

# Resize all imgs
base_img = base_img.resize(size)
img_filter = img_filter.resize(size)

#Split each img into RGB vectors
r,g,b = base_img.split()
R,G,B = img_filter.split()

#Merge RGB vectors
im=Image.merge("HSV",(r,G,B))
im.show()

# im.save('1_merge.jpg')

# RGB HSV CMYK