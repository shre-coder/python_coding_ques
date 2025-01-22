import PIL
from PIL import Image

img = PIL.Image.open("C:/Users/lodhi/Desktop/1736916039312.jpeg")

width, height = img.size
# print(img.size)
print(width, "x", height)
