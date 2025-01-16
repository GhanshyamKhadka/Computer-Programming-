'''2. Write a function that has a single string as its parameter, and returns the number of
 uppercase letters, and the number of lowercase letters in the string. Test the
 function with a short program.'''

def count_case(input_string):
   
    uppercase_count = 0
    lowercase_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count


def test_count_case():
    test_string = "Hello World."
    uppercase, lowercase = count_case(test_string)
    print(f"String: {test_string}")
    print(f"Uppercase letters: {uppercase}")
    print(f"Lowercase letters: {lowercase}")

test_count_case()

