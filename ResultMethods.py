import datetime
import os



def MakeList():
    target = os.path.join("./", "output", str((datetime.date.today().strftime("%d_%m_%Y"))), "followers.txt")
    with open(target, "r") as file:
        followersList = [line.strip() for line in file.readlines()]

    target = os.path.join("./", "output", str((datetime.date.today().strftime("%d_%m_%Y"))), "followings.txt")
    with open(target, "r") as file:
        followingsList = [line.strip() for line in file.readlines()]

    # print(f"followers length: {len(followersList)} - followings length: {len(followingsList)} \n")

    # print("followers:\n")
    # for line in followersList:
    #     print(line)

    # print("followings:\n")
    # for line in followingsList:
    #     print(line)
    
    return followersList,followingsList





def FindImpostors():
    followersList, followingsList = MakeList()
    followers_set = set(followersList)
    followings_set = set(followingsList)

    impostors = followings_set - followers_set
    impostorsList = []
    for impostor in impostors:
        impostorsList.append(impostor)
    return impostorsList

def FindLastFollowDate():
    returnList = []
    impostorsList = FindImpostors()
    filePath = "./output/"
    days = [(file, os.path.getctime(os.path.join(filePath, file))) for file in os.listdir(filePath)]
    daysSorted = sorted(days, key=lambda x: x[1], reverse=True)
    # for file, _ in daysSorted:
    #     print(f"Klasör Adı: {file}")
    for impostor in impostorsList:
        lastFollowDate = "Unknown"
        found = False  # impostor zaten bulundu mu?
        for day, _ in daysSorted:
            if found:
                break  # impostor zaten bulundu, dıştaki döngüye geç
            followersFilePath = os.path.join(filePath, day, "followers.txt")
            if os.path.exists(followersFilePath):
                with open(followersFilePath, "r") as followers_file:
                    followers_content = followers_file.readlines()
                    for line in followers_content:
                        if impostor == line.strip():
                            lastFollowDate = day
                            returnList.append(f"İmpostor: {impostor} - Kayıtlardaki Son Takip Tarihi: {lastFollowDate}")
                            found = True  # impostor bulunduğunda bayrağı işaretleyin
                            break
            else:
                returnList.append(f"Followers dosyası bulunamadı: {followersFilePath}")
                break
        if not found:
            returnList.append(f"İmpostor: {impostor} - Kayıtlardaki Son Takip Tarihi: {lastFollowDate}")
    for item in returnList:
        print(item)
    return returnList