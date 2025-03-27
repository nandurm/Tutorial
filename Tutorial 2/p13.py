# Write a python function to find the area of a circle.

def area_of_circle(radius):
    return math.pi * radius ** 2

radius = float(input("Enter the radius of the circle: "))
print(area_of_circle(radius))
