Tests Package
Overview
This package contains the complete unit test suite for the "Python - Almost a Circle" project. It implements comprehensive testing for all classes, methods, and edge cases using Python's unittest framework, ensuring code reliability and maintainability.

Testing Philosophy
	* Complete Coverage: Every method, class, and module is thoroughly tested
	* Edge Case Testing: Boundary conditions and error scenarios are validated
	* PEP 8 Compliance: All test code follows Python style guidelines
	* Isolation: Each test is independent and can run in any order
	* Documentation: Clear test names and docstrings explain test purposes

Package Structure
tests/
├── __init__.py                    # Package initialization (empty)
└── test_models/
    ├── __init__.py               # Test models package initialization
    ├── test_base.py              # Tests for Base class
    ├── test_rectangle.py         # Tests for Rectangle class
    └── test_square.py            # Tests for Square class

Running Tests
All Tests
# Run complete test suite
python3 -m unittest discover tests

# Expected output format:
# ...................................................................................
# ...................................................................................
# .......................
# ----------------------------------------------------------------------
# Ran 189 tests in 13.135s
# 
# OK

Individual Test Files
# Test Base class only
python3 -m unittest tests.test_models.test_base

# Test Rectangle class only
python3 -m unittest tests.test_models.test_rectangle

# Test Square class only
python3 -m unittest tests.test_models.test_square

Specific Test Methods
# Test specific method
python3 -m unittest tests.test_models.test_base.TestBase.test_init_with_id

# Verbose output
python3 -m unittest -v tests.test_models.test_base

Test Classes Documentation
TestBase (test_base.py)
Tests the foundational Base class functionality.

Test Categories
Initialization Tests:

	* test_init_no_id(): Auto-increment ID assignment
	* test_init_with_id(): Manual ID assignment
	* test_init_multiple_instances(): ID counter behavior
	* test_init_mixed_ids(): Mixed auto/manual ID assignment

JSON Serialization Tests:

	* test_to_json_string_empty_list(): Empty list handling
	* test_to_json_string_none(): None input handling
	* test_to_json_string_valid_list(): Valid dictionary list conversion
	* test_from_json_string_empty(): Empty string handling
	* test_from_json_string_none(): None input handling
	* test_from_json_string_valid(): Valid JSON string parsing

File I/O Tests:

	* test_save_to_file_none(): None list handling
	* test_save_to_file_empty_list(): Empty list saving
	* test_save_to_file_valid_objects(): Valid object list saving
	* test_load_from_file_no_file(): Missing file handling
	* test_load_from_file_valid(): Valid file loading

Factory Method Tests:

	* test_create_rectangle(): Rectangle creation from dictionary
	* test_create_square(): Square creation from dictionary
	* test_create_invalid_class(): Error handling for invalid classes

Example Test Structure
class TestBase(unittest.TestCase):
    """Test cases for Base class"""
    
    def setUp(self):
        """Reset class counter before each test"""
        Base._Base__nb_objects = 0
    
    def test_init_no_id(self):
        """Test Base instantiation without id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

----

TestRectangle (test_rectangle.py)
Tests Rectangle class functionality including inheritance from Base.

Test Categories
Initialization Tests:

	* test_init_basic(): Basic rectangle creation
	* test_init_with_coordinates(): Rectangle with x, y coordinates
	* test_init_with_id(): Rectangle with custom ID
	* test_init_all_parameters(): All parameters provided

Validation Tests:

	* test_width_validation(): Width type and value validation
	* test_height_validation(): Height type and value validation
	* test_x_validation(): X coordinate validation
	* test_y_validation(): Y coordinate validation
	* test_invalid_types(): Non-integer input handling
	* test_negative_values(): Negative value handling
	* test_zero_dimensions(): Zero width/height handling

Property Tests:

	* test_width_getter_setter(): Width property functionality
	* test_height_getter_setter(): Height property functionality
	* test_x_getter_setter(): X coordinate property functionality
	* test_y_getter_setter(): Y coordinate property functionality

Method Tests:

	* test_area(): Area calculation accuracy
	* test_display_basic(): Basic display functionality
	* test_display_with_coordinates(): Display with x, y offsets
	* test_str_representation(): String format validation
	* test_update_args(): Update with positional arguments
	* test_update_kwargs(): Update with keyword arguments
	* test_update_mixed(): Mixed args/kwargs behavior

Serialization Tests:

	* test_to_dictionary(): Dictionary conversion
	* test_to_dictionary_values(): Dictionary content validation

Example Validation Test
def test_width_validation(self):
    """Test width validation"""
    with self.assertRaises(TypeError):
        Rectangle("10", 2)
    
    with self.assertRaises(ValueError):
        Rectangle(-5, 2)
    
    with self.assertRaises(ValueError):
        Rectangle(0, 2)

----

TestSquare (test_square.py)
Tests Square class functionality including Rectangle inheritance.

Test Categories
Initialization Tests:

	* test_init_size_only(): Square with size parameter only
	* test_init_with_coordinates(): Square with position
	* test_init_with_id(): Square with custom ID
	* test_init_all_parameters(): All parameters provided

Size Property Tests:

	* test_size_getter(): Size property getter
	* test_size_setter(): Size property setter
	* test_size_validation(): Size validation (inherits from width)
	* test_size_updates_dimensions(): Size updates both width and height

Inheritance Tests:

	* test_inherits_from_rectangle(): Inheritance verification
	* test_inherited_methods(): Inherited method functionality
	* test_area_calculation(): Area calculation (size²)
	* test_display_functionality(): Display method inheritance

Method Override Tests:

	* test_str_representation(): Square string format
	* test_update_args(): Update with positional arguments (id, size, x, y)
	* test_update_kwargs(): Update with keyword arguments
	* test_to_dictionary(): Square dictionary format

Edge Case Tests:

	* test_size_boundary_values(): Minimum valid sizes
	* test_large_squares(): Large dimension handling
	* test_coordinate_boundaries(): Position boundary testing

Example Inheritance Test
def test_inherits_from_rectangle(self):
    """Test Square inherits from Rectangle"""
    s = Square(5)
    self.assertIsInstance(s, Rectangle)
    self.assertIsInstance(s, Base)
    self.assertEqual(s.width, s.height)
    self.assertEqual(s.size, 5)

Testing Strategies
Test Data Organization
class TestRectangle(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""
        Base._Base__nb_objects = 0
        self.valid_rect = Rectangle(10, 2, 1, 9)
        self.simple_rect = Rectangle(5, 5)
    
    def tearDown(self):
        """Clean up after each test method"""
        # Remove any created files
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

Error Testing Patterns
def test_invalid_width_type(self):
    """Test TypeError for non-integer width"""
    with self.assertRaises(TypeError) as context:
        Rectangle("invalid", 5)
    self.assertEqual(str(context.exception), "width must be an integer")

def test_negative_width(self):
    """Test ValueError for negative width"""
    with self.assertRaises(ValueError) as context:
        Rectangle(-5, 10)
    self.assertEqual(str(context.exception), "width must be > 0")

File I/O Testing
def test_save_and_load_cycle(self):
    """Test complete save/load cycle"""
    rectangles = [Rectangle(10, 7, 2, 8), Rectangle(2, 4)]
    Rectangle.save_to_file(rectangles)
    
    loaded = Rectangle.load_from_file()
    self.assertEqual(len(loaded), 2)
    self.assertEqual(loaded[0].width, 10)
    self.assertEqual(loaded[1].height, 4)

Test Coverage Areas
Functional Testing
	* ✅ Constructor validation
	* ✅ Property getters/setters
	* ✅ Method return values
	* ✅ String representations
	* ✅ Area calculations
	* ✅ Display output

Error Handling Testing
	* ✅ Type validation
	* ✅ Value range validation
	* ✅ Exception messages
	* ✅ Edge case handling

Integration Testing
	* ✅ Inheritance behavior
	* ✅ Method overriding
	* ✅ File I/O operations
	* ✅ Serialization round-trips

Boundary Testing
	* ✅ Minimum valid values
	* ✅ Maximum reasonable values
	* ✅ Zero and negative values
	* ✅ Empty and None inputs

Test Organization Best Practices
Naming Conventions
	* Test files: test_<module_name>.py
	* Test classes: Test<ClassName>
	* Test methods: test_<functionality>_<scenario>()

Documentation Standards
def test_rectangle_area_calculation(self):
    """
    Test that Rectangle.area() returns correct area calculation.
    
    Tests:
    - Basic area calculation (width * height)
    - Area with different dimensions
    - Area independence from coordinates
    """
    rect = Rectangle(3, 4)
    self.assertEqual(rect.area(), 12)

Assertion Guidelines
	* Use specific assertions (assertEqual, assertRaises, etc.)
	* Include descriptive failure messages
	* Test both positive and negative cases
	* Validate exact error messages

Running Test Coverage Analysis
# Install coverage tool
pip3 install coverage

# Run tests with coverage
coverage run -m unittest discover tests

# Generate coverage report
coverage report -m

# Generate HTML coverage report
coverage html

Common Testing Patterns
Setup and Teardown
def setUp(self):
    """Prepare test environment"""
    Base._Base__nb_objects = 0
    
def tearDown(self):
    """Clean up test environment"""
    # Remove test files, reset state

Parameterized Testing
def test_multiple_invalid_types(self):
    """Test various invalid types for width"""
    invalid_types = ["string", 3.14, [1, 2], {"key": "value"}, None]
    for invalid_type in invalid_types:
        with self.subTest(type=invalid_type):
            with self.assertRaises(TypeError):
                Rectangle(invalid_type, 5)

Debugging Failed Tests
Verbose Output
python3 -m unittest -v tests.test_models.test_rectangle.TestRectangle.test_area

Debug Specific Failures
def test_debug_example(self):
    """Example of debugging approach"""
    rect = Rectangle(10, 2)
    print(f"Debug: rect.area() = {rect.area()}")  # Temporary debug output
    self.assertEqual(rect.area(), 20)

Test Maintenance
	* Regular Updates: Update tests when functionality changes
	* Refactoring: Keep tests DRY (Don't Repeat Yourself)
	* Documentation: Maintain clear test documentation
	* Performance: Ensure tests run quickly and efficiently
