# File: main.py
from function import dataModule
#import commands

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [['Bondowoso', 'cintaroro', 'bandung_bondowoso'],['Roro', 'gasukabondo', 'roro_jonggrang']] # Matriks data user
candi = [['165513215', 'in pembuat 1', 'pasir 1', 'Batu 1', 'air 1'],['165513215', 'in pembuat 2', 'pasir 1', 'Batu 1', 'air 1']] # Matriks data candi
bahan_bangunan = [['Nama 1', 'Des 1', 'Jum 1'], ['Nam 2', 'des 2', 'Jum 2']] # Data bahan bangunan

# users = dataModule.load("file/user.csv", users)
# dataModule.load("file/candi.csv", candi)
# dataModule.load("file/bahan_bangunan.csv", bahan_bangunan)
#print(users)

for i in range(2):
    for j in range(3):
        print(users[i][j], end=" ")
    print("")

# while True:
#   masukan = input(">>> ")
#   commands.run(masukan)