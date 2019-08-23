with open('vegetables.txt', 'a+') as file:
  file.write('\nCucumber')
  file.seek(0)
  print(file.read())