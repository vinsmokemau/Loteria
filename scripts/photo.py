"""Take photos."""
import cv2

from skimage import io
from skimage.color import rgb2gray

import matplotlib.pyplot as plt

webcam = cv2.VideoCapture(0)

check, frame = webcam.read()
cv2.imwrite(filename='saved_img.jpg', img=frame)
webcam.release()
cv2.destroyAllWindows()

image = io.imread('saved_img.jpg')
# plt.figure(1)
# plt.imshow(image)

number1 = image[20:65, 200:240]
# cv2.imwrite(filename='data/3-5.jpg', img=number1)

# plt.figure(2)
# plt.imshow(number1)

number2 = image[20:65, 245:285]
cv2.imwrite(filename='data/5-0.jpg', img=number2)
plt.figure(3)
plt.imshow(number2)
# gray = rgb2gray(image)
"""
gray = (gray * 255) // 1
[rows, columns] = gray.shape

for row in range(rows):
    for column in range(columns):
        if gray[row, column] > 100:
            gray[row, column] = 0
        else:
            gray[row, column] = 255

number1 = gray[20:65, 200:240]
cv2.imwrite(filename='data/0-1.jpg', img=number1)

plt.figure(2)
plt.imshow(number1, cmap='gray')

number2 = gray[20:65, 240:280]
cv2.imwrite(filename='data/x-1.jpg', img=number2)
plt.figure(3)
plt.imshow(number2, cmap='gray')

# number1 = cv2.resize(number1, (28, 28))
"""
plt.show()
