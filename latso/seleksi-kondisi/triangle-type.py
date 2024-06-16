def triangle_type(a, b, c):
    if a == b and b == c:
        print("Segitiga sama sisi")
    elif a == b or a == c:
        print("Segitiga sama kaki")
    else:
        print("Segitiga sebarang")

a = int(input("Masukkan sisi pertama: "))
b = int(input("Masukkan sisi kedua: "))
c = int(input("Masukkan sisi ketiga: "))

triangle_type(a, b, c)