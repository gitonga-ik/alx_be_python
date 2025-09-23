FAHRENHEIT_TO_CELSIUS_FACTOR = 9/5
CELSIUS_TO_FAHRENHEIT_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * CELSIUS_TO_FAHRENHEIT_FACTOR
    

def convert_to_fahrenheit(celsius):
    return celsius * FAHRENHEIT_TO_CELSIUS_FACTOR + 32

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if unit == "C":
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
elif unit == "F":
    print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
else:
    print("Invalid temperature units.")