from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import random
import os
import time

# define the extensions, relative path and create the empty list for the images
extensions = ['.png', '.jpg']

boss_path = "./download_image/"

images = []

# add all images paths from the thread's folders to the images lists
for folder, dirs, files in os.walk(boss_path):
    for file in files:
        if file.endswith(tuple(extensions)):
            images.append(os.path.join(folder, file))

# function definition
def degrade_image(image_path, iterations):
    img = Image.open(image_path).convert('RGB')  # convert to rgb mode to edit the image
    img.show() # return not neccesary bc of the .show() function
    
    for i in range(iterations):
        overshared_img = ImageEnhance.Sharpness(img).enhance(100.0) 
        overshared_img.show()
        
# function that enhaces and sharpens the image 
def edge_enhace(image_path, iterations, segs):
    """Function that fries an image (accesses through its path) an specified number of times (iterations),
    returning as the output the before and after of the editing.
    
    Args:
        image_path (str): The path of the image file.
        iterations (int64): The number of times to apply the frying effect to the image.
        segs (float64): The seconds between each image is displayed
    Returns:
        Image: The image before and after applying the frying effect the specified number of times.
    """
    img = Image.open(image_path).convert('RGB') # convert to rgb mode to edit the image
    # print the image before the edit.
    img.show() # return not neccesary bc of the .show() function
    time.sleep(segs)
    for i in range(iterations):
        overshared_img = img.filter(ImageFilter.EDGE_ENHANCE)
        overshared_img_enhaced = ImageEnhance.Sharpness(overshared_img).enhance(20)
        # print the image after the edit# return not neccesary bc of the .show() function
        overshared_img_enhaced.show()
        time.sleep(segs)
        img = overshared_img_enhaced
        # overshared_img.close()
        # overshared_img_enhaced.close()
    #return overshared_img.show()

#for image in random.sample(images, 5):
#   degrade_image(image, 3)

for image in random.sample(images, 15):
   edge_enhace(image, 2, 0.5)