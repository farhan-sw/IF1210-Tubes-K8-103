import sys
sys.path.insert(0, 'function')
import dataModule
def hancurkanCandi(data_candi, id, NMax_candi):
    id = int(input("Masukkan ID candi: "))
    posisi = dataModule.cariIndeks
    if (posisi == (-999)):
        print("Tidak ada candi dengan ID tersebut.")
    else:
        pilihan = print(f"Apakah Anda yakin ingin menghancurkan candi ID {id}: (Y/N)")
        while pilihan != "Y" and pilihan != "N":
            pilihan = input(f"Input tidak benar \nApakah anda yakin ingin menghapus jin dengan username {id}: (Y/N)?")
        if pilihan == "N":
            print("Candi tidak dihancurkan")
        else:
            for i in range(NMax_candi):
                if(data_candi[i][0] == id):
                    data_candi[i][0] = "*"
                    data_candi[i][1] = "*"
                    data_candi[i][2] = "*"
                    data_candi[i][3] = "*"


