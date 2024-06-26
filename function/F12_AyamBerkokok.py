import sys
sys.path.insert(0, 'function')
import dataModule

# PROSEDUR AYAM BERKOKOK           ayamberkokok(INPUT candi : list[list[str]], INPUT NMax_candi : int, OUTPUT : String)
def ayamberkokok (candi : list[list[str]], NMax_candi : int) :
    # I.S fungsi menerima jumlah candi yang sudah terbentuk
    # F.S fungsi mengembalikan hasil akhir dair permainan apakah roro menang atau bondowoso yang menang

    # KAMUS LOKAL :

    total_candi : int

    # ALGORITMA UTAMA
    total_candi = dataModule.hitungCandi(candi, NMax_candi)

    print("Jumlah Candi:",total_candi) 

    if total_candi < 100:
        print(" *Bandung Bondowoso angry noise* ")
        print(" Roro Jonggrang dikutuk menjadi candi. ")
    else:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
