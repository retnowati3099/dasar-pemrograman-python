def calculate_discount(price, membership):
    if membership == 'gold':
        return (100 - 20) / 100 * price
    elif membership == 'silver':
        return (100 - 10) / 100 * price
    elif membership == 'bronze':
        return price
    
print("Jenis keanggotaan: ")
print("1. Gold")
print("2. Silver")
print("3. Bronze")
membership = input("Masukkan jenis keanggotaan: ")
membership_lower = membership.lower()
price = int(input("Masukkan harga: "))
print("Harga yang harus dibayar:", calculate_discount(price, membership_lower))