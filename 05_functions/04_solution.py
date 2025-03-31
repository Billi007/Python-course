# Create a function that returns both area and circumference of a circle given its radius.
import math
def calculate_circle_properties(radius):
    area = round(math.pi*radius**2)
    circumference = round(2*math.pi*radius)

    return area, circumference

area, circumference = calculate_circle_properties(3)
print("area:",area,",", "circumference:", circumference)


