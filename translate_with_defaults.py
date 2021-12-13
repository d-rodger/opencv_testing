import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
ap.add_argument("-x", "--move_x", required=False, default=0, help="Amount to translate x")
ap.add_argument("-y", "--move_y", required=False, default=0, help="Amount to translate y")
args = vars(ap.parse_args())

M = np.float32([[1, 0, args["move_x"]], [0, 1, args["move_y"]]])
image = cv2.imread(args["image"])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Image", image)
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)
