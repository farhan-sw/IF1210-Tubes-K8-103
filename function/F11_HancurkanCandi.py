import sys
sys.path.insert(0, 'function')
import dataModule

# FUNGSI HANCURKAN CANDI           hancurkanCandi(data_candi : array of array str, NMax_candi : int) -> data_candi : array of array str
def hancurkanCandi(data_candi : list[list[str]], NMax_candi : int):
    
    # KAMUS LOKAL
    id      : str
    posisi  : int

    # ALGORITMA
    id = (input("Masukkan ID candi: "))
    posisi = dataModule.cariIndeks(id, data_candi, 0,0, NMax_candi)
    
    if (posisi == (-999)):                              # Indeks tidak tidemukan
        print("Tidak ada candi dengan ID tersebut.")
    else:                                               # Indeks ditemukan
        pilihan = input(f'Apakah anda yakin ingin menghapus jin dengan id {id}: (Y/N)?')
        while pilihan != "Y" and pilihan != "N":
            pilihan = input(f'Input tidak benar \nApakah anda yakin ingin menghancurkan candi dengan id {id}: (Y/N)?')
        
        if pilihan == "N":
            print("Candi tidak dihancurkan")
            return(data_candi)
        else:
            data_candi[posisi][0] = "*"
            data_candi[posisi][1] = "*"
            data_candi[posisi][2] = "*"
            data_candi[posisi][3] = "*"
            
            print("Candi berhasil dihancurkan")
            return(data_candi)              # Kembalikan data candi terupdate

