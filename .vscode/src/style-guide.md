## Baris Lanjutan ##    
    # Opsi 1
    # Rata kiri dengan kurung atau pemisah dengan argumen utama

```python
   foo = long_function_name(var_one, var_two,
                             var_three, var_four)
```  

    # Opsi 2
    # Tambahkan indentasi ekstra - (level indentasi baru) untuk memisahkan parameter/argument dari bagian lainnya
    def long_function_name(
            var_one, var_two, var_three,
            var_four):
        print(var_one)
     
    # Opsi 3
    # Hanging indents dengan penambahan level indentasi saja
    foo = long_function_name(
        var_one, var_two,
        var_three, var_four)

## Kondisional IF ##

    # Contoh kondisi visual yang tidak diubah/tanpa indentasi
    if (sebuah kondisi dan
        kondisi yang lain):
        lakukanSesuatu()
     
    # Tambahkan komentar
    if (sebuah kondisi dan
        kondisi yang lain):
        #Mengingat Keduanya Benar, lakukan hal berikut
        lakukanSesuatu()
     
    # Tambahkan ekstra indentasi pada baris lanjutan
    if (sebuah kondisi dan
            kondisi yang lain):
        lakukanSesuatu()        


## Kurung/siku penutup ##

```python
    my_list = [
        1, 2, 3,
        4, 5, 6,
        ]
     
    result = some_function_that_takes_arguments(
        'a', 'b', 'c',
        'd', 'e', 'f',
        )        
```        

    my_list = [
        1, 2, 3,
        4, 5, 6,
    ]
     
    result = some_function_that_takes_arguments(
        'a', 'b', 'c',
        'd', 'e', 'f',
    )


