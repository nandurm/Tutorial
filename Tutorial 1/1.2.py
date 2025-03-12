from math import*

def areaperi(radius):
    area=pi*radius**2
    perimeter=2*pi*radius
    return f"area is: {area:.2f} & perimeter is: {perimeter:.2f}"

radius=int(input("Enter the radius of the circle: "))
calc=areaperi(radius)
print(calc)