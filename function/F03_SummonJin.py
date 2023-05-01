# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import dataModule
import commands

    # Fungsi SummonJin        summonjin(data_username : list[list[str]], NMax : int) -> data_username : list[list[str]]
def summonjin(data_username, NMax : int):
    # { INPUT   : data_username : list[list[str]], NMax : int}
    #   OUTPUT  : data_username : list[list[str]] }

    # KAMUS LOKAL
    # indeks    : integer
    # username  : string
    # password  : string
    # jenis_jin : string
    # isUsername, isPassword    : Boolean
    # data_username             : array of array string
    # indeks    : integer
    # str_jenisJin : string

    #ALGORITMA

    total_jin = 0
    for i in range (1, NMax) :
        if data_username[i][0] != "*" and data_username[i][1] != "*" and (data_username [i][2] == 'jin_pengumpul'or data_username [i][2] == 'jin_pembangun') :
            total_jin += 1

    if total_jin < 100 :
        # Meminta Input Jenis Jin
        print("Jenis jin yang dapat dipanggil: \n (1) Pengumpul - Bertugas mengumpulkan bahan bangunan \n (2) Pembangun - Bertugas membangun candi")
        jenis_jin   : str   = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ")

        ## Validasi input Jenis Jin
        str_jenisJin : str
        while(jenis_jin != '1' and jenis_jin != '2'):
            print("\nTidak ada jenis jin bernomor “", jenis_jin, "”!")
            jenis_jin = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ")

        # -------------------- Jenis Jin sudah valid --------------------
        if jenis_jin == '1' :
            print("\nMemilih jin “Pengumpul”.")
            str_jenisJin = "jin_pengumpul"
        else :
            print("\nMemilih jin “Pembangun”.")
            str_jenisJin = "jin_pengumpul"


        isUsername  : bool  = False                          # Deklarasi nilai awal, username tidak ditemukan

        # Validasi, username harus belum diambil
        while (isUsername == False):
            # Input username jin
            username    : str   = input("\nMasukkan username jin: ") # meminta masukan user
        
            # Pencarian username di database
            indeks      : int   = dataModule.cariIndeks(username, data_username, 0, 0, NMax)

            if (indeks == (-999)): # Username tidak ditemukan
               isUsername   = True                          # Deklarasi nilai awal, username tidak ditemukan
        
            else: # Ditemukan username serupa, cek role nya
                # Cek Role
                i = indeks
                found : bool = False
                while i < NMax and found  == False:
                    if(data_username[i][2] == str_jenisJin and data_username[i][0] == username):  # "0" karena username berada di kolom 0
                        found  = True
                    i += 1
             
                if (found):
                    print("\nUsername “", username, "” sudah diambil!")
                    isUsername   = False
                else:
                    isUsername   = True


        # -------------------- Username Belum Diambil  --------------------

        password    : str   = input("Masukkan password jin: ")
        while (len(password) < 5 or len(password) > 25):
            print("\nPassword panjangnya harus 5-25 karakter!")
            password    = input("Masukkan password jin: ")
    
        # -------------------- Password Sudah Valid  --------------------
        # Cari indeks data kosong terdekat
        indeks  : int   = 0
        found   : bool  = False
        while (indeks < NMax) and (found == False):
            indeks += 1                                         # Tambahkan indeks
            if(data_username[indeks][0] == "*"):
                found = True

        # Update data user di berdasarkan indeks
        if (jenis_jin == '1') : # Jin Pengumpul
            data_username[indeks][0] = username                  # Update username
            data_username[indeks][1] = password                  # Update password
            data_username[indeks][2] = 'jin_pengumpul'           # Update role
        else: #(jenis_jin == 2)
            data_username[indeks][0] = username                  # Update username
            data_username[indeks][1] = password                  # Update password
            data_username[indeks][2] = 'jin_pembangun'           # Update role
            
        # Print Mantra
        print(f"\nMengumpulkan sesajen... \nMenyerahkan sesajen... \nMembacakan mantra... \n \nJin {username} berhasil dipanggil!")
    else:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")

    # Kembalikan nilai matriks baru
    return data_username

