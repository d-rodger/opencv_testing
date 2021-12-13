import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
ap.add_argument("-r", "--rotate", required=False, default=45, help="Amount to rotate")
ap.add_argument("-s", "--scale", required=False, default=1.0, help="Amount to scale")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

(cY, cX) = image.shape[:2]
M = cv2.getRotationMatrix2D((cX, cY), int(args["rotate"]), float(args["scale"]))
rotate = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Image", image)
cv2.imshow("Rotated", rotate)
cv2.waitKey(0)
