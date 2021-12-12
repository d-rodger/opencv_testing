import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
ap.add_argument("-x", "--move_x", required=True, help="Amount to translate x")
ap.add_argument("-y", "--move_y", required=True, help="Amount to translate y")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
M = np.float32([[1, 0, args["move_x"]], [0, 1, args["move_y"]]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Original", image)
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)
