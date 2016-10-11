import math
in_a = input("Please, enter 'a' for your quadratic equation: ")
in_b = input("Please, enter 'b' for your quadratic equation: ")
in_c = input("Please, enter 'c' for your quadratic equation: ")
a = float(in_a)
b = float(in_b)
c = float(in_c)
in_check = (b**2) - (4*a*c)
x_1 = ((b)*(-1) + (math.sqrt(in_check)))
x_2 = ((b)*(-1) - (math.sqrt(in_check)))
if in_check < 0:
    print("Your quadratic equation does not have any real value solutions")
else:
    print("The solutions of your equation are", x_1, x_2)
