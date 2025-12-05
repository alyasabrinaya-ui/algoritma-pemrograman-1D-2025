def validasi_nama(nama):
    return nama.replace(" ", "").isalpha()


def validasi_email(email):
    return email.endswith("@gmail.com")


def validasi_telepon(telepon):
    return telepon.isdigit() and 10 <= len(telepon) <= 13


def tampilkan_kontak(contacts):
    if not contacts:
        print("Belum ada kontak.")
        return
    
    print("=== Daftar Kontak ===")
    for nama, data in contacts.items():
        print(f"Nama    : {nama}")
        print(f"Telepon : {data[0]}")
        print(f"Email   : {data[1]}")
        print("-----------------------------")

def cari_kontak(contacts):
    if not contacts :
        print("Belum ada data kontak.")
    else:
        nama = input("Masukkan nama kontak: ")
        if nama in contacts:
            print("Kontak ditemukan:")
            print(f"Nama    : {nama}")
            print(f"Telepon : {contacts[nama][0]}")
            print(f"Email   : {contacts[nama][1]}")
        else:
            print("Kontak tidak ditemukan.")

def tambah_kontak(contacts):
    while True:
        nama = input("Masukkan nama: ")
        if not validasi_nama(nama):
            print("Nama hanya boleh huruf dan spasi!")
        elif nama in contacts:
            print("Kontak sudah ada!")
        else:
            break

    while True:
        telepon = input("Masukkan nomor telepon (10-13 digit): ")
        if not validasi_telepon(telepon):
            print("Nomor telepon harus angka dan 10-13 digit!")
        else:
            break

    while True:
        email = input("Masukkan email (@gmail.com): ")
        if not validasi_email(email):
            print("Email harus menggunakan @gmail.com!")
        else:
            break

    contacts[nama] = [telepon, email]
    print("Kontak berhasil ditambahkan!")

def update_email(contacts):
    if not contacts :
        print("Belum ada data kontak.")
    else : 
        nama = input("Masukkan nama kontak: ")
            
        if nama not in contacts:
            print("Kontak tidak ditemukan.")
            return
        
        while True:
            if not contacts :
                print("Belum ada data kontak.")
            else :
                email_baru = input("Masukkan email baru (@gmail.com): ")
                if not validasi_email(email_baru):
                    print("Email harus menggunakan @gmail.com!")
                else:
                    break
            
        contacts[nama][1] = email_baru
        print("Email berhasil diperbarui!")

def hapus_kontak(contacts):
    if not contacts :
        print("Belum ada data kontak.")
    else :
        nama = input("Masukkan nama kontak: ")
        if nama in contacts:
            del contacts[nama]
            print("Kontak berhasil dihapus!")
        else:
            print("Kontak tidak ditemukan.")

def main():
    contacts = {}

    while True:
        print("=== MENU CONTACT BOOK ===")
        print("1. Tampilkan semua kontak")
        print("2. Cari kontak")
        print("3. Tambah kontak")
        print("4. Update email kontak")
        print("5. Hapus kontak")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tampilkan_kontak(contacts)
        elif pilihan == "2":
            cari_kontak(contacts)
        elif pilihan == "3":
            tambah_kontak(contacts)
        elif pilihan == "4":
            update_email(contacts)
        elif pilihan == "5":
            hapus_kontak(contacts)
        elif pilihan == "6":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

main()