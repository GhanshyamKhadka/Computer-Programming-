'''7. Modify your "Times Table" program so that the user enters the number of the table
 they require. This number should be between 0 and 12 inclusive.'''


while True:
    try:
        number = int(input("Enter the number for the times table (0-12): "))
        if 0 <= number <= 12:
            break
        else:
            print("Please enter a number between 0 and 12.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"\n{number} Times Table:")
for i in range(13):  
    print(f"{i} x {number} = {i * number}")
