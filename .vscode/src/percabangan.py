var1 = 100
if var1:
    print("nilai benar")
    print(var1)
var2 = 9
if var2 > 8:
    print("nilai lebih dari 8")

# if else

total = int(input("masukkan total pembelian : "))

if total > 300000:
    diskon = total * 0.05
    print("anda mendapatkan diskon : ", diskon)
else:
    diskon = total * 0.103
    print("anda mendapatkan diskon : ", diskon)

print("Total pembayaran : ", total - diskon)


# Elif - Alternatif untuk Switch/Case dan IF bertingkat di python
totalBelanja = int(input("input total :"))

if total > 300000:
    diskon = total * 0.05
    print("anda mendapatkan diskon : ", diskon)
elif totalBelanja < 5000:
    discount = totalBelanja * 0.10
    print("Discount", discount)
else:
    diskon = total * 0.103
    print("anda mendapatkan diskon : ", total - discount)
