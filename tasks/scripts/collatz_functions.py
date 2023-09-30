# functions.py
# Author: Sean Humphreys
# File that contains functions created for use in testing the Collatz Conjecture

# function to verify the Collatz conjecture holds true for a positive integer
def collatz(number):
    collatz_sequence_list = []
    wrong_list = []
    loop_list = [4, 2, 1]
    if number == 1:
        # to test 1 the 4,2,1 loop needs to be included to test against
        collatz_sequence_list = [1, 4, 2, 1]
    elif number == 2:
        # to test 2 the 4,2,1 loop needs to be included to test against
        collatz_sequence_list = [2, 4, 2, 1]
    else:
        collatz_sequence_list.append(number)
        while (number != 1):
            if (number % 2 == 0):
                number = number//2
                collatz_sequence_list.append(number)
            else:
                number = number*3+1
                collatz_sequence_list.append(number)
    if loop_list != collatz_sequence_list[-3:]:
        wrong_list.append(collatz_sequence_list[0])
        return wrong_list
    else:
        return collatz_sequence_list


def wrong_list(lower, upper):
    wrong_list = []
    for i in range(lower, upper):
        if len(collatz(i)) == 1:
            wrong_list.append(i)
    return (wrong_list)


def right_list(lower, upper):
    right_list = []
    for i in range(lower, upper):
        if len(collatz(i)) > 1:
            right_list.append(i)
    return (right_list)


def result(lowest_number, highest_number):
    wrong_list_var = wrong_list(lowest_number, highest_number)
    right_list_var = right_list(lowest_number, highest_number)
    string = 'The numbers that Collatz Conjecture does not hold true for are: '
    result = ', '.join(str(item) for item in wrong_list_var)
    if len(wrong_list_var) > 0:
        print(string + result)
    elif len(right_list_var) > 0:
        print(
            f'The Collatz Conjecture holds true for the numbers from {lowest_number} up to and including {highest_number-1}.')


# test function - execute Code When the File Runs as a Script, but Not When It’s Imported as a Module
# https://realpython.com/if-name-main-python/ accessed 27/04/2023
if __name__ == "__main__":
    lower_limit = 1
    upper_limit = 11
    result(lower_limit, upper_limit)
