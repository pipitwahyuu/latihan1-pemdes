username=("pipitwahyuu")
kunciku=("kopatkapit")

def masuk(user,kunci):
    if user != username and kunci != kunciku:
        stop = False
    else:
        stop = True
    return stop

a=3
for i in range(0,a):
    user_baru = input("Username = ")
    kunci_baru = input("Password = ")
    stop = (masuk(user_baru,kunci_baru))
    if stop == True:
        print("Anda Berhasil Masuk")
        break
    else:
        print("Username dan Password anda salah")
