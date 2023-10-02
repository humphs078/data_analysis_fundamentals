# data_analysis_fundamentals

Data repository for the Fundamentals of Data Analysis module

## Tasks

### Task 1 - Collatz Conjecture
*Verify, using Python, that the conjecture is true for the first 10,000 positive integers.*

Named after mathematician Lothar Collatz (https://en.wikipedia.org/wiki/Lothar_Collatz), the Collatz conjecture (https://en.wikipedia.org/wiki/Collatz_conjecture) asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1.

$f(n) = \begin{cases} n/2 &\text{if } n \equiv 0 \\
(3n +1)/2 & \text{if } n \equiv 1 \end{cases}$

The Collatz conjecture is often thought of as the simplest impossible problem. It has been suggested that a new understanding of maths will be required to solve the Collatz Conjecture. To date the Collatz Conjecture ha



The script collatz.py runs from the command line and will check if the Collatz Conjecture is true for each number in a range of values. The range of values to be checked are passed as command line arguments. The script will accept a range of positive integer values as an a command line argument. For example to check from 1 to 10000 enter the following command into the bash shell.

```bash
python collatz.py 1 10000
```

The script will output an indication of any values that the Collatz Conjecture does or does not hold true for in the given range.


References: https://kogler.wordpress.com/2008/03/21/latex-multiline-equations-systems-and-matrices/
