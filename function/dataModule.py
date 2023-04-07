import sys
sys.path.insert(0, 'function')
import commands

# -------------------------------- MODUL PEMBACAAN DATA ----------------------------------------

# function load(filename : string, NMax : integer, data_matriks : Matriks of integer, kolom : integer) -> (matriks)
# { Menerima input path dari data .csv dan mengeluarkan output matriks data}

# function cariIndeks(username : string, data_username : matriks, NMax : integer) -> (integer)
# { Menerima input username dan akan memberikan output indeks baris bersesuaian dengan data }

# function cariRole( username : string, data_username : matriks, NMax : integer) -> string
# { Menerima input username dan akan mengeluarkan role dari username tersebut}

# procedure printInfo(username : string, data_username : matriks, NMax : integer)
# I.S.  data_username sudah terdefinisi terdiri dari data user
# F.S.  Mengeluarkan output informasi username, password, role berdasar input username

def load(filename, NMax, data_matriks, kolom):
    file = open(filename, 'r')
    lines = file.readlines()
    data = [commands.separate(line, NMax,'\n') for line in lines]
    file.close()

    rows = commands.count(data)
    matrix = [[(cell) for cell in commands.separate(data[i][0], NMax, ';')] for i in range(rows)]

    # Lanjutkan isi Matriks
    for i in range(rows):
        for j in range(kolom):
            data_matriks[i][j] = matrix[i][j]
    return data_matriks

def cariIndeks(username, data_username, NMax):
    for i in range(NMax):
        if(data_username[i][0] == username):
            return i
    return (-999)

def cariRole(username, data_username, NMax):
    for i in range(NMax):
        if(data_username[i][0] == username):
            return (data_username[i][2])
    return ("Unknown")

def printInfo(username, data_username, NMax):
    indeks = cariIndeks(username, data_username, NMax)
    for j in range(3):
        if (j == 0) : print("Username: ", end="")
        elif(j == 1): print("Password: ", end="")
        elif(j==2)  : print("Role: ", end="")
        print(data_username[indeks][j], end="  ||  ")

        if(j==(commands.count(data_username[indeks])-1)): print("")