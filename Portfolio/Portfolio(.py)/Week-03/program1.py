'''1. Modify your greeting program so that if the user does not enter a name (i.e. they
 just press enter), the program responds "Hello, Stranger!". Otherwise it should print
 a greeting with their name as before.'''

def greeting_program():
    name = input("Please enter your name: ").strip()
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, Stranger!")

greeting_program()
