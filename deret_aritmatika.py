def deret_aritmatika(n, a1, d):
    deret = []
    for i in range(n):
        an = a1 + i * d
        deret.append(an)
    return deret

a1 = input("Masukan nilai suku pertama: ")
d = input("Masukan selisih antar suku: ")
n = input("Masukan jumlah suku yang di inginkan: ")
print(deret_aritmatika(int(n), int(a1), int(d)))