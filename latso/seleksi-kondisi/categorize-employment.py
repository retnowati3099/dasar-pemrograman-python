def categorize_employment(years):
    if years > 10:
        return "Kamu Expert"
    elif years >= 5:
        return "Kamu Senior"
    elif years >= 2:
        return "Kamu Mid-Level"
    else:
        return "Kamu Junior"

years = int(input("Masukkan lama kamu bekerja (tahun): "))
print(categorize_employment(years))