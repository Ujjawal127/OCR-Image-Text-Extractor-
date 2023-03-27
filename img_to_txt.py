from PIL import Image
import pytesseract


image_path = input("Enter path to image file: ")


img = Image.open(image_path)


text = pytesseract.image_to_string(img)


print(text)