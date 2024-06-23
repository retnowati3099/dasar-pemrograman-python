class Student:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.grade = 0

    def info(self):
        print(f"Student name: {self.name}")
        print(f"Student age: {self.age}")
        print(f"Student grade: {self.grade}")
        print()

    def set_details(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


all_student = []

student1 = Student()
student1.name = "Retno Wati"
student1.age = 23
student1.grade = 3.53
all_student.append(student1)

student2 = Student()
student2.name = "Queena Putri Askawati"
student2.age = 21
student2.grade = 4.00
all_student.append(student2)

print(all_student)

for mahasiswa in all_student:
    print(f"Student name: {mahasiswa.name}")
    print(f"Student age: {mahasiswa.age}")
    print(f"Student grade: {mahasiswa.grade}")
    print()

for mahasiswa in all_student:
    mahasiswa.info()

student3 = Student()
print(student3.name)  # output: ""
print(student3.age)  # output: 0
print(student3.grade)  # output: 0

student3.name = "Askara Yusuf Erwana"
student3.age = 21
student3.grade = 4.00
print(student3.name)  # output: Askara Yusuf Erwana
print(student3.age)  # output: 21
print(student3.grade)  # output: 4.00

student3.set_details("Askara Yusuf Erwandika", 22, 4.00)
print(student3.name)  # output: Askara Yusuf Erwandika
print(student3.age)  # output: 22
print(student3.grade)  # output: 4.00


class FavoriteFood:
    def __init__(self):
        self.name = ""

    def print_name(self):
        print(self.name)

    def get_name(self) -> str:
        return self.name

    def set_name(self, name):
        self.name = name


food1 = FavoriteFood()

# pengaksesan instance method lewat instance object
food1.set_name("Pizza")
food1.print_name()
print(food1.get_name())

# pengaksesan instance method lewat class
FavoriteFood.set_name(food1, "Burger")
FavoriteFood.print_name(food1)
print(FavoriteFood.get_name(food1))

"""
- Jika attribute adalah variabel yang berasosiasi dengan class, maka method adalah fungsi yang berasosiasi dengan class.
- Python mengenal 3 jenis method, yaitu instance method, class method, dan static method.
- Karakteristik instance method jika dilihat dari sintaksnya: deklarasinya di dalam block class, parameter pertamanya adalah self, dan method diakses menggunakan notasi object.method().
- Salah satu aturan pada instance method adalah fungsi harus memiliki parameter pertama bernama self.
- Parameter pertama bernama self wajib ada saat deklarasi dan tidak boleh diisi argument saat pemanggilan. Jika dipaksa diisi dengan argument, maka pasti muncul error. Pun jika parameter self tidak  ditulis saat deklarasi instance method, hasilnya juga error.
- Parameter self bisa disebut parameter implicit atau implisit karena kita tidak berinteraksi langsung saat pengisian nilai. Nilai self otomatis terisi saat pemanggilan instance method via instance object.
-Parameter self merupakan variabel yang merepresentasikan suatu object atau instance.
- Melalui variabel self, kita bisa mengakses instance attribute maupun instance method (selama properti tersebut masih dalam satu class).
- Nama method dianjurkan untuk ditulis menggunakan snake_case (seperti fungsi). Sedangkan aturan penulisan nama parameter / argument adalah sama seperti nama variabel, yaitu menggunakan snake_case juga.
- Terdapat dua cara untuk mengakses instance method, yaitu lewat instance object dan lewat class dengan ketentuan dalam pemanggilan methodnya, parameter pertama harus diisi dengan instance object.
"""
