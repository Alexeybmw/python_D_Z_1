from distutils.command.check import check


def inputNumbers(x):
      xyz = ["X","Y","Z"]
      a = []
      for i in range(x):
            numbert = int(input(f'Введите значение {xyz[i]}: '))

def checkPredicate(x):
      left = not (x[0] or x[1] or x[2])
      rigth = not x[0] and not x[1] and not x[2]
      result = left == rigth
      return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
      print (f'Истина')
else:
      print (f'Ложно')