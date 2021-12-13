import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
ap.add_argument("-x", "--move_x", required=False, default=0, help="Amount to translate x")
ap.add_argument("-y", "--move_y", required=False, default=0, help="Amount to translate y")
ap.add_argument("-r", "--rotate", required=False, default=45, help="Amount to rotate")
ap.add_argument("-s", "--scale", required=False, default=1.0, help="Amount to scale")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

MT = np.float32([[1, 0, args["move_x"]], [0, 1, args["move_y"]]])
shifted = cv2.warpAffine(image, MT, (image.shape[1], image.shape[0]))

(cY, cX) = image.shape[:2]
MR = cv2.getRotationMatrix2D((cX, cY), int(args["rotate"]), float(args["scale"]))
rotate = cv2.warpAffine(image, MR, (image.shape[1], image.shape[0]))

shifted_and_rotate = cv2.warpAffine(shifted, MR, (image.shape[1], image.shape[0]))

cv2.imshow("Image", image)
cv2.imshow("Shifted", shifted)
cv2.imshow("Rotated", rotate)
cv2.imshow("Shifted and Rotated", shifted_and_rotate)
cv2.waitKey(0)
