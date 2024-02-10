import os
import datetime

splittedList = str.split("https://www.instagram.com/busezeynep/","/")
print(str(splittedList) + "uzunluk: " + str(len(splittedList)))

targetPath = os.path.join("./", "output", "b")
#os.makedirs(targetPath, exist_ok=True)

#(datetime.date.today().strftime("%d_%m_%Y"))

targetFolderPath = os.path.join("./", "output", str((datetime.date.today().strftime("%d_%m_%Y"))))
targetTxtPath = os.path.join(targetFolderPath, "followings.txt")
with open(targetTxtPath, "r") as dosya:
    satir_sayisi = len(dosya.readlines())
    print("Dosyanın içindeki toplam satır sayısı:", satir_sayisi)