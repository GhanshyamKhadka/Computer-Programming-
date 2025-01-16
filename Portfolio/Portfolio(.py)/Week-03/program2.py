'''2.Write a program that simulates the way in which a user might choose a password.
 The program should prompt for a new password, and then prompt again. If the two
 passwords entered are the same the program should say "Password Set" or
 similar, otherwise it should report an error.'''

user_password=input("Please enter a new password: ")
conform_password=input("Please conform your password: ")

if user_password==conform_password:
    print("Password Set")

else:
    print("Error: Password donot match.")    