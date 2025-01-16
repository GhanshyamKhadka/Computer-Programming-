'''7. Write a program that reads 6 temperatures (in the same format as before), and
 displays the maximum, minimum, and mean of the values.
 Hint: You should know there are built-in functions for max and min. If you hunt, you
 might also find one for the mean.'''

def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


temperatures = []
for i in range(6):
    temp_input = input(f"Enter temperature {i+1} in Centigrade (e.g., 25 C): ")
    celsius = float(temp_input[:-1]) 
    fahrenheit = convert_to_fahrenheit(celsius)
    temperatures.append(fahrenheit)


max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures) / len(temperatures)


print(f"Maximum temperature: {max_temp} F")
print(f"Minimum temperature: {min_temp} F")
print(f"Mean temperature: {mean_temp:.2f} F")


