Python - Almost a Circle
Description
This project is part of the Higher Level Programming curriculum and serves as preparation for the AirBnB project. It implements a comprehensive object-oriented programming solution featuring geometric shapes with serialization capabilities.

The project demonstrates mastery of advanced Python concepts including inheritance, class methods, static methods, unit testing, JSON serialization, and file I/O operations.

Project Structure
python-almost_a_circle/
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── rectangle.py
│   └── square.py
├── tests/
│   └── test_models/
│       ├── __init__.py
│       ├── test_base.py
│       ├── test_rectangle.py
│       └── test_square.py
└── README.md

Classes
Base Class (models/base.py)
The foundation class that manages ID attribution for all other classes.

Features:

	* Automatic ID assignment using class attribute __nb_objects
	* JSON serialization/deserialization methods
	* File I/O operations for saving and loading instances

Rectangle Class (models/rectangle.py)
Inherits from Base and represents rectangular shapes.

Attributes:

	* width: Rectangle width (private with getter/setter)
	* height: Rectangle height (private with getter/setter)
	* x: X coordinate position (private with getter/setter)
	* y: Y coordinate position (private with getter/setter)

Methods:

	* area(): Calculate rectangle area
	* display(): Print rectangle using '#' characters
	* update(): Update attributes using *args or **kwargs
	* to_dictionary(): Convert instance to dictionary representation

Square Class (models/square.py)
Inherits from Rectangle and represents square shapes.

Attributes:

	* size: Square size (getter/setter for width and height)
	* Inherits x, y from Rectangle

Methods:

	* Inherits all Rectangle methods
	* update(): Update attributes using *args or **kwargs (adapted for Square)
	* to_dictionary(): Convert instance to dictionary representation

Key Features
Input Validation
	* Type checking for all numeric attributes
	* Value range validation (positive dimensions, non-negative coordinates)
	* Comprehensive error messages for debugging

Serialization Support
	* Convert instances to dictionary format
	* JSON string serialization for data persistence
	* File-based saving and loading of object collections

Unit Testing
	* Comprehensive test suite covering all functionality
	* Edge case testing for validation and error handling
	* PEP 8 compliant code style

Usage Examples
Creating Shapes
from models.rectangle import Rectangle
from models.square import Square

# Create a rectangle
r1 = Rectangle(10, 2, 1, 9)
print(r1)  # [Rectangle] (1) 1/9 - 10/2

# Create a square
s1 = Square(5, 2, 1)
print(s1)  # [Square] (1) 2/1 - 5

Working with Areas and Display
# Calculate area
print(r1.area())  # 20

# Display shape
r1.display()
# Prints the rectangle using '#' characters

Updating Attributes
# Update using positional arguments
r1.update(89, 2, 3, 4, 5)

# Update using keyword arguments
r1.update(height=1, width=2, x=3, y=4, id=89)

Serialization
# Convert to dictionary
r1_dict = r1.to_dictionary()

# Save to file
Rectangle.save_to_file([r1, r2])

# Load from file
rectangles = Rectangle.load_from_file()

Requirements
Python Scripts
	* Python Version: 3.8.5 (Ubuntu 20.04 LTS)
	* Code Style: PEP 8 compliant (pycodestyle 2.7.*)
	* Documentation: All modules, classes, and functions documented
	* Executable: All Python files must be executable

Testing
	* Framework: Python unittest module
	* Coverage: All files, classes, and methods unit tested
	* Execution: python3 -m unittest discover tests

Running Tests
# Run all tests
python3 -m unittest discover tests

# Run specific test file
python3 -m unittest tests/test_models/test_base.py

# Expected output example:
# Ran 189 tests in 13.135s
# OK

Learning Objectives
This project demonstrates understanding of:

	* Object-oriented programming principles
	* Inheritance and method overriding
	* Property decorators and validation
	* *args and **kwargs parameter handling
	* JSON serialization/deserialization
	* File I/O operations
	* Unit testing methodologies
	* Exception handling
	* Code documentation and style

Author
Alieu O. Jobe
ALU Higher Level Programming

Repository Information
	* GitHub Repository: alu-higher_level_programming
	* Directory: python-almost_a_circle
