try:
    import dataModule
except ImportError:
    from function import dataModule

def login(username, data_username):
    password = input("Password: ")

    # Cek apakah user terdaftar
    isUsername = False
    isPassword = False
    for i in range((dataModule.count(data_username))):
        if(data_username[i][0] == username):
            isUsername = True
        if(data_username[i][1] == password):
            isPassword = True
    
    # Pecah beberapa kondisi
    if (isUsername and isPassword):
        print(f'Selamat datang, {username}!')
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        return True
    elif (isUsername == True and isPassword == False):
        print("Password salah!")
        return False
    else:
        print("Username tidak terdaftar!")
        return False


def Test():
    users = [['Bondowoso', 'cintaroro', 'bandung_bondowoso'],['Roro', 'gasukabondo', 'roro_jonggrang']] # Matriks data user
    username = input("Username: ")
    isLogin = login("Bondowoso", users)
    print(isLogin)
    indeks = dataModule.cariIndeks(username, users)
    print(indeks)

