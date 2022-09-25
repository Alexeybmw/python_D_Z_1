def inputNumbers(x):
      xy = ["X","Y"]
      for i in range(x):
            number = int(input(f'Введите координату по {xy[i]}: '))

def calculateLenghtSegment(a,b):
      lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0,5)
      return lengthSegment

print("Ведите координаты точки A")
pointA = inputNumbers(2)
print("Введите координаты точки B")
pointB = inputNumbers(2)

print (f"Длинна отрезка: {format (calculateLenghtSegment(pointA, pointB))} .2f")