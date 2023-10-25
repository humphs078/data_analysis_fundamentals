# Fundamentals of Data Analysis Module Repository
![python_logo](/images/illustrations/python_logo_mod_sh_title.png) ![jupyter_logo](/images/illustrations/jupyter_logo_mod_sh_title.png) ![markdown_logo](/images/illustrations/markdown_title.png) ![laytex_logo](/images/illustrations/laytex_title.png)

Author: Sean Humphreys

Data repository for the Fundamentals of Data Analysis module

## Contents

1. [Jupyter Notebooks](#jupyter-notebooks)

1. [Tasks](#tasks)

    1. [Task 1 - Collatz-Conjecture](#task-1---collatz-conjecture)
    2. [Task 2 - Penguins Variables](#task-2---penguins-variables)
    3. [Task 3 - Penguins Probability Distribution](#task-3---penguins-probability-distribution)

2. [Project - Iris Data Set Analysis](#project)
---
## Jupyter Notebooks  ![jupyter_logo](/images/illustrations/jupyter_logo_mod_sh.png)

Jupyter Notebooks are an interactive way to explain code, visualize data and share your ideas with others. Further information on Jupyter Notebooks can be found [here](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html).

This repository contains two Jupyter Notebooks:
1. [tasks.ipynb](tasks.ipynb) - The *Tasks Jupyter Notebook* contains the submission for the module tasks.
2. [project.ipynb](project.ipynb) - The *Project Jupyter Notebook* contains the submission for the module project.
---
## Tasks

### [Task 1 - Collatz Conjecture](/tasks/task_1/collatz.py)
**Task -** *Verify, using Python, that the conjecture is true for the first 10,000 positive integers.*

Named after mathematician Lothar Collatz (https://en.wikipedia.org/wiki/Lothar_Collatz), the Collatz conjecture (https://en.wikipedia.org/wiki/Collatz_conjecture) asks whether repeating two simple arithmetic operations will eventually transform every positive integer into $1$.

![Collatz Function](/images/illustrations/what-is-the-collatz-conjecture-unsolved-mathematical-problems.png "Collatz Function")

The Collatz conjecture is often thought of as the simplest impossible problem. It has been suggested that a new understanding of maths will be required to solve the Collatz Conjecture. To date the Collatz Conjecture ha*

**Assumptions**
- The script should indicate to the end user if the Collatz Conjecture holds true for the desired range of positive integers.
- If the Collatz conjecture does not hold true for any values, the script should return the values that do not hold true.
- For usability purposes the script should be able to handle any range of input values not just the first 10,000 positive integers.
- The script will not run if negative integers, floating point decimals or strings are entered as arguments.
- If these values are entered as arguments the script will give clear instruction to the end user of the correct format for arguments to be entered.

#### Solution

[Jupyter Notebook with solution](tasks.ipynb) ![jupyter_logo](/images/illustrations/jupyter_logo_mod_sh_2.png)

[Python Script](/tasks/task_1/collatz.py) ![python logo](/images/illustrations/python_logo_mod_sh.png)

The script [collatz.py](/tasks/task_1/collatz.py) runs from the command line and will check if the Collatz Conjecture is true for each number in a range of values. The range of values to be checked are passed as command line arguments. The script will accept a range of positive integer values as an a command line argument. For example to check from $1$ to $10000$ enter the following command into the bash shell.

```bash
python collatz.py 1 10000
```

The script will output an indication of any values that the Collatz Conjecture does or does not hold true for in the given range.

#### References

Wikipedia. (2022). Lothar Collatz. [online] Available at: https://en.wikipedia.org/wiki/Lothar_Collatz.

### [Task 2 - Penguins Variables](/tasks/task_2/penguins.py)
**Task 2** - *Give an overview of the famous penguins data set, explaining the types of variables it contains. Suggest the types of variables that should be used to model them in Python, explaining your rationale.*

The **Penguins** dataset contains size measurements for three penguin species observed on three islands in the Palmer Archipelago, Antarctica. The data was as part of the Palmer Station, Antarctica, Long-Term Ecological Research program and is also known as the Palmer Penguins dataset. The research paper on the Palmer Penguins dataset by Gorman, Williams and Fraser (2014) is available [here](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0090081#s2).

![image 1](images/illustrations/penguins.png "Palmer Penguins")

Mednick, 2021

#### Solution

[Jupyter Notebook with solution](tasks.ipynb) ![jupyter_logo](/images/illustrations/jupyter_logo_mod_sh_2.png)

[Python Script](/tasks/task_2/penguins.py) ![python logo](/images/illustrations/python_logo_mod_sh.png)

The script [penguins.py](/tasks/task_2/penguins.py) runs from the command line and outputs a summary of the variables in the *Palmer Penguins* dataset. The script is run from the command line with the following command:

```bash
python penguins.py
```
#### References

Gorman, K.B., Williams, T.D. and Fraser, W.R. (2014). Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins (Genus Pygoscelis). PLoS ONE, 9(3), p.e90081. doi:https://doi.org/10.1371/journal.pone.0090081. [Accessed 16 Oct. 2023]

PhD, G.M. (2021). Palmer penguins. [online] Gabe Mednick. Available at: https://www.gabemednick.com/post/penguin/ [Accessed 16 Oct. 2023].

---
### Task 3 - Penguins Probability Distribution

**Task** - *For each of the variables in the penguins data set, suggest what probability distribution from the numpy random distributions list is the most appropriate to model the variable.*

*In probability theory and statistics, a [probability distribution](https://en.wikipedia.org/wiki/Probability_distribution) is the mathematical function that gives the probabilities of occurrence of different possible outcomes for an experiment.* (Wikipedia Contributors, 2019).

#### Solution

[Jupyter Notebook with solution](tasks.ipynb) ![jupyter_logo](/images/illustrations/jupyter_logo_mod_sh_2.png)

#### References

Wikipedia Contributors (2019). Probability distribution. [online] Wikipedia. Available at: https://en.wikipedia.org/wiki/Probability_distribution. [Accessed 25 Oct. 2023]

‌


---
## Project

**Problem Statement**:
- create a notebook investigating the variables and data points within the well-known iris flower data set associated with Ronald A Fisher.
- in the notebook, you should discuss the classification of each variable within the data set according to common variable types and scales of measurement in mathematics, statistics, and Python.
- Select, demonstrate, and explain the most appropriate summary statistics to describe each variable.
- Select, demonstrate, and explain the most appropriate plot(s) for each variable
- The notebook should follow a cohesive narrative about the data set.
---

### Background

The [Iris Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set) is a data set that consists of fifty samples from 
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

## Markdown References

GitHub. (n.d.). Markdown nested lists deeper than two levels don’t get indented. · Issue #4009 · go-gitea/gitea. [online] Available at: https://github.com/go-gitea/gitea/issues/4009 [Accessed 11 Oct. 2023].

Meta Stack Exchange. (n.d.). How to write nested numbered lists. [online] Available at: https://meta.stackexchange.com/questions/85474/how-to-write-nested-numbered-lists [Accessed 11 Oct. 2023].

---