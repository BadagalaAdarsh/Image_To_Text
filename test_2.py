#importing pytesseract for conversion of image to text
import pytesseract

#adding image processing capabilities to the code through Image importing from PIL
from PIL import Image

#for conversion of text to speech
import pyttsx3

#following library is for translation into given langugae
from googletrans import Translator

img = Image.open('hai.JPG')

print(img)

text = pytesseract.image_to_string(img, lang='eng')
# writing text to the text file and saving it to the file

with open('Check.txt',mode='w') as file:
    file.write(text)
    print(text)

# P = Translator()
#
# k = P.translate(text,dest='german')
# print(k)
#
# engine  = pyttsx3.init()
#
# engine.say(k)
#
# engine.runAndWait()
