import random

n = int(input('Quantidade de numeros: '))
circle = 0
square = 0
for i in range(n):
  r = random.random()
  g = random.random()
  result = (r**2)+(g**2)

  if (result <= 1):
    circle += 1
  square += 1

print((circle/square)*4)