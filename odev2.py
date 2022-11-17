lessonCount = int(input("Kaç adet sınav notu gireceksiniz"))
x = 0
y = 0

gecilen_sinav = []
kalinan_sinav = []

for i in range(lessonCount):
    vize = float(input(f"{i+1}.  Vize Notunu Giriniz"))
    final = float(input(f"{i+1}. Final Notunu Giriniz"))
    ortalama = vize * 0.4 + final * 0.6
    if ortalama>=0 and ortalama<50:
        print("FF")
    elif ortalama>=50 and ortalama<60:
         print("DD")
    elif ortalama>=60 and ortalama<70:
        print("CC")
    elif ortalama>=70 and ortalama<80:
        print("BB")
    else:
        print("AA")

    if ortalama<50 :
        gecilen_sinav.append(ortalama)
        x=x+1
    else:
        kalinan_sinav.append(ortalama)
        y=y+1

print(f"{gecilen_sinav} adet sınavdan geçtiniz. {kalinan_sinav} adet sınavdan kaldınız")       
print(f"Geçilen sinavlar:{gecilen_sinav}") 
print(f"Kalınan sinavlar:{kalinan_sinav}")  
  


    






