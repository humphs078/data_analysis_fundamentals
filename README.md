# data_analysis_fundamentals

Data repository for the Fundamentals of Data Analysis module

## Contents
[Notebooks](#notebooks)

[Tasks](#tasks)

[Task 1 - Collatz-Conjecture](#task-1---collatz-conjecture)

[Project - Iris Data Set Analysis](#project)

## Notebooks
This repository contains 2 Jupyter Notebooks:
1. [tasks](tasks.ipynb) - This note book contains the submission for the topic tasks

## Tasks

### [Task 1 - Collatz Conjecture](/tasks/task_1/collatz.py)
**Task -** *Verify, using Python, that the conjecture is true for the first 10,000 positive integers.*

Named after mathematician Lothar Collatz (https://en.wikipedia.org/wiki/Lothar_Collatz), the Collatz conjecture (https://en.wikipedia.org/wiki/Collatz_conjecture) asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1.

![Collatz Function](/images/illustrations/what-is-the-collatz-conjecture-unsolved-mathematical-problems.png "Collatz Function")

The Collatz conjecture is often thought of as the simplest impossible problem. It has been suggested that a new understanding of maths will be required to solve the Collatz Conjecture. To date the Collatz Conjecture ha*

**Assumptions**
- The script should indicate to the end user if the Collatz Conjecture holds true for the desired range of positive integers.
- If the Collatz conjecture does not hold true for any values, the script should return the values that do not hold true.
- For usability purposes the script should be able to handle any range of input values not just the first 10,000 positive integers.
- The script will not run if negative integers, floating point decimals or strings are entered as arguments.
- If these values are entered as arguments the script will give clear instruction to the end user of the correct format for arguments to be entered.

The script collatz.py runs from the command line and will check if the Collatz Conjecture is true for each number in a range of values. The range of values to be checked are passed as command line arguments. The script will accept a range of positive integer values as an a command line argument. For example to check from 1 to 10000 enter the following command into the bash shell.

```bash
python collatz.py 1 10000
```

The script will output an indication of any values that the Collatz Conjecture does or does not hold true for in the given range.

#### References

Wikipedia. (2022). Lothar Collatz. [online] Available at: https://en.wikipedia.org/wiki/Lothar_Collatz.

#### Background Reading

bobbyhadz.com. (n.d.). Print a List without the Commas and Brackets in Python | bobbyhadz. [online] Available at: https://bobbyhadz.com/blog/python-print-list-without-commas-and-brackets [Accessed 6 Oct. 2023].

Chaudhuri, D.A.K. (2020). Collatz Conjecture-the simplest impossible problem. [online] Cooking Cosmos. Available at: https://asischaudhuri.wordpress.com/2020/11/09/collatz-conjecture/ [Accessed 6 Oct. 2023].

Machine Intelligence ? (2008). LaTeX – Multiline equations, systems and matrices. [online] Available at: https://kogler.wordpress.com/2008/03/21/latex-multiline-equations-systems-and-matrices/ [Accessed 6 Oct. 2023].

www.w3schools.com. (n.d.). Python Try Except. [online] Available at: https://www.w3schools.com/python/python_try_except.asp. [Accessed 6 Oct. 2023].

## Project

**Problem Statement**:
- create a notebook investigating the variables and data points within the well-known iris flower data set associated with Ronald A Fisher.
- in the notebook, you should discuss the classification of each variable within the data set according to common variable types and scales of measurement in mathematics, statistics, and Python.
- Select, demonstrate, and explain the most appropriate summary statistics to describe each variable.
- Select, demonstrate, and explain the most appropriate plot(s) for each variable
- The notebook should follow a cohesive narrative about the data set.
---

### Background

The [Iris Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set) is a data set that consists 50 samples from 
three species of Iris - Iris-setosa, Iris-virginica and Iris-versicolor. Each sample contains 4 measurements:
1. Petal width
2. Petal length
3. Sepal width
4. Sepal length

This data set is an example of a multivariate data set and was popularised by statistician and biologist [Sir Ronald
Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) in his 1936 paper entitled 
[*"The use of multiple measurements in taxonomic problems"*](https://digital.library.adelaide.edu.au/dspace/bitstream/2440/15227/1/138.pdf)
. The data was collected by [Dr. Edgar Anderson](https://en.wikipedia.org/wiki/Edgar_Anderson) from the Gaspé Peninsula
in Canada. Two of the three species were collected from the same meadow, by the same person, using standard equipment 
in order to minimise the risk of variation in the data samples arising from the way in which it was collected and 
measured. Dr. Anderson is recognised as a significant contributor in the field of botanical genetics.

As can be seen from the picture below the appearance of each species is similar. Sir Fisher's Analysis of the data set
enabled accurate classification of the species from petal and sepal measurement and as a result the data set is 
routinely used as a beginners dataset for machine learning purposes.

![image 1](/images/illustrations/Iris_Image.png "Iris Species")

---
