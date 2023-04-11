# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import commands
import B01_RNG

def bangun(pembuat : str, data_candi, NMax_candi : int, data_bahan, NMax_bahan : int):
    # Fnction Membangun Candi
    # { INPUT : }

    # KAMUS LOKAL

    # ALGORITMA

    # ----------------------------------------------------------------------------
    # BUat req. untuk bahan candi
    rand_pasir_candi    : int   = B01_RNG.randomNumber(1, 5)
    rand_batu_candi     : int   = B01_RNG.randomNumber(1, 5)
    rand_air_candi      : int   = B01_RNG.randomNumber(1, 5)
    # ----------------------------------------------------------------------------


    # ----------------------- Ambil data bahan tersedia --------------------------
    # Deklarasi variabel
    stok_pasir          : int   = 0
    stok_batu           : int   = 0
    stok_air            : int   = 0

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
    # Deklarasi Variabel
    isEnough        : bool  = True

    print(f'Batu: Stok: {stok_batu} Rnd {rand_batu_candi} \n Pasir: Stok: {stok_pasir} Rnd {rand_pasir_candi} \n Air: Stok {stok_air} Rnd {rand_air_candi}')

    if ((stok_batu - rand_batu_candi < 0) or (stok_pasir - rand_pasir_candi < 0) or (stok_air - rand_air_candi < 0)):
        isEnough    = False
        print ("Bahan bangunan tidak mencukupi.")
        print ("Candi tidak bisa dibangun!")
        return (data_candi, data_bahan)             # Mengembalikan nilai tanpa perubahan (keluar dari fungsi)
    #-----------------------------------------------------------------------------


    # ------------------------- Hitung Sisa Candi ---------------------------------
    isBuild         : bool  = False
    candi_target    : int   = 100
    candi_sekarang  : int   = commands.countMatriks(data_candi, NMax_candi)
    candi_selisih   : int   = candi_target - candi_sekarang

    if(candi_selisih > 0):
        isBuild     = True  # Jika belum 100, maka candi dibangun dan disimpan
    # -----------------------------------------------------------------------------


    # ----------------------- Lakukan Perubahan Data Bahan ------------------------
    # Bahan sudah cukup, lakukan pengurangan bahan di database
    # Update pasir, cari lokasi pasir
    if isBuild:                                             # Hanya jika kurang taget yang di save
        for i in range(NMax_bahan):
            if(data_bahan[i][0] == "pasir"):
                data_bahan[i][2]    = str(stok_pasir - rand_pasir_candi)
        
        # Update batu, cari lokasi batu
        for i in range(NMax_bahan):
            if(data_bahan[i][0] == "batu"):
                data_bahan[i][2]    = str(stok_batu - rand_batu_candi)

        # Update air, cari lokasi air
        for i in range(NMax_bahan):
            if(data_bahan[i][0] == "air"):
                data_bahan[i][2]    = str(stok_air - rand_air_candi)

    
    #--------------------- Lakukan Perubahan Data Candi --------------------------
    i       : int   = 1
    isDone  : bool  = False
    while (isBuild == True and isDone == False and i < NMax_candi): # Hanya jika kurang taget yang di save
        if (data_candi[i][0] == "*"):                   # Cari ID Kosong terdekat dari 1
            data_candi[i][0] = str(i )               # Update ID dengan indeks pengisian indeks sekarang
            data_candi[i][1] = pembuat                  # Update Pembuat candi dengan nama jin sekarang
            data_candi[i][2] = str(rand_pasir_candi)    # Update bahan pasir candi
            data_candi[i][3] = str(rand_batu_candi)     # Update bahan batu candi
            data_candi[i][4] = str(rand_air_candi)      # Update bahan air candi
            isDone = True
        i += 1
    
    # -------- Print Status Pembangunan ------------------
    if isDone or isBuild == False: print("Candi berhasil dibangun.")
    else: print("Terjadi kesalahan dalam pemasukkan candi")

    # -------- Print Sisa Candi yang perlu dibangun ------
    if(candi_selisih > 0):
        print("Sisa candi yang perlu dibangun:", candi_selisih, end=". \n")
    else: # Candi sudah meleihi target
        print("Sisa candi yang perlu dibangun: 0.")

    return (data_candi, data_bahan)