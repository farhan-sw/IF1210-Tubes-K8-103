import argparse
import os

def load(data_user, data_candi, data_bahan):
    # setup argumen command line
    parser = argparse.ArgumentParser(description='Membuka file dalam folder file')
    parser.add_argument('nama_folder', type=str, help='Nama folder yang ingin dibuka')

    # parse argumen command line
    args = parser.parse_args()

    # buka folder
    folder_path = os.path.join(os.getcwd(), args.nama_folder)

    if os.path.exists(folder_path):
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
                return(data_user, data_candi, data_bahan)
            
        return(data_user, data_candi, data_bahan)
    else:
        print(f'Folder {args.nama_folder} tidak ditemukan')
        return(data_user, data_candi, data_bahan)


def unpack(filename : str, data_matriks):
    
    file = open(filename, 'r')
    lines = file.readlines()

    # Hitung jumlah baris
    count   : int   = 0
    for line in lines:
        count += 1

    # Jalan setiap baris
    for baris in range(count):    

        kolom_now       : int = 0
        tmp_string      : str = ""
        baris_now       : str = lines[baris].rstrip("\n")
        jumlah_karakter : int = len(lines[baris])

        for j in range(jumlah_karakter-1):
            # print(baris_now[j])
            if (baris_now[j] != ";"):
                tmp_string += baris_now[j]
            elif(baris_now[j] == ";"):
                data_matriks[baris][kolom_now] = tmp_string
                tmp_string  = ""
                kolom_now   += 1
        data_matriks[baris][kolom_now] = tmp_string
                
    return(data_matriks)
