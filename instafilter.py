from PIL import Image

base_img = Image.open("433random.jpg")
img_filter = Image.open("filter1.jpeg")

size=(760,760)

base_img = base_img.resize(size)
img_filter = img_filter.resize(size)

r,g,b = base_img.split()
R,G,B = img_filter.split()

im=Image.merge("HSV",(r,G,B))
im.show()

# im.save('1_merge.jpg')

# RGB HSV CMYK