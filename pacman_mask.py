import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Create a mask in the shape of Pacman, starting with the circle
body_mask = np.zeros(image.shape[:2], dtype="uint8")
(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)

cv2.circle(body_mask, (w // 2, h // 2), 100, 255, -1)
body_image = cv2.bitwise_and(image, image, mask=body_mask)
cv2.imshow("Body", body_image)

mouth_mask = np.zeros(image.shape[:2], dtype="uint8")
# mouth = cv2.bitwise_and(image, image, mask=mask)

M = cv2.getRotationMatrix2D((w / 2, h / 2), 45, 1.0)
cv2.rectangle(mouth_mask, (w // 2 + 0, h // 2 + 25), (w // 2 + 100, h // 2 + 125), 255, -1)
rotated = cv2.warpAffine(mouth_mask, M, (w, h))
new_mask = cv2.bitwise_xor(body_mask, rotated)
new_image = cv2.bitwise_and(image, image, mask=new_mask)

cv2.imshow("New image", new_image)

cv2.waitKey(0)
