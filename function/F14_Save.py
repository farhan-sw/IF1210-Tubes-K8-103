# Import modul dari sistem
import os

def save_data(data, subfolder : str):

    folder_path = os.path.join(os.getcwd(), "save", subfolder)

    if not os.path.exists(folder_path):
        print ("Membuat folder save...")
        print(f"Membuat folder {subfolder}...")
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, "data.csv")
    with open(file_path, "w") as f:
        f.write("")
        for d in data:
            f.write(f"{d}\n")
    print(f"Berhasil menyimpan data di {subfolder}!")
    
# Testes
my_data = [["a","dua"], ["dua","tiga"]]
subfolder = input("Masukkan nama folder :")
save_data(my_data, subfolder)