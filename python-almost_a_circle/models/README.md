Models Package
Overview
This package contains the core classes for the "Python - Almost a Circle" project. It implements a hierarchical object-oriented design for geometric shapes with comprehensive validation, serialization, and file I/O capabilities.

Package Structure
models/
├── __init__.py          # Package initialization (empty)
├── base.py             # Base class with ID management and serialization
├── rectangle.py        # Rectangle class inheriting from Base
└── square.py          # Square class inheriting from Rectangle

Class Hierarchy
Base
└── Rectangle
    └── Square

Classes Documentation
Base Class (base.py)
The foundational class that provides ID management and serialization functionality for all geometric shapes.

Class Attributes
	* __nb_objects (private): Counter for automatic ID assignment

Instance Attributes
	* id: Unique identifier for each instance

Methods
Constructor:

def __init__(self, id=None)

	* If id is provided, assigns it to the instance
	* If id is None, auto-increments __nb_objects and assigns the new value

Static Methods:

@staticmethod
def to_json_string(list_dictionaries)

	* Converts a list of dictionaries to JSON string
	* Returns "[]" if input is None or empty

@staticmethod
def from_json_string(json_string)

	* Converts JSON string back to list of dictionaries
	* Returns empty list if input is None or empty

Class Methods:

@classmethod
def save_to_file(cls, list_objs)

	* Saves list of instances to JSON file
	* Filename format: <ClassName>.json
	* Creates empty file if list_objs is None

@classmethod
def load_from_file(cls)

	* Loads instances from JSON file
	* Returns empty list if file doesn't exist
	* Uses create() method to instantiate objects

@classmethod
def create(cls, **dictionary)

	* Creates instance with attributes set from dictionary
	* Uses dummy instance + update() method pattern
	* Supports both Rectangle and Square creation

----

Rectangle Class (rectangle.py)
Represents rectangular shapes with position coordinates, inheriting ID management from Base.

Instance Attributes (Private with Getters/Setters)
	* __width: Rectangle width (must be > 0)
	* __height: Rectangle height (must be > 0)
	* __x: X coordinate position (must be >= 0)
	* __y: Y coordinate position (must be >= 0)

Constructor
def __init__(self, width, height, x=0, y=0, id=None)

Validation Rules
	* Type Validation: All attributes must be integers
	* Value Validation: 

		* width and height must be > 0
		* x and y must be >= 0
	* Error Messages:

		* "<attribute> must be an integer"
		* "<attribute> must be > 0" (for width/height)
		* "<attribute> must be >= 0" (for x/y)

Public Methods
Area Calculation:

def area(self)

Returns the area of the rectangle (width × height)

Display:

def display(self)

Prints the rectangle using '#' characters, respecting x/y positioning

String Representation:

def __str__(self)

Returns: [Rectangle] (<id>) <x>/<y> - <width>/<height>

Update:

def update(self, *args, **kwargs)

	* args order: id, width, height, x, y
	* kwargs: any attribute by name
	* kwargs ignored if args is not empty

Serialization:

def to_dictionary(self)

Returns dictionary with keys: id, width, height, x, y

----

Square Class (square.py)
Represents square shapes as a special case of Rectangle where width equals height.

Instance Attributes
	* Inherits all Rectangle attributes
	* size property: getter/setter for width and height (always equal)

Constructor
def __init__(self, size, x=0, y=0, id=None)

Calls Rectangle constructor with size as both width and height

Property Methods
Size Property:

@property
def size(self)

Returns the size (width) of the square

@size.setter
def size(self, value)

Sets both width and height to the same value with Rectangle validation

Overridden Methods
String Representation:

def __str__(self)

Returns: [Square] (<id>) <x>/<y> - <size>

Update:

def update(self, *args, **kwargs)

	* args order: id, size, x, y
	* kwargs: any attribute by name (including 'size')
	* kwargs ignored if args is not empty

Serialization:

def to_dictionary(self)

Returns dictionary with keys: id, size, x, y

Design Patterns Used
Inheritance
	* Square inherits from Rectangle (IS-A relationship)
	* Rectangle inherits from Base (common functionality)

Encapsulation
	* Private attributes with public getters/setters
	* Input validation in setters

Polymorphism
	* __str__ method overriding
	* update() method specialization
	* to_dictionary() method customization

Template Method Pattern
	* Base class provides serialization framework
	* Subclasses implement specific dictionary conversion

Validation Architecture
Type Checking
if not isinstance(value, int):
    raise TypeError(f"{attribute} must be an integer")

Range Validation
# For width/height
if value <= 0:
    raise ValueError(f"{attribute} must be > 0")

# For x/y coordinates
if value < 0:
    raise ValueError(f"{attribute} must be >= 0")

Serialization Flow
	1. Instance → Dictionary: to_dictionary()
	2. Dictionary → JSON String: to_json_string()
	3. JSON String → File: save_to_file()
	4. File → JSON String: load_from_file()
	5. JSON String → Dictionary: from_json_string()
	6. Dictionary → Instance: create()

Usage Examples
Basic Shape Creation
from models.rectangle import Rectangle
from models.square import Square

# Rectangle
rect = Rectangle(10, 2, 1, 9, 12)
print(rect)  # [Rectangle] (12) 1/9 - 10/2

# Square
square = Square(5, 2, 1, 89)
print(square)  # [Square] (89) 2/1 - 5

Validation Examples
try:
    Rectangle(10, "2")  # TypeError: height must be an integer
except TypeError as e:
    print(e)

try:
    Rectangle(-5, 10)  # ValueError: width must be > 0
except ValueError as e:
    print(e)

Serialization Examples
# Save rectangles to file
rectangles = [Rectangle(10, 7, 2, 8), Rectangle(2, 4)]
Rectangle.save_to_file(rectangles)

# Load rectangles from file
loaded_rectangles = Rectangle.load_from_file()

# Individual serialization
rect_dict = rectangles[0].to_dictionary()
new_rect = Rectangle.create(**rect_dict)

Error Handling
The models package implements comprehensive error handling:

	* TypeError: For non-integer inputs
	* ValueError: For out-of-range values
	* FileNotFoundError: Gracefully handled in load_from_file()

Testing Considerations
When testing these models:

	* Test all validation scenarios
	* Test serialization round-trip (save → load)
	* Test inheritance behavior
	* Test edge cases (zero values, negative values)
	* Test file I/O error conditions

Dependencies
	* Standard Library: json module for serialization
	* Python Version: 3.8.5+
	* Style: PEP 8 compliant
