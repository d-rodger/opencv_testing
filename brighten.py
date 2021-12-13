import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
group = ap.add_mutually_exclusive_group()
group.add_argument("-b", "--brighter", help="Amount to adjust brighter")
group.add_argument("-d", "--darker", help="Amount to adjust darker")
args = ap.parse_args()
image = cv2.imread(args.image)

amount = 0
if args.brighter:
    amount = int(args.brighter)
if args.darker:
    amount = int(args.darker)

M = np.ones(image.shape, dtype="uint8") * amount
if args.brighter:
    new_image = cv2.add(image, M)
else:
    new_image = cv2.subtract(image, M)
cv2.imshow("Image", image)
cv2.imshow("New Image", new_image)
cv2.waitKey(0)
