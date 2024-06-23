for i in range(5):
    print("index:", i)

r = range(5)
print(r)
print(list(r))

# contoh perulangan yang ekuivalen
for i in range(3):
    print("index:", i)

for i in range(0, 3):
    print("index:", i)

for i in range(0, 3, 1):
    print("index:", i)

# decrement
for i in range(3, -3, -1):
    print(i)

# iterasi data list
messages = ["morning", "afternoon", "evening"]
for m in messages:
    print(m)

# iterasi data tuple
fruits = ("apple", "pineapple", "banana")
for f in fruits:
    print(f)

# iterasi data string
for char in "hello afriska":
    print(char)

# iterasi data dictionary
bio = {"name": "Afriska Yusuf Widyamto", "birthday": "13-04-1998"}
for key in bio:
    print("key:", key, "value:", bio[key])

# iterasi data set
colors = {"red", "blue", "white"}
for c in colors:
    print(c)

# perulangan bercabang (nested for)
max = int(input("Masukkan jumlah bintang: "))
for i in range(max):
    for j in range(i + 1):
        print("* ", end="")
    print()

"""
- Perulangan atau looping merupakan teknik untuk mengulang - ulang eksekusi suau blok kode atau mengiterasi elemen milik tipe data kolektif(contohnya list)
- Perulangan di Python bisa dibuat menggunakan kombinasi keyword for dan fungsi range().
- Keyword for adalah keyword untuk perulangan, dalam penerapannya diikuti dengan keyword in.
- Fungsi range() digunakan untuk membuat object range, yang umumnya dipakai sebagai kontrol perulangan.
- Fungsi range menghasilkan object sequence, yaitu jenis data yang strukturnya mirip seperti list tetapi bukan list yang kegunaan utamanya adalah untuk kontrol perulangan.
- Object sequence bisa dikonversi bentuk list dengan cara dibungkus menggunakan fungsi list().
- Statement range(n) enghasilkan data range sejumlah n yang isinya dimulai dari angka 0.
- Selain range(n) ada range(start, stop), hasilnya data range dimulai dari start dan hingga stop - 1. Selain itu ada juga range(start, stop, step), hasilnya data range dimulai dari start dan hingga stop - 1, dengan nilai increment sejumlah step.
- Tipe data yang bisa digunakan pada keyword for biasa disebut dengan tipe iterator.
- Penggunaan keyword for pada tipe daa dict akan mengiterasi key-nya. Dari key tersebut value bisa diambil dengan mudah menggunakan notasi dict[key].
"""
