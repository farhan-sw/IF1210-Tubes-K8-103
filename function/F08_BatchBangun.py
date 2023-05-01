# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import commands
import dataModule
import F06_Pembangun

# FUNGSI MEMBANGUN CANDI SEKALIGUS UNTUK SEMUA JIN PERJENIS PEMBANGUN     (data_user : list[list[str]], NMax_user : int, data_candi : list[list[str]], NMax_candi : int, data_bahan : list[list[str]], NMax_bahan : int) -> (data_candi : list[list[str]], data_bahan : list[list[str]])
def batchbangun(data_user : list[list[str]], NMax_user : int, data_candi : list[list[str]], NMax_candi : int, data_bahan : list[list[str]], NMax_bahan : int):
    # { INPUT   : data user, data candi, dan data bahan awal
    #   OUTPUT  : data candi dan data bahan yang telah dimodifikasi }

    # KAMUS LOKAL
    total_candi     : int 
    needsCandi      : list[list[int]]
    needCandiTotal  : list[list[int]]    
    bahan_stok      : list[int]
    kurang_pasir    : int
    kurang_batu     : int
    kurang_air      : int
    isBelowTarget   : bool
    candi_target    : int
    candi_sekarang  : int
    candi_selisih   : int
    i               : int
    j               : int
    k               : int
    isDone          : bool
    next            : bool

    # ALGORITMA
    # -------------- Hitung Ada Berapa Candi yang akan dibangun ----------------------
    # Hitung yang memiliki role jin_pembangun di database
    total_candi     = 0
    needsCandi      = [[0 for j in range(3)] for i in range(1)]     # matriks indeks kolom 0 pasir, 1 batu, 2 air
    needCandiTotal  = [0 for i in range(3)]                         # array indeks kolom 0 pasir, 1 batu, 2 air

    for i in range (NMax_user):
        if (data_user[i][2] == "jin_pembangun"):
            total_candi += 1
    if (total_candi == 0):
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else: #total_candi != 0
        needsCandi, needCandiTotal = F06_Pembangun.countNeeds(total_candi)
    
    print("Mengerahkan", total_candi, " jin untuk membangun candi dengan total bahan", needCandiTotal[0], " pasir,", needCandiTotal[1], " batu, dan", needCandiTotal[2], " air.")
    # ---------------------------------------------------------------------------------


    # ------------------------ Kalkulasi Apakah Bahan Cukup ---------------------------
    # Deklarasi Variabel
    bahan_stok      = [0 for i in range(3)]                         # array indeks kolom 0 pasir, 1 batu, 2 air
    kurang_pasir    = 0
    kurang_batu     = 0
    kurang_air      = 0

    # Update pasir, cari lokasi pasir
    for i in range(NMax_bahan):
        if(data_bahan[i][0] == "pasir"):
            bahan_stok[0]       = int(data_bahan[i][2])
    
    # Update batu, cari lokasi batu
    for i in range(NMax_bahan):
        if(data_bahan[i][0] == "batu"):
            bahan_stok[1]        = int(data_bahan[i][2])

    # Update air, cari lokasi air
    for i in range(NMax_bahan):
        if(data_bahan[i][0] == "air"):
            bahan_stok[2]       = int(data_bahan[i][2])

    if ((bahan_stok[0] - needCandiTotal[0] < 0) or (bahan_stok[1] - needCandiTotal[1] < 0) or (bahan_stok[2] - needCandiTotal[2] < 0)):
        if ((bahan_stok[0] - needCandiTotal[0] < 0)): kurang_pasir = needCandiTotal[0] - bahan_stok[0]
        if ((bahan_stok[1] - needCandiTotal[1] < 0)): kurang_batu = needCandiTotal[1] - bahan_stok[1]
        if ((bahan_stok[2] - needCandiTotal[2] < 0)): kurang_air = needCandiTotal[2] - bahan_stok[2]

        print ("Bangun gagal. Kurang", kurang_pasir, " pasir,", kurang_batu, " batu, dan", kurang_air, " air.")
        return (data_candi, data_bahan)             # Mengembalikan nilai tanpa perubahan (keluar dari fungsi)

    # ---------------------------------------------------------------------------------


    # ------------------------- Hitung Sisa Candi ---------------------------------
    isBelowTarget   = False
    candi_target    = 101
    candi_sekarang  = dataModule.hitungCandi(data_candi, NMax_candi)
    candi_selisih   = candi_target - candi_sekarang - total_candi
    
    if(candi_selisih > 0):
        isBelowTarget     = True  # Jika belum 100, maka candi dibangun dan disimpan
    else:
        print("Candi akan melebihi target, tidak ada candi yang dibangun")
        return (data_candi, data_bahan)             # Mengembalikan nilai tanpa perubahan (keluar dari fungsi)
    # ---------------------------------------------------------------------------------
    

    # ----------------------- Lakukan Perubahan Data Bahan ------------------------
    # Bahan sudah cukup, lakukan pengurangan bahan di database
    # Update pasir, cari lokasi pasir
    if isBelowTarget:                                             # Hanya jika kurang taget yang di save
        for i in range(NMax_bahan):
            if(data_bahan[i][0] == "pasir"):
                data_bahan[i][2]    = str(bahan_stok[0] - needCandiTotal[0])
        
        # Update batu, cari lokasi batu
        for i in range(NMax_bahan):
            if(data_bahan[i][0] == "batu"):
                data_bahan[i][2]    = str(bahan_stok[1] - needCandiTotal[1])

        # Update air, cari lokasi air
        for i in range(NMax_bahan):
            if(data_bahan[i][0] == "air"):
                data_bahan[i][2]    = str(bahan_stok[2] - needCandiTotal[2])

    # ---------------------------------------------------------------------------------


    # ---------------------- Lakukan Perubahan Data Candi -----------------------------
    i       = 0     # Untuk menandakan candi keberapa (maks total_candi)
    j       = 0     # Untuk menandakan sedang jalan di baris berapa ( username ) sampai ketemu pembanun
    k       = 0     # Untuk menandakan berjalan di indeks berapa (data candi)
    isDone  = True      # Nandain candi udah diubah
    next    = False     # Nandain next candi

    while (i < total_candi):
        next    = False

        while (next == False and j <= NMax_user):
            if (data_user[j][2] == "jin_pembangun"):

                isDone = False
                while(isDone == False and k < NMax_candi):
                    if (data_candi[k][0] == "*"):                   # Cari ID Kosong terdekat dari 1
                        data_candi[k][0] = str(k)                   # Update ID dengan indeks pengisian indeks sekarang
                        data_candi[k][1] = data_user[j][0]          # Update Pembuat candi dengan nama jin sekarang
                        data_candi[k][2] = str(needsCandi[i][0])    # Update bahan pasir candi
                        data_candi[k][3] = str(needsCandi[i][1])    # Update bahan batu candi
                        data_candi[k][4] = str(needsCandi[i][2])    # Update bahan air candi
                        isDone  = True
                        next    = True
                    k += 1
            j += 1
        i += 1
    
    return (data_candi, data_bahan)
