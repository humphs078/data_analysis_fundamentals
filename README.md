# Fundamentals of Data Analysis Module Repository

![python_logo](/images/illustrations/python_logo_mod_sh_title.png) ![jupyter_logo](/images/illustrations/jupyter_logo_mod_sh_title.png) ![markdown_logo](/images/illustrations/markdown_title.png) ![laytex_logo](/images/illustrations/laytex_title.png)

Author: Sean Humphreys

Data repository for the Fundamentals of Data Analysis module

## Contents

1. [Repository Installation](#repository-installation)

2. [Jupyter Notebooks](#jupyter-notebooks)

2. [Python Libraries](#python-libraries-python-logo)

1. [Tasks](#tasks)

    1. [Task 1 - Collatz-Conjecture](#task-1---collatz-conjecture)

    2. [Task 2 - Penguins Variables](#task-2---penguins-variables)

    3. [Task 3 - Penguins Probability Distribution](#task-3---penguins-probability-distribution)
    
    4. [Task 4 - Coin Toss Entropy](#task-4---coin-toss-entropy)
    
    5. [Task 5 - Penguins Dataset Plots](#task-5-penguins-dataset-plots)

2. [Project - Iris Data Set Analysis](#project)

---

## Repository Installation

![github_logo](/images/illustrations/git_hub_logo_08122023.jpg)

To access the files in this repository Git Desktop must be installed on the local machine.

Git desktop installation files are accessed [here](https://desktop.github.com/).

Guides on the use of Git are available [here](https://docs.github.com/en/desktop/overview/getting-started-with-github-desktop).


This repository can be cloned with the following git command:

```bash
git clone https://github.com/humphs078/data_analysis_fundamentals.git
```



## Jupyter Notebooks ![jupyter_logo](/images/illustrations/jupyter_logo_mod_sh.png)

Jupyter Notebooks are an interactive way to explain code, visualize data and share your ideas with others. Further information on Jupyter Notebooks can be found [here](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html).

To run this file in a fully interactive way the Jupyter Notebooks server must be installed on the local machine. Instructions on how to install Jupyter Notebooks server can be found [here](https://jupyter.org/install).

This repository contains two Jupyter Notebooks:
1. [tasks.ipynb](tasks.ipynb) - The *Tasks Jupyter Notebook* contains the submission for the module tasks.
2. [project.ipynb](project.ipynb) - The *Project Jupyter Notebook* contains the submission for the module project.

---
## Python Libraries ![python logo](/images/illustrations/python_logo_mod_sh.png)

The following python libraries must be installed on the local machine to run the python scripts and notebooks in this repository:

+ matplotlib - `pip install matplotlib`
+ numpy - `pip install numpy`
+ pandas - `pip install pandas`
+ seaborn - `pip install seaborn`
+ sys - the sys package is part of python's standard library and does not need to be installed
+ ucimlrepo - to install - `pip install ucimlrepo`

---

## Tasks

### [Task 1 - Collatz Conjecture](/tasks/task_1/collatz.py)
**Task -** *Verify, using Python, that the conjecture is true for the first 10,000 positive integers.*

#### Solution

[Jupyter Notebook with solution](tasks.ipynb) ![jupyter_logo](/images/illustrations/jupyter_logo_mod_sh_2.png)

[Python Script](/tasks/task_1/collatz.py) ![python logo](/images/illustrations/python_logo_mod_sh.png)

The script [collatz.py](/tasks/task_1/collatz.py) runs from the command line and will check if the Collatz Conjecture is true for each number in a range of values. The range of values to be checked are passed as command line arguments. The script will accept a range of positive integer values as an a command line argument. For example to check from $1$ to $10000$ enter the following command into the bash shell.

```bash
python collatz.py 1 10000
```

The script will output an indication of any values that the Collatz Conjecture does or does not hold true for in the given range.

### [Task 2 - Penguins Variables](/tasks/task_2/penguins.py)
**Task 2** - *Give an overview of the famous penguins data set, explaining the types of variables it contains. Suggest the types of variables that should be used to model them in Python, explaining your rationale.*

#### Solution

[Jupyter Notebook with solution](tasks.ipynb) ![jupyter_logo](/images/illustrations/jupyter_logo_mod_sh_2.png)

[Python Script](/tasks/task_2/penguins.py) ![python logo](/images/illustrations/python_logo_mod_sh.png)

The script [penguins.py](/tasks/task_2/penguins.py) runs from the command line and outputs a summary of the variables in the *Palmer Penguins* dataset. The script is run from the command line with the following command:

```bash
python penguins.py
```

---

### Task 3 - Penguins Probability Distribution

**Task** - *For each of the variables in the penguins data set, suggest what probability distribution from the numpy random distributions list is the most appropriate to model the variable.*

#### Solution

[Jupyter Notebook with solution](tasks.ipynb) ![jupyter_logo](/images/illustrations/jupyter_logo_mod_sh_2.png)

---

### Task 4 - Coin Toss Entropy

Task - *Suppose you are flipping two coins, each with a probability p of giving heads. Plot the entropy of the total number of heads versus p.*

#### Solution

[Jupyter Notebook with solution](tasks.ipynb) ![jupyter_logo](/images/illustrations/jupyter_logo_mod_sh_2.png)

### Task 5 Penguins Dataset Plots

Task - *Create an appropriate individual plot for each of the variables in the penguin data set.*

#### Solution

[Jupyter Notebook with solution](tasks.ipynb) ![jupyter_logo](/images/illustrations/jupyter_logo_mod_sh_2.png)

---

## Project

**Problem Statement**:
- create a notebook investigating the variables and data points within the well-known iris flower data set associated with Ronald A Fisher.
- in the notebook, you should discuss the classification of each variable within the data set according to common variable types and scales of measurement in mathematics, statistics, and Python.
- Select, demonstrate, and explain the most appropriate summary statistics to describe each variable.
- Select, demonstrate, and explain the most appropriate plot(s) for each variable
- The notebook should follow a cohesive narrative about the data set.

#### Solution

[Jupyter Notebook with solution](project.ipynb) ![jupyter_logo](/images/illustrations/jupyter_logo_mod_sh_2.png)

---