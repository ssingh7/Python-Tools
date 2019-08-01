from PIL import Image
import pytesseract
import cv2
from scipy.misc.pilutil import imread
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(Image.open(r"E:\Tickets.jpg"))
print('Without processing : '+text)
img = cv2.imread(r"E:\Tickets.jpg")
img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
text = pytesseract.image_to_string(img)
print('With processing : '+text)
    


    
