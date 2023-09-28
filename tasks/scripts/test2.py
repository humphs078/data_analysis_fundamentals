# collatz.py
# Author: Sean Humphreys
# Description: Script to test the Collatz Conjecture for the first positive 10,000 integers

# reference - https://www.educative.io/answers/how-to-generate-the-collatz-sequence-in-python
 # https://stackoverflow.com/questions/70434977/collatz-conjecture-and-plotting-hep

import time as t
from numba import jit

lower = 1
upper = 10001


def collatz(number):
  collatz_sequence_list=[]
  wrong_list=[]
  loop_list = [16, 8, 4, 2, 1]
  if number == 1:
    collatz_sequence_list = [1 ,4, 2, 1]
  elif number == 2:
    collatz_sequence_list = [2, 4, 2, 1]
  else:
    collatz_sequence_list.append(number)
    while(number!=1):
      if(number%2==0):
        number=number//2
        collatz_sequence_list.append(number)
      else:
        number=number*3+1
        collatz_sequence_list.append(number)
  if loop_list != collatz_sequence_list[-5:]:
    wrong_list.append(collatz_sequence_list[0])
  else:
    print(f'{collatz_sequence_list[0]} - yes')
  return wrong_list
 
starttime = t.time()

wrong_list_2=[]
#@jit
def mult(lower, upper):
    wrong_list_2=[]
    for y in range(lower, upper):
        if len(collatz(y)) >0:
            wrong_list_2.append(collatz(y))
    print(f'{(*wrong_list_2, sep=\'\')} - no')
    #for item in wrong_list_2:
     #   print(item[0], ', '.join(map(str, item[1:])))


mult(1, 10001)

endtime = t.time()
elapsed = endtime-starttime
print(elapsed)

#  #t.sleep(.1)
