# Дополнительно устанавливаемые модули
# Модуль графики PIL (Python Imaging Library - pillow)
# PIP - Python Installation Package
# pip install pillow
# Создание и рисование
from PIL import Image, ImageFilter, ImageDraw

#image = Image.open('images/python.jpg')

# 1. Создание холста#
#new_image = Image.new('RGB', (600, 400), (255, 0, 255))
#new_image.save('images/canvas.jpg')

#------------
# 2. Создание холста
new_image = Image.new('RGB', (600, 400), (180, 180, 180))
#new_image.save('images/canvas.jpg')

# создаем объект для рисования и указываем на чем рисовать
draw = ImageDraw.Draw(new_image)
# Рисуем прямоугольник по контуру
draw.rectangle((0, 0, 599, 399), outline=(0, 0, 255), width=3)

# Рисуем линию, разделяющую холст пополам
#draw.line((299, 0, 299, 399), fill=(0, 0, 255), width=3)
draw.line((0, 0, 599, 399), fill=(0, 0, 255), width=3)
draw.line((599, 0, 0, 399), fill=(0, 0, 255), width=3)

new_image.draw('images/canvas.jpg')

# cropped = image.crop(
#     (140, 40, 390, 280)
# # )
# new_size = image.resize((150, 100))
#
# # new_image.paste(cropped, (100, 100))
# new_image.paste(new_size, (180, 120))
# draw = ImageDraw.Draw(new_image)
# draw.rectangle((180, 120, 330, 220), outline=(0, 0, 255), width=5)
# #draw.rectangle((180, 120, 330, 220), outline=(0, 0, 255), width=5, fill=(255, 255,0))
# #new_image.save('images/canvas.jpg')
#
# #------------
# # Создание холста
# new_image = Image.new('RGB', (600, 400), (180, 180, 180))
#new_image.save('images/canvas.jpg')
