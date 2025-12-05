def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

while True:
    n = int(input("Masukkan bilangan bulat non-negatif: "))
    
    if n < 0:
        print("Bilangan harus non-negatif!")
        continue 
    
    print("Hasil faktorial dari", n, "adalah:", faktorial(n))
    
    lanjut = input("Apakah ingin menghitung lagi? (y/n): ")
    if lanjut != 'y':
        print("Program selesai.")
        break

