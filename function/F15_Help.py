# PROSEDUR HELP         help(INPUT user_role : str, INPUT isLogin : bool, OUTPUT str)
def help(user_role : str, isLogin : bool):
    # { I.S. user_role terdefinisi dan isLogin mememiliki nilai True/False
    #   F.S. Menampilkan seluruh command yang dimiliki tiap user ke terminal }

    # ALGORITMA
    if (isLogin == False):
        print("=========== HELP ===========")
        print("1. login \n   Untuk masuk menggunakan akun")
        print("2. exit \n   Untuk kembali ke terminal")
    else: # isLogin == True
        if(user_role == "bandung_bondowoso"):
            print("=========== HELP ===========")
            print("1. logout \n   Untuk keluar dari akun yang digunakan sekarang")
            print("2. summonjin \n   Untuk memanggil jin")
            print("3. hapusjin \n   Untuk menghapus jin beserta candi yang dibangun jin terkait")
            print("4. ubahjin \n   Untuk mengubah tipe jin")
            print("5. batchkumpul \n   Untuk memanggil semua jin pengumpul")
            print("6. batchbangun \n   Untuk memanggil semua jin pembangun")
            print("7. laporanjin \n   Untuk menampilkan semua laporan jin")
            print("8. laporancandi \n   Untuk menampilkan semua laporan candi")
            print("9. hancurkancandi \n   Untuk menghancurkan id candi tertentu\n")
        elif(user_role == "roro_jonggrang"):
            print("=========== HELP ===========")
            print("1. logout \n   Untuk keluar dari akun yang digunakan sekarang")
            print("2. hancurkancandi \n   Untuk menhacurkan candi dengan indeks tertentu")
            print("3. ayamberkokok \n   Untuk menyelesaikan permainan dengan memalsukan siang/malam") 
        elif(user_role == "Jin Pengumpul") :
            print("=========== HELP ===========")
            print("1. logout \n   Untuk keluar dari akun yang digunakan sekarang")
            print("2. kumpul \n   Untuk mengumpulkan resource candi")
        elif(user_role == "Jin Pembangun") :
            print("=========== HELP ===========")
            print("1. logout \n   Untuk keluar dari akun yang digunakan sekarang")
            print("2. bangun \n   Untuk membangun candi")
