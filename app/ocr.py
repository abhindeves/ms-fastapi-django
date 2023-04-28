import pathlib
import pytesseract
from PIL import Image

BASE_DIR = pathlib.Path(__file__).parent
IMG_DIR = BASE_DIR / "images"

img_path = IMG_DIR / "Screenshot (2).png"

img = Image.open(img_path)


pred = pytesseract.image_to_string(img)

print(pred)