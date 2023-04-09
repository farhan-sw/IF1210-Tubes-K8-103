# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import dataModule
import commands

    # Fungsi SummonJin        login(jenis_jin, data_username)
def summonjin(jenis_jin, data_username, NMax):

    # KAMUS LOKAL
    # username : string
    # password : string
    # isUsername, isPassword : Boolean
    # data : array of string

    #ALGORITMA
    if jenis_jin == '1' or jenis_jin == '2':            # jenis_jin benar
        if jenis_jin == '1' :
            print("\nMemilih jin “Pengumpul”.")
        else :
            print("\nMemilih jin “Pembangun”.")

        username = input("\nMasukkan username jin: ") # meminta masukan user
        password = ""                               # deklarasi variabel
        isUsername = False                          # Deklarasi nilai awal, username tidak ditemukan
        isPassword = False                          # Deklarasi nilai awal, password salah

        # Looping pencarian username di database
        for i in range(NMax):
            if(data_username[i][0] == username):
                isUsername = True                   # Jika username ditemukan, update kondisi
            if(data_username[i][1] == password):
                isPassword = True                   # Jika password benar, update kondisi
    
        if isUsername == False :                    # username tidak ditemukan
            password = input("Masukkan password jin: ")
            if len(password) < 5 or len(password) > 25:
                print("\nPassword panjangnya harus 5-25 karakter!")
                password = input("Masukkan password jin: ")
                import csv
                if jenis_jin == '1' :
                    data = [username, password, 'jin_pengumpul']    # data yang ditambahkan ke csv
                else:   #(jenis_jin == 2)
                    data = [username, password, 'jin_pembangun']    # data yang ditambahkan ke csv

                # membuka file CSV dengan mode append (menambahkan)
                with open('file/user.csv', mode='a', newline='') as f:
                    # membuat objek writer
                    writer = csv.writer(f)

                    # menulis data ke dalam file csv
                    writer.writerow(data)
                print(f"\nMengumpulkan sesajen... \nMenyerahkan sesajen... \nMembacakan mantra... \n \nJin {username} berhasil dipanggil!")
            else: #(len(password) >=5 and len(password) <=25)
                import csv
                if jenis_jin == '1' :
                    data = [username, password, 'jin_pengumpul']    # data yang ditambahkan ke csv
                else:   #(jenis_jin == 2)
                    data = [username, password, 'jin_pembangun']    # data yang ditambahkan ke csv

                # membuka file CSV dengan mode append (menambahkan)
                with open('file/user.csv', mode='a', newline='') as f:
                    # membuat objek writer
                    writer = csv.writer(f)

                    # menulis data ke dalam file csv
                    writer.writerow(data)
                print(f"\nMengumpulkan sesajen... \nMenyerahkan sesajen... \nMembacakan mantra... \n \nJin {username} berhasil dipanggil!")

        else : #(isUsername == True)                # username ditemukan
            print("\nUsername “", username, "” sudah diambil!") 
    else:   # (jenis_jin != 1 and jenis_jin != 2)       # jenis_jin benar
        print("\nTidak ada jenis jin bernomor “",jenis_jin,"”!")



