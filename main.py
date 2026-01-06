def celsius_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_celsius(f):
    return (f - 32) * 5 / 9

def celsius_kelvin(c):
    return c + 273.15


from harorat import *

print("25°C → F:", celsius_fahrenheit(25))
print("25°C → K:", celsius_kelvin(25))
print("77°F → C:", fahrenheit_celsius(77))
