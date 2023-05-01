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

# def cariIndeks(nilai, data_nilai, kolom, NMax):
#     for i in range(NMax):
#         if(data_nilai[i][kolom] == nilai):
#             return i
#     return (-999)

def cariIndeks(nilai : str, data_nilai : list[list[str]], kolom : int, start : int, NMax :int):
    if start == NMax:
        return -999                         # Basis
    elif data_nilai[start][kolom] == nilai:
        return start                        # Basis
    
    else:                                   # Rekurens
        return cariIndeks(nilai, data_nilai, kolom,start+1, NMax)

def cariRole(username : str, data_username : list[list[str]], NMax : int):
    for i in range(NMax):
        if(data_username[i][0] == username):
            return (data_username[i][2])
    return ("Unknown")

def cariBahan(nama_bahan : str, data_bahan, NMax : int = 3):
    for i in range(NMax):
        if(data_bahan[i][0] == nama_bahan):
                return data_bahan[i][2]

def printUsername(data_username, NMax):
    for i in range(NMax):
        if (data_username[i][0] != "*"):
            print(f' Nama : {data_username[i][0]},   Pass : {data_username[i][1]},   Role : {data_username[i][2]}')
    print("\n")

def printCandi(data_candi, NMax):
    for i in range(NMax):
        if (data_candi[i][0] != "*" and data_candi[i][0] != "id"):
            print(f' ID : {data_candi[i][0]},   Pembuat : {data_candi[i][1]},   Pasir : {data_candi[i][2]},     Batu : {data_candi[i][3]},  Air : {data_candi[i][4]}')
    print("\n")

def printBahan(data_bahan, NMax):
    for i in range(NMax):
        if(data_bahan[i][0] == "pasir"):
            print("Pasir:", data_bahan[i][2], end=", ")      # Jumlah Pasir berada di kolom indeks 2
    
    # Update batu, cari lokasi batu
    for i in range(NMax):
        if(data_bahan[i][0] == "batu"):
            print("Batu:", data_bahan[i][2], end=", ")       # Jumlah Batu berada di kolom indeks 2

    # Update air, cari lokasi air
    for i in range(NMax):
        if(data_bahan[i][0] == "air"):
            print("Air:", data_bahan[i][2])        # Jumlah air berada di kolom indeks 2
    print("\n")

def hitungCandi (data_candi, NMax_candi):
    total_candi = 0
    for i in range (1, NMax_candi) :
        if data_candi[i][0] != "*" and data_candi[i][1] != "*" and data_candi [i][2] != "*" :
            total_candi += 1
    return total_candi