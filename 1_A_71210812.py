UG = float(input("Masukan nilai rata-rata UG anda : "))
TTS = float(input("Masukan nilai TTS anda : "))
TAS = float(input("Masukan nilai TAS anda : "))

#proses
rata = (UG * 70/100) + (TTS * 15/100) + (TAS * 15/100)

print("==========================")
print("Nilai anda: ", rata)

if rata >= 85:
    print ("Nilai huruf anda: A")

elif rata >= 80:
    print ("Nilai huruf anda: A-")

elif rata >= 75:
    print ("Nilai huruf anda: B+")

elif rata >= 70:
    print ("Nilai huruf anda: B")

elif rata >= 65:
    print ("Nilai huruf anda: B-")

elif rata >= 60:
    print ("Nilai huruf anda: C+")

elif rata >= 55:
    print ("Nilai huruf anda: C")

elif rata >= 45:
    print ("Nilai huruf anda: D")

else:
    print ("Nilai huruf anda: E")



