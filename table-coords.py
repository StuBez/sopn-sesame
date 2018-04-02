import os
import sys

import cv2

if len(sys.argv) < 2:
    sys.exit('Usage: {0} Image file name'.format(sys.argv[0]))

path = sys.argv[1]
shortname, extension = os.path.splitext(path)
extension = extension.lstrip('.')

if not os.path.exists(path):
    sys.exit('ERROR: File {0} was not found'.format(path))

# List of rectangles that have been found
rectangles = []

img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, img_w, img_h = img.shape[::-1]
_, contours, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i, contour in enumerate(contours):
    perimeter = cv2.arcLength(contour, True)

    if 500 < perimeter < 1500:
        rectangles.append(cv2.boundingRect(contour))

        # Calculate a bounding rectangle from the contour and get the dimensions
        x, y, w, h = cv2.boundingRect(contour)

        # Add the rectangle in green on the original image
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # The y position on a PDF starts from the top and the bottom in the image.
        # We convert from image to PDF y by subtracting the image height from the y and adding the height.
        pdf_y = str(abs(y - img_h + h))
        # Add some debugging info in each rectangle so we can see which text part in the XML file relates to this.
        cv2.putText(img, 'x:' + str(x) + ', y:' + str(y) + ' (' + pdf_y + ')', (x + 10, y + 15),
                    cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
        cv2.putText(img, 'w:' + str(w) + ', h:' + str(h), (x + 10, y + 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))

# Debug: Ucomment to load image
# cv2.imshow("Output", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

filename = '{0}-processed.{1}'.format(shortname, extension)
cv2.imwrite(filename, img)
print('Saved processed {0} as {1}'.format(extension.upper(), filename))
