from PIL import Image, ImageDraw, ImageFont

n = input("Введите имя получателя: ")
im = Image.open('8_1.jpg')
f = ImageFont.truetype("arial_bold.ttf", 20)
draw = ImageDraw.Draw(im)
draw.text((100,85), n + ", поздравляю, " , font = f, fill = "#E6399B")
im.show()
im.save(n + 'otkr.png')