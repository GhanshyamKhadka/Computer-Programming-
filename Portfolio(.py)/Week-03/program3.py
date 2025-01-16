'''3.Modify your previous program so that the password must be between 8 and 12
 characters (inclusive) long.'''

password= input("Enter a password: ")
if len(password)<8 or len(password)>12:
    print("Error: Password must be between 8 and 12 characters long.")

else:
    print("Password set.")    