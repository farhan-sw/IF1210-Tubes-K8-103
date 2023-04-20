# Import Modul bentukan 
import sys
sys.path.insert(0, 'function')
import dataModule
import commands

def ambillaporanjin (data_candi, NMax_candi, data_bahan, data_username, NMax_username):

    total_jin_pengumpul = hitungJin('jin_pengumpul', data_username, NMax_username)
    total_jin_pembangun = hitungJin('jin_pembangun', data_username, NMax_username)
    total_jin = total_jin_pengumpul + total_jin_pembangun

    jin = (pembuat_terajin(data_candi, NMax_candi, data_username))
    terajin = jin[0][0]
    termalas = jin[1][0]
    if jin[0][1] == jin[1][1]:
        termalas = '-'
    if jin[0][0] == '':
        terajin = '-'
    if jin[1][0] == '':
        termalas = '-'
    

    print("\n> Total Jin: ", total_jin)
    print("> Total Jin Pengumpul: ", total_jin_pengumpul)
    print("> Total Jin Pembangun: ", total_jin_pembangun)
    print("> Jin Terajin: ", terajin) 
    print("> Jin Termalas: ", termalas)
    print("> Jumlah Pasir: ", data_bahan[1][2])
    print("> Jumlah Air: ", data_bahan[3][2])
    print("> Jumlah Batu: ", data_bahan[2][2])

def hitungJin (role, data_user, NMax_user):
    total_jin = 0
    for i in range (1, NMax_user) :
        if data_user[i][0] != "*" and data_user[i][1] != "*" and data_user [i][2] == role:
            total_jin += 1
    return total_jin

def pembuat_terajin (data_candi, NMax, data_user):

    jumlah_candi = [['' for i in range(2)]for i in range (NMax)]
    
    for i in range(NMax):
        jumlah_candi[i][1] = 0
        if data_user[i][2] == 'jin_pembangun': 
            jumlah_candi[i][0] = data_user[i][0]

    # Iterate through each element in array1
    for i in range(NMax):
        # Iterate through each element in array2
        for j in range(NMax):
            # Check if the current element in array1 is the same as the current element in array2
            if jumlah_candi[i][0] == data_candi[j][1]:
                jumlah_candi[i][1]  +=1
         
    # Outer loop to iterate over all elements in the array
    for i in range(NMax):
        # Inner loop to compare adjacent elements and swap them if necessary
        for j in range(NMax-1-i):
            if jumlah_candi[j][1] < jumlah_candi[j+1][1]:
                jumlah_candi[j], jumlah_candi[j+1] = jumlah_candi[j+1], jumlah_candi[j]

    length = commands.countMatriks(jumlah_candi, NMax, '')
    max_idx = 0
    min_idx = length-1
    first_element = jumlah_candi[0][1]
    last_element = jumlah_candi[length-1][1]
    for j in range (length):  
            if jumlah_candi[j+1][1] == first_element:
                for k in range(j+1, length):
                    if jumlah_candi[k][0] < jumlah_candi[max_idx][0]:
                        max_idx = k
                    jumlah_candi[j], jumlah_candi[max_idx] = jumlah_candi[max_idx], jumlah_candi[j]

            elif jumlah_candi[j][1] == last_element:
                for k in range(j+1, length):
                    if jumlah_candi[k][0] < jumlah_candi[min_idx][0]:
                        min_idx = k
                    jumlah_candi[j], jumlah_candi[min_idx] = jumlah_candi[min_idx], jumlah_candi[j]
                
    return(jumlah_candi[0], jumlah_candi[length-1])