'''Write a program that prompts a user to enter a temperature in Celsius, and then
 displays the corresponding temperature in Fahrenheit, like so:
 Enter a temperature in Celsius: 32.5
 32.5C is equivalent to 90.5F.'''

temperature_celsius=float(input("Enter your Temperature in Celsius:"))


temperature_fahrenheit= (9/5*temperature_celsius)+32
print(f"{temperature_celsius}C is equivalent to {temperature_fahrenheit}F.")
