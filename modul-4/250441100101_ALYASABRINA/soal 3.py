n = int(input("Masukkan nilai n: "))

lebar = len(str(n)) + 1  

for i in range(1, n + 1):     
   
    for j in range(1, i + 1):
        print(f"{j:{lebar}}", end="")

    jarak = (n - i) * lebar * 2 
    print(" " * jarak, end="")

    for j in range(i, 0, -1):
        print(f"{j:{lebar}}", end="")
    print()
