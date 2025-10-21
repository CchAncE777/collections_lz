import numpy #Импорт
import matplotlib.pyplot as plt #Импорт

x = numpy.linspace(0, 10, 50) #Область определения X и количество точек функции
y = x**3 + 1 #Сама функция
plt.plot(x, y) #Связывание функции. Область определния и область значения
plt.show() #Показать функцию