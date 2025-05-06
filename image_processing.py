# image_processing.py

import pytesseract
from PIL import Image

# Set the correct path to tesseract binary for Linux (Render uses Debian-based systems)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def extract_text_from_image(image_file):
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)
    return text


