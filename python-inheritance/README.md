# Python - Inheritance

This project explores the concept of inheritance in Python programming, covering fundamental concepts like superclasses, subclasses, method overriding, and built-in functions for type checking.

## Description

This project contains implementations and examples demonstrating various aspects of Python inheritance, including:
- Object introspection and attribute lookup
- Class inheritance and method overriding
- Type checking with isinstance, issubclass, and type
- Multiple inheritance concepts
- Geometry classes with inheritance hierarchy

## Learning Objectives

By completing this project, you will understand:
- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- How to use isinstance, issubclass, type and super built-in functions

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- First line of all files should be exactly `#!/usr/bin/python3`
- Code should use pycodestyle (version 2.7.*)
- All files must be executable
- File length will be tested using `wc`

### Python Test Cases
- All test files should be inside a folder `tests`
- All test files should be text files (extension: `.txt`)
- All tests should be executed using: `python3 -m doctest ./tests/*`
- All modules, classes, and functions should have documentation

## Files

| File | Description |
|------|-------------|
| `0-lookup.py` | Function that returns the list of available attributes and methods of an object |
| `1-my_list.py` | Class MyList that inherits from list with a print_sorted method |
| `2-is_same_class.py` | Function that checks if object is exactly an instance of specified class |
| `3-is_kind_of_class.py` | Function that checks if object is an instance of, or inherited from, specified class |
| `4-inherits_from.py` | Function that checks if object is an instance of a class that inherited from specified class |
| `5-base_geometry.py` | Empty BaseGeometry class |
| `6-base_geometry.py` | BaseGeometry class with area method that raises an exception |
| `7-base_geometry.py` | BaseGeometry class with area method and integer_validator method |
| `8-rectangle.py` | Rectangle class that inherits from BaseGeometry |
| `9-rectangle.py` | Rectangle class with area method implemented |
| `10-square.py` | Square class that inherits from Rectangle |
| `11-square.py` | Square class with custom string representation |

## Usage

### Running the Files

Each file can be executed directly:

bash
./0-lookup.py
./1-my_list.py
# etc.

### Running Tests

Execute all doctests:

bash
python3 -m doctest ./tests/*

### Code Style Check

Check code style compliance:

bash
pycodestyle *.py

## Examples

### Lookup Function

python
lookup = __import__('0-lookup').lookup
class MyClass1(object):
    pass

print(lookup(MyClass1))

Output: ['class', 'delattr', 'dict', ...]

### MyList Class

python
MyList = __import__('1-my_list').MyList
my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
print(my_list)           # [1, 4, 2]
my_list.print_sorted()   # [1, 2, 4]
print(my_list)           # [1, 4, 2]


## Author

**Alieu O. Jobe**

## Repository

- **GitHub repository**: `alu-higher_level_programming`
- **Directory**: `python-inheritance`

Save this as README.md in your python-inheritance directory. This README provides a comprehensive overview of your project and meets the requirements specified in the task! 📝
