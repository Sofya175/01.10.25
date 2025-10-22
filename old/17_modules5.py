# Дополнительно устанавливаемые модули
# Модуль графики PIL (Python Imaging Library - pillow)
# PIP - Python Installation Package
# pip install pillow
from PIL import Image, ImageFilter

image = Image.open('images/Python.jpg')
pixel = image.load()  # загрузить массив пикселей
w, h = image.size

# Размытие
blur = image.filter(ImageFilter.GaussianBlur(2.5))

blur.save('images/python3.jpg')

# Вырезем кусок
cropped =image.crop(
    (140, 40, 390, 280)
)
cropped.save('images/python4.jpg')

# Контуры
contour = image.filter(ImageFilter.CONTOUR)
contour.save('images/python5.jpg')

# отражение по горизонтали
h_mirror = image.transpose(Image.FLIP_LEFT_RIGHT)
h_mirror.save('images/python6.jpg')

# отражение по вертикали
v_mirror = image.transpose(Image.FLIP_TOP_BOTTOM)
v_mirror.save('images/python7.jpg')
# image.show()
