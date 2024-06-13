bil_1 = 1001
bil_2 = 1001
hasil = bil_1 is bil_2
print("bil_1 is bil_2 =", hasil)
print("id(bil_1): %s, id(bul_2): %s" % (id(bil_1), id(bil_2)))

"""
- Operaor is memiliki kemiripan dengan operator logika ==, pembedanya pada operator is yang dibandingkan bukan nilai, melainkan identitas atau ID-nya.
- Bisa saja ada dua variabel bernilai sama tapi identitasnya berbeda
- Operator id() digunakan untuk mengambil nilai identitas atau ID dari suatu data, kembaliannya bertipe numerik.
"""
