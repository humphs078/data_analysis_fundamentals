# collatz.py
# Author: Sean Humphreys
# Script to test the Collatz Conjecture from a range of integers read in from the command line as an argument.

# import required libraries
import collatz_functions as sh
import sys

try:
    low_number = int(sys.argv[1]) # cast to int
    high_number = int(sys.argv[2]) + 1 # need to add 1 for desired range
    if low_number > 0 and low_number < high_number:
        sh.result(low_number, high_number)
    elif low_number > 0 and high_number < low_number:
        print(f'{high_number} is lower than {low_number}. The script requires that the second argument is greater than'
              f' the first. Please run the script again with the correct parameters.')
    else:
        print(f'{low_number} is not a positive integer. Please run the script again and enter a positive integer as '
              f'an argument.')
except ValueError: # error handling
    print(f'Please enter a positive integer as an argument.')
except IndexError: # error handling
    print('Please enter two command line arguments. The arguments must be positive integers with the first number '
          f'greater than the second number.')
