import os #os kütüphanesi import edilmiş

secenek = input("İşlem?\nDosya okuma\nDosyaya yazı yazma\n: ") #kullanıcı girişte işlem yazıyor
dosya_ismi = input("Dosya ismi (sonuna .txt eklenmesi gerekiyor): ") #dosya ismini .txt halinde yazıyor

while True: #kodlar döngü halinde 
    if secenek == "Dosya okuma": #Dosya okuma komutu giriliyor
        if os.path.isfile(dosya_ismi): #.txt halinde girilen dosya var mı yok mu kontrol ediliyor
            with open(dosya_ismi,"r") as dosya: #.txt halinde girilen dosya hazırlanıyor
                print(dosya.read()) #.txt halinde girilen dosya okunuyor
                print("----------------------") #-- işareti koyuluyor
                secenek = input("İşlem?\nDosya okuma\nDosyaya yazı yazma\n: ") #tekrar işlem soruluyor
                dosya.close #dosya kapatılıyor
        else:
            print(dosya_ismi," Adında dosya yok.") #Dosya bulunmadığını söylüyor
    elif secenek == "Yazma": #Yazma komutu giriliyor
        if os.path.isfile(dosya_ismi): #.txt halinde girilen dosya var mı yok mu kontrol ediliyor
            metin = input("Metin (Metnin başına boşluk eklenmesi gerekiyor): ") #.txt halinde girilen dosyaya yazılacak metin yazılıyor
            dosya = open(dosya_ismi,"a") #Metnin içindekiler zarar görmeden hazırlanıyor
            dosya.write(metin) #Metnin içindekiler zarar görmeden yazılıyor
            print("----------------------") #-- işareti yazılıyor
            secenek = input("İşlem?\nDosya okuma\nDosyaya yazı yazma\n: ") #Kullanıcıya işlem soruluyor
            dosya.close #Dosya kapatılıyor
        else:
            print(dosya_ismi," Adında dosya yok.") #Dosyanın bulunmadığını söylüyor
    else:
        print("Hata") #Hata olduğunu söylüyor
        
