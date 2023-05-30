from PIL import Image
image = Image.open('8_1.jpg')
image.crop((60,90,250,250)).save('8_1_1.jpg')