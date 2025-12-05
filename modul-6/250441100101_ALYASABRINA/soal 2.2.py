while True:
    t1 = input("Masukkan angka tuple 1(pisahkan dengan spasi): ").split()
    t2 = input("Masukkan angka tuple 2(pisahkan dengan spasi): ").split()

    tuple1 = ()
    for i in t1:
        tuple1 += (int(i),)
    tuple2 = ()
    for j in t2:
        tuple2 += (int(j),)

    gabung = tuple1 + tuple2
    print("Gabungan sebelum diurutkan:", gabung)

    hasil = ()
    for x in gabung:
        if x not in hasil:
            hasil += (x,)

    hasil = list(hasil)
    for i in range(len(hasil)):
        for j in range(i + 1, len(hasil)):
            if hasil[i] < hasil[j]:
                hasil[i], hasil[j] = hasil[j], hasil[i]
    hasil = tuple(hasil)

    print("Hasil akhir (setelah diurutkan):", hasil)

    lagi = input("Mau gabung lagi? (y/n): ").lower()
    if lagi != "y":
        print("Program selesai.")
        break