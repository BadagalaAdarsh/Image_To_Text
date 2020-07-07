#Working

#this code worked after installing tesseract-ocr
#command to install in sudo apt-get install tesseract-ocr
import pytesseract
from PIL import Image

img = Image.open('Adarsh.png')
text = pytesseract.image_to_string(img)
print(text)

#for writing into file

with open('wiki.xlsx',mode='w') as file:
    file.write(text)
    print(text)