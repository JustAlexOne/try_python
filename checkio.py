import io
import os

from PIL import Image, ImageChops


def compare_images(path_one, path_two, diff_save_location):
    """
    Compares to images and saves a diff image, if there
    is a difference

    @param: path_one: The path to the first image
    @param: path_two: The path to the second image
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)

    diff = ImageChops.difference(image_one, image_two)

    if diff.getbbox():
        diff.save(diff_save_location)

path1 = os.path.join(os.getcwd(), 'Screen1.png')
path2 = os.path.join(os.getcwd(), 'Screen2.png')
diff = os.path.join(os.getcwd(), 'diff.jpg')

compare_images(path1, path2, diff)