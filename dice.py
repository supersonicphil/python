
import random
from random import randint

while True:
    x = (randint(1, 6))
    roll=input('do you wish to roll?: ')
    if roll == 'y' or' Y':
        print('The dice has been rolled and is a: ' + str(x))
    else:
        break
        
