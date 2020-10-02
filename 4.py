data = []
stop = False
i = 0

while not stop:
    data_baru = int(input("Masukkan data yang ke-{} = " .format(i)))
    data.append(data_baru)

    i+=1

    choose = input("Mau isi lagi?(y/t)")
    if choose == "t":
        stop = True

print(">>>>>>>-------------<<<<<<<")
print(data)

nilai_terkecil = min(data)
nilai_terbesar = max(data)
print(">>>>>>>-------------<<<<<<<")
print("nilai terkecil dari list = " ,nilai_terkecil)
print("nilai terbesar dari list = " ,nilai_terbesar)
