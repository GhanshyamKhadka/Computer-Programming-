# 5.  Write and test a function that converts a temperature measured in degrees centigrade into the equivalent in fahrenheit, and another that does the reverse conversion. Test both functions. (Google will find you the formulae).
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


print("Celsius to Fahrenheit:")
print(f"0°C = {celsius_to_fahrenheit(0)}°F")

print("Fahrenheit to Celsius:")
print(f"32°F = {fahrenheit_to_celsius(32)}°C")
