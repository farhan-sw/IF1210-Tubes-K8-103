# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import dataModule

def hapusjin(data_user, NMax_user, data_candi, NMax_candi):
    # FUNGSI MENGHAPUS JIN DAN CANDI
    # { INPUT : 
    #   OUTPUT : }

    # KAMUS LOKAL
    #

    # ALGORITMA
    # Input Username Jin
    jin_username    : str = input("Masukkan username jin: ")
    
    # Cari Lokasi jin
    indeks_jin      : int = dataModule.cariIndeks(jin_username, data_user, 0, NMax_user)
    if (indeks_jin == (-999)):  # Jin tidak ditemukan
        print("Tidak ada jin dengan username tersebut.")
        return(data_user, data_candi)
    else:                       # Jin ditemukan
        # Meminta pilihan user
        pilihan     : str = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
        while (pilihan != "Y" and pilihan != "N"):           # Validasi jawaban
            pilihan     : str = input("Input tidak benar \nApakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")

        if(pilihan == "N"):
            print("Jin tidak dihapus, kembali ke main program")
            return(data_user, data_candi)
        else:   # pilihan == "Y"
            # ---------------- HAPUS JIN DARI USERNAME DATABASE --------------
            data_user[indeks_jin][0] = "*"
            data_user[indeks_jin][1] = "*"
            data_user[indeks_jin][2] = "*"

            # ---------------- HAPUS SETIAP CANDI DIBUAT OLEH JIN ------------
            for i in range(NMax_candi):
                if(data_candi[i][1] == jin_username):
                    data_candi[i][0] = "*"
                    data_candi[i][1] = "*"
                    data_candi[i][2] = "*"
                    data_candi[i][3] = "*"
            
            return(data_user, data_candi)

