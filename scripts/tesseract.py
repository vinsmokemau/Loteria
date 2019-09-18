import cv2
import pytesseract

webcam = cv2.VideoCapture(0)
check, frame = webcam.read()
cv2.imwrite(filename='saved_img.jpg', img=frame)
webcam.release()
cv2.destroyAllWindows()

imagen = cv2.imread('saved_img.jpg')
    
text = pytesseract.image_to_string(imagen)

print(text)
