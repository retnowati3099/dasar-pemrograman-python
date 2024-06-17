def is_prime(num):
    if num <= 0 or num == 1:
        return False
    else:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        return count == 2

num = int(input("Masukkan sebarang bilangan: "))
print(num, "bilangan prima?", is_prime(num))
    