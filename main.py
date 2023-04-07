# File: main.py
from function import dataModule
from function import F01_Login
from function import commands
#import commands

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [['Bondowoso', 'cintaroro', 'bandung_bondowoso'],['Roro', 'gasukabondo', 'roro_jonggrang']] # Matriks data user
candi = [['165513215', 'in pembuat 1', 'pasir 1', 'Batu 1', 'air 1'],['165513215', 'in pembuat 2', 'pasir 1', 'Batu 1', 'air 1']] # Matriks data candi
bahan_bangunan = [['Nama 1', 'Des 1', 'Jum 1'], ['Nam 2', 'des 2', 'Jum 2']] # Data bahan bangunan

# users = dataModule.load("file/user.csv", users)
# dataModule.load("file/candi.csv", candi)
# dataModule.load("file/bahan_bangunan.csv", bahan_bangunan)
#print(users)

# Deklarasi Variabel Global
username = ""
user_isLogin = False
user_indeks = -999
user_role = "Unknown"

isStart = True
while isStart:
   masukan = input(">>> ")
   #commands.run(masukan)

   # --------------------------------------------------------------------------------------------
   # IMPLEMENTASI FUNGSI LOGIN F01
   if(masukan == "login" and user_isLogin == False):
      username = input("Username: ")
      user_isLogin = F01_Login.login(username, users)
      user_indeks = dataModule.cariIndeks(username, users)
      user_role = dataModule.cariRole(username, users)

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
         dataModule.printInfo(search_username, users)
      else:
         print("Perintah tidak ditemukan, ketik 'Help' untuk bantuan")

   
     