import os
import random
import string

data = dict()

while True:
    os.system("cls")  # WIN
    # os.system("clear") # mac/linux
    print(f"{'DATA PENERBANGAN':_^45}")
    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range(3))
    Maskapai = input("Enter Maskapai\t\t:")
    Tujuan = input("Enter Tujuan\t\t:")
    Hari = input("Enter Hari\t\t:")
    
    data[keyFinal] = {
        'Maskapaikey': Maskapai,
        'Tujuankey': Tujuan,
        'Harikey': Hari
    }

    opsi = input("input data LAGI (y/t) :").lower()
    if opsi == 't':
        break

print("-" *40)
print(f"Key\t Maskapai\t Tujuan\t Hari")
print("-" * 40)
for key, value in data.items():
    print(f"{key} \t {value.get('Maskapaikey')} \t {value.get('Tujuankey')} \t {value.get('Harikey')}")
