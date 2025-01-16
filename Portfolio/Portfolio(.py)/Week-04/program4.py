'''4. When processing data it is o en useful to remove the last character from some
 input (it is o en a newline). Write and test a function that takes a string parameter
 and returns it with the last character removed. (If the string contains one or fewer
 characters, return it unchanged.)'''

def remove_last_character(input_string):
   
    if len(input_string) > 1:
        return input_string[:-1]
    return input_string


def test_remove_last_character():
    test_cases = [
        "Hello, World!",
        "Python",
        "A",
        "",
    ]

    for test in test_cases:
        result = remove_last_character(test)
        print(f"Input: '{test}' |  Output: '{result}'")


test_remove_last_character()