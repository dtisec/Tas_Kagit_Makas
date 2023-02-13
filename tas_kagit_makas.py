import random
import os

# Terminali temizliyoruz.
os.system("clear||cls")

# Değişkenlerimizi tanımlıyoruz.
gameChars = ["Taş", "Kağıt", "Makas"]

# Yukarıda verilen değişkenleri inputluyoruz.
user_choice = input("Taş, Kağıt ya da Makas seçiniz: ")
computer_choice = random.choice(gameChars)

if user_choice == computer_choice: # Kullanıcı ile bilgisayarı eşitliyoruz.
     conclusion = "Berabere kaldınız!" # Eğer cevaplar aynıysa verilen cevap 'Beraber Kaldınız' olarak geri dönüş sağlıyor bize.

elif (user_choice == "Taş" and computer_choice == "Makas") or (user_choice == "Kağıt" and computer_choice == "Taş") or (user_choice == "Makas" and computer_choice == "Kağıt"): # Kullanıcının cevabına bilgisayarında cevap vermesini tanımlıyoruz. 
     conclusion = ("Kazandınız!")

else:
     conclusion = ("Kaybettiniz")

print("Bilgisayar: ", computer_choice) # Biz cevabımızı verdiğimizde bilgisayarın verdiği cevabı öğrenmek için Bilgisayarın cevabını tanımlıyoruz.
print("Sonuç: ", conclusion) # Kazanan veya Kaybedenin kim olduğu sonucu almamızı sağlıyoruz.
