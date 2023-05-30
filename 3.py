from PIL import Image, ImageDraw, ImageFont

name = input("Кого хотите поздравить: ")
image = Image.open('8_1.jpg')
font = ImageFont.truetype("arial_bold.ttf", 22)
draw = ImageDraw.Draw(image)
draw.text((110,80), name + ", поздравляю, " , font = font, fill = "#FF00FF")
image.show()
image.save(name + 'card.png')