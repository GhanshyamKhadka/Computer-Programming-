'''5. Modify your program a final time so that it executes until the user successfully
 chooses a password. That is, if the password chosen fails any of the checks, the
 program should return to asking for the password the first time.'''


BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']


while True:
    password = input("Choose a password: ")


    if password in BAD_PASSWORDS:
        print("That password is too common. Please choose a more secure password.")
    elif not password:
        print("Password cannot be empty. Please try again.")
    else:
        print("Password accepted!")
        break 
