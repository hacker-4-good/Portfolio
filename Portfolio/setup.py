from PIL import Image
from rembg import remove

output = remove(Image.open("Portfolio/Images/hi.png")).save("Portfolio/Images/3.png")