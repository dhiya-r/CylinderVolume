# Calculate the volume of a cylinder given its dimensions
# Dhiya Ramadhar
# 09/05/2021

import math

def circle_area(diameter):
    return ((1/4) * math.pi * diameter * diameter) # Calculates and returns the area

def cylinder_volume(diameter, height):
    vol = circle_area(diameter) * height # Calls the area function and calculates the volume
    return vol
def main():
    diameter = eval(input("Enter diameter:\n"))
    height = eval(input("Enter height:\n"))
    output = cylinder_volume(diameter, height)
    print("The volume of the cylinder is", "{0:5.2f}".format(output))
    
if __name__ == '__main__':
    main()