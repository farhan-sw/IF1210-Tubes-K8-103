
# Fungsi Login          login(username : str, data_username : list[list[str]]) -> bool
def login(username : str, data_username : list[list[str]], NMax : int):

    # KAMUS LOKAL
    password        : str
    isUsername      : bool 
    isPassword      : bool

    # ALGORITMA
    password    = input("Password: ")            # Meminta masukkan user
    isUsername  = False                          # Deklarasi nilai awal, username tidak ditemukan
    isPassword  = False                          # Deklarasi nilai awal, password salah

    # Looping pencarian username di database
    for i in range(NMax):
        if(data_username[i][0] == username):
            isUsername = True                   # Jika username ditemukan, update kondisi
        if(data_username[i][1] == password):
            isPassword = True                   # Jika password benar, update kondisi
    
    # Identifikasi kemungkinan
    if (isUsername and isPassword):                     # Username ditemukan dan password benar
        print(f'Selamat datang, {username}!')
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        return True
    elif (isUsername == True and isPassword == False):  # Username ditemukan tetapi password salah
        print("Password salah!")
        return False
    else: #(isUsername == False and isPassword == False) # Username tidak ditemukan dan password salah
        print("Username tidak terdaftar!")
        return False
