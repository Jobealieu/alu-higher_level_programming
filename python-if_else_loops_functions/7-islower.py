#!/usr/bin/python3
def islower(c):
    """Check if a character is lowercase"""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
