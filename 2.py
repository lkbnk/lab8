from PIL import Image
image = {1:'8_1.jpg',2:'8_2.jpg',3:'8_3.jpg'}

print(" С Днём рождения -- 1\n","С Новым годом -- 2\n","С днём победы -- 3")
a = int(input("Введите номер прадника : "))
card = Image.open(image[a])
card.show()