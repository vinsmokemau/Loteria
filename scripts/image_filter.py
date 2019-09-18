"""Processing Image."""
import cv2
from skimage import io
from skimage.color import rgb2gray

import matplotlib.pyplot as plt


image = io.imread('saved_img.jpg')
gray = rgb2gray(image)
gray = (gray * 255) // 1
[rows, columns] = gray.shape

for row in range(rows):
    for column in range(columns):
        if gray[row, column] > 100:
            gray[row, column] = 0
        else:
            gray[row, column] = 255

gray = gray / 255

number1 = gray[15:60, 200:235]

plt.figure(1)
plt.imshow(number1, cmap='gray')

number2 = gray[15:60, 240:275]

plt.figure(2)
plt.imshow(number2, cmap='gray')

# number1 = cv2.resize(number1, (28, 28))

plt.show()
