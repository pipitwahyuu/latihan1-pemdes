tinggi=float(input("masukkan tinggi badan anda(meter) = "))
berat=float(input("masukkan berat badan anda(kilogram) = "))
bmi=round(berat/(tinggi*tinggi),2)
print("index massa tubuhmu adalah = " ,bmi)

if bmi<18.5:
    print("Berat badan Anda kurang")
elif bmi>=18.5 and bmi <=22.9:
    print ("berat badan Anda normal")
elif bmi>=23 and bmi<=29.9:
    print ("berat badan Anda berlebih(cenderung obesitas)")
elif bmi>=30:
    print ("obesitas")
