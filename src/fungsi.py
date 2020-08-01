def ucapkan_salam():
    print("hallo")

ucapkan_salam()

#fungsi dengan return value
def tambah(angka1,angka2):
    return angka1 + angka2

print(tambah(angka1=21,angka2=22))    

#fungsi anonim di deklarasikan menggunakan keyword lambda
tambah = lambda param1,param2: param1 + param2;
print("100 + 200 :", tambah(100,200))

