
def cari_tahun(tahun):
    if ((tahun % 400 == 0) or (tahun % 4 == 0)):
        print(tahun," adalah tahun kabisat")
    else:
        print(tahun, "bukan tahun kabisat")

tahun  = 2020
cari_tahun(tahun)