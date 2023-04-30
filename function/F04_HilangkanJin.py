# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import dataModule

# FUNGSI MENGHAPUS JIN DAN CANDI        hapusjin(data_user : list[list[str]], NMax_user : int, data_candi : list[list[str]], NMax_candi : int) -> (data_user : list[list[str]], data_candi : list[list[str]])
def hapusjin(data_user : list[list[str]], NMax_user : int, data_candi : list[list[str]], NMax_candi : int):
    # { INPUT : data_user : list[list[str]], NMax_user : int, data_candi : list[list[str]], NMax_candi : int
    #   OUTPUT : (data_user : list[list[str]], data_candi : list[list[str]]) }

    # KAMUS LOKAL
    jin_username    : str
    indeks_jin      : int
    pilihan         : str

    # ALGORITMA
    # Input Username Jin
    jin_username    = input("Masukkan username jin: ")
    
    # Cari Lokasi jin
    indeks_jin      = dataModule.cariIndeks(jin_username, data_user, 0, NMax_user)
    if (indeks_jin == (-999)):  # Jin tidak ditemukan
        print("Tidak ada jin dengan username tersebut.")
        return(data_user, data_candi)
    else:                       # Jin ditemukan
        # Meminta pilihan user
        pilihan     = input(f"Apakah anda yakin ingin menghapus jin dengan username {jin_username} (Y/N)? ")
        while (pilihan != "Y" and pilihan != "N"):           # Validasi jawaban
            pilihan = input(f"Input tidak benar \nApakah anda yakin ingin menghapus jin dengan username {jin_username} (Y/N)? ")

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

