import os
import datetime

# splittedList = str.split("https://www.instagram.com/busezeynep/","/")
# print(str(splittedList) + "uzunluk: " + str(len(splittedList)))

# targetPath = os.path.join("./", "output", "b")
#os.makedirs(targetPath, exist_ok=True)

#(datetime.date.today().strftime("%d_%m_%Y"))

# targetFolderPath = os.path.join("./", "output", str((datetime.date.today().strftime("%d_%m_%Y"))))
# targetTxtPath = os.path.join(targetFolderPath, "followings.txt")
# with open(targetTxtPath, "r") as dosya:
#     satir_sayisi = len(dosya.readlines())
#     print("Dosyanın içindeki toplam satır sayısı:", satir_sayisi)

countsList = ["308&nbsp;B","6,3&nbsp;Mn", "10&nbsp;B","151"]

for count in countsList:
    tempList = count.split("&nbsp;")
    tempList[0] = tempList[0].replace(",", ".")
    if len(tempList) == 1:
        number = tempList[0]
        print(int(number))
    else:
        if tempList[1] == "B":
            number = float(tempList[0])*1000
            print(int(number))
        elif tempList[1] == "Mn":
            number = float(tempList[0])*1000000
            print(int(number))
