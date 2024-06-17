class Car:
    def __init__(self):
        self.name = ""
        self.manufacturer = ""
        self.year = 0

# deklarasi class tanpa atribut
class Animal:
    def __init__(self):
        pass

class Fruit:
    pass

class Person:
    def __init__(self):
        self.first_name = "Retno"
        self.last_name = "Wati"

# Pembuatan instance object dari class Person
person1 = Person()
print(f"instance object: {person1}")
print(f"type: {type(person1)}")

# mengakses instance attribute dari class Person
print(f"firstname: {person1.first_name}")
print(f"lastname: {person1.last_name}")

person1.first_name = "Afriska Yusuf"
person1.last_name ="Widyamto"

print(f"firstname: {person1.first_name}")
print(f"lastname: {person1.last_name}")

# pengecekan instance object
if isinstance(person1, Person):
    print(f"person1 class is Person") # output: person1 class is Person


'''
- Class adalah blueprint untuk membuat variabel, bisa juga diartikan sebagai tipe data.
- Di Python, setiap data pasti memiliki tipe data yang tipe tersebut merupakan class.
- Selain menggunakan class - class yang tersedia di Python Stdlib, kita bisa membuat custom class via keyword class.
- Custom class (atau cukup class) digunakan untuk membuat variabel object.
- Deklarasi class dilakukan dengan menggunakan keyword class diikuti oleh nama class yang diinginkan, lalu di dalam block class tersebut perlu dideklarasikan suatu fungsi dengan skema __init__(self) dengan isi body fungsi adalah deklarasi atribut.
- Fungsi __init__(self) disebut dengan method konstruktor.
- Disarankan untuk menulis nama class dalam bentuk TitleCase.
- Instance = inctance variable = instance object = object = variabel objek.
- object adalah variabel yang dibuat dari class yaitu dengan cara memanggil nama class diikuti oleh tanda kurung fungsi () (seperti pemanggilan fungsi) yang mengembalikan nilai balik berupa object baru yang bertipe data sesuai dengan class yang digunakan.
- Salah satu properti class adalah atribut.
- Atribut adalah variabel yang terasosiasi dengan class sehingga dalam pengaksesannya harus dilakukan melalui class dan /atau instance object.
- Atribut sebenernya ada dua jenis, yaitu instance attribute dan class attribute.
- Cara deklarasi instance atribbute mirip dengan deklarasi variabel, pembedanya pada penulisannya diawali self.. Selain itu deklarasinya harus berada di dalam body fungsi __init__(self).
- Untuk mengakses instance attribute, kita dapat melakukannya melalui variabel objek yang dibuat dari cass dengan notasi pengaksesan: object.attribute.
- Class jika dilihat dari strukturnya memiliki kesamaan dengan dictionary. Cass memiliki attribute name dan value, sementara dictionary memiliki key dan value.
- Perbedaan utama dari class dan dictionary adalah padd dictionary key-nya bisa dikelola secara dinamis, sedangkan pada class nama attribute-nya adalah fixed.
- Fungsi isinstance() dapat digunakan untuk mengecek apakah suatu object tipe datanya adalah class tertentu atau class yang meng-inherit class tertentu.
- Cara penggunaan fungsi isinstance() adalah dengan memanggil fungsi tersebut lalu sertakan variable object yang ingin dicek sebagai argumen pertama dan tipe data class sebagai argumen kedua.
'''