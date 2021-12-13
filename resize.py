import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
group = ap.add_mutually_exclusive_group()
group.add_argument("-w", "--width", help="New width")
group.add_argument("--height", help="New height")
args = ap.parse_args()
image = cv2.imread(args.image)

new_width = None
new_height = None

if args.width:
    new_width = int(args.width)
if args.height:
    new_height = int(args.height)

if new_width:
    ratio = new_width / image.shape[1]
    new_height = int(image.shape[0] * ratio)
if new_height:
    ratio = new_height / image.shape[0]
    new_width = int(image.shape[1] * ratio)

resized = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Image", image)
cv2.imshow("Resized", resized)
cv2.waitKey(0)
