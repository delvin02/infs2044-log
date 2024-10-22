# INFS2044 SP5 2024 Assignment 2

The code given in this folder provides a skeleton and some functions that you can use to develop your assignment 2 solution.

## Installation

Several packages are required for this code to work. They are listed in file `requirements.txt`.

It is recommended that you create a dedicated Python environment for this assignment. That is, do not install the necessary packages in your system-wide Python environment.

To create a Python environment, you can use [conda](https://www.anaconda.com/download) or venv/pip.

Using `conda` (run from a terminal/command line):

```shell
conda create --channel conda-forge --name infs2044a2 --file requirements.txt

conda activate infs2044a2
```

Instructions for `venv` and `pip` are at <https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/>

If you use an IDE such as [PyCharm](https://www.jetbrains.com/pycharm/) or [Visual Studio Code](https://code.visualstudio.com/), you will need to select this environment as the Python interpreter.

## Code

File log_analyzer.py is the main entry point for this application. 
The provided code handles all the command line interactions for this application. 
You will need to extend its main() function to implement the system.

## Example

There is an example pattern file and a log file to illustrate the computation the program will need to accomplish. The contents of example_output_basic.txt and example_output_grouped.txt show the expected output of the program when invoked as follows:

```shell
python log_analyzer.py --format=basic patterns.csv log.csv

python log_analyzer.py --format=grouped patterns.csv log.csv
```

# infs2044-log
