"""Tesseract test."""
import cv2
import pytesseract
import matplotlib.pyplot as plt

webcam = cv2.VideoCapture(0)
check, frame = webcam.read()
cv2.imwrite(filename='saved_img.jpg', img=frame)
webcam.release()
cv2.destroyAllWindows()

imagen = cv2.imread('saved_img.jpg')
plt.figure()
plt.imshow(imagen[380:460, 150:480])

text = pytesseract.image_to_string(imagen[380:460, 150:480]).lower()

print(text)

plt.show()
