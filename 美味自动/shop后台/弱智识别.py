import tesserocr
from PIL import Image
image=Image.open("D:/Desktop/project/code.jpg")

image = image. convert('L')
threshold = 175
table = []
for i in range(256):

    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table,'1')
# image.show()
print(tesserocr.image_to_text(image))