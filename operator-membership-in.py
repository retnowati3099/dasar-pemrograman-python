sample_list = [2, 3, 4]
is_3_exists = 3 in sample_list
print(is_3_exists) # output: True

sample_tuple = ("hello", "afriska")
is_hello_exists = "hello" in sample_tuple
print(is_hello_exists) # output: True

sample_dict = {
    "nama": "afriska",
    "age": 26
}
is_key_name_exists = "nama" in sample_dict
print(is_key_name_exists) # output: True

sample_set = {"besuk", "libur"}
is_libur_exists = "libur" in sample_set
print(is_libur_exists) # output: True

sample_str = "Afriska Yusuf Widyamto"
is_yusuf_exists = "Yusuf" in sample_str
print(is_yusuf_exists) # output: True

'''
- Operator in  digunakan untuk mengecek apakah suatu nilai merupakan bagian dari data kolektif atau tidak.
- Operator in bisa dipergunakan pada semua tipe data kolektif seperti dictionary, set, tuple, dan list. Selain itu bisa juga digunakan pada string untuk pengecekan substring.
- Operator in jikaditerapkan pada tipe dictionary, yang dicek adalah key-nya bukan value-nya
'''