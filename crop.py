import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
ap.add_argument("-x", required=True, help="Start x position for crop")
ap.add_argument("-y", required=True, help="Start y position for crop")
ap.add_argument("-w", required=True, help="Width for crop")
ap.add_argument("-ht", required=True, help="Height for crop")
args = ap.parse_args()
image = cv2.imread(args.image)

x = int(args.x)
y = int(args.y)
w = int(args.w)
h = int(args.ht)
crop = image[y:h, x:w]
cv2.imshow("Image", image)
cv2.imshow("Cropped", crop)
cv2.waitKey(0)
