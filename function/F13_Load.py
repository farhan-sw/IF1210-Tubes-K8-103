

# function load(filename : string, NMax : integer, data_matriks : Matriks of integer, kolom : integer) -> (matriks)
# { Menerima input path dari data .csv dan mengeluarkan output matriks data}

def load(filename : str, NMax : int, data_matriks, kolom : int):
    
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
        


    #print(lines)
def testing():
    NMax_user   : int = 1000 ; kolom_user  : int = 3
    data_matriks_tmp  = [["*" for col in range(kolom_user)] for row in range(NMax_user)]
    
    data = load("file/user.csv", NMax_user, data_matriks_tmp, kolom_user)

    print(data[:10])
    
#testing()
