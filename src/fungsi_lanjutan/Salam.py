from datetime import datetime

def ucapkan_salam():
    print("Selamat Pagi Indonesia")
    print("Selamat Datang")
    print("Merdeka!!!!")

def tampilkan_waktu_sekarang():
    now = datetime.today()
    return now.strftime("%d/%m/%Y %H:%S")