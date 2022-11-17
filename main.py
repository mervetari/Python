print("Merhaba Etiya ashhd")
 # string = "metinsel ifade"
text ="10"
print(text)


# integer = tam sayı
number = 5
print(number)

# double,float,decimal = ondalıklı sayı
dnumber = 5.3
print(dnumber)

#! matematiksel operatörler
print(number + 5)
print(number - 5)
print(number * 5)
print(number / 5)
print(number % 3) #bölümünden kalanı veriyor

#! boolean, bool operatörler = true veya false olur. Genellikle karar yapılarında ve doğru veya yanlışta kullanılır.
isVerified = True
 
#! Mantıksal, Karşılaştırma Operatörler => her mantıksal operatörler boolean değer döner.
print(1 == 2)
print(2 != 2)

print(2 > 2)
print(2 < 2)

print(2 >= 2)
print(2 <= 2)

print(10%2 == 0)

print(50/2 == 25)
print(50/2 == 25.00)

#!string operatörler
text ="Merhaba Etiya"
print(text.upper()) #upper bütün harfler büyük yazılıyor
print(text.lower()) #lower bütün harfler küçük yazılıyor
print(text.startswith("Mer")) #İlgili fonksiyone verdiğim ifade ile mi başlıyor yoksa soununda verdiğim değer ile mi bitiyor

name = "Merve"
age = "23"
company = "Etiya"

#! Merve 23 yaşında Etiya'da çalışıyor
print(name + " " + age + " yaşında "  + company + "'de çalışıyor.")
print(f"{name} {age} yaşında {company}'de çalışıyor.")