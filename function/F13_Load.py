import argparse
import os

# FUNGSI LOAD               load(data_user : list[list[str]], data_candi : list[list[str]], data_bahan : list[list[str]]) -> ( data_user : list[list[str]], data_candi : list[list[str]], data_bahan : list[list[str]], isExist : boolean)    
def load(data_user : list[list[str]], data_candi : list[list[str]], data_bahan : list[list[str]], isExist):
    # { INPUT   : data_user : list[list[str]], data_candi : list[list[str]], data_bahan : list[list[str]]
    #   OUTPUT  : data_user : list[list[str]], data_candi : list[list[str]], data_bahan : list[list[str]] }
    
    # KAMUS LOKAL
    files       : list[list[str]]
    i           : int
    isExist     : bool

    # setup argumen command line
    parser = argparse.ArgumentParser(description='Membuka file dalam folder file')
    parser.add_argument('nama_folder', type=str, help='Nama folder yang ingin dibuka')

    # parse argumen command line
    args = parser.parse_args()

    # buka folder
    folder_path = os.path.join(os.getcwd(), args.nama_folder)

    if os.path.exists(folder_path):
        print("Loading... \nSelamat datang di program “Manajerial Candi” \nSilahkan masukkan username Anda")
        # buka file
        files = ['bahan_bangunan.csv', 'candi.csv', 'user.csv']
        for i in range(3):
            file_path = os.path.join(folder_path, files[i])
            if os.path.exists(file_path):
                if (files[i] == "bahan_bangunan.csv"):
                    data_bahan = unpack(file_path, data_bahan)
                elif (files[i] == "candi.csv"):
                    data_candi = unpack(file_path, data_candi)
                else: # files[i] == "user.csv"
                    data_user = unpack(file_path, data_user)

                
            else:
                print(f'File {files[i]} tidak ditemukan')
                return(data_user, data_candi, data_bahan, isExist)
        
        isExist = True
        return(data_user, data_candi, data_bahan, isExist)
    else:
        print(f'Folder {args.nama_folder} tidak ditemukan')
        return(data_user, data_candi, data_bahan, isExist)


# FUNGSI UNPACK         unpack(filename : str, data_matriks : list[list[str]]) -> data_matriks : list[list[str]]
def unpack(filename : str, data_matriks : list[list[str]]):
    # { INPUT   : filename : str, data_matriks : list[list[str]]
    #   OUTPUT  : data_matriks : list[list[str]] }
    
    # KAMUS LOKAL
    lines       : list[list[str]]
    count       : int
    baris       : int
    kolom_now   : int
    tmp_string  : str
    baris_now   : str
    jumlah_karakter : int

    file = open(filename, 'r')
    lines = file.readlines()

    # Hitung jumlah baris
    count   = 0
    for line in lines:
        count += 1

    # Jalan setiap baris
    for baris in range(count):    
        kolom_now       = 0
        tmp_string      = ""
        baris_now       = lines[baris]
        jumlah_karakter = len(lines[baris])

        for j in range(jumlah_karakter):
            if (baris_now[j] != ";" and baris_now[j] != '\n'):
                tmp_string += baris_now[j]
            elif(baris_now[j] == ";"):
                data_matriks[baris][kolom_now] = tmp_string
                tmp_string  = ""
                kolom_now   += 1
        data_matriks[baris][kolom_now] = tmp_string
                
    return(data_matriks)
