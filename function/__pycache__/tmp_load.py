import sys
sys.path.insert(0, 'function')
import commands

# function load(filename : string, NMax : integer, data_matriks : Matriks of integer, kolom : integer) -> (matriks)
# { Menerima input path dari data .csv dan mengeluarkan output matriks data}

def load(filename : str, NMax : int, data_matriks, kolom : int):
    
    file = open(filename, 'r')
    lines = file.readlines()
    data = [separate(line, NMax,'\n') for line in lines]
    file.close()

    rows = 0
    for i in data:
        rows += 1

    matrix = [[(cell) for cell in separate(data[i][0], NMax, ';')] for i in range(rows)]

    # Lanjutkan isi Matriks
    for i in range(rows):
        for j in range(kolom):
            data_matriks[i][j] = matrix[i][j]
    return data_matriks

def separate(sentence, NMax, mark=";"):

    # function separate(sentence : string, NMax : integer) -> array
    # { Menerima masukan berupa string dan akan memberikan output pemenggalan mark}
    # { Alternatif fungsi .split() }

    split_value = ["*" for i in range(NMax)]
    tmp = ''
    i = 0
    for c in sentence:
        if c == mark:
            split_value[i] = (tmp)
            i += 1
            tmp = ''
        else:
            tmp += c
    if tmp:
        split_value[i] = (tmp)
    split_value = commands.excludeEmptyArray(split_value, NMax)
    return split_value