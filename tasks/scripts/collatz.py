# collatz.py
# Author: Sean Humphreys
# Description: Script to test the Collatz Conjecture for the first positive 10,000 integers

# reference - https://www.educative.io/answers/how-to-generate-the-collatz-sequence-in-python
 # https://stackoverflow.com/questions/70434977/collatz-conjecture-and-plotting-hep

import time as t

lower = 1
upper = 10001


def collatz(number):
  collatz_sequence_list=[]
  loop_list = [4, 2, 1]
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
  if loop_list != collatz_sequence_list[-3:]:
   print(f'The Collatz conjecture does not hold true for {collatz_sequence_list[0]}')
  else: 
    print(f'The Collatz Conjecture holds true for {collatz_sequence_list[0]}')
  
 

for y in range(lower, upper):
  collatz(y)
  t.sleep(.1)
