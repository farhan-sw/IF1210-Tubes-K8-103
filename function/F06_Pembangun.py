# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import commands
import B01_RNG


# FUNGSI BANGUN           bangun(pembuat : str, data_candi : list[list[str]], NMax_candi : int, data_bahan : list[list[str]], NMax_bahan : int) -> (data_candi : list[list[str]], data_bahan : list[list[str]])
def bangun(pembuat : str, data_candi : list[list[str]], NMax_candi : int, data_bahan : list[list[str]], NMax_bahan : int):
    # Fnction Membangun Candi
    # { INPUT : pembuat : str, data_candi : list[list[str]], NMax_candi : int, data_bahan, NMax_bahan : int}
    # { OUTPUT : data_candi : list[list[str]], data_bahan : list[list[str]]}

    # KAMUS LOKAL
    needsCandi      : list[list[int]]
    needCandiTotal  : list[list[int]]
    stok_pasir      : int
    stok_batu       : int
    stok_air        : int
    isBelowTarget   : bool
    candi_target    : int
    candi_sekarang  : int
    candi_selisih   : int
    i               : int
    isDone          : bool

    # ALGORITMA
    # --------------- Hitung kebutuhan candi sebanyak total_candi -----------------
    # Deklarasi variabel
    needsCandi          = [[0 for j in range(3)] for i in range(1)]     # matriks indeks kolom 0 pasir, 1 batu, 2 air
    needCandiTotal      = [0 for i in range(3)]                         # array indeks kolom 0 pasir, 1 batu, 2 air
    needsCandi, needCandiTotal = countNeeds(1)                          # Fungsi F06 hanya membangun tepat 1 candi
    #-----------------------------------------------------------------------------


    # ----------------------- Ambil data bahan tersedia --------------------------
    # Deklarasi variabel
    stok_pasir  = 0
    stok_batu   = 0
    stok_air    = 0

    # Update pasir, cari lokasi pasir
    for i in range(NMax_bahan):
        if(data_bahan[i][0] == "pasir"):
            stok_pasir      = int(data_bahan[i][2])
    
    # Update batu, cari lokasi batu
    for i in range(NMax_bahan):
        if(data_bahan[i][0] == "batu"):
            stok_batu       = int(data_bahan[i][2])

    # Update air, cari lokasi air
    for i in range(NMax_bahan):
        if(data_bahan[i][0] == "air"):
            stok_air        = int(data_bahan[i][2])
    # ----------------------------------------------------------------------------


    # ----------------------------- Cek apakah bahan cukup -----------------------
    if ((stok_pasir - needCandiTotal[0] < 0) or (stok_batu - needCandiTotal[1] < 0) or (stok_air - needCandiTotal[2] < 0)):
        print ("Bahan bangunan tidak mencukupi.")
        print ("Candi tidak bisa dibangun!")
        return (data_candi, data_bahan)             # Mengembalikan nilai tanpa perubahan (keluar dari fungsi)
    #-----------------------------------------------------------------------------


    # ------------------------- Hitung Sisa Candi ---------------------------------
    isBelowTarget   = False
    candi_target    = 100
    candi_sekarang  = commands.countMatriks(data_candi, NMax_candi)
    candi_selisih   = candi_target - candi_sekarang

    if(candi_selisih > 0):
        isBelowTarget     = True  # Jika belum 100, maka candi dibangun dan disimpan
    # -----------------------------------------------------------------------------


    # ----------------------- Lakukan Perubahan Data Bahan ------------------------
    # Bahan sudah cukup, lakukan pengurangan bahan di database
    # Update pasir, cari lokasi pasir
    if isBelowTarget:                                             # Hanya jika kurang taget yang di save
        for i in range(NMax_bahan):
            if(data_bahan[i][0] == "pasir"):
                data_bahan[i][2]    = str(stok_pasir - needsCandi[0][0])
        
        # Update batu, cari lokasi batu
        for i in range(NMax_bahan):
            if(data_bahan[i][0] == "batu"):
                data_bahan[i][2]    = str(stok_batu - needsCandi[0][1])

        # Update air, cari lokasi air
        for i in range(NMax_bahan):
            if(data_bahan[i][0] == "air"):
                data_bahan[i][2]    = str(stok_air - needsCandi[0][2])
    
    #--------------------- Lakukan Perubahan Data Candi --------------------------
    i           = 1
    isDone      = False
    while (isBelowTarget == True and isDone == False and i < NMax_candi): # Hanya jika kurang taget yang di save
        if (data_candi[i][0] == "*"):                   # Cari ID Kosong terdekat dari 1
            data_candi[i][0] = str(i )                  # Update ID dengan indeks pengisian indeks sekarang
            data_candi[i][1] = pembuat                  # Update Pembuat candi dengan nama jin sekarang
            data_candi[i][2] = str(needsCandi[0][0])    # Update bahan pasir candi
            data_candi[i][3] = str(needsCandi[0][1])    # Update bahan batu candi
            data_candi[i][4] = str(needsCandi[0][2])    # Update bahan air candi
            isDone = True
        i += 1
    
    # -------- Print Status Pembangunan ------------------
    if isDone or isBelowTarget == False: print("Candi berhasil dibangun.")
    else: print("Terjadi kesalahan dalam pemasukkan candi")

    # -------- Print Sisa Candi yang perlu dibangun ------
    if(candi_selisih > 0):
        print("Sisa candi yang perlu dibangun:", candi_selisih, end=". \n")
    else: # Candi sudah meleihi target
        print("Sisa candi yang perlu dibangun: 0.")

    return (data_candi, data_bahan)

# Fungsi countNeeds                 countNeeds(total_candi : int) -> (bahan_random : list[list[int]], bahan_random_total : list[list[int]])
def countNeeds(total_candi : int):
    # { INPUT   : Total candi yang ingin dibangun
    #   OUTPUT  : array of array int berisikan bahan tiap candi dan total bahan }

    # KAMUS LOKAL
    bahan_random        : list[list[int]]
    bahan_random_total  : list[list[int]]

    # ALGORITMA
    # Deklarasi Variabel
    bahan_random        = [[0 for j in range(3)] for i in range(total_candi)]   # matriks indeks kolom 0 pasir, 1 batu, 2 air
    bahan_random_total  = [0 for i in range(3)]                                 # array indeks kolom 0 pasir, 1 batu, 2 air

    # ----------------------------------------------------------------------------
    # Random bahan pembuatan candi, simpan ke matriks
    for i in range(total_candi):
        bahan_random[i][0]      = B01_RNG.randomNumber(1, 5)       # Pasir
        bahan_random_total[0]   += bahan_random[i][0]

        bahan_random[i][1]     = B01_RNG.randomNumber(1, 5)       # Batu
        bahan_random_total[1]   += bahan_random[i][1]

        bahan_random[i][2]     = B01_RNG.randomNumber(1, 5)       # Air
        bahan_random_total[2]   += bahan_random[i][2]
    # ----------------------------------------------------------------------------

    return (bahan_random, bahan_random_total)