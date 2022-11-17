#! Karar blokları
#! Döngüler
print("2. gün başlangınç")

userInput = input()
print(f"Girilen değer: {userInput}")

#! type conversion
numberStr = "10";
print(type(numberStr))
number = int(numberStr);
print(number + 10);
print(type(number))
 
userInput = input();
lessonNote =int(userInput)
print(f"Ders notunuz: {lessonNote}")

if lessonNote>50:
    print("Geçtiniz")
elif lessonNote == 50:
    print("Sınırda Geçtiniz")
elif lessonNote == 49:
    print("Sınırda Kaldınız")
else:
    print("Kaldınız")