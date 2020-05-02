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

#fungsi else setelah for


