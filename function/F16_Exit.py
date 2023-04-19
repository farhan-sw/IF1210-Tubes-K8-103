import F14_Save

# Fungsi Exit                   exit (masukkan : str)
def exit (masukkan : str) :
# I.S fungsi menerima masukkan dari user apakah ingin menyimpan data sebelum keluar atau tidak
# F.S jika iya, fungsi membuat file "save" an dalam format csv dalam folder save. Jika tidak, program akan langsung keluar
    
    # Kamus Lokal 

    masukkan : str

    # ALGORITMA UTAMA

    while ((masukkan != "Y") or (masukkan != "y") or (masukkan != "N") or (masukkan != "n")) :
        masukkan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    if ((masukkan == "Y") or (masukkan == "y")) :
        F14_Save.save_data
        exit()
    else : # Masukkan = "N" or Masukkan == "n"
        exit()

    