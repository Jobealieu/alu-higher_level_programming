#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    
    while count < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip non-integer values
            pass
        except IndexError:
            # Re-raise IndexError when trying to access beyond list bounds
            raise
        
        i += 1
    
    print()  # Print newline after all integers
    return count
