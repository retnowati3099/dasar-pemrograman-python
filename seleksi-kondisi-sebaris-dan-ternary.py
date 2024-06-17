grade = int(input("Masukkan nilai Anda: "))

# bentuk umum if else
if grade >= 65:
    print("passed the exam")
else:
    print("below the passing grade")

# one-line / sebaris
if grade >= 65:
    print("passed the exam")
if grade < 65:
    print("below the passing grade")

# ternary
print("passed the exam") if grade >= 60 else print("below the passing grade")

"""
- Metode penulisan sebaris cocok diterapkan pada situasi dimana seleksi kondisi hanya memiliki 1 kondisi saja.
- Metode penulisan ternary umum diterapkan pada blok kode seleksi kondisi yang memiliki 2 kondisi (True dan False)
"""
