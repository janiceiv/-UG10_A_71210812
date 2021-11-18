artikel = input("Masukan artikel yang ingin dipindai: ")
klub = input("Masukan nama klub favorit anda: ")
skor = int(input("Masukan skor yang ingin dicari: "))

if 'klub' and 'skor' in artikel: 
    print("Hasil pencarian ditemukan")

elif 'klub' in artikel:
    print("Hanya kata", klub, "yang ditemukan pada artikel ini")
    
elif 'skor' in artikel:
    print("Hanyan skor", skor, "yang ditemukan pada artikel ini")

else:
    print("Hasil pencarian", klub, "dan", skor, "tidak ditemukan")
