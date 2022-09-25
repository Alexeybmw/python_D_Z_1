def InputDay(inputText):
     
      day = int(input(f'{inputText}'))
     

def checkDay(day):
      if day == 6 or day == 7:
            print(f'Выходной')
      
      else:
            print(f'Не выходной')


day = InputDay("Введите день недели: ")
checkDay(day)
