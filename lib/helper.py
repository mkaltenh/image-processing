import numpy as np
import cv2
import logging
from PIL import Image

class OpenCVHelper():
  def __init__(self):
    print("Loaded OpenCV Helper")
    self._logger = logging.getLogger(__name__)

  def display_image(self, image, resize_factor=None):
    """
    Display a cv2 image by converting it to PIL and calling the display() function.
    This is a workaround for Jupyter Notebook as it doesnt support cv2.imshow()
    
    :param np_array img: cv2 Image data
    """
    # pil images
    if Image.isImageType(image):
            out = image

    # cv2 images
    elif isinstance(image, np.ndarray):
        if isinstance(image[0][0], np.uint8):
            _io = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        elif isinstance(image, np.ndarray) and len(image[0][0]) == 3:
            _io = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        elif isinstance(image, np.ndarray) and len(image[0][0]) == 4:
            _io = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
        else:
            _io = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        out = Image.fromarray(_io)

    # path to image
    elif isinstance(image, str):
        out = Image.open(image)

    if resize_factor:
        width, height = out.size
        self._logger.info("Resizing by factor %s" % resize_factor)
        out = out.resize((int(width * resize_factor), int(height * resize_factor)), Image.ANTIALIAS)
    
    return out