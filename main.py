# File: main.py
from function import dataModule
from function import commands
from function import F01_Login
from function import F02_Logout
from function import F03_SummonJin
from function import F05_UbahJin
from function import F06_Pembangun 
from function import F07_Pengumpul
from function import F13_Load

# Siapkan nilai awal
NMax_user   : int = 1000 ; kolom_user  : int = 3
NMax_candi  : int = 1000 ; kolom_candi : int = 5
NMax_bahan  : int = 4 ; kolom_bahan : int = 3

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [["*" for col in range(kolom_user)] for row in range(NMax_user)]            # Matriks data user
candi = [["*" for col in range(kolom_candi)] for row in range(NMax_candi)]          # Matriks data candi
bahan = [["*" for col in range(kolom_bahan)] for row in range(NMax_bahan)]          # Matriks data bahan bangunan

users = F13_Load.load("file/user.csv", NMax_user, users, kolom_user)
candi = F13_Load.load("file/candi.csv", NMax_candi, candi, kolom_candi)
bahan = F13_Load.load("file/bahan_bangunan.csv", NMax_bahan, bahan, kolom_bahan)

# Deklarasi Variabel User
username       : str    = ""
user_isLogin   : bool   = False
user_indeks    : int    = -999
user_role      : str    = "Unknown"

print(commands.excludeEmptyMatriks(users, NMax_user, kolom_user))
print(commands.excludeEmptyMatriks(candi, NMax_candi, kolom_candi))
print(commands.excludeEmptyMatriks(bahan, NMax_bahan, kolom_bahan))

isStart = True
while isStart:
   masukan = input(">>> ")
   #commands.run(masukan)
   if(masukan=="exit()"): isStart=False

   # --------------------------------------------------------------------------------------------
   # IMPLEMENTASI FUNGSI LOGIN F01
   if(masukan == "login" and user_isLogin == False):
      username = input("Username: ")
      user_isLogin   = F01_Login.login(username, users, NMax_user)
      user_indeks    = dataModule.cariIndeks(username, users, 0 ,NMax_user)   # Username ada di kolom 0
      user_role      = dataModule.cariRole(username, users, NMax_user)

   elif (masukan == "logout" and user_isLogin == False):
      print("Logout gagal! Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
   else:
      print("Harap masukkan command yang valid (login/logout)!")
   # --------------------------------------------------------------------------------------------
   
   # Loop ketika terdeteksi sudah login
   while user_isLogin:
      masukan = input(">>> ")

      # --------------------------------------------------------------------------------------------
      # IMPLEMEMNTASI FUNGSI LOGOUT F02
      if(masukan == "logout"):
         user_isLogin = F02_Logout.logout(user_isLogin)
         print("User berhasil loggout")
      
      elif(masukan == "login" and user_isLogin == True):
         print("Anda sudah login, silahkan logout untuk login kembali.")
      # --------------------------------------------------------------------------------------------

      
      # -----------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI SUMMONJIN F03
      elif (masukan == "summonjin"):
         if user_role == "bandung_bondowoso": 
               users = F03_SummonJin.summonjin (users, NMax_user)
         else:
            print("Anda tidak memiliki akses untuk menggunakan perintah ini")
      # -----------------------------------------------------------------------------------------


      # --------------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI HILANGKAN JIN F04

      # --------------------------------------------------------------------------------------------


      # --------------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI UBAH TIPE JIN F05
      elif(masukan == "ubahjin"):
         users = F05_UbahJin.ubahJin(users, NMax_user)
      # --------------------------------------------------------------------------------------------


      # --------------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI JIN PEMBANGUN F06
      elif(masukan == "bangun"):
         if (user_role == "jin_pembangun"):
            candi, bahan = F06_Pembangun.bangun(username, candi, NMax_candi, bahan, NMax_bahan)
         else: # Role selain jin pengumpul
            print("Anda tidak memiliki akses pada menu ini")
      # --------------------------------------------------------------------------------------------
      

      # --------------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI JIN PENGUMPUL F07
      elif(masukan == "kumpul"):
         if (user_role == "jin_pengumpul"):
            bahan = F07_Pengumpul.kumpul(bahan, NMax_bahan)
         else: # Role selain jin pengumpul
            print("Anda tidak memiliki akses pada menu ini")

      # --------------------------------------------------------------------------------------------


      # --------------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI BATCH KUMPUL/BANGUN F08

      # --------------------------------------------------------------------------------------------


      # --------------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI AMBIL LAPORAN JIN F09

      # --------------------------------------------------------------------------------------------


      # --------------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI AMBIL LAPORAN CANDI F10

      # --------------------------------------------------------------------------------------------
      

      # --------------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI HANCURKAN CANDI F11

      # --------------------------------------------------------------------------------------------


      # --------------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI AYAM BERKOKOK F12

      # --------------------------------------------------------------------------------------------
      





      elif( masukan == "printInfo"):
         search_username = input("Masukkan username yang ingin dicari: ")
         dataModule.printInfo(search_username, users, NMax_user)
      elif( masukan == "Info" ):
         print(username, user_isLogin, user_indeks, user_role)


      # --------------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI PRINT DATABASE LOKAL
      # Hanya untuk role : bandung_bondowoso

      elif(masukan == "print all"):
         if user_role == "bandung_bondowoso0": 
            print("Anda tidak memiliki akses untuk menggunakan perintah ini")
         
         else: # role bandung_bondowoso
            # Insiasi data awal dan validasi pilihan
            isPrint  : bool   = False
            pilihan  : str    = ""
            while (isPrint == False):
               pilihan = input("Apa yang ingin di print? \n (1) User \n (2) Candi \n (3) Bahan \n \n")
               if (pilihan == "1" or pilihan == "2" or pilihan == "3"):
                  isPrint = True
            
            # Jika print semua user
            if (pilihan == "1"):
               dataModule.printUsername(users, NMax_user)
            # Jika print candi
            elif(pilihan == "2"):
               dataModule.printCandi(candi, NMax_candi)
            # Jika print semua bahan
            else: # pilihan == "3"
               dataModule.printBahan(bahan, NMax_bahan)
      
      # --------------------------------------------------------------------------------------------
            
      # IMPLEMENTASI FUNGSI SAVE F14

      # --------------------------------------------------------------------------------------------

      else:
         print("Perintah tidak ditemukan, ketik 'Help' untuk bantuan")
