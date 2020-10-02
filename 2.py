def menu():
    print("---------Menghitung Luas dan Keliling Persegi Panjang--------")
    print("1. Luas")
    print("2. Keliling")
    choose=int(input("masukkan pilihan anda = "))
    if choose==1:
        print (luas1())
    elif choose==2:
        print (keliling1())
    else:
        print("yang anda masukkan tidak ada dimenu")
        

def luas1():
    print("----------------------")
    print(">>>>>>menghitung luas persegi panjang<<<<<<")
    p=int(input("masukkan panjang = "))
    l=int(input("masukkan lebar = "))
    luas = (p*l)
    return luas

def keliling1():
    print("----------------------")
    print(">>>>>>menghitung keliling persegi panjang<<<<<<")
    p=int(input("masukkan panjang = "))
    l=int(input("masukkan lebar = "))
    keliling = (2*(p+l))
    return keliling
menu()



