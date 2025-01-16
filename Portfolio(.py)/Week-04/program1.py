'''1. Functions are often used to validate input. Write afunction that accepts a single
 integer as a parameter and returns Trueif the integer is in the range 0 to 100 
(inclusive), or False otherwise. Write a short program to test the function.'''

def is_in_range(value):
    
    return 0 <= value <= 100

def validate_input(value):
   
    if is_in_range(value):
        return True
    else:
        return False

value= float(input("Enter your value:")) 
print(validate_input(value))
 

