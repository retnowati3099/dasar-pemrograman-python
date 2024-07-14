# list dengan tipe data elemennya berupa int
list_1 = [2, 4, 6, 8]
print(list_1)

# list dengan tipe data elemennya berupa str
list_2 = ['Afriska', 'Yusuf', 'Widyamto', 'Retno', 'Wati']
print(list_2)

# list dengan beberapa jenis tipe data di dalam elemennya
list_3 = [24, 'True', "Hello Afriska"]
print(list_3)

# list kosong
list_4 = []

# list dengan deklarasi element secara variabel
list_5 = [
    2,
    4,
    6,
    8
]

# pengaksesan elemen list
print(list_1[0]) # output: 2
print(list_2[1]) # output: 'Yusuf'
print(list_3[2]) # output: 'Hello Afriska'

# perulangan list
numbers = [1, 3, 5, 7, 9]
for number in numbers:
    print("elemen:", number)

# perulangan list menggunakan indeks
for i in range(0, len(numbers)):
    print("elemen", i,":", numbers[i])

#perulangan dengan fungsi enumerate
for index, value in enumerate(numbers):
    print("elemen", index, ":", value)

# nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for cel in row:
        print(cel, end=" ")
    print()

# konversi range ke list
# list dimulai angka 0 hingga 9
range_1 = range(0, 10)
print(list(range_1))

# list dimulai dari angka 1 hingga 21 dengan penambahan 3
range_2 = range(1, 22, 3)
print(list(range_2))

# list dimulai dari angka 100 hingga 0 dengan pengurangan -10
range_3 = range(100, 0, -10)
print(list(range_3))

# konversi string ke list
full_name = "Retno Wati"
print(list(full_name))

# konversi tuple ke list
tuple_1 = (1, 2, 3, 4)
print(list(tuple_1))

# mengecek apakah elemen ada


"""
- List adalah tipe data untuk menampung nilai kolektif yang disimpan secara urut, dengan isi bisa berupa banyak varian tipe data (tidak harus sejenis).
- Penerapan list adalah dengan menuliskan nilai kolektif dengan pembatas tanda koma dan diapit tanda kurung siku.
- Data dalam list biasa disebut dengan elemen.
- Setiap elemen disimpan di list secara urut dengan penanda urutan yang disebut indeks.
- Pengaksesan elemen list menggunakan notasi nama_list[indeks].
- Pengaksesanelemen menggunakan indeks di luar kapasitas data akan menghasilkan error.
"""
