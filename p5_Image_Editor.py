import os

from PIL import Image, ImageEnhance, ImageFilter

# Path for the image and the new image
path = './images/'
pathOut = './images/out/'

for filename in os.listdir(path):
    if filename.endswith('.jpg'):
        img = Image.open(path + filename)
        # Convert to grayscale
        img = img.convert('L')
        # Apply a filter
        img = img.filter(ImageFilter.SHARPEN)
        # Apply a contrast
        img = ImageEnhance.Contrast(img).enhance(1.5)
        # Save the image
        img.save(pathOut + filename)
        print('Image saved: ' + filename)
    else:
        print('Not an image: ' + filename)

# Path: p6_Image_Editor.py
