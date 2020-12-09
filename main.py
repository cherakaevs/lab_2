from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
circle = True
while circle:
       path = input("Введите путь до файла:")
       root_ext = os.path.splitext(path)
       if os.path.isfile and (root_ext[1] == ('.png')):
              lena = Image.open(path)

              arr = np.asarray(Image.open('Lena.png', 'r'))

              print(arr)

              MinColorChannel = np.amin(arr, axis=(0, 1))
              print('Минимальные значения каналов изображения:')
              print('Красный:', MinColorChannel[0])
              print('Зеленый:', MinColorChannel[1])
              print('Синий:', MinColorChannel[2])

              MaxColorChannel = np.amax(arr, axis=(0, 1))
              print('Максимальные значения каналов изображения:')
              print('Красный:', MaxColorChannel[0])
              print('Зеленый:', MaxColorChannel[1])
              print('Синий:', MaxColorChannel[2])

              AverageColorChannel = np.mean(arr, axis=(0, 1))
              print('Средние значения каналов изображения:')
              print('Красный:', AverageColorChannel[0])
              print('Зеленый:', AverageColorChannel[1])
              print('Синий:', AverageColorChannel[2])

              arr = np.uint8(arr[0:512, 0:512, 0] * 0.299 + arr[0:512, 0:512, 1] * 0.587 + arr[0:512, 0:512, 2] * 0.114)

              img = Image.fromarray(arr)
              img.save('lena_grayscaled.png')


              print(arr)

              np.putmask(arr, arr < 100, 0)

              print(arr)

              img = Image.fromarray(arr)
              img.save('lena_thresholded.png')


              unique, counts = np.unique(arr, return_counts=True)
              print(counts)
              fig = plt.figure()
              ax = fig.add_subplot(111)

              fig.set(facecolor = 'floralwhite')
              ax.set(facecolor = 'seashell',
                     xlim=[0, 255],
                     ylim=[0, 3000],
                     title='Яркость изображения',
                     xlabel='Яркость пикселя',
                     ylabel='Количетсво пикселей')

              ax.bar(unique, counts)
              plt.show()
              circle = False
       else:
              print('Неверный путь до файла, попробуйте заново.')











