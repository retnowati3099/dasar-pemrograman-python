# keyword if
grade = 100

if grade == 100:
    print("perfect")

if grade == 90:
    print("ok")
    print("keep working hard!")


# keyword elif dan else
str_input = input("Enter your grade: ")
res = int(str_input)
if res == 100:
    print("perfect")
elif res >= 85:
    print("awesome")
elif res >= 65:
    print("passed the exam")
else:
    print("below the passing grade")

'''
- Seleksi kondisi adalah suatu blok kode yang dieksekusi hanya ketika kriteria yang ditentukan terpenuhi.
- Keyword if adalah keyword seleksi kondisi di Python. Cara penerapannya: tulis if diikuti kondisi berupa nilai boolean atau statement logika, lalu dibawahnya ditulis blok kode yang ingin dieksekusi ketika kondisi tersebut terpenuhi.
- Di python, suatu blok kondisi ditandai dengan indentation atau spasi yang menjadikan kode semakin menjorok ke kanan.
- Indentasi di python menggunakan 4 karakter spasi dan bukan karakter tab.
- elif kepanjangan dari else if, digunakan untuk menambahkan blok seleksi kondisi baru, untuk mengantisipasi blok if yang tidak terpenuhi.
- Dalam penerapannya, suatu blok seleksi kondisi harus diawali dengan if, keyword elif hanya bisa dipergunakan pada kondisi setelahnya yang masih satu rantai.
- else digunakan sebagai blok seleksi kondisi penutup ketika blok if dan / atau elif dalam satu rantai tidak ada yang terpenuhi.
'''