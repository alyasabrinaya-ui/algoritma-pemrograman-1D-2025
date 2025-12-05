def tambah(data):
    deret = input("Masukkan deret angka (pisahkan spasi): ").split()
    for i in deret:
        data.append(int(i))
    print("Data berhasil ditambah!")
    return data


def lihat(data):
    if not data:
        print("Belum ada data.")
    else:
        print("Data sekarang:", data, "")


def ubah(data):
    if not data:
        print("Belum ada data.")
        return data

    ganti = int(input("Angka yang mau diganti: "))
    if ganti in data:
        baru = int(input("Ganti jadi: "))
        data[data.index(ganti)] = baru
        print("Data berhasil diganti!")
    else:
        print("Angka tidak ditemukan.")
    return data


def hapus(data):
    if not data:
        print("Belum ada data.")
        return data

    hapus = int(input("Angka yang mau dihapus: "))
    if hapus in data:
        data.remove(hapus)
        print("Data berhasil dihapus!")
    else:
        print("Angka tidak ditemukan.")
    return data


def cek_bagi_dua(data):
    if not data:
        print("Belum ada data.")
    elif len(data) % 2 != 0:
        print("Gak bisa dibagi dua, jumlah angkanya ganjil.")
    else:
        tengah = len(data)//2
        kiri = data[:tengah]
        kanan = data[tengah:]
        print("Bagian kiri:", kiri)
        print("Bagian kanan:", kanan)
        if sum(kiri) == sum(kanan):
            print("Bisa dibagi dua dengan jumlah sama!")
        else:
            print("Tidak bisa dibagi dua karena jumlahnya beda.")

data_angka = []

while True:
    print("Menu:")
    print("1. Tambah data")
    print("2. Lihat data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("5. Cek bisa dibagi dua sama besar")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        data_angka = tambah(data_angka)
    elif pilih == "2":
        lihat(data_angka)
    elif pilih == "3":
        data_angka = ubah(data_angka)
    elif pilih == "4":
        data_angka = hapus(data_angka)
    elif pilih == "5":
        cek_bagi_dua(data_angka)
    elif pilih == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak ada.")