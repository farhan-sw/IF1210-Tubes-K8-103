# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import B01_RNG

def kumpul(data_bahan, NMax : int):
    # function kumpul(data_bahan : array of array string, NMax : integer) -> array of array string
    # { Mengenerate pencarian bahan bangunan dari 0-5 dan akan  mereturn update data bahan bangunan }

    # KAMUS LOKAL
    # rand_pasir, rand_batu, rand_air : integer

    # ALGORITMA

    # Ambil data random untuk pasir, batu, air dari 0-5
    rand_pasir  : int   = B01_RNG.randomNumber(0, 5)
    rand_batu   : int   = B01_RNG.randomNumber(0, 5)
    rand_air    : int   = B01_RNG.randomNumber(0, 5)
    tmp         : int   = 0     # Variabel penampung sementara str-int

    # Update Data Bahan untuk pasir, batu, air
    # Update pasir, cari lokasi pasir
    tmp = 0 # reset variabel
    for i in range(NMax):
        if(data_bahan[i][0] == "pasir"):
            tmp = int(data_bahan[i][2])         # Konversi string ke integer
            tmp += rand_pasir
            data_bahan[i][2] = str(tmp)      # update nilai
    
    # Update batu, cari lokasi batu
    tmp = 0 # reset variabel
    for i in range(NMax):
        if(data_bahan[i][0] == "batu"):
            tmp = int(data_bahan[i][2])         # Konversi string ke integer
            tmp += rand_batu
            data_bahan[i][2] = str(tmp)       # Jumlah Batu berada di kolom indeks 2

    # Update air, cari lokasi air
    tmp = 0 # reset variabel
    for i in range(NMax):
        if(data_bahan[i][0] == "air"):
            tmp = int(data_bahan[i][2])         # Konversi string ke integer
            tmp += rand_air
            data_bahan[i][2] = str(tmp)        # Jumlah air berada di kolom indeks 2
    
    # Print hasil temuan
    print("Jin menemukan", rand_pasir, " pasir,", rand_batu ," batu, dan", rand_air ," air.")
    
    return data_bahan