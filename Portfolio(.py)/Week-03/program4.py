'''Modify your program again so that the chosen password cannot be one of a list of
 common passwords, defined thus:
 BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']'''

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
user_password = input("Please enter a new password: ")
confirm_password = input("Please confirm your password: ")
if user_password == confirm_password:
    if len(user_password) >= 8 and len(user_password) <= 12:
        if user_password not in BAD_PASSWORDS:
            print("Password Set")
        else:
            print("Error: Password is too common.")
    else:
        print("Error: Password must be between 8 and 12 characters.")


else:
    print("Error: Passwords do not match.")