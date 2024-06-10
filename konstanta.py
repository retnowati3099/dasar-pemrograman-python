from typing import Final

#  tipe konstanta PI tidak ditentukan secara eksplisit, melainkandidapat dari tipe data nilai
PI: Final = 3.14
print("pi: %.2f" % (PI))

# tipe konstanta TOTAL_MONNTH ditentukan secara eksplisit yaitu int
TOTAL_MONTH: Final[int] = 12

'''
- Deklarasi konstanta di Python dilakukan menggunakan bantuan tipe data class bernama typing.Final.
- Untuk menggunakannya, typing.Final perlu di-import terlebih dahulu menggunakan keyword from dan import
- Keyword import digunakan untuk mengimport sesuatu, sedangkan keyword from digunakan untuk menentukan dari module mana sesuatu tersebut akan diimport.
- Statement from typing import Final artinya adalah meng-impor tipe Final dari module typing yang dimana module ini merupakan bagian dari Python standard library.
- Tipe Final digunakan untuk menandai suatu variabel adalah tidak bisa diubah nilainya (konstanta).
- Cara penerapan Final bisa dengan dituliskan tipe data konstantanya secara eksplisit atau boleh tidak ditentukan (tipe akan diidentifikasi oleh interpreter berdasarkan tipe data dan nilainya).
- Nama konstanta harus dituliskan dalam huruf besar (UPPER_cASE)
'''