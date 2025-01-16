'''8. Modify the "Times Table" again so that the user still enters the number of the table,
 but if this number is negative the table is printed backwards. So entering "-7"
 would produce the Seven Times Table starting at "12 times" down to "0 times".'''


while True:
    try:
        number = int(input("Enter the number for the times table (positive for normal, negative for reverse): "))
        if -12 <= number <= 12:
            break
        else:
            print("Please enter a number between -12 and 12.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

table_number = abs(number)
if number < 0:
    print(f"\n{table_number} Times Table (Reverse):")
    for i in range(12, -1, -1):  
        print(f"{i} x {table_number} = {i * table_number}")
else:
    print(f"\n{table_number} Times Table:")
    for i in range(13):  
        print(f"{i} x {table_number} = {i * table_number}")
