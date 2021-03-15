# Напишите код на Python, реализующий расчет длины вектора, заданного его координатами. (в программе)
import math

vector = [10, 10, 0]
print(math.sqrt(sum([el ** 2 for el in vector])))
