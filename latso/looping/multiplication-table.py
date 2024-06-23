print("\t", end="")
for i in range(1, 6):
    print(i, end="\t")
print()
for i in range(1, 6):
    print(i, end="\t")
    for j in range(1, 6):
        print(i * j, end="\t")
    print()

"""
Write a python program that uses nested for loops to print a multipication table for numbers 1 to 5.
The output should be formatted so that each row corresponds to a multiplier and each column corresponds to the multiplicand.
"""
