'''8.Modify the previous program so that it can process any numberof values. The input
 terminates when the user just pressed "Enter" at the prompt rather than entering a
 value.'''

def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


temperatures = []


while True:
    temp_input = input("Enter temperature in Centigrade (e.g., 25 C) or press Enter to finish: ")
    
    if temp_input == "":
        break
    
    celsius = float(temp_input[:-1])  
    fahrenheit = convert_to_fahrenheit(celsius)
    temperatures.append(fahrenheit)


if temperatures:
    print(f"Maximum temperature: {max(temperatures)} F")
    print(f"Minimum temperature: {min(temperatures)} F")
    print(f"Mean temperature: {sum(temperatures)/len(temperatures):.2f} F")
else:
    print("No temperatures entered.")
