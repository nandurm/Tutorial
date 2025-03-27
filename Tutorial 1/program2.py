import math

def circle_area_circumference(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

radius = float(input("Enter the radius of the circle: "))
area, circumference = circle_area_circumference(radius)
print(f"Area: {area}, Circumference: {circumference}")
