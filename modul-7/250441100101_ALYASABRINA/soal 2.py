def tampilkan_inventaris(inventaris):
    if not inventaris:
        print("Belum ada barang di inventaris.")
        return
    
    print("=== Daftar Inventaris Gudang ===")
    for ID, data in inventaris.items():
        print(f"ID      : {ID}")
        print(f"Nama    : {data[0]}")
        print(f"Harga   : {data[1]}")
        print(f"Stok    : {data[2]}")
        print("-----------------------------")

def cari_barang(inventaris):
    if not inventaris:
        print("Belum ada data barang.")
    else:
        ID = input("Masukkan ID barang: ")
        if ID in inventaris:
            data = inventaris[ID]
            print("Barang ditemukan:")
            print(f"ID      : {ID}")
            print(f"Nama    : {data[0]}")
            print(f"Harga   : {data[1]}")
            print(f"Stok    : {data[2]}")
        else:
            print("Barang tidak ditemukan.")

def tambah_barang(inventaris):
    while True:
        ID = input("Masukkan ID barang (angka saja): ")
        if not ID.isdigit():
            print("ID harus berupa angka!")
        elif ID in inventaris:
            print("ID sudah ada! Gunakan ID lain.")
        else:
            break
    
    nama = input("Masukkan nama barang: ")
    
    while True:
        harga_input = input("Masukkan harga barang: ")
        try:
            harga = int(harga_input)
            if harga < 0:
                print("Harga tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Harga harus angka!")
    
    while True:
        stok_input = input("Masukkan jumlah stok: ")
        try:
            stok = int(stok_input)
            break
        except ValueError:
            print("Stok harus angka!")
    
    inventaris[ID] = [nama, harga, stok]
    print("Barang berhasil ditambahkan!")

def update_stok(inventaris):
    if not inventaris:
        print("Belum ada data barang.")
    else:
        ID = input("Masukkan ID barang yang ingin diperbarui stoknya: ")
        if ID not in inventaris:
            print("Barang tidak ditemukan.")
            return
        
        while True:
            tambahan_input = input("Masukkan jumlah stok yang ditambahkan (negatif untuk mengurangi): ")
            try:
                tambahan = int(tambahan_input)
                if inventaris[ID][2] + tambahan < 0:
                    print(f"Stok tidak boleh negatif! Stok sekarang: {inventaris[ID][2]}")
                else:
                    inventaris[ID][2] += tambahan
                    print(f"Stok berhasil diperbarui! Stok baru: {inventaris[ID][2]}")
                    break
            except ValueError:
                print("Harap masukkan angka yang valid!")

def hapus_barang(inventaris):
    if not inventaris:
        print("Belum ada data barang.")
    else :
        ID = input("Masukkan ID barang yang ingin dihapus: ")
        if ID in inventaris:
            del inventaris[ID]
            print("Barang berhasil dihapus!")
        else:
            print("Barang tidak ditemukan.")

def main():
    inventaris = {}

    while True:
        print("=== MENU INVENTARIS GUDANG ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang")
        print("3. Tambah barang")
        print("4. Update stok barang")
        print("5. Hapus barang")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tampilkan_inventaris(inventaris)
        elif pilihan == "2":
            cari_barang(inventaris)
        elif pilihan == "3":
            tambah_barang(inventaris)
        elif pilihan == "4":
            update_stok(inventaris)
        elif pilihan == "5":
            hapus_barang(inventaris)
        elif pilihan == "6":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

main()