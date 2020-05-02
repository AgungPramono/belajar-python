for letter in "Python":
    print("karakter : {}".format(letter))

# iterasi untuk list

fruits = ["banana", "apel", "manggo", "orange"]
for f in fruits:
    print("fruit : {}".format(fruits))

# menggunakan fungsi len
animals = ["cow", "cat", "snack", "chicken"]
for index in range(len(animals)):
    print("animal {}".format(animals[index]))

# perulangan while
count = 0
while count < 5:
    print("count is {}".format(count))
    count = count + 1

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

