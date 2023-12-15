import requests
from PIL import Image
from io import BytesIO
import os

def savePicture(urls):
    for url in urls:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        filename = os.path.basename(url)
        img.save(f"image/{filename}")
