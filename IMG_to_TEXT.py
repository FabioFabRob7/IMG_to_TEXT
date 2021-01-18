import cv2
import pytesseract
import webbrowser

webbrowser.open("https://github.com/UB-Mannheim/tesseract/wiki")
input("Install relase of tesseract from github then press enter. . .")
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
PATH_IMG = input("Insert directory of an image with text: ")
img = cv2.imread(PATH_IMG)
text = pytesseract.image_to_string(img)
print(text)