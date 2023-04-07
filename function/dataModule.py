try:
    import commands
except:
    from function import commands

# -------------------------------- MODUL PEMBACAAN DATA ----------------------------------------

# function load(filename : string) -> (matriks)
# { Menerima input path dari data .csv dan mengeluarkan output matriks data}

# function cariIndeks(username : string, data_username : matriks) -> (integer)
# { Menerima input username dan akan memberikan output indeks baris bersesuaian dengan data }

# function cariRole( username : string, data_username : matriks ) -> string
# { Menerima input username dan akan mengeluarkan role dari username tersebut}

# procedure printInfo(username : string, data_username : matriks)
# I.S.  data_username sudah terdefinisi terdiri dari data user
# F.S.  Mengeluarkan output informasi username, password, role berdasar input username

def load(filename, data):

    print(filename)
    file=open(filename, "r")

    return data

def cariIndeks(username, data_username):
    for i in range(commands.count(data_username)):
        if(data_username[i][0] == username):
            return i
    return (-999)

def cariRole(username, data_username):
    for i in range(commands.count(data_username)):
        if(data_username[i][0] == username):
            return (data_username[i][2])
    return ("Unknown")

def printInfo(username, data_username):
    indeks = cariIndeks(username, data_username)
    for j in range(commands.count(data_username[indeks])):
        if (j == 0) : print("Username: ", end="")
        elif(j == 1): print("Password: ", end="")
        elif(j==2)  : print("Role: ", end="")
        print(data_username[indeks][j], end="  ||  ")

        if(j==(commands.count(data_username[indeks])-1)): print("")