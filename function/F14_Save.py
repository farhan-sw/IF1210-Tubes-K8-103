# Import modul dari sistem
import os

def save_data(data : list[list[str]], nama_data : str, subfolder : str, baris_max : int, kolom_max : int):


    folder_path = os.path.join(os.getcwd(), "save", subfolder)

    if not os.path.exists(folder_path):
        print ("Membuat folder save...")
        print(f"Membuat folder {subfolder}...")
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, nama_data)

    with open(file_path, "w") as f:
        f.write("")

        for i in range(baris_max):
            for j in range(kolom_max):
                # Tulis jika data tidak kosong
                if (data[i][j] != "*"):
                    f.write(data[i][j])

                    # Tulis pemisah
                    if (j < kolom_max - 1):
                        if (data[i][j+1] != "*"):
                            f.write(";")

            # Tulis Enter jika tidak sekarang tidak kosong
            if (i < baris_max - 1):
                if (data[i][j] != "*"):
                    f.write('\n')
    
    
# # Testes
# my_data = [["pertama","kedua", "Ada lagi"], ["dua","tiga", "Hiya"], ["*","*", "*", "*"], ["dua","tiga", "Hiya"]]
# subfolder = input("Masukkan nama folder :")
# save_data(my_data, subfolder, 4, 3)