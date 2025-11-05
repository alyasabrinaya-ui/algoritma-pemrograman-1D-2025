jumlah_baris = int (input("masukkan jumlah baris lampu : "))


for i in range (1,jumlah_baris+1) :
    jumlah_lampu = int(input(f"masukkan jumlah lampu pada baris ke {i} : "))

    for j in range (1, jumlah_lampu + 1) : 
        if j % 3 == 0 :
            print(f"lampu ke {j} pada baris ke {i} rusak. ")
        else :
            print (f"lampu ke {j} pada baris ke {i} menyala.")

    if i == jumlah_baris :
        print ("periksa sambungan daya utama.")