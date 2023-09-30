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

# this function return a list of values where the Collatz conjecture does not hold true for the given range
def wrong_list(lower, upper):
    wrong_list = []
    for i in range(lower, upper):
        if len(collatz(i)) == 1:
            wrong_list.append(i)
    return (wrong_list)

# this function returns a list of values where the Collatz conjecture holds true the given range
def right_list(lower, upper):
    right_list = []
    for i in range(lower, upper):
        if len(collatz(i)) > 1:
            right_list.append(i)
    return (right_list)

# this function prints the list of numbers that either are true or false for the Collatz conjecture in a given range
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

# test that functions work when all conditions are met
if __name__ == "__main__":
    lower_limit = 1
    upper_limit = 11
    result(lower_limit, upper_limit)

    # test that function will return a list of the numbers where Collatz does not hold true

    # function to verify the Collatz conjecture holds true for a positive integer, note that the loop list and length of values have been changed so that the range of values to be tested will not meet the criteria for Collatz. 
    def collatz(number):
        collatz_sequence_list = []
        wrong_list = []
        loop_list = [4, 2, 1]
        if number == 1:
            # to test 1 the 4,2,1 loop needs to be included to test against
            collatz_sequence_list = [13, 1, 4, 2, 1]
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
        if loop_list != collatz_sequence_list[-4:]:
            wrong_list.append(collatz_sequence_list[0])
            return wrong_list
        else:
            return collatz_sequence_list

    # this function return a list of values where the Collatz conjecture does not hold true for the given range
    def wrong_list(lower, upper):
        wrong_list = []
        for i in range(lower, upper):
            if len(collatz(i)) == 1:
                wrong_list.append(i)
        return (wrong_list)

    # this function returns a list of values where the Collatz conjecture holds true the given range
    def right_list(lower, upper):
        right_list = []
        for i in range(lower, upper):
            if len(collatz(i)) > 1:
                right_list.append(i)
        return (right_list)

    # this function prints the list of numbers that either are true or false for the Collatz conjecture in a given range
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

    lower_limit = 1
    upper_limit = 11
    result(lower_limit, upper_limit)
