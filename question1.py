# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).

import math

x1 = int(input("Enter cordinates of x1: "))
y1 = int(input("Enter cordinates of y1: "))
x2 = int(input("Enter cordinates of x2: "))
y2 = int(input("Enter cordinates of y2: "))

distance = math.sqrt((x2-x1) + (y2-y1))
print(f"The distnce between two cordinates of points (x1,x2) and (y1,y2) is {distance:.2f}")


# Question 1(ii)
# Write a Python program to find maximum between three numbers.

numbers = [4,6,8]
for x in numbers:
    print(max(x))
