
#tipe data bilangan bulat
a = 5
print(a)

#tipe data float / pecahan
a = 2.0
print(a)

#tipe data complex
a = 1+2j
print(a)

#deret fibonaci
x = [0] * 10005 #inisialisasi array sebanyak 10005
x[1] = 1

for j in range(2,10001):
    x[j]=x[j-1]+x[j-2]
print(x[10000])    


b = 0.1234567890123456789
print(b)

b = 1234567890123456789
print(b)

#string
s = "Hallo Selamat Datang"
print(s)
print(s[4])
print(s[6:13])

#boolean


#List
a = [1,2.0,"agung"]
print(a[0])
print(a[1])
print(a[2])


#hapus karakter
animal = ["cat","snack","python"]
del animal[2]
print(animal)

#tuple list yg tidak bisa diubah
t = (3,2.0,"5+hewan")
print(t)

# t[0]=21 tidak bisa dilakukan

#Set kumpulan element unik tanpa urutan
# jika ada element yang sama maka salah satu otomatis akan
# dihapus
set = {1,2,2,3,4,5}
print(set)
print(type(set))
print("isi dari set :", set)

#Disctionary : kumpulan kunci-nilai
#setiap elemen dipisahkan koma(,)
#key & value dipisahkan :
#key dapat berupa tipe data apapun
d = {1:"ini value","ini kunci":22}
print(type(d))

#CAST -  konversi tipe data
float(5)
print(float(5))