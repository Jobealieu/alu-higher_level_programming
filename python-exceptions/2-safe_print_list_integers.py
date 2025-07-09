#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    
    while count < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
            i += 1
        except (ValueError, TypeError):
            # Skip non-integer values, move to next element
            i += 1
        except IndexError:
            # Re-raise IndexError when list is exhausted
            raise
    
    print()  # Print newline after all integers
    return count
