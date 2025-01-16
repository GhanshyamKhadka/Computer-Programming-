'''Write and test a function that takes a string as a parameter and returns a sorted list
 of all the unique letters used in the string. So, if the string is cheese, the list
 returned should be ['c', 'e', 'h', 's'].'''

def unique_sorted_letters(input_string):
    unique_letters = set(input_string.lower())
    unique_letters = {char for char in unique_letters if char.isalpha()}
    return sorted(unique_letters)

test_string = "cheese"
result = unique_sorted_letters(test_string)
print(result)  
