def is_even_or_odd(n):
    if n % 2 == 0:
        print("%s is even number" % (n))
    else:
        print("%s is odd number" % (n))

str_input = input("Enter your number: ")
num = int(str_input)
is_even_or_odd(num)