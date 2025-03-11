# Kullanıcıdan sayı al
sayi = int(input("Bir sayı girin: "))

# 1'den girilen sayıya kadar olan sayıların toplamını for döngüsü ile hesapla
toplam_for = 0
for i in range(1, sayi + 1):
    toplam_for += i

# 1'den girilen sayıya kadar olan sayıların toplamını while döngüsü ile hesapla
toplam_while = 0
n = 1
while n <= sayi:
    toplam_while += n
    n += 1

print(f"For döngüsü ile toplam: {toplam_for}")
print(f"While döngüsü ile toplam: {toplam_while}")
