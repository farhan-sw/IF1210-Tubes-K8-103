# -------------------------------- MODUL BASIC COMMANDS ----------------------------------------



# function countArray(data: array, NMax : integer) -> integer
# { Menerima input array dan memberikan output banyaknya data di array tersebut yang tidak kosong }

# function countMatriks(data: array, NMax : integer) -> integer
# { Menerima input matriks dan memberikan output banyaknya baris di matriks tersebut yang tidak kosong }

# function excludeEmptyArray(array : array of string, NMax : integer)
# { Menghilangkan data kosong yang ada di dalam array }

# function excludeEmptyMatriks(matriks : matriks of string, NMax : integer)
# { Menghilangkan data kosong yang ada di dalam matriks } 

def countArray(array, NMax : int, mark="*"):
    counter = 0
    for i in range(NMax):
        if array[i] != mark:
            counter += 1
    return counter

def countMatriks(matriks, NMax : int, mark="*"):
    counter = 0
    for i in range(NMax):
        if matriks[i][0] != mark:
            counter += 1
    return counter

def excludeEmptyArray(array, NMax : int, mark="*"):
    count = 0
    for i in range(NMax):

        if array[i] != mark:
            count += 1
    
    result = ["*" for i in range(count)]
    for i in range(count):
        result[i] = array[i]
    return result

def excludeEmptyMatriks(matriks, NMax, kolom : int, mark="*"):
    count = 0
    for i in range(NMax):
        if matriks[i][0] != mark:
            count += 1
    
    result = [["*" for j in range(kolom)] for i in range(count)]
    for i in range(count):
        result[i] = matriks[i]
    return result
