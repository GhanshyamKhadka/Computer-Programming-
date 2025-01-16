'''6. Write a program that takes a centigrade temperature and displays the equivalent in
 fahrenheit. The input should be a number followed by a letter C. The output should
 be in the same format.'''

def c_to_f(c):
    return (c * 9 / 5) + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

while True:
    temp = input("Enter a temperature: ")
    if temp[-1] == 'C':
        print(temp, "=", c_to_f(float(temp[:-1])), "F")

    elif temp[-1] == 'F':
        print(temp, "=", f_to_c(float(temp[:-1])), "C")

    else:
        print("Invalid Input")