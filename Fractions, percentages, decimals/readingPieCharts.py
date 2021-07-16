import random
import math
import numpy as np, numpy.random

def formatNumber(num):
  if num % 1 == 0:
    return int(num)
  else:
    return num

_sum = 100
n = 4
values = np.random.multinomial(_sum, np.ones(n)/n, size=1)[0]


shoppers = math.ceil(random.randint(100, 1000) / 10.0) * 10 #Round to nearest 10

potato = values[0]
carrot = values[1]
broccoli = values[2]
beetroot = values[3]

vegetables = [potato, carrot, broccoli, beetroot]

vegetable = random.choice(vegetables)
Question = str(shoppers) + ' shoppers are asked about their favourite vegetables. How many like ' + str(vegetable) + '?'
if isinstance(formatNumber((vegetable/100) * shoppers), int):
    Answer = (vegetable/100) * shoppers
    print(Question)
    print(vegetable, shoppers, Answer) 
else:
    print('')

