Python - Test-driven development
This project focuses on implementing Test-Driven Development (TDD) practices in Python, emphasizing writing comprehensive tests before implementation and understanding edge cases.

Description
This project is part of the ALU Higher Level Programming curriculum, designed to teach students the fundamentals of Test-Driven Development in Python. The project emphasizes writing documentation and tests first, then implementing the actual code functionality.

Learning Objectives
By the end of this project, you should be able to explain:

	* Why Python programming is awesome
	* What's an interactive test
	* Why tests are important
	* How to write Docstrings to create tests
	* How to write documentation for each module and function
	* What are the basic option flags to create tests
	* How to find edge cases

Requirements
Python Scripts
	* Allowed editors: vi, vim, emacs
	* Environment: Ubuntu 20.04 LTS using python3 (version 3.8.5)
	* All files should end with a new line
	* First line of all files should be exactly #!/usr/bin/python3
	* Code should use the pycodestyle (version 2.7.*)
	* All files must be executable
	* File length will be tested using wc

Python Test Cases
	* Allowed editors: vi, vim, emacs
	* All files should end with a new line
	* All test files should be inside a folder tests
	* All test files should be text files (extension: .txt)
	* Tests executed using: python3 -m doctest ./tests/*
	* All modules and functions must have documentation
	* Documentation should be meaningful sentences, not simple words

Project Structure
python-test_driven_development/
├── README.md
├── 0-add_integer.py
├── 2-matrix_divided.py
├── 3-say_my_name.py
├── 4-print_square.py
├── 5-text_indentation.py
├── 6-max_integer.py
└── tests/
    ├── 0-add_integer.txt
    ├── 2-matrix_divided.txt
    ├── 3-say_my_name.txt
    ├── 4-print_square.txt
    ├── 5-text_indentation.txt
    └── 6-max_integer_test.py

Tasks
0. Integers addition
File: 0-add_integer.py, tests/0-add_integer.txt

Write a function that adds 2 integers with proper type checking and error handling.

1. Divide a matrix
File: 2-matrix_divided.py, tests/2-matrix_divided.txt

Write a function that divides all elements of a matrix with comprehensive validation.

2. Say my name
File: 3-say_my_name.py, tests/3-say_my_name.txt

Write a function that prints a formatted name string with type validation.

3. Print square
File: 4-print_square.py, tests/4-print_square.txt

Write a function that prints a square using the # character with size validation.

4. Text indentation
File: 5-text_indentation.py, tests/5-text_indentation.txt

Write a function that formats text with proper indentation after specific characters.

5. Max integer - Unittest
File: tests/6-max_integer_test.py

Write comprehensive unit tests for a max integer function using the unittest module.

Testing
Running Doctest
python3 -m doctest -v ./tests/[test_file].txt

Running Unittest
python3 -m unittest tests.6-max_integer_test

Checking Documentation
# Module documentation
python3 -c 'print(__import__("module_name").__doc__)'

# Function documentation
python3 -c 'print(__import__("module_name").function_name.__doc__)'

Important Notes
	* Write tests and documentation FIRST before implementing functionality
	* Consider all possible edge cases
	* Don't trust user input - validate everything
	* Work together on test cases but implement functions individually
	* Focus on comprehensive error handling

Resources
	* doctest — Test interactive Python examples
	* doctest – Testing through documentation
	* Unit Tests in Python

Repository Information
	* GitHub repository: alu-higher_level_programming
	* Directory: python-test_driven_development
	* Author: Alieu O. Jobe
