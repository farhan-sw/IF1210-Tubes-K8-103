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
isLogin = False
username = ""
indeks = -999

isStart = True
while isStart:
  masukan = input(">>> ")
  #commands.run(masukan)

    # FUNGSI LOGIN F01
  if(masukan == "login" and isLogin == False):
    username = input("Username: ")
    isLogin = F01_Login.login(username, users)
    indeks = dataModule.cariIndeks(username, users)
  elif(masukan == "login" and isLogin == True):
     print("Anda sudah login, silahkan logout untuk login kembali.")

    # FUNGSI LOGOUT F02
  elif(masukan == "logout" and isLogin == True):
     print("Keluar dari semua akun.")
     isLogin = False
  elif(masukan == "logout" and isLogin == False):
     print("Anda tidak sedang login.")

     #
  elif(masukan == "exit"):
     isStart = False
     
  else :
     print("ulangi")
     