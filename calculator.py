import math

shape = int(input("""================== 
Area Calculator 
================== 
                  
1) Triangle
2) Rectangle
3) Square
4) Circle
5) Quit\

Which shape: """))
#switch cases to determine the right formula

match shape:
    case 1: #This is the case for the triangle
        height = int(input("Height: "))
        base = int(input("Base: "))
        print("")
        area = (height * base)/2
        
    case 2: #this is the case for the rectangle
        lenght = int(input("Lenght: "))
        width = int(input("Width: "))
        area = (lenght * width)

    case 3: #this is the case for the square
        side = int(input("Side: "))
        area = side**2

    case 4: #this is the case for the circle
        radius = int(input("Radius: "))
        area = math.pi * (radius**2)

    case 5: #this is the case for quitting
        print("you quited the calculator")

    case _: # this is the case for any incorrect inputs
        print("Your input was incorect.")

if shape <=4:
    print(f"the area is {round(area, 2)}")
