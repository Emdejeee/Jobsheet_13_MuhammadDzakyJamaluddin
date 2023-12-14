def wieght_conversion():
    weight = int(input("Masukkan Massa tubuh anda:"))
    types = input("Masukkan satuan K atau L ")

    if (types == "K"):
        kg = weight * 0.453592
        print(kg)
    elif(types == "L"):
        lbs = weight * 2.20462
        print(lbs)
