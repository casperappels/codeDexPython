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

match shape:
    case 1: #This is the case for the triangle
        height = int(input("Height: "))
        base = int(input("Base: "))
        print("")
        area = (height * base)/2
        print(f" the area is {area}")
    case 2: #this is the case for the rectangle
        
    case 3: #this is the case for the square
        print()
    case 4: #this is the case for the circle
        print()
    case 5: #this is the case for quitting
        print()
    case _: # this is the case for any incorrect inputs
        print("Your input was incorect.")
