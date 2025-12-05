def cek_anagram(kata1, kata2):
    return sorted(kata1) == sorted (kata2)

while True:
    kata1 = input("Masukkan kata pertama: ").lower()
    kata2 = input("Masukkan kata kedua: ").lower()
    
    if cek_anagram (kata1, kata2):
        print("Kedua kata tersebut merupakan anagram.")
    else:
        print("Kedua kata tersebut bukan anagram.")
    
    lanjut = input("Apakah ingin mengecek kata lain? (y/n): ").lower()
    if lanjut != 'y':
        print("Program selesai.")
        break
