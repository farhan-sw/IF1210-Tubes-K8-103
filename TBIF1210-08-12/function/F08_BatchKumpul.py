# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import F07_Pengumpul


# FUNGSI BATCH KUMPUL           batchkumpul(data_user : list[list[str]], NMax_user : int, data_bahan : list[list[str]], NMax_bahan : int) -> data_bahan : list[list[str]]
def batchkumpul(data_user : list[list[str]], NMax_user : int, data_bahan : list[list[str]], NMax_bahan : int):
    # Fungsi mengumpulkan semua jin pengumpul
    # { INPUT : database bahan
    #   OUTPUT : database bahan yang telah ditambahkan }

    # KAMUS LOKAL
    pasir_old       : int
    batu_old        : int
    air_old         : int 
    count           : int 
    pasir_new       : int
    batu_new        : int
    air_new         : int
    
    # ALGORITMA
    # ----------------------- Ambil data bahan awal --------------------------
    # Deklarasi variabel
    pasir_old   = 0
    batu_old    = 0
    air_old     = 0

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
    count       = 0
    # Lakukan proses pencarian role dalam data user
    for i in range(NMax_user):
        if(data_user[i][2] == "jin_pengumpul"):         # Ditemukan jin pengumpul
            data_bahan = F07_Pengumpul.kumpul(data_bahan, NMax_bahan, False)
            count += 1
    # ------------------------------------------------------------------------


    # ----------------------- Ambil data bahan akhir --------------------------
    pasir_new   = 0
    batu_new    = 0
    air_new     = 0

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