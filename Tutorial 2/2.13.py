""" Write a python function to find the area of a circle."""


import math

def area_of_circle(radius):
    if radius < 0:
        return "Radius cannot be negative"
    
    area = math.pi * radius ** 2
    return area


r = float(input("Enter the radius of the circle: "))


print(f"Area of the circle: {area_of_circle(r):.2f}")
