def tampilkan_kupon(kupon):
    if not kupon:
        print("Belum ada kupon yang tersedia.")
        return
    
    print("=== Kupon Tersedia ===")
    for kode, diskon in kupon.items():
        print(f"Kode: {kode} | Diskon: {diskon}%")
    print("----------------------")

def format_rupiah(nominal):
    return f"Rp{int(nominal):,}".replace(",", ".")

def proses_transaksi(kupon):
    total_belanja_input = input("Masukkan total belanja: ")
    
    try:
        total_belanja = int(total_belanja_input)
        if total_belanja < 0:
            print("Total belanja tidak boleh negatif!")
            return
    except ValueError:
        print("Total belanja harus berupa angka!")
        return
    
    kode_kupon = input("Masukkan kode kupon (kosong jika tidak ada): ")
    
    if kode_kupon in kupon:
        diskon = kupon[kode_kupon]
        total_bayar = total_belanja * (100 - diskon) / 100  
        print(f"Kupon valid! Diskon {diskon}% digunakan")
        print(f"Total yang harus dibayar: {format_rupiah(total_bayar)}")
        del kupon[kode_kupon]  
    else:
        if kode_kupon:  
            print(f"Kupon '{kode_kupon}' tidak valid atau sudah digunakan!")
        else:  
            print("Tidak ada kupon digunakan.")
        total_bayar = total_belanja
        print(f"Total yang harus dibayar: {format_rupiah(total_bayar)}")

def tambah_kupon(kupon):
    kode = input("Masukkan kode kupon baru: ")
    if not kode:
        print("Kode kupon tidak boleh kosong!")
        return
    if kode in kupon:
        print("Kode kupon sudah ada!")
        return
    
    try:
        diskon = int(input("Masukkan persentase diskon (1-100): "))
        if diskon < 1 or diskon > 100:
            print("Diskon harus antara 1 hingga 100%!")
            return
    except ValueError:
        print("Diskon harus berupa angka!")
        return
    
    kupon[kode] = diskon
    print(f"Kupon '{kode}' dengan diskon {diskon}% berhasil ditambahkan!")

def main():
    kupon = {
        "cihuyy": 10,
        "murahey": 30,
        "belanjayu": 50
    }

    while True:
        print("=== MENU ===")
        print("1. Tampilkan semua kupon")
        print("2. Proses transaksi")
        print("3. Tambah kupon baru")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            tampilkan_kupon(kupon)
        elif pilihan == "2":
            proses_transaksi(kupon)
        elif pilihan == "3":
            tambah_kupon(kupon)
        elif pilihan == "4":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

main()