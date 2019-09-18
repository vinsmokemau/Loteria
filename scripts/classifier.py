"""."""
import cv2

import numpy as np

import matplotlib.pyplot as plt

from skimage import io
from skimage.color import rgb2gray

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

"""
webcam = cv2.VideoCapture(0)

check, frame = webcam.read()
cv2.imwrite(filename='saved_img_test.jpg', img=frame)
webcam.release()
cv2.destroyAllWindows()
"""

image = io.imread('saved_img2.jpg')
gray = rgb2gray(image)
gray = (gray * 255) // 1
[rows, columns] = gray.shape

for row in range(rows):
    for column in range(columns):
        if gray[row, column] > 50:
            gray[row, column] = 0
        else:
            gray[row, column] = 255

gray = gray / 255

number1 = gray[15:60, 200:235]
number1 = cv2.resize(number1, (28, 28))

plt.figure(1)
plt.imshow(number1, cmap='gray')

number2 = gray[15:60, 240:275]
number2 = cv2.resize(number2, (28, 28))

plt.figure(2)
plt.imshow(number2, cmap='gray')

mnist = fetch_openml('mnist_784')
X = mnist['data'][:40000, :]
y = mnist['target'][:40000]

y = y.astype("int32")
X = X / 255

train_X, test_X, train_y, test_y = train_test_split(X, y)

clf = MultinomialNB()
clf.fit(train_X, train_y)

n1 = number1.reshape(784)
n2 = number2.reshape(784)

numbers = np.array([n1, n2])

predictions = clf.predict(numbers)
print(predictions)

plt.show()
