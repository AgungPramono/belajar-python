# break
for letter in "Indonesia":
    if letter == "e":
        break
    print("current letter {}".format(letter))

var = 30
while var > 0:
    print("current variabel value {}".format(var))
    var = var - 1
    if var == 5:
        break

# fungsi else setelah for
# mencari bilangan prima
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n / x)
            break
    else:
        # loop fell through without finding a factor
        print(n, "is a prime number")

# else setelah while
n = 5
while n > 0:
    n = n - 1
    if n == 2:
        break
    print(n)
else:
    print("Loop is finished")

# Pass : Digunakan jika Anda menginginkan sebuah pernyataan atau blok
# pernyataan (statement), namun tidak melakukan apapun
# melanjutkan eksekusi sesuai dengan seharusnya
for letter in "Python":
    if letter == "h":
        pass
        print("This is pass block")
    print("Current letter: {}".format(letter))

# List comprehension adalah salah satu cara untuk menghasilkan
# list baru berdasarkan list atau iterables yang telah ada
# sebelumnya

# cara 1
number = [1, 2, 3, 4, 5]
square = []
for n in number:
    square.append(n ** 2)
    print(square)

# cara 2 menggunakan list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)

list_a = range(1, 10, 2)
x = [[a ** 2, a ** 3] for a in list_a]
print("hasil",x)
