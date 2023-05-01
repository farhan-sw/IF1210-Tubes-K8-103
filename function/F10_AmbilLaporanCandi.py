# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import dataModule
import commands

# PROSEDUR AMBIL LAPORAN CANDI          ambillaporancanndi(INPUT data_candi : list[list[str]], INPUT NMax : int, OUTPUT str)
def ambillaporancandi (data_candi, NMax):
    # { I.S. data_candi terdefinisi dan NMax terdefinisi
    #   F.S. Menampilkan data laporan candi ke terminal }

    # KAMUS LOKAL
    total_bahan     : int
    idcandi         : list[list[str]]
    length          : int
    harga_termahal  : str
    termahal        : str
    harga_termurah  : str
    termurah        : str

    # ALGORITMA
    # -------------- hitung total candi ----------------------
    print("> Total Candi: ", dataModule.hitungCandi(data_candi, NMax))

    # -------------- hitung total bahan yang digunakan ----------------------
    total_bahan = hitung_bahan(data_candi, NMax)
    print("> Total Pasir yang digunakan: ", total_bahan[0])
    print("> Total Batu yang digunakan: ", total_bahan[1])
    print("> Total Air yang digunakan: ", total_bahan[2])

    # -------------- mencari id candi termahal dan termurah ----------------------
    idcandi = [['' for i in range(2)]for i in range (NMax)]     # matriks indeks kolom 0 data jin, 1 jumlah candi

    # hitung harga tiap candi
    for i in range (1, NMax):
        if data_candi[i][0] != "*" and data_candi[i][1] != "*" and data_candi[i][2] != "*" and data_candi[i][3] != "*" and data_candi[i][4] != "*":
            idcandi[i-1][0] = i
            idcandi[i-1][1] = (int(data_candi[i][2])*10000) + (int(data_candi[i][3])*15000) + (int(data_candi[i][4])*7500)
    
    # update letak baris dalam matriks berdasar harga candi
    length = commands.countMatriks (idcandi, NMax, '')
    for i in range(length):
        for j in range(0, length-1-i):
            if idcandi[j][1] < idcandi[j+1][1]:
                idcandi[j], idcandi[j+1] = idcandi[j+1], idcandi[j]

    # update letak baris dalam matriks berdasar id candi
    for j in range (1, length):  
        if idcandi[j][1] == idcandi[0][1]:
            if idcandi[j][0] < idcandi[0][0]:
                idcandi[0], idcandi[j] = idcandi[j], idcandi[0]
    for j in range (length-2, 0, -1):
        if idcandi[j][1] == idcandi[length-1][1]:
            if idcandi[j][0] < idcandi[length-1][0]:
                idcandi[j], idcandi[length-1] = idcandi[length-1], idcandi[j]
    
    # candi termahal
    harga_termahal = f"(Rp {idcandi[0][1]})"
    termahal = idcandi[0][0]
    if idcandi[0][0] == '':
        termahal = '-'
        harga_termahal = ''
    print(f"> ID Candi Termahal: {termahal} {harga_termahal}" )

    # candi termurah
    harga_termurah = f"(Rp {idcandi[length-1][1]})"
    termurah = idcandi[length-1][0]
    if idcandi[length-1][0] == '':
        termurah = '-'
        harga_termurah = ''
    print(f"> ID Candi Termurah: {termurah} {harga_termurah}")

# FUNGSI HITUNG BAHAN               hitung_bahan(data_candi : list[list[str]], NMax : int) -> (total_pasir : int, total_batu : int, total_air : int)
def hitung_bahan (data_candi, NMax):
    # { INPUT   : array or array str berisikakn data candi
    #   OUTPUT  : int total_pasir, total_batu dan total_air }

    # KAMUS LOKAL
    total_pasir = int
    total_batu = int
    total_air = int

    # ALGORITMA
    # Hitung total pasir, total batu dan total air di database
    total_pasir = 0
    total_batu = 0
    total_air = 0
    length = commands.countMatriks (data_candi, NMax, '*')
    for i in range (1, length):
        total_pasir = total_pasir + int(data_candi[i][2])
        total_batu = total_batu + int(data_candi[i][3])
        total_air = total_air + int(data_candi[i][4])
    return (total_pasir, total_batu, total_air)