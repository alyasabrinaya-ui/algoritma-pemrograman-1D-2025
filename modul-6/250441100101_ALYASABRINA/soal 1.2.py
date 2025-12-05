def tambah_data(data_kunjungan, id_antrian):
    print("Tambah Data Pengunjung")
    while True:
        nama = input("Nama pengunjung: ")
        if any(char.isdigit() for char in nama):
            print("Nama tidak boleh angka!")
        else:
            break
    while True:
        nama_santri = input("Nama santri yang dijenguk: ")
        if any(char.isdigit() for char in nama_santri):
            print("Nama santri tidak boleh angka!")
        else:
            break
    while True:
        daerah = input("Daerah asal (sumatra/kalimantan/jawa): ")
        if daerah not in ["sumatra", "kalimantan", "jawa"]:
            print("Pilihan daerah tidak sesuai!")
        else:
            break
    data_kunjungan.append([id_antrian, nama, nama_santri, daerah])
    print("Data berhasil ditambahkan dengan ID:", id_antrian)
    id_antrian += 1
    return data_kunjungan, id_antrian

def tampil_data(data_kunjungan):
    print("Daftar Pengunjung Berdasarkan Daerah")
    if not data_kunjungan:
        print("Belum ada data pengunjung.")
    else:
        for daerah in ["sumatra", "kalimantan", "jawa"]:
            print("Daerah", daerah)
            ada = False
            for data in data_kunjungan:
                if data[3] == daerah:
                    print("ID:", data[0], "| Nama:", data[1], "| Santri:", data[2])
                    ada = True
            if not ada:
                print("Belum ada pengunjung dari daerah ini")

def ubah_data(data_kunjungan):
    if not data_kunjungan:
        print("Belum ada data pengunjung.")
    else :
        ubah_id = int(input("Masukkan ID yang akan diubah: "))
        for data in data_kunjungan:
            if data[0] == ubah_id:
                print("Data lama ->", data)
                nama_baru = input("Nama pengunjung baru (kosong jika tidak diubah): ")
                if nama_baru != "":
                    data[1] = nama_baru
                santri_baru = input("Nama santri baru (kosong jika tidak diubah): ")
                if santri_baru != "":
                    data[2] = santri_baru
                daerah_baru = input("Daerah baru (sumatra/kalimantan/jawa): ")
                if daerah_baru != "":
                    data[3] = daerah_baru
                print("Data berhasil diubah!")
                return data_kunjungan
        print("ID tidak ditemukan!")
        return data_kunjungan

def hapus_data(data_kunjungan):
    if not data_kunjungan:
        print("Belum ada data pengunjung.")
    else:
        hapus_id = int(input("Masukkan ID yang akan dihapus: "))
        for data in data_kunjungan:
            if data[0] == hapus_id:
                data_kunjungan.remove(data)
                print("Data berhasil dihapus!")
                return data_kunjungan
        print("ID tidak ditemukan!")
        return data_kunjungan

def main():
    data_kunjungan = []
    id_antrian = 1

    while True:
        print("Menu:")
        print("1. Tambah Data Pengunjung")
        print("2. Tampilkan Semua Pengunjung per Daerah")
        print("3. Ubah Data Pengunjung")
        print("4. Hapus Data Pengunjung")
        print("5. Keluar")
        pilih = input("Pilih menu (1-5): ")
        if pilih == "1":
            data_kunjungan, id_antrian = tambah_data(data_kunjungan, id_antrian)
        elif pilih == "2":
            tampil_data(data_kunjungan)
        elif pilih == "3":
            data_kunjungan = ubah_data(data_kunjungan)
        elif pilih == "4":
            data_kunjungan = hapus_data(data_kunjungan)
        elif pilih == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

main()