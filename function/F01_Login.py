# Import Modul bentukan 
try:
    import dataModule
except ImportError:
    from function import dataModule

    # Fungsi Login          login(username, data_username)
def login(username, data_username):

    # KAMUS LOKAL
    # password : string
    # isUsername, isPassword : Boolean

    # ALGORITMA
    password = input("Password: ")              # Meminta masukkan user
    isUsername = False                          # Deklarasi nilai awal, username tidak ditemukan
    isPassword = False                          # Deklarasi nilai awal, password salah

    # Looping pencarian username di database
    for i in range((dataModule.count(data_username))):
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

    # prosedur Testing untuk memastikan program sudah berjalan dengan benar
def Test():
    # KAMUS LOKAL
    # user      : array of string
    # username  : string
    # isLogin   : Boolean

    # ALGORITMA
    users = [['Bondowoso', 'cintaroro', 'bandung_bondowoso'],['Roro', 'gasukabondo', 'roro_jonggrang']] # Matriks data user
    username = input("Username: ")
    isLogin = login("Bondowoso", users)
    print(isLogin)
    indeks = dataModule.cariIndeks(username, users)
    print(indeks)

