import time
import os

while True:
  if os.path.exists('vegetables.txt'):
    with open('vegetables.txt') as file:
      print(file.read())
  else:
    print("File doesn't exist")
  time.sleep(5)