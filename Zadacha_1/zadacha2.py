def inputKoord(x):
      for i in range(x):
           number = float(input(f'Введите {i + 1} координату: '))
            
     
def checkCoordinates(xy):
      text = 4
      if xy[0] > 0 & xy[1] > 0:
            text = 1
      elif  xy[0] < 0 & xy[1] > 0:
            text = 2
      elif  xy[0] < 0 & xy[1] < 0:
            text = 3
      print (f'Точка находится в {text} четверти плоскости')

koordinate = inputKoord()
checkCoordinates(koordinate)