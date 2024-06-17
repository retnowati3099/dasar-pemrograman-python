def is_leap_year(year):
    if year % 4 == 0:
        if year% 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False
    
year = int(input("Masukkan tahun: "))
print(year, "tahun kabisat? ", is_leap_year(year))