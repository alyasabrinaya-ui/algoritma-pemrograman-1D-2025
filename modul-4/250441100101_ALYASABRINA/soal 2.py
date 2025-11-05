total_gaji = 0
total_lembur = 0
total_bonus = 0 
total_jam_lembur = 0   

for hari in range (1,8) :
    print(f"hari ke {hari}")
    lembur = int(input("masukkan jumlah jam lembur : "))
    shift = input("apakah shift malam?(y/n) : ")
    
    gaji = 100000

    if lembur <= 3 :
        upah_lembur = lembur * 25000
    elif lembur == 4 :
        upah_lembur = 100000
    elif lembur == 5 :
        upah_lembur = 125000
    elif lembur == 6 : 
        upah_lembur = 200000
    elif lembur == 7 :
        upah_lembur = 225000
    elif lembur == 8 :
        upah_lembur = 300000
    else : 
        upah_lembur = 0
        print("lembur melebihi batas, tidak dihitung.")
        lembur = 0
        
    if shift == "y" :
        bonus = 50000
    else : 
        bonus = 0

    total_harian = gaji + upah_lembur + bonus
    total_gaji += total_harian
    total_lembur += upah_lembur
    total_bonus += bonus
    total_jam_lembur += lembur  

print("=====HASIL GAJI MINGGUAN======")
print("total jam lembur :", total_jam_lembur, "jam")  
print("total upah lembur : Rp.",total_lembur)
print("total bonus shift malam : Rp.",total_bonus)
print("total gaji seminggu : Rp.",total_gaji)
