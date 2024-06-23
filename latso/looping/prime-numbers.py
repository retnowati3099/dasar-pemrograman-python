for i in range(10, 51):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)  

'''
Write a python program that uses a for loop to find all prime numbers between 10 and 50! A prime numbers is a number greater than 1 that has no positive divisors other than 1 and itself.
'''