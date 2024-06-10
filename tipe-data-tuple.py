# tuple dengan tipe data elemennya berupa int
tuple_1 = (2, 4, 6, 8)
print(tuple_1)

# tuple dengan tipe data elemennya berupa str
tuple_2 = ('Afriska', 'Yusuf', 'Widyamto', 'Retno', 'Wati')
print(tuple_2)

# tuple dengan beberapa jenis tipe data di dalamnya
tuple_3 = (24, 'True', 'Hello Afriska')

# pengaksesan elemen tuple
print(tuple_1[0])
print(tuple_2[1])
print(tuple_3[2])

'''
- Tuple adalah tipe data kolektif yang mirip dengan list dengan pembeda yaitu: 
(1) nilai pada data list bisa diubah sedangkan nilai pada data tuple tidak bisa berubah.
(2) List menggunakan tanda kurung siku [] untuk penulisan literal, sedangkan pada tuple menggunakan tanda kurung biasa ().
- Pengaksesan elemen tuple menggunakan notasi nama_tuple[indeks]
'''