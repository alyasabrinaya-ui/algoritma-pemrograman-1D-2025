def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok

    if jabatan == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0

    gaji_bersih = gaji_pokok - pajak + tunjangan
    
    print("======== Rincian Gaji ========")
    print("Nama:", nama)
    print("Jabatan:", jabatan)
    print(f"Gaji Pokok: Rp{gaji_pokok:,.0f}")
    print(f"Pajak (5%): Rp{pajak:,.0f}")
    print(f"Tunjangan: Rp{tunjangan:,.0f}")
    print(f"Gaji Bersih: Rp{gaji_bersih:,.0f}")
    return gaji_bersih

while True:
    while True:
        nama = input("Masukkan nama karyawan: ")
        if nama.isalpha():
            break
        else:
            print("Nama harus berupa huruf tanpa spasi atau angka!")

   
    while True:
        jabatan = input("Masukkan jabatan (manager/staff): ")
        if jabatan.isalpha():
            break
        else:
            print("Jabatan harus berupa huruf!")

    while True:
        gaji_input = input("Masukkan gaji pokok: ")
        if gaji_input.isdigit():
            gaji_pokok = int(gaji_input)
            break
        else:
            print("Gaji harus berupa angka non-negatif!")

    hitung_gaji(nama, jabatan, gaji_pokok)

    lanjut = input("Apakah ingin menghitung gaji karyawan lain? (y/n): ")
    if lanjut != 'y':
        print("Program selesai.")
        break
