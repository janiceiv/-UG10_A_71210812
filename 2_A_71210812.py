print("############################")
print("Kalkulator Advance Sederhana")
print("############################")
print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan ke bawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")

pilih = int(input("Masukan menu yang anda pilih: "))

if pilih == 1:
    bagi = float(input("Masukan bilangan yang ingin dibagi: "))
    pembagi = float(input("Masukan bilangan pembagi: "))
    sisa = bagi % pembagi
    print("Sisa hasil bagi", bagi, "dibagi dengan", pembagi, "adalah", sisa)

elif pilih == 2:
   dibagi = float(input("Masukan bilangan yang ingin dibagi: "))
   pembagii = float(input("Masukan bilangan pembagi: "))
   pembulatan = (dibagi / pembagii)
   hasil = round(pembulatan)- 1
   print("Hasil pembagian", dibagi, "dibagi dengan", pembagii, "dibulatkan kebawah adalah", hasil)

elif pilih == 3:
    bilangan = float(input("Masukan bilangan yang ingin dicari akar kubiknya: "))
    akar = bilangan ** (1/3)
    hasil_akar = round(akar)
    print("Akar kubik dari", bilangan, "adalah", hasil_akar)

else:
    print("Menu yang ada pilih tidak tersedia")
    
