import sys
sys.path.insert(0, 'function')
import commands

# -------------------------------- MODUL PEMBACAAN DATA ----------------------------------------

# function cariIndeks(username : string, data_username : matriks, NMax : integer) -> (integer)
# { Menerima input username dan akan memberikan output indeks baris bersesuaian dengan data }

# function cariRole( username : string, data_username : matriks, NMax : integer) -> string
# { Menerima input username dan akan mengeluarkan role dari username tersebut}

# procedure printInfo(username : string, data_username : matriks, NMax : integer)
# I.S.  data_username sudah terdefinisi terdiri dari data user
# F.S.  Mengeluarkan output informasi username, password, role berdasar input username

def cariIndeks(nilai, data_nilai, kolom, NMax):
    for i in range(NMax):
        if(data_nilai[i][kolom] == nilai):
            return i
    return (-999)

def cariRole(username : str, data_username, NMax : int):
    for i in range(NMax):
        if(data_username[i][0] == username):
            return (data_username[i][2])
    return ("Unknown")

def printUsername(data_username, NMax):
    for i in range(NMax):
        if (data_username[i][0] != "*"):
            print(f' Nama : {data_username[i][0]},   Pass : {data_username[i][1]},   Role : {data_username[i][2]}')
    print("\n")