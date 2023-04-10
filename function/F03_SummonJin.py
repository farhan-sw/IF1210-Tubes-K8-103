# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import dataModule
import commands

    # Fungsi SummonJin        login(jenis_jin, data_username)
def summonjin(data_username, NMax : int):

    # KAMUS LOKAL
    # indeks    : integer
    # username  : string
    # password  : string
    # jenis_jin : string
    # isUsername, isPassword    : Boolean
    # data_username             : array of array string

    #ALGORITMA

    # Meminta Input Jenis Jin
    print("Jenis jin yang dapat dipanggil: \n (1) Pengumpul - Bertugas mengumpulkan bahan bangunan \n (2) Pembangun - Bertugas membangun candi")
    jenis_jin   : str   = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ")

    ## Validasi input Jenis Jin
    while(jenis_jin != '1' and jenis_jin != '2'):
        print("\nTidak ada jenis jin bernomor “", jenis_jin, "”!")
        jenis_jin = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ")

    # -------------------- Jenis Jin sudah valid --------------------
    if jenis_jin == '1' :
        print("\nMemilih jin “Pengumpul”.")
    else :
        print("\nMemilih jin “Pembangun”.")

    # Input username jin
    username    : str   = input("\nMasukkan username jin: ") # meminta masukan user
    isUsername  : bool  = False                          # Deklarasi nilai awal, username tidak ditemukan

    # Pencarian username di database
    if(dataModule.cariIndeks(username, data_username, 0, NMax) != (-999)):  # "0" karena username berada di kolom 0
        isUsername = True                       # Username ditemukan

    # Validasi, username harus belum diambil
    while (isUsername == True):
        print("\nUsername “", username, "” sudah diambil!")
        username = input("\nMasukkan username jin: ")

        # Pencarian username di database
        if(dataModule.cariIndeks(username, data_username, 0, NMax) == (-999)): 
            isUsername = False                       # Username tidak ditemukan

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
    
    # Kembalikan nilai matriks baru
    return data_username

