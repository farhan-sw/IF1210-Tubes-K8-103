# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import dataModule
import commands

    # Procedure ubahJin(data_user)
def ubahJin(data_username, NMax):
    # { I.S data_user terdefinisi }
    # { F.S data_user termodifikasi pengubahan tipe jin }

    # KAMUS LOKAL
    # username      : string
    # role_jin      : string
    # jawaban       : string
    # indeks_jin    : integer
    # isUsername    : boolean

    # ALGORITMA

    # -------------------- Validasi Username Jin  --------------------
    # Meminta input nama jin yang ingin diubah
    username    : str   = input("\nMasukkan username jin: ") # meminta masukan user
    isUsername  : bool  = False                          # Deklarasi nilai awal, username tidak ditemukan

    # Pencarian username di database
    if(dataModule.cariIndeks(username, data_username, 0, NMax) != (-999)):  # "0" karena username berada di kolom 0
        isUsername = True                       # Username ditemukan

    # Jika username tidak ada, tidak lakukan apa-apa
    if (isUsername == False):
        print("Tidak ada jin dengan username tersebut.")
        return data_username
    # -------------------- Username Ditemukan  --------------------


    # -------------------- Validasi Jawaban Pengubahan  --------------------
    # Deklarasi variabel role jin
    role_jin    : str   = dataModule.cariRole(username, data_username, NMax)

    # Jika jin pengumpul, ubah ke jin pembangun
    if (role_jin == 'jin_pengumpul'):
        print("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?")
    else: # role_jin == jin_pembangun
        print("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)?")

    # Deklarasi dan validasi jawaban user
    jawaban     : str   = input()
    while(jawaban != "Y" and jawaban != "N"):
        print("Pilihan hanya (Y/N)!")
        jawaban : str   = input("Yakin ingin mengubah pilihan")
    # -------------------- Jawaban Sudah Valid  --------------------


    # -------------------- Prosedur Pengubahan Role Jin  --------------------
    indeks_jin  : int   = dataModule.cariIndeks(username, data_username, 0, NMax)
    if (jawaban == "N"):
        print("Perubahan tidak disimpan")
    else: # jawaban == "Y"
        if (role_jin == 'jin_pengumpul'):
            data_username[indeks_jin][2] = 'jin_pembangun'
        else: # role_jin == jin_pembangun
            data_username[indeks_jin][2] = 'jin_pengumpul'
        
        print("Jin telah berhasil diubah.")