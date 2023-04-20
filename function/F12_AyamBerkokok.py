# PROSEDUR Ayam Berkokok           ayamberkokok(input total_candi : int) 

def ayamberkokok (total_candi : int) :
    
# I.S fungsi menerima jumlah candi yang sudah terbentuk
# F.S fungsi mengembalikan hasil akhir dair permainan apakah roro menang atau bondowoso yang menang
    
    # KAMUS LOKAL :
    
    total_candi : int

    # ALGORITMA UTAMA
    if total_candi is not None and total_candi < 100 :
        print("Kukuruyuk.. Kukuruyuk..\n")
        print("Jumlah Candi:",total_candi) 
        print("\nSelamat, Roro Jonggrang memenangkan permainan!\n\n*Bandung Bondowoso angry noise*\n\nRoro Jonggrang dikutuk menjadi candi.")
        exit()
    else : # total_candi >= 100
        print ("Kukuruyuk.. Kukuruyuk..\n\nJumlah Candi:",str(total_candi)+"\n\nYah, Bandung Bondowoso memenangkan permainan!\n")
        exit()

