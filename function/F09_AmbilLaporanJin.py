# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import dataModule
import commands

# PROSEDUR AMBIL LAPORAN JIN           ambillaporanjin(INPUT data_candi : list[list[str]], INPUT NMax_candi : int, INPUT data_bahan : list[list[str]], INPUT data_username : list[list[str]], INPUT NMax_username : int, OUTPUT str) 
def ambillaporanjin (data_candi, NMax_candi, data_bahan, data_username, NMax_username):
    # { I.S. data_candi terdefinisi, NMax_candi terdefinisi, data_bahan terdefinisi data_username terdefinisi dan NMax_username terdefinisi
    #   F.S. Menampilkan data laporan jin ke terminal }

    # KAMUS LOKAL
    total_jin_pengumpul = int
    total_jin_pembangun = int
    total_jin = int
    jumlah_candi = list[list[str]]
    length = int
    terajin = str
    termalas = str

    # ALGORITMA
    # -------------- Hitung berapa total jin, jin pengumpul dan jin pembangun yang ada ----------------------
    # Hitung yang memiliki role jin_pengumpul di database
    total_jin_pengumpul = hitungJin('jin_pengumpul', data_username, NMax_username)

    # Hitung yang memiliki role jin_pembangun di database
    total_jin_pembangun = hitungJin('jin_pembangun', data_username, NMax_username)

    # Hitung total jin
    total_jin = total_jin_pengumpul + total_jin_pembangun

    print("\n> Total Jin: ", total_jin)
    print("> Total Jin Pengumpul: ", total_jin_pengumpul)
    print("> Total Jin Pembangun: ", total_jin_pembangun)

    # -------------- cari jin terajin dan jin termalas ----------------------

    jumlah_candi = [['' for i in range(2)]for i in range (NMax_candi)]  # matriks indeks kolom 0 data jin, 1 jumlah candi
    
    # update nilai matriks kolom 1
    for i in range(NMax_candi):
        jumlah_candi[i][1] = 0

    # update nama jin pengumpul, cari jin pengumpul
    for i in range(NMax_candi):
        if data_username[i][2] == 'jin_pembangun': 
            jumlah_candi[i][0] = data_username[i][0]

    # update data jumlah candi yang dibangun
    for i in range(NMax_candi):
        for j in range(NMax_candi):
            if jumlah_candi[i][0] == data_candi[j][1]:
                jumlah_candi[i][1] +=1
         
    # update letak baris dalam matriks berdasar jumlah candi yang dibangun
    for i in range(NMax_candi):
        for j in range(NMax_candi-1-i):
            if jumlah_candi[j][1] < jumlah_candi[j+1][1]:
                jumlah_candi[j], jumlah_candi[j+1] = jumlah_candi[j+1], jumlah_candi[j]

    # update letak baris dalam matriks berdasar abjad nama jin pembangun
    length = commands.countMatriks(jumlah_candi, NMax_candi, '')
    for j in range (1, length):  
        if jumlah_candi[j][1] == jumlah_candi[0][1]:
            if jumlah_candi[j][0] < jumlah_candi[0][0]:
                jumlah_candi[0], jumlah_candi[j] = jumlah_candi[j], jumlah_candi[0]
    for j in range (length-2, 0, -1):
        if jumlah_candi[j][1] == jumlah_candi[length-1][1]:
            if jumlah_candi[j][0] < jumlah_candi[length-1][0]:
                jumlah_candi[j], jumlah_candi[length-1] = jumlah_candi[length-1], jumlah_candi[j]
           
    # ambil nilai jin terajin
    terajin = jumlah_candi[0][0]
    if jumlah_candi[0][0] == '':
        terajin = '-'
    print("> Jin Terajin: ", terajin) 

    # ambil nilai jin termalas
    termalas = jumlah_candi[length-1][0]
    if jumlah_candi[0][1] == jumlah_candi[length-1][1]:
        termalas = '-'
    elif jumlah_candi[length-1][0] == '':
        termalas = '-'
    print("> Jin Termalas: ", termalas)

    # -------------- cari jumlah pasir, air, dan batu ----------------------
    print("> Jumlah Pasir: ", data_bahan[1][2])
    print("> Jumlah Air: ", data_bahan[3][2])
    print("> Jumlah Batu: ", data_bahan[2][2])

# FUNGSI HITUNG JIN                 hitungjin(role : str, data_user : list[list[str]], NMax_user : int) -> (total_jin : int)
def hitungJin (role, data_user, NMax_user):
    # { INPUT   : role dari jin yang ingin dihitung dan data username 
    #   OUTPUT  : int jumlah jin yang ingin dihitung }

    # KAMUS LOKAL
    total_jin = int

    # ALGORITMA
    # Hitung yang memiliki role jin yang dicari di database
    total_jin = 0
    for i in range (1, NMax_user) :
        if data_user[i][0] != "*" and data_user[i][1] != "*" and data_user [i][2] == role:
            total_jin += 1
    return total_jin