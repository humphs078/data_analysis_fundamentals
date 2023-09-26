# collatz.py
# Author: Sean Humphreys
# Description: Script to test the Collatz Conjecture for the first positive 10,000 integers

# reference - https://www.educative.io/answers/how-to-generate-the-collatz-sequence-in-python

lower = 1
upper = 10001

def collatz(number):
  collatz_sequence_list=[]
  loop_list = [4, 2, 1]
  if number == 1:
    collatz_sequence_list = [4, 2, 1]
  elif number == 2:
    collatz_sequence_list = [1, 4, 2, 1]
  else:
    collatz_sequence_list.append(number)
    while(number!=1):
      if(number%2==0):
        number=number//2
        collatz_sequence_list.append(number)
      else:
        number=number*3+1
        collatz_sequence_list.append(number)
  # validate that the last three numbers of the list are equal to the collatz sequence loop
  # print(collatz_sequence_list[-3:])
  # print(collatz_sequence_list)
  # print(collatz_sequence_list[0])
  if loop_list != collatz_sequence_list[-3:]:
   print(f'The Collatz conjecture does not hold true for {collatz_sequence_list[0]}')
  elif collatz_sequence_list[0] == 10000 and loop_list == collatz_sequence_list[-3:]:
    print(f'If this text is displaying the Collatz Conjecture holds true for all numbers in the range of {lower} to {upper}')
 


for y in range(lower, upper):
  collatz(y)
