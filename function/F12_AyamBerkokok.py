# Fungsi Ayam Berkokok           ayamberkokok(total_candi : int)
def ayamberkokok (total_candi : int) :
    # KAMUS LOKAL :
    
    # total_candi : int

    # ALGORITMA UTAMA
    if total_candi is not None and total_candi < 100 :
        print("Kukuruyuk.. Kukuruyuk..\n")
        print("Jumlah Candi:",total_candi) 
        print("\nSelamat, Roro Jonggrang memenangkan permainan!\n\n*Bandung Bondowoso angry noise*\n\nRoro Jonggrang dikutuk menjadi candi.")
        exit()
    else : # total_candi >= 100
        print ("Kukuruyuk.. Kukuruyuk..\n\nJumlah Candi:",str(total_candi)+"\n\nYah, Bandung Bondowoso memenangkan permainan!\n")
        exit()
