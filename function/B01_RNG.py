import time

def randomNumber(start, stop):
    time.sleep(0.005)
    # Membuat seed berdasarkan waktu saat ini
    seed = int(time.time() * 1000)
    
    # Parameter LCG
    m = 2**32
    a = 1103515245
    c = 12345
    
    # Menghasilkan angka acak berdasarkan LCG
    seed = (a * seed + c) % m
    
    # Menghasilkan angka di antara start dan stop
    result = start + (seed % (stop - start))
    
    return result

for i in range(10):
    print(randomNumber(0, 5))
