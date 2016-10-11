import math
side_a = input("Enter the length of the first side of the triangle: ")
side_b = input("Enter the length of the second side of the triangle: ")
side_c = input("Enter the length of the third side of the triangle: ")
a = float(side_a)
b = float(side_b)
c = float(side_c)
total_area = (1/4) * math.sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))
print(total_area)
