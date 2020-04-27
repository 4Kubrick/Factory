from abc import ABC, abstractmethod
import cv2
import numpy as np


class ImageEdit(ABC):
    @abstractmethod
    def __call__(self):
        pass

    def img_operation(self, img):
        pass


class RotateImage(ImageEdit):
    def __call__(self):
        pass

    def img_operation(self, image, angle=90):
        if image is not None:
            image_center = tuple(np.array(image.shape[1::-1]) / 2)
            rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
            result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
            return result


class InversImage(ImageEdit):
    def __call__(self):
        pass

    def img_operation(self, image):
        if image is not None:
            th, im_th = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY_INV)
            im_floodfill = im_th.copy()
            h, w = im_th.shape[:2]
            mask = np.zeros((h + 2, w + 2), np.uint8)
            cv2.floodFill(im_floodfill, mask, (0, 0), 255)
            im_floodfill_inv = cv2.bitwise_not(im_floodfill)
            im_out = im_th | im_floodfill_inv
            return im_th



class SmoothingImage(ImageEdit):
    def __call__(self):
        pass

    def img_operation(self, img):
        return cv2.blur(img, (5, 5))