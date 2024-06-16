def categorize_age(age):
    if age >= 65:
        print("Anda Lansia")
    elif age >= 18:
        print("Anda Dewasa")
    elif age >= 12:
        print("Anda Remaja")
    else:
        print("Anda Anak - Anak")

age = int(input("Masukkan umur Anda: "))
categorize_age(age)