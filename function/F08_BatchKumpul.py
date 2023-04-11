# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import F07_Pengumpul


def batchkumpul(data_user, NMax_user : int, data_bahan, NMax_bahan : int):
    # Fungsi mengumpulkan semua jin pengumpul
    # { INPUT : database bahan
    #   OUTPUT : database bahan yang telah ditambahkan }

    # KAMUS LOKAL
    #
    
    # ALGORITMA
    # ----------------------- Ambil data bahan awal --------------------------
    # Deklarasi variabel
    pasir_old       : int   = 0
    batu_old        : int   = 0
    air_old         : int   = 0

    # Update pasir, cari lokasi pasir
    for i in range(NMax_bahan):
        if(data_bahan[i][0] == "pasir"):
            pasir_old      = int(data_bahan[i][2])
    
    # Update batu, cari lokasi batu
    for i in range(NMax_bahan):
        if(data_bahan[i][0] == "batu"):
            batu_old       = int(data_bahan[i][2])

    # Update air, cari lokasi air
    for i in range(NMax_bahan):
        if(data_bahan[i][0] == "air"):
            air_old        = int(data_bahan[i][2])
    # ------------------------------------------------------------------------


    # ----------------------- Proses Kumpul Batch ----------------------------
    # Deklarasi variabel
    count   : int   = 0
    # Lakukan proses pencarian role dalam data user
    for i in range(NMax_user):
        if(data_user[i][2] == "jin_pengumpul"):         # Ditemukan jin pengumpul
            data_bahan = F07_Pengumpul.kumpul(data_bahan, NMax_bahan, False)
            count += 1
    # ------------------------------------------------------------------------


    # ----------------------- Ambil data bahan akhir --------------------------
    pasir_new       : int   = 0
    batu_new        : int   = 0
    air_new         : int   = 0

    # Update pasir, cari lokasi pasir
    for i in range(NMax_bahan):
        if(data_bahan[i][0] == "pasir"):
            pasir_new      = int(data_bahan[i][2])
    
    # Update batu, cari lokasi batu
    for i in range(NMax_bahan):
        if(data_bahan[i][0] == "batu"):
            batu_new       = int(data_bahan[i][2])

    # Update air, cari lokasi air
    for i in range(NMax_bahan):
        if(data_bahan[i][0] == "air"):
            air_new        = int(data_bahan[i][2])
    # ------------------------------------------------------------------------


    # ------- Print Hasil ------------
    print("Mengerahkan", count," jin untuk mengumpulkan bahan.")
    print("Jin menemukan total", pasir_new - pasir_old," pasir,", batu_new - batu_old," batu, dan", air_new - air_old," air.")


    return data_bahan