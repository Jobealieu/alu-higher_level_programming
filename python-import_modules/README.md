# Python - import & modules

This project is part of the ALU Higher Level Programming curriculum, focusing on Python imports, modules, and command line arguments.

## Description

This project teaches the fundamentals of importing functions from other files, creating modules, and working with command line arguments in Python. Through practical exercises, you'll learn how to structure Python programs using modular design principles.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, **without the help of Google**:

### General
- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

## Resources

**Read or watch:**
- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

**man or help:**
- `python3`

## Project Structure


python-import_modules/
├── README.md
├── 0-add.py
├── add_0.py
├── 1-calculation.py
├── calculator_1.py
├── 2-args.py
├── 3-infinite_add.py
├── 4-hidden_discovery.py
├── hidden_4.pyc
├── 5-variable_load.py
└── variable_load_5.py


## Tasks

### 0. Import a simple function from a simple file
**File:** `0-add.py`
- Imports the function `add(a, b)` from the file `add_0.py`
- Prints the result of the addition 1 + 2 = 3
- Uses string format to display integers
- Code should not be executed when imported

**Example:**

bash
$ ./0-add.py
1 + 2 = 3


### 1. My first toolbox!
**File:** `1-calculation.py`
- Imports functions from `calculator_1.py`
- Performs mathematical operations with values a=10 and b=5
- Calls each imported function (add, sub, mul, div)
- Uses the word "calculator_1" only once

**Example:**

bash
$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2


### 2. How to make a script dynamic!
**File:** `2-args.py`
- Prints the number of and list of command line arguments
- Handles different argument scenarios (0, 1, or multiple arguments)
- Shows position and value of each argument

**Examples:**

bash
$ ./2-args.py
0 arguments.

$ ./2-args.py Hello
1 argument:
1: Hello

$ ./2-args.py Hello Welcome To School
4 arguments:
1: Hello
2: Welcome
3: To
4: School


### 3. Infinite addition
**File:** `3-infinite_add.py`
- Prints the result of addition of all command line arguments
- Handles any number of arguments including big numbers
- Casts arguments to integers using `int()`

**Examples:**

bash
$ ./3-infinite_add.py
0

$ ./3-infinite_add.py 79 10
89

$ ./3-infinite_add.py 79 10 -40 -300 89
-162


### 4. Who are you?
**File:** `4-hidden_discovery.py`
- Prints all names defined by the compiled module `hidden_4.pyc`
- Prints one name per line in alphabetical order
- Excludes names that start with `__`

**Example:**

bash
$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school


### 5. Everything can be imported
**File:** `5-variable_load.py`
- Imports the variable `a` from `variable_load_5.py`
- Prints the value of the imported variable
- Does not use `*` for importing or `__import__`

**Example:**

bash
$ ./5-variable_load.py
98


## Usage

1. Clone the repository:

bash
git clone https://github.com/[username]/alu-higher_level_programming.git
cd alu-higher_level_programming/python-import_modules

2. Make files executable:

bash
chmod +x *.py

3. Run individual tasks:

bash
./0-add.py
./1-calculation.py
./2-args.py [arguments]
./3-infinite_add.py [numbers]
./4-hidden_discovery.py
./5-variable_load.py

## Style Guide

This project follows the PEP 8 style guide for Python code. Use `pycodestyle` to check your code:


bash
pycodestyle *.py

## Repository Information

- **GitHub repository:** `alu-higher_level_programming`
- **Directory:** `python-import_modules`
- **Project Weight:** 1
- **Project Type:** Novice
- **By:** Guillaume

## Author

**Alieu O. Jobe**
- ALU Student
- Higher Level Programming Track

---

*This project is part of the ALU Software Engineering Program curriculum.*

This README provides comprehensive documentation for your project, including all tasks, examples, requirements, and usage instructions. It's structured to be both informative and professional! 📚✨
