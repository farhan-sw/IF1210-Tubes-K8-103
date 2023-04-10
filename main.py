# File: main.py
from function import dataModule
from function import commands
from function import F01_Login
from function import F02_Logout
from function import F03_SummonJin
from function import F13_Load

#import commands

NMax_user = 1000 ; kolom_user = 3
NMax_candi = 1000 ; kolom_candi = 5
NMax_bahan = 1000 ; kolom_bahan = 3

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [["*" for col in range(kolom_user)] for row in range(NMax_user)]            # Matriks data user
candi = [["*" for col in range(kolom_candi)] for row in range(NMax_candi)]          # Matriks data candi
bahan_bangunan = [["*" for col in range(kolom_bahan)] for row in range(NMax_bahan)] # Data bahan bangunan

users          = F13_Load.load("file/user.csv", NMax_user, users, kolom_user)
candi          = F13_Load.load("file/candi.csv", NMax_candi, candi, kolom_candi)
bahan_bangunan = F13_Load.load("file/bahan_bangunan.csv", NMax_bahan, bahan_bangunan, kolom_bahan)

# Deklarasi Variabel User
username       : str    = ""
user_isLogin   : bool   = False
user_indeks    : int    = -999
user_role      : str    = "Unknown"

print(commands.excludeEmptyMatriks(users, NMax_user, kolom_user))
print(commands.excludeEmptyMatriks(candi, NMax_user, kolom_candi))
print(commands.excludeEmptyMatriks(bahan_bangunan, NMax_user, kolom_bahan))

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
         user_isLogin =F02_Logout.logout(user_isLogin)
         print("User berhasil loggout")
      # --------------------------------------------------------------------------------------------

      
      # -----------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI SUMMONJIN F03
      elif (masukan == "summonjin"):
         if user_role == "bandung_bondowoso": 
               jin_baru = F03_SummonJin.summonjin (users, NMax_user)
         else:
            print("Anda tidak memiliki akses untuk menggunakan perintah ini")
      # -----------------------------------------------------------------------------------------


      # --------------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI HILANGKAN JIN F04

      # --------------------------------------------------------------------------------------------


      # --------------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI UBAH TIPE JIN F05

      # --------------------------------------------------------------------------------------------


      # --------------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI JIN PEMBANGUN F06

      # --------------------------------------------------------------------------------------------
      

      # --------------------------------------------------------------------------------------------
      # IMPLEMENTASI FUNGSI JIN PENGUMPUL F07

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
      
      elif(masukan == "login" and user_isLogin == True):
         print("Anda sudah login, silahkan logout untuk login kembali.")

      elif( masukan == "printInfo"):
         search_username = input("Masukkan username yang ingin dicari: ")
         dataModule.printInfo(search_username, users, NMax_user)
      elif( masukan == "Info" ):
         print(username, user_isLogin, user_indeks, user_role)

      elif(masukan == "print semua user"):
         dataModule.printUsername(users, NMax_user)

      else:
         print("Perintah tidak ditemukan, ketik 'Help' untuk bantuan")
