# collatz.py
# Author: Sean Humphreys
# Description: Script to test the Collatz Conjecture for the first positive 10,000 integers

# reference - https://www.educative.io/answers/how-to-generate-the-collatz-sequence-in-python

def collatz(number):
  lst=[]
  lst.append(number)
  while(number!=1):
      if(number%2==0):
          number=number//2
          lst.append(number)
      else:
          number=number*3+1
          lst.append(number)
  print(lst)


collatz(999)
