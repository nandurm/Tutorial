def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "Quadrant I"
    elif x < 0 and y > 0:
        return "Quadrant II"
    elif x < 0 and y < 0:
        return "Quadrant III"
    elif x > 0 and y < 0:
        return "Quadrant IV"
    else:
        return "On an axis"

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
print(find_quadrant(x, y))
