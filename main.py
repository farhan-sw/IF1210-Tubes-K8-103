# File: main.py
from function import dataModule
from function import F01_Login
from function import commands
#import commands

NMax_user = 30 ; kolom_user = 3
NMax_candi = 1000 ; kolom_candi = 5
NMax_bahan = 1000 ; kolom_bahan = 3

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [["*" for col in range(kolom_user)] for row in range(NMax_user)] # Matriks data user
candi = [["*" for col in range(kolom_candi)] for row in range(NMax_candi)] # Matriks data candi
bahan_bangunan = [["*" for col in range(kolom_bahan)] for row in range(NMax_bahan)] # Data bahan bangunan

users = dataModule.load("file/user.csv", NMax_user, users, kolom_user)
candi =  dataModule.load("file/candi.csv", NMax_candi, candi, kolom_candi)
bahan_bangunan = dataModule.load("file/bahan_bangunan.csv", NMax_bahan, bahan_bangunan, kolom_bahan)

# Deklarasi Variabel User
username = ""
user_isLogin = False
user_indeks = -999
user_role = "Unknown"

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
      user_isLogin = F01_Login.login(username, users, NMax_user)
      user_indeks = dataModule.cariIndeks(username, users, NMax_user)
      user_role = dataModule.cariRole(username, users, NMax_user)

   elif(masukan == "login" and user_isLogin == True):
      print("Anda sudah login, silahkan logout untuk login kembali.")
   else:
      print("Anda belum login, pastikan anda suah login")
   # --------------------------------------------------------------------------------------------
   
   # Loop ketika terdeteksi sudah login
   while user_isLogin:
      masukan = input(">>> ")

      if (masukan == "summonjin"):
         print("summonjin")


      elif( masukan == "printInfo"):
         search_username = input("Masukkan username yang ingin dicari: ")
         dataModule.printInfo(search_username, users, NMax_user)
      elif( masukan == "Info" ):
         print(username, user_isLogin, user_indeks, user_role)
      elif( masukan == "exit" ):
         user_isLogin = False
         isStart = False
      else:
         print("Perintah tidak ditemukan, ketik 'Help' untuk bantuan")

   
     