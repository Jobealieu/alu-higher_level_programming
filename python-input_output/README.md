
# Python - Input/Output

This project focuses on file handling and JSON operations in Python. It covers reading and writing files, working with JSON data, and implementing object serialization.

## Description

This project is part of the ALU Higher Level Programming curriculum. It demonstrates fundamental concepts of file I/O operations and JSON manipulation in Python.

## Learning Objectives

By the end of this project, you should be able to explain:

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is JSON
- What is serialization and deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use the pycodestyle (version 2.7.*)
- All files must be executable
- File length will be tested using `wc`

### Python Test Cases
- All test files should be inside a `tests` folder
- All test files should be text files (extension: `.txt`)
- All tests should be executed using: `python3 -m doctest ./tests/*`
- All modules, classes, and functions should have documentation

## Files

| File | Description |
|------|-------------|
| `0-read_file.py` | Function that reads a text file and prints it to stdout |
| `1-write_file.py` | Function that writes a string to a text file |
| `2-append_write.py` | Function that appends a string at the end of a text file |
| `3-to_json_string.py` | Function that returns the JSON representation of an object |
| `4-from_json_string.py` | Function that returns an object from a JSON string |
| `5-save_to_json_file.py` | Function that writes an object to a text file using JSON |
| `6-load_from_json_file.py` | Function that creates an object from a JSON file |
| `7-add_item.py` | Script that adds all arguments to a Python list and saves them to a file |
| `8-class_to_json.py` | Function that returns the dictionary description of an object |
| `9-student.py` | Class Student that defines a student with JSON serialization |
| `10-student.py` | Class Student with filtered JSON serialization |
| `11-student.py` | Class Student with disk persistence and reload functionality |

## Usage

Each script can be run independently. For example:


bash
./0-read_file.py
./1-write_file.py

## Testing

Run tests using:

bash
python3 -m doctest ./tests/*

## Author

Alieu O. Jobe - ALU Student

## Repository

- **GitHub repository**: `alu-higher_level_programming`
- **Directory**: `python-input_output`
