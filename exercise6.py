n = 0
x_1 = input("Please, enter number of triangle numbers: ")
x = int(x_1)
for n in range (x):
    n = n + 1
    x = n * (n+1)/2
    print(int(x), end=" ")
print(" ")
