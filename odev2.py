vize = float(input("Vize Notunu Giriniz"))
final = float(input("Final Notunu Giriniz"))

ortalama = vize * 0.4 + final * 0.6
print(f"Ortalamaınız: {ortalama}")

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
    