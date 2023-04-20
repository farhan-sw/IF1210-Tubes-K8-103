# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import dataModule
import commands

def ambillaporancandi (data_candi, NMax):

    total_bahan = hitung_bahan(data_candi, NMax)
    pasir = total_bahan[0]
    batu = total_bahan[1]
    air = total_bahan[2]
    idcandi = id_candi(data_candi, NMax)
    harga_termahal = f"(Rp {idcandi[0][1]})"
    harga_termurah = f"(Rp {idcandi[1][1]})"
    termahal = idcandi[0][0]
    termurah = idcandi[1][0]
    if idcandi[0][0] == '':
        termahal = '-'
        harga_termahal = ''
    if idcandi[1][0] == '':
        termurah = '-'
        harga_termurah = ''


    print("> Total Candi: ", dataModule.hitungCandi(data_candi, NMax))
    print("> Total Pasir yang digunakan: ", pasir)
    print("> Total Batu yang digunakan: ", batu)
    print("> Total Air yang digunakan: ", air)
    print(f"> ID Candi Termahal: {termahal} {harga_termahal}" )
    print(f"> ID Candi Termurah: {termurah} {harga_termurah}")

def hitung_bahan (data_candi, NMax):
    total_pasir = 0
    total_batu = 0
    total_air = 0
    length = commands.countMatriks (data_candi, NMax, '*')
    for i in range (1, length):
        total_pasir = total_pasir + int(data_candi[i][2])
        total_batu = total_batu + int(data_candi[i][3])
        total_air = total_air + int(data_candi[i][4])
    return (total_pasir, total_batu, total_air)

def id_candi (data_candi, NMax):
    idCandi = [['' for i in range(2)]for i in range (NMax)]
    for i in range (1, NMax):
        if data_candi[i][0] != "*" and data_candi[i][1] != "*" and data_candi[i][2] != "*" and data_candi[i][3] != "*" and data_candi[i][4] != "*":
            idCandi[i-1][0] = i
            idCandi[i-1][1] = (int(data_candi[i][2])*10000) + (int(data_candi[i][3])*15000) + (int(data_candi[i][4])*7500)
    
    length = commands.countMatriks (idCandi, NMax, '')
    for i in range(length):
        for j in range(0, length-1-i):
            if idCandi[j][1] < idCandi[j+1][1]:
                idCandi[j], idCandi[j+1] = idCandi[j+1], idCandi[j]
    
    return (idCandi[0], idCandi[length-1])



